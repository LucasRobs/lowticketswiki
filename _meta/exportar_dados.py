#!/usr/bin/env python3
"""
exportar_dados.py — transforma o vault em dados para o dashboard (dashboard/data/).

    python3 _meta/exportar_dados.py              # exporta (so reescreve se algo mudou)
    python3 _meta/exportar_dados.py --verificar  # so valida; sai com 1 se houver erro
    python3 _meta/exportar_dados.py --forcar     # reescreve mesmo sem mudanca

O vault continua sendo a fonte da verdade. Este script so LE as notas e escreve JSON:

    dashboard/data/versao.json          hash + quando os dados mudaram (o site consulta a cada minuto)
    dashboard/data/painel.json          lista compacta de ofertas, rodadas, series e qualidade
    dashboard/data/rodadas.json         notas do Radar e das passadas, com o texto
    dashboard/data/ofertas/<slug>.json  nota completa da oferta + snapshots + onde e citada

A saida e funcao pura do conteudo do vault (nada de "hoje" nem de relogio no calculo),
entao rodar duas vezes sem mudar nota nenhuma nao gera diff — o git so ve mudanca quando
o dado mudou de verdade. Stdlib pura, Python 3.8+.
"""

import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import vault as V  # noqa: E402

ESQUEMA = 1
RAIZ = Path(__file__).resolve().parent.parent
SAIDA_PADRAO = RAIZ / "dashboard" / "data"

RE_WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]")
RE_BLOCO_OBSIDIAN = re.compile(r"```(?:base|dataview|dataviewjs|query)\b.*?```", re.DOTALL)
RE_COMENTARIO_HTML = re.compile(r"<!--.*?-->", re.DOTALL)


# ---------------------------------------------------------------------------
# Texto
# ---------------------------------------------------------------------------

def limpar_corpo(md: str) -> str:
    md = RE_BLOCO_OBSIDIAN.sub("", md)
    md = RE_COMENTARIO_HTML.sub("", md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip() + "\n" if md.strip() else ""


def texto_plano(md: str) -> str:
    t = RE_COMENTARIO_HTML.sub("", md)
    t = RE_WIKILINK.sub(lambda m: (m.group(2) or m.group(1)).strip(), t)
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
    t = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", t, flags=re.MULTILINE)
    t = re.sub(r"^>\s?", "", t, flags=re.MULTILINE)
    t = re.sub(r"\s+", " ", t)  # antes da enfase: negrito que atravessa linha tambem sai
    t = re.sub(r"`([^`]*)`", r"\1", t)
    t = re.sub(r"(\*\*|__)(?=\S)(.+?)(?<=\S)\1", r"\2", t)
    t = re.sub(r"(?<![\w*])(\*|_)(?=\S)(.+?)(?<=\S)\1(?![\w*])", r"\2", t)
    t = t.replace("**", "").replace("\\$", "$").replace("\\|", "|")
    return t.strip()


def truncar(t: str, n: int) -> str:
    if len(t) <= n:
        return t
    corte = t[:n].rsplit(" ", 1)[0].rstrip(",.;:—-")
    return corte + "…"


def secoes(md: str):
    """[(titulo, texto)] das secoes ## de um corpo markdown."""
    out, atual, buf = [], None, []
    for linha in md.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", linha)
        if m:
            if atual is not None or buf:
                out.append((atual, "\n".join(buf).strip()))
            atual, buf = m.group(1), []
        else:
            buf.append(linha)
    out.append((atual, "\n".join(buf).strip()))
    return out


def primeiro_paragrafo(md: str) -> str:
    for bloco in re.split(r"\n\s*\n", md):
        b = bloco.strip()
        if not b or b.startswith(("#", "|", "```", "---", "<!--")):
            continue
        if b.startswith(">") and len(b) < 40:
            continue
        return b
    return ""


def resumo_oferta(corpo: str) -> str:
    for titulo, texto in secoes(corpo):
        if titulo and re.match(r"^[ÂA]ngulo\b", titulo, re.IGNORECASE):
            p = primeiro_paragrafo(texto)
            if p:
                return truncar(texto_plano(p), 260)
    sem_h1 = re.sub(r"^#\s+.*$", "", corpo, count=1, flags=re.MULTILINE)
    return truncar(texto_plano(primeiro_paragrafo(sem_h1)), 260)


def secao(md: str, nome_regex: str) -> str:
    for titulo, texto in secoes(md):
        if titulo and re.match(nome_regex, titulo, re.IGNORECASE):
            return texto
    return ""


def links_no_texto(md: str):
    return {m.group(1).strip() for m in RE_WIKILINK.finditer(md)}


# ---------------------------------------------------------------------------
# Leitura e validacao
# ---------------------------------------------------------------------------

class Relatorio:
    def __init__(self):
        self.erros, self.avisos = [], []

    def erro(self, arquivo, campo, msg):
        self.erros.append({"arquivo": arquivo, "campo": campo, "msg": msg})

    def aviso(self, arquivo, campo, msg, codigo=None):
        self.avisos.append({"arquivo": arquivo, "campo": campo, "msg": msg, "codigo": codigo or campo})


def n(v):
    x = V.num(v)
    return int(x) if float(x).is_integer() else round(x, 2)


def data_ok(v) -> bool:
    return isinstance(v, str) and bool(V.RE_DATA.match(v))


def carregar(vault: Path, rel: Relatorio):
    ofertas, observacoes, dias, passadas, analises = {}, [], [], [], []
    estilos = Counter()

    for p in V.notas(vault, "Ofertas"):
        arq = str(p.relative_to(vault))
        dados, corpo, info = V.ler_nota(p)
        estilos[info["estilo"]] += 1
        if not info["tem_fm"]:
            rel.erro(arq, "frontmatter", "nota sem frontmatter — nao entra no dashboard")
            continue
        for e in info["erros"]:
            rel.erro(arq, "frontmatter", e)
        if dados.get("tipo") != "oferta":
            rel.aviso(arq, "tipo", "tipo=%r dentro de Ofertas/ — ignorada" % dados.get("tipo"))
            continue
        d = V.normalizar_dados(dados)
        slug = str(d.get("slug") or p.stem)
        if slug != p.stem:
            rel.erro(arq, "slug", "slug %r diferente do nome do arquivo" % slug)
        if not V.RE_SLUG.match(slug):
            rel.aviso(arq, "slug", "slug fora do padrao kebab-case: %r" % slug)
        if slug in ofertas:
            rel.erro(arq, "slug", "slug duplicado (tambem em %s)" % ofertas[slug]["arquivo"])
            continue
        ofertas[slug] = {"arquivo": arq, "fm": d, "corpo": corpo, "estilo": info["estilo"]}

    for p in V.notas(vault, "Observacoes"):
        arq = str(p.relative_to(vault))
        dados, corpo, info = V.ler_nota(p)
        estilos[info["estilo"]] += 1
        if dados.get("tipo") != "observacao":
            continue
        d = V.normalizar_dados(dados)
        observacoes.append({"arquivo": arq, "fm": d, "corpo": corpo})

    for p in V.notas(vault, "Radar"):
        arq = str(p.relative_to(vault))
        dados, corpo, info = V.ler_nota(p)
        if dados.get("tipo") == "radar":
            dias.append({"arquivo": arq, "fm": V.normalizar_dados(dados), "corpo": corpo})

    for p in V.notas(vault, "Radar/rodadas"):
        arq = str(p.relative_to(vault))
        dados, corpo, info = V.ler_nota(p)
        if dados.get("tipo") == "rodada":
            passadas.append({"arquivo": arq, "fm": V.normalizar_dados(dados), "corpo": corpo})

    for p in V.notas(vault, "Analises", recursivo=True):
        arq = str(p.relative_to(vault))
        dados, corpo, info = V.ler_nota(p)
        titulo = dados.get("titulo") or (re.search(r"^#\s+(.+)$", corpo, re.MULTILINE) or [None, p.stem])[1]
        data = dados.get("data") if data_ok(dados.get("data")) else ""
        if not data:
            m = re.match(r"^(\d{4}-\d{2}-\d{2})", p.name)
            data = m.group(1) if m else ""
        analises.append({"arquivo": arq, "titulo": str(titulo).strip(), "data": data,
                         "tipo": dados.get("tipo") or "", "corpo": corpo})

    return ofertas, observacoes, dias, passadas, analises, estilos


def validar_oferta(slug, o, rel: Relatorio):
    fm, arq = o["fm"], o["arquivo"]
    for campo in ("nome", "status", "visto_primeiro", "visto_ultimo"):
        if fm.get(campo) in (None, ""):
            rel.erro(arq, campo, "campo obrigatorio vazio")
    if fm.get("classe", "") not in V.CLASSES:
        rel.aviso(arq, "classe", "classe %r fora de oferta|angulo (tratada como oferta)" % fm.get("classe"), "vocabulario")
    if fm.get("status") and fm["status"] not in V.STATUS:
        rel.aviso(arq, "status", "status %r fora do vocabulario" % fm["status"], "vocabulario")
    if fm.get("veredito") and fm["veredito"] not in V.VEREDITOS:
        rel.aviso(arq, "veredito", "veredito %r fora do vocabulario" % fm["veredito"], "vocabulario")
    if fm.get("checkout") and fm["checkout"] not in V.GATEWAYS:
        rel.aviso(arq, "checkout", "checkout %r fora do vocabulario de gateway" % fm["checkout"], "vocabulario")
    for campo in ("gateways_detectados", "ra_plataformas"):
        for g in fm.get(campo) or []:
            if g not in V.GATEWAYS:
                rel.aviso(arq, campo, "%r fora do vocabulario de gateway" % g, "vocabulario")
    for m in fm.get("modelo") or []:
        if m not in V.MODELOS:
            rel.aviso(arq, "modelo", "modelo %r fora do vocabulario" % m, "vocabulario")
    for f in fm.get("formato_entrega") or []:
        if f not in V.FORMATOS:
            rel.aviso(arq, "formato_entrega", "formato %r fora do vocabulario" % f, "vocabulario")
    for campo in V.CAMPOS_DATA:
        v = fm.get(campo)
        if v not in (None, "") and not data_ok(v):
            rel.aviso(arq, campo, "data fora do formato AAAA-MM-DD: %r" % v, "data")
    for campo in ("s_ticket", "s_lucro", "s_replica", "s_saturacao", "prioridade"):
        v = fm.get(campo)
        if v in (None, ""):
            continue
        if not isinstance(v, (int, float)) or isinstance(v, bool):
            rel.aviso(arq, campo, "valor nao numerico: %r" % v, "tipo")
        elif not (0 <= v <= (3 if campo == "prioridade" else 10)):
            rel.aviso(arq, campo, "fora da escala: %r" % v, "escala")
    for campo in V.CAMPOS_NUMERICOS:
        v = fm.get(campo)
        if v not in (None, "") and (not isinstance(v, (int, float)) or isinstance(v, bool)):
            rel.aviso(arq, campo, "valor nao numerico: %r" % v, "tipo")
    if data_ok(fm.get("visto_primeiro")) and data_ok(fm.get("visto_ultimo")) \
            and fm["visto_ultimo"] < fm["visto_primeiro"]:
        rel.aviso(arq, "visto_ultimo", "visto_ultimo anterior a visto_primeiro", "data")


def flags_oferta(fm: dict, ultima_rodada: str):
    f = []
    sem_longevidade = V.num(fm.get("dias_no_ar")) <= 0 and not fm.get("ra_primeira_reclamacao")
    if fm.get("classe") != "angulo" and V.num(fm.get("s_lucro")) >= 7 and sem_longevidade:
        f.append("lucro-sem-medicao")
    if fm.get("classe") != "angulo" and any(V.num(fm.get(k)) == 0 for k in ("s_lucro", "s_replica", "s_ticket", "s_saturacao")):
        f.append("score-provisorio")
    if sem_longevidade:
        f.append("sem-longevidade")
    if fm.get("classe") != "angulo" and fm.get("checkout") in ("", "desconhecido"):
        f.append("checkout-desconhecido")
    if not fm.get("url_pagina"):
        f.append("sem-lp")
    if fm.get("status") == "nova" and ultima_rodada and str(fm.get("visto_primeiro", "")) < ultima_rodada:
        f.append("status-vencido")
    return f


# ---------------------------------------------------------------------------
# Montagem
# ---------------------------------------------------------------------------

def montar(vault: Path):
    rel = Relatorio()
    ofertas, observacoes, dias, passadas, analises, estilos = carregar(vault, rel)

    datas_rodada = sorted({d["fm"].get("data") for d in dias if data_ok(d["fm"].get("data"))}
                          | {p["fm"].get("data") for p in passadas if data_ok(p["fm"].get("data"))})
    ultima_rodada = datas_rodada[-1] if datas_rodada else ""

    # --- observacoes por oferta ---
    obs_por_slug = defaultdict(list)
    for ob in observacoes:
        fm, arq = ob["fm"], ob["arquivo"]
        slug = str(fm.get("slug") or "")
        if not data_ok(fm.get("data")):
            rel.erro(arq, "data", "data invalida: %r" % fm.get("data"))
            continue
        if slug not in ofertas:
            rel.erro(arq, "slug", "snapshot aponta para oferta inexistente: %r" % slug)
            continue
        esperado = "%s -- %s.md" % (fm["data"], slug)
        if Path(arq).name != esperado:
            rel.aviso(arq, "arquivo", "nome esperado: %s" % esperado, "nome-arquivo")
        obs_por_slug[slug].append({
            "data": fm["data"],
            "fonte": fm.get("fonte") or "",
            "ra_reclamacoes": fm.get("ra_reclamacoes", ""),
            "criativos_ativos": fm.get("criativos_ativos", ""),
            "criativos_novos": fm.get("criativos_novos", ""),
            "dias_no_ar": fm.get("dias_no_ar", ""),
            "ticket_frente": fm.get("ticket_frente", ""),
            "preco_mudou": bool(fm.get("preco_mudou")),
            "angulo_novo": bool(fm.get("angulo_novo")),
            "texto": limpar_corpo(ob["corpo"]).strip(),
        })
    for lst in obs_por_slug.values():
        lst.sort(key=lambda x: x["data"])

    # --- validacao de radar/passadas ---
    for d in dias:
        if not data_ok(d["fm"].get("data")):
            rel.erro(d["arquivo"], "data", "data invalida: %r" % d["fm"].get("data"))
    for p in passadas:
        fm = p["fm"]
        if not data_ok(fm.get("data")):
            rel.erro(p["arquivo"], "data", "data invalida: %r" % fm.get("data"))
        if fm.get("coleta") and fm["coleta"] not in V.COLETAS:
            rel.aviso(p["arquivo"], "coleta", "coleta %r fora de ok|parcial|sem-coleta" % fm["coleta"], "vocabulario")

    # --- backlinks: quem cita cada oferta ---
    citacoes = defaultdict(list)
    for d in dias:
        for s in links_no_texto(d["corpo"]):
            if s in ofertas:
                citacoes[s].append({"tipo": "radar", "arquivo": d["arquivo"], "data": d["fm"].get("data", ""),
                                    "titulo": "Radar " + str(d["fm"].get("data", ""))})
    for p in passadas:
        for s in links_no_texto(p["corpo"]):
            if s in ofertas:
                citacoes[s].append({"tipo": "passada", "arquivo": p["arquivo"], "data": p["fm"].get("data", ""),
                                    "titulo": "Passada %s %s" % (p["fm"].get("data", ""), p["fm"].get("hora", ""))})
    for a in analises:
        for s in links_no_texto(a["corpo"]):
            if s in ofertas:
                citacoes[s].append({"tipo": "analise", "arquivo": a["arquivo"], "data": a["data"], "titulo": a["titulo"]})
    for lst in citacoes.values():
        lst.sort(key=lambda x: (x["data"], x["arquivo"]), reverse=True)

    # --- ofertas ---
    compactas, detalhes = [], {}
    for slug in sorted(ofertas):
        o = ofertas[slug]
        fm = o["fm"]
        validar_oferta(slug, o, rel)
        if fm.get("classe") not in V.CLASSES:
            fm["classe"] = "oferta"
        flags = flags_oferta(fm, ultima_rodada)
        if "lucro-sem-medicao" in flags:
            rel.aviso(o["arquivo"], "s_lucro", "s_lucro %s sem dias_no_ar nem ra_primeira_reclamacao (teto 6, Scoring.md 31/08)"
                      % fm.get("s_lucro"), "regra-s_lucro")
        obs = obs_por_slug.get(slug, [])
        gateways = sorted({g for g in ([fm.get("checkout")] + list(fm.get("gateways_detectados") or [])
                                       + list(fm.get("ra_plataformas") or []))
                           if g and g != "desconhecido"})
        reg = {
            "slug": slug,
            "nome": str(fm.get("nome") or slug),
            "classe": fm.get("classe"),
            "nicho": fm.get("nicho") or "nao-classificado",
            "sub_nicho": fm.get("sub_nicho") or "",
            "status": fm.get("status") or "",
            "veredito": fm.get("veredito") or "",
            "prioridade": int(V.num(fm.get("prioridade"))),
            "checkout": fm.get("checkout") or "",
            "gateways": gateways,
            "plataforma_ads": fm.get("plataforma_ads") or [],
            "modelo": fm.get("modelo") or [],
            "formato_entrega": fm.get("formato_entrega") or [],
            "recorrente": bool(fm.get("tem_recorrencia")),
            "moeda": fm.get("moeda") or "BRL",
            "ticket_frente": n(fm.get("ticket_frente")),
            "ticket_bump": n(fm.get("ticket_bump")),
            "ticket_upsell": n(fm.get("ticket_upsell")),
            "ticket_medio_est": n(fm.get("ticket_medio_est")),
            "s_ticket": n(fm.get("s_ticket")),
            "s_lucro": n(fm.get("s_lucro")),
            "s_replica": n(fm.get("s_replica")),
            "s_saturacao": n(fm.get("s_saturacao")),
            "score": V.score(fm),
            "decisao": V.decisao(fm),
            "visto_primeiro": fm.get("visto_primeiro") or "",
            "visto_ultimo": fm.get("visto_ultimo") or "",
            "rodadas_vista": int(V.num(fm.get("rodadas_vista"))),
            "dias_no_ar": int(V.num(fm.get("dias_no_ar"))),
            "criativos_ultima": int(V.num(fm.get("criativos_ultima"))),
            "criativos_delta": int(V.num(fm.get("criativos_delta"))),
            "ra_reclamacoes": int(V.num(fm.get("ra_reclamacoes"))),
            "ra_primeira_reclamacao": fm.get("ra_primeira_reclamacao") or "",
            "ra_checado": fm.get("ra_checado") or "",
            "bump_oculto": bool(fm.get("bump_oculto")),
            "upsell_oculto": bool(fm.get("upsell_oculto")),
            "url_pagina": fm.get("url_pagina") or "",
            "url_ads": fm.get("url_ads") or "",
            "n_obs": len(obs),
            "ultima_obs": obs[-1]["data"] if obs else "",
            "n_citacoes": len(citacoes.get(slug, [])),
            "resumo": resumo_oferta(o["corpo"]),
            "flags": flags,
        }
        compactas.append(reg)
        detalhes[slug] = {
            "slug": slug,
            "arquivo": o["arquivo"],
            "fm": fm,
            "calc": {"score": reg["score"], "decisao": reg["decisao"], "flags": flags, "gateways": gateways},
            "corpo": limpar_corpo(o["corpo"]),
            "observacoes": obs,
            "citacoes": citacoes.get(slug, []),
        }

    # --- status 'nova' vencido: um aviso agregado, nao 60 linhas ---
    vencidas = [r["slug"] for r in compactas if "status-vencido" in r["flags"]]
    if vencidas:
        rel.aviso("Ofertas/", "status", "%d nota(s) com status 'nova' depois da rodada de estreia "
                  "(Scoring.md, adendo 23/08: 'nova' so vale na estreia)" % len(vencidas), "status-vencido")

    # --- dias e passadas ---
    passadas_por_dia = Counter(p["fm"].get("data") for p in passadas)
    dias_out, dias_full = [], []
    for d in sorted(dias, key=lambda x: (str(x["fm"].get("data", "")), x["arquivo"]), reverse=True):
        fm = d["fm"]
        titulo_m = re.search(r"^#\s+(.+)$", d["corpo"], re.MULTILINE)
        titulo = titulo_m.group(1).strip() if titulo_m else "Radar " + str(fm.get("data", ""))
        leitura = secao(d["corpo"], r"^Leitura") or ""
        base = {
            "arquivo": d["arquivo"],
            "data": fm.get("data", ""),
            "titulo": titulo,
            "ofertas_vistas": int(V.num(fm.get("ofertas_vistas"))),
            "novas": int(V.num(fm.get("novas"))),
            "retornaram": int(V.num(fm.get("retornaram"))),
            "sumiram": int(V.num(fm.get("sumiram"))),
            "fontes": fm.get("fontes") or [],
            "duracao_min": int(V.num(fm.get("duracao_min"))),
            "n_passadas": passadas_por_dia.get(fm.get("data"), 0),
        }
        dias_out.append(dict(base, leitura=truncar(texto_plano(leitura), 420) if leitura else ""))
        dias_full.append(dict(base, corpo=limpar_corpo(d["corpo"])))

    passadas_out, passadas_full = [], []
    for p in sorted(passadas, key=lambda x: (str(x["fm"].get("data", "")), str(x["fm"].get("hora", "")), x["arquivo"]), reverse=True):
        fm = p["fm"]
        corpo = limpar_corpo(p["corpo"])
        sem_cab = re.sub(r"^(>.*\n)+", "", corpo).strip()
        sem_cab = re.sub(r"^#\s+.*\n", "", sem_cab).strip()
        base = {
            "arquivo": p["arquivo"],
            "data": fm.get("data", ""),
            "hora": str(fm.get("hora") or ""),
            "gateways": fm.get("gateways") or [],
            "paginas": int(V.num(fm.get("paginas"))),
            "coleta": fm.get("coleta") or "",
            "origem": fm.get("origem") or "",
            "ofertas": sorted(s for s in links_no_texto(corpo) if s in ofertas),
        }
        passadas_out.append(dict(base, resumo=truncar(texto_plano(sem_cab), 240)))
        passadas_full.append(dict(base, corpo=corpo))

    # --- series ---
    descobertas = defaultdict(lambda: {"oferta": 0, "angulo": 0})
    for r in compactas:
        if data_ok(r["visto_primeiro"]):
            descobertas[r["visto_primeiro"]][r["classe"] if r["classe"] in ("oferta", "angulo") else "oferta"] += 1
    obs_dia = Counter(ob["data"] for lst in obs_por_slug.values() for ob in lst)

    # --- qualidade ---
    reais = [r for r in compactas if r["classe"] == "oferta"]
    def cobertura(campo, rotulo, cond):
        return {"campo": campo, "rotulo": rotulo, "preenchidas": sum(1 for r in reais if cond(r)), "total": len(reais)}
    cob = [
        cobertura("dias_no_ar", "Tempo no ar medido", lambda r: r["dias_no_ar"] > 0 or bool(r["ra_primeira_reclamacao"])),
        cobertura("criativos_ultima", "Criativos contados", lambda r: r["criativos_ultima"] > 0),
        cobertura("url_pagina", "Página de vendas", lambda r: bool(r["url_pagina"])),
        cobertura("checkout", "Gateway identificado", lambda r: r["checkout"] not in ("", "desconhecido")),
        cobertura("ticket_medio_est", "Ticket estimado", lambda r: r["ticket_medio_est"] > 0),
        cobertura("s_replica", "Replicabilidade avaliada", lambda r: r["s_replica"] > 0),
        cobertura("s_saturacao", "Saturação avaliada", lambda r: r["s_saturacao"] > 0),
        cobertura("ra_reclamacoes", "Reclamações contadas", lambda r: r["ra_reclamacoes"] > 0),
    ]
    fila = sorted([r for r in reais if "sem-longevidade" in r["flags"] and r["decisao"] != "descartar"
                   and r["veredito"] != "descartar"],
                  key=lambda r: (-r["score"], -r["prioridade"], r["slug"]))[:15]
    resumo_avisos = Counter(a["codigo"] for a in rel.avisos)
    qualidade = {
        "erros": rel.erros,
        "avisos": [a for a in rel.avisos if a["codigo"] != "status-vencido"][:300],
        "resumo_avisos": dict(sorted(resumo_avisos.items())),
        "cobertura": cob,
        "fila_enriquecimento": [r["slug"] for r in fila],
        "status_vencido": vencidas,
        "estilos_frontmatter": dict(sorted(estilos.items())),
    }

    totais = {
        "ofertas": len(reais),
        "angulos": sum(1 for r in compactas if r["classe"] == "angulo"),
        "observacoes": sum(len(v) for v in obs_por_slug.values()),
        "dias_radar": len(dias),
        "passadas": len(passadas),
        "analises": len(analises),
        "ultima_rodada": ultima_rodada,
    }

    painel = {
        "esquema": ESQUEMA,
        "totais": totais,
        "ofertas": compactas,
        "dias": dias_out,
        "passadas": passadas_out,
        "serie": {
            "descobertas": {k: descobertas[k] for k in sorted(descobertas)},
            "observacoes": {k: obs_dia[k] for k in sorted(obs_dia)},
        },
        "analises": [{"arquivo": a["arquivo"], "titulo": a["titulo"], "data": a["data"], "tipo": a["tipo"]}
                     for a in sorted(analises, key=lambda a: (a["data"], a["arquivo"]), reverse=True)],
        "qualidade": qualidade,
        "vocabulario": {"gateways": V.GATEWAYS, "status": V.STATUS, "vereditos": V.VEREDITOS,
                        "classes": V.CLASSES},
    }
    rodadas = {"esquema": ESQUEMA, "dias": dias_full, "passadas": passadas_full}
    return painel, rodadas, detalhes, rel


# ---------------------------------------------------------------------------
# Escrita
# ---------------------------------------------------------------------------

def dump(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"


def mover_para_quarentena(p: Path, raiz: Path):
    try:
        p.unlink()
        return
    except OSError:
        pass
    dest = raiz / "_to_delete" / ("dashboard-data-" + p.name)
    dest.parent.mkdir(exist_ok=True)
    try:
        shutil.move(str(p), str(dest))
    except OSError:
        pass


def exportar(vault: Path = RAIZ, saida: Path = SAIDA_PADRAO, forcar=False, verificar=False, silencioso=False):
    painel, rodadas, detalhes, rel = montar(vault)

    arquivos = {"painel.json": dump(painel), "rodadas.json": dump(rodadas)}
    for slug, det in detalhes.items():
        arquivos["ofertas/%s.json" % slug] = dump(det)

    h = hashlib.sha256()
    for nome in sorted(arquivos):
        h.update(nome.encode())
        h.update(b"\0")
        h.update(arquivos[nome].encode("utf-8"))
    hash_ = h.hexdigest()[:16]

    resumo = {
        "hash": hash_,
        "ofertas": painel["totais"]["ofertas"],
        "angulos": painel["totais"]["angulos"],
        "observacoes": painel["totais"]["observacoes"],
        "erros": len(rel.erros),
        "avisos": len(rel.avisos),
        "mudou": False,
    }
    if verificar:
        return resumo, rel

    versao_path = saida / "versao.json"
    anterior = {}
    if versao_path.exists():
        try:
            anterior = json.loads(versao_path.read_text(encoding="utf-8"))
        except ValueError:
            anterior = {}
    if anterior.get("hash") == hash_ and not forcar:
        return resumo, rel

    ultima = painel["passadas"][0] if painel["passadas"] else {}
    versao = {
        "esquema": ESQUEMA,
        "hash": hash_,
        "atualizado_em": V.agora_local().replace(microsecond=0).isoformat(),
        "ofertas": painel["totais"]["ofertas"],
        "angulos": painel["totais"]["angulos"],
        "observacoes": painel["totais"]["observacoes"],
        "ultima_rodada": painel["totais"]["ultima_rodada"],
        "ultima_passada": {k: ultima.get(k) for k in ("data", "hora", "coleta", "gateways")} if ultima else None,
    }
    # o painel carrega o proprio hash para o site saber se o que esta na tela e o atual
    arquivos["painel.json"] = dump(dict(painel, versao=versao))
    arquivos["versao.json"] = dump(versao)

    (saida / "ofertas").mkdir(parents=True, exist_ok=True)
    escritos = 0
    for nome, conteudo in arquivos.items():
        p = saida / nome
        if p.exists() and p.read_text(encoding="utf-8") == conteudo:
            continue
        V.escrever_texto(p, conteudo)
        escritos += 1
    validos = {"%s.json" % s for s in detalhes}
    for p in (saida / "ofertas").glob("*.json"):
        if p.name not in validos:
            mover_para_quarentena(p, vault)
    resumo.update(mudou=True, escritos=escritos, atualizado_em=versao["atualizado_em"])
    return resumo, rel


def imprimir(resumo, rel, silencioso=False, detalhar=False):
    if silencioso and not rel.erros:
        return
    print("dashboard: %d ofertas, %d angulos, %d snapshots | %d erro(s), %d aviso(s) | %s"
          % (resumo["ofertas"], resumo["angulos"], resumo["observacoes"], len(rel.erros), len(rel.avisos),
             ("dados atualizados (%s arquivo(s))" % resumo.get("escritos", 0)) if resumo.get("mudou") else "sem mudanca nos dados"))
    for e in rel.erros[:40]:
        print("  ERRO  %s [%s] %s" % (e["arquivo"], e["campo"], e["msg"]))
    if detalhar:
        for a in rel.avisos[:200]:
            print("  aviso %s [%s] %s" % (a["arquivo"], a["campo"], a["msg"]))
    elif rel.avisos and not silencioso:
        c = Counter(a["codigo"] for a in rel.avisos)
        print("  avisos por tipo: " + ", ".join("%s=%d" % kv for kv in sorted(c.items())) + "  (detalhes: --verificar)")


def main(argv=None):
    ap = argparse.ArgumentParser(description="Exporta o vault para dashboard/data/")
    ap.add_argument("--vault", default=str(RAIZ))
    ap.add_argument("--saida", default=None)
    ap.add_argument("--forcar", action="store_true", help="reescreve mesmo sem mudanca")
    ap.add_argument("--verificar", action="store_true", help="so valida e lista erros/avisos")
    ap.add_argument("--silencioso", action="store_true")
    args = ap.parse_args(argv)
    vault = Path(args.vault).resolve()
    saida = Path(args.saida).resolve() if args.saida else vault / "dashboard" / "data"
    resumo, rel = exportar(vault, saida, forcar=args.forcar, verificar=args.verificar, silencioso=args.silencioso)
    imprimir(resumo, rel, silencioso=args.silencioso, detalhar=args.verificar)
    return 1 if (args.verificar and rel.erros) else 0


if __name__ == "__main__":
    sys.exit(main())
