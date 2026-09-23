#!/usr/bin/env python3
"""
sync_vault.py — grava os achados de uma rodada do radar-low-ticket DIRETO no vault
Obsidian (Ofertas/, Observacoes/, Radar/), seguindo o contrato de _meta/Schema.md.

Uso:
    python3 _meta/sync_vault.py achados.json --vault . --leitura "texto da leitura da rodada"

Roda LOCAL (device_bash), sempre a partir da raiz do vault. Sem dependências externas
(stdlib só), porque o Python do dispositivo do usuário pode não ter pyyaml.

Regras que este script NUNCA quebra (ver _meta/Schema.md e _meta/Scoring.md):
  - slug é imutável — chave primária das notas de Ofertas/.
  - Observacoes/ é append-only — nunca edita nem duplica um snapshot do mesmo dia.
  - Scores (s_lucro, s_replica, s_ticket, s_saturacao) de uma nota JÁ EXISTENTE nunca
    são sobrescritos por este script — só o humano ou uma etapa de mineração mais funda
    (Ads Library / unFunnelizer) muda isso. Nota nova entra com s_ticket calculado
    objetivamente da faixa de preço e os demais eixos como sentinela (0) até serem
    avaliados — isso é o comportamento correto documentado no Scoring.md, não um bug.
  - Datas sempre YYYY-MM-DD. Valores monetários como número puro.
  - "rodada" aqui é adaptado para granularidade de DIA (a automação roda 6x/dia; a
    contagem de rodadas_vista e o ciclo de vida de status do Scoring.md foram desenhados
    pensando em cadência ~diária). Múltiplas passadas no mesmo dia atualizam ra_reclamacoes
    e o corpo da nota, mas só contam como uma rodada para fins de rodadas_vista/status.
"""

import json
import re
import sys
import unicodedata
import argparse
from pathlib import Path
from datetime import date

FIELD_ORDER = [
    "tipo", "classe", "slug", "nome", "nicho", "sub_nicho", "idioma", "pais",
    "plataforma_ads", "checkout", "url_pagina", "url_ads",
    "moeda", "ticket_frente", "ticket_bump", "ticket_upsell", "ticket_medio_est", "margem_est",
    "modelo", "formato_entrega", "tem_recorrencia",
    "s_ticket", "s_lucro", "s_replica", "s_saturacao",
    "status", "visto_primeiro", "visto_ultimo", "rodadas_vista",
    "dias_no_ar", "criativos_ultima", "criativos_delta",
    "unfunnelizer_capturado", "ativos_pasta", "gateways_detectados", "bump_oculto", "upsell_oculto",
    "ra_reclamacoes", "ra_plataformas", "ra_primeira_reclamacao", "ra_checado",
    "veredito", "prioridade", "tags",
]

QUOTE_KEYS = {"nome", "url_pagina", "url_ads", "ativos_pasta", "ra_primeira_reclamacao"}
BARE_KEYS = {"slug", "nicho", "sub_nicho", "idioma", "pais", "checkout", "status", "veredito", "moeda", "tipo", "classe"}

RADAR_FIELD_ORDER = ["tipo", "data", "ofertas_vistas", "novas", "retornaram", "sumiram", "fontes", "duracao_min"]
OBSERVACAO_FIELD_ORDER = ["tipo", "data", "slug", "oferta", "criativos_ativos", "dias_no_ar",
                          "ticket_frente", "preco_mudou", "angulo_novo", "fonte",
                          "ra_reclamacoes", "criativos_novos"]


def truncar_frase(texto: str, limite: int) -> str:
    texto = texto.strip()
    if len(texto) <= limite:
        return texto
    corte = texto[:limite].rsplit(" ", 1)[0]
    return corte.rstrip(",.;:") + "…"

GATEWAY_SLUG = {
    "perfectpay": "perfectpay", "perfect pay": "perfectpay",
    "cakto": "cakto", "cakto pay": "cakto",
    "kiwify": "kiwify", "hotmart": "hotmart", "monetizze": "monetizze", "braip": "braip",
    "payt": "payt", "mangofy": "mangofy-tecnologia", "yampi": "yampi", "ticto": "ticto",
    "eduzz": "eduzz", "kirvano": "kirvano", "lastlink": "lastlink", "wiapy": "wiapy",
    "lowify": "lowify", "hubla": "hubla", "ggcheckout": "ggcheckout", "onprofit": "onprofit",
}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-")


def gateway_slug(nome_gateway: str) -> str:
    return GATEWAY_SLUG.get(nome_gateway.strip().lower(), slugify(nome_gateway))


def s_ticket_from_valor(ticket_medio_est: float) -> int:
    if ticket_medio_est <= 0:
        return 0
    if ticket_medio_est < 20:
        return 2
    if ticket_medio_est < 35:
        return 4
    if ticket_medio_est < 60:
        return 6
    if ticket_medio_est < 120:
        return 8
    return 10


def s_lucro_conservador(mencoes: int) -> int:
    # Sem dias_no_ar/ra_primeira_reclamacao o teto do Scoring.md é 6 — nunca passar disso aqui.
    if mencoes >= 4:
        return 5
    if mencoes >= 2:
        return 3
    return 2


def parse_faixa_preco(faixa: str):
    """'R$ 19-47' -> (19,47) ; 'R$ 97' -> (97,97) ; retorna (0,0) se não der pra ler."""
    nums = re.findall(r"[\d.]+(?:,\d+)?", faixa.replace(".", "").replace(",", "."))
    try:
        nums = [float(n) for n in nums]
    except ValueError:
        return (0, 0)
    if not nums:
        return (0, 0)
    if len(nums) == 1:
        return (nums[0], nums[0])
    return (min(nums), max(nums))


def yaml_value(key, val):
    if val is None or val == "":
        return ""
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        if isinstance(val, float) and val == int(val):
            val = int(val)
        return str(val)
    if isinstance(val, list):
        return "[" + ", ".join(str(v) for v in val) + "]"
    s = str(val)
    if key in QUOTE_KEYS:
        return f'"{s}"'
    if key in BARE_KEYS:
        return s
    # heurística: se tem espaço ou caractere especial, aspas
    if re.search(r'[:#\[\]{}",]', s) or " " in s:
        return f'"{s}"'
    return s


def serialize_frontmatter(data: dict, field_order=FIELD_ORDER) -> str:
    lines = ["---"]
    for k in field_order:
        if k in data:
            lines.append(f"{k}: {yaml_value(k, data[k])}")
    lines.append("---")
    return "\n".join(lines)


def parse_frontmatter(text: str):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm_text, body = m.group(1), m.group(2)
    data = {}
    for line in fm_text.split("\n"):
        if not line.strip() or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip() for v in inner.split(",") if v.strip()] if inner else []
        elif val.startswith('"') and val.endswith('"'):
            data[key] = val[1:-1]
        elif val == "true":
            data[key] = True
        elif val == "false":
            data[key] = False
        elif val == "":
            data[key] = ""
        else:
            try:
                data[key] = int(val)
            except ValueError:
                try:
                    data[key] = float(val)
                except ValueError:
                    data[key] = val
    return data, body


def dias_sem_ver(hoje: date, visto_ultimo_str: str) -> int:
    if not visto_ultimo_str:
        return 999
    try:
        y, m, d = [int(x) for x in visto_ultimo_str.split("-")]
        return (hoje - date(y, m, d)).days
    except Exception:
        return 999


def status_por_ausencia(dias: int) -> str:
    if dias <= 1:
        return "ativa"
    if dias <= 6:
        return "esfriando"
    return "morta"


def compactar(s: str) -> str:
    """Remove hifens/espacos pra comparar 'Cash no Pix' com 'Cashnopix' como a mesma coisa."""
    return slugify(s).replace("-", "")


def find_existing_slug(ofertas_dir: Path, nome: str, slug_candidato: str):
    """Dedup: match exato de slug primeiro; senao, nome compactado contido/contendo
    (pega grafias tipo 'Cash no Pix' == 'Cashnopix')."""
    p = ofertas_dir / f"{slug_candidato}.md"
    if p.exists():
        return slug_candidato
    norm_nome = compactar(nome)
    if len(norm_nome) < 4:
        return None  # nome curto demais pra dedup por substring com seguranca
    for f in ofertas_dir.glob("*.md"):
        try:
            data, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        existing_nome = compactar(str(data.get("nome", "")))
        existing_slug = str(data.get("slug", f.stem))
        if not existing_nome or len(existing_nome) < 4:
            continue
        if norm_nome == existing_nome or norm_nome in existing_nome or existing_nome in norm_nome:
            return existing_slug
    return None


def build_new_oferta(achado, hoje_str, slug):
    tipo_achado = achado["tipo"]  # marca | angulo
    classe = "oferta" if tipo_achado == "marca" else "angulo"
    lo, hi = parse_faixa_preco(achado.get("faixa_preco", ""))
    ticket_medio_est = round((lo + hi) / 2, 2) if (lo or hi) else 0
    gw = gateway_slug(achado["gateway"])
    ads_url = ("https://www.facebook.com/ads/library/?active_status=active&ad_type=all"
               f"&country=BR&q={achado['termo_busca'].replace(' ', '%20')}"
               "&search_type=keyword_unordered&media_type=all")
    data = {
        "tipo": "oferta",
        "classe": classe,
        "slug": slug,
        "nome": achado["produto"],
        "nicho": slugify(achado.get("nicho", "")) or "nao-classificado",
        "sub_nicho": slugify(achado.get("sub_nicho", "")) if achado.get("sub_nicho") else "",
        "idioma": "pt-BR",
        "pais": "BR",
        "plataforma_ads": ["meta"],
        "checkout": gw if classe == "oferta" else "desconhecido",
        "url_pagina": achado.get("url_pagina", ""),
        "url_ads": ads_url,
        "moeda": "BRL",
        "ticket_frente": achado.get("ticket_frente", lo or 0),
        "ticket_bump": achado.get("ticket_bump", 0),
        "ticket_upsell": achado.get("ticket_upsell", 0),
        "ticket_medio_est": ticket_medio_est,
        "margem_est": 0.8,
        "modelo": ["direct"],
        "formato_entrega": ["app"] if "app" in achado.get("descricao", "").lower() else [],
        "tem_recorrencia": False,
        "s_ticket": s_ticket_from_valor(ticket_medio_est),
        "s_lucro": s_lucro_conservador(achado.get("mencoes", 1)),
        "s_replica": 0,
        "s_saturacao": 0,
        "status": "nova",
        "visto_primeiro": hoje_str,
        "visto_ultimo": hoje_str,
        "rodadas_vista": 1,
        "dias_no_ar": 0,
        "criativos_ultima": 0,
        "criativos_delta": 0,
        "unfunnelizer_capturado": False,
        "ativos_pasta": f"Ativos/{slug}",
        "gateways_detectados": [gw] if classe == "oferta" else [],
        "bump_oculto": False,
        "upsell_oculto": False,
        "ra_reclamacoes": achado.get("mencoes", 1),
        "ra_plataformas": [gw] if classe == "oferta" else [],
        "ra_primeira_reclamacao": "",
        "ra_checado": hoje_str,
        "veredito": "observar",
        "prioridade": 0,
        "tags": ["oferta", "lowticket", "marca" if classe == "oferta" else "angulo"],
    }
    body = f"""
# {achado['produto']}

## Angulo
{achado.get('descricao', '').strip()}

## Funil
anuncio -> pagina -> checkout {gw if classe == 'oferta' else '(nao mapeado)'} -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, {achado.get('mencoes', 1)} mencao(oes) na varredura de {hoje_str} (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: {achado.get('evidencia_url', '')}

## Historico
```base
filters:
  and:
    - 'note.tipo == "observacao"'
    - 'note.slug == this.slug'
views:
  - type: table
    name: Snapshots
    order:
      - note.data
      - note.ra_reclamacoes
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
"""
    return serialize_frontmatter(data) + "\n" + body


def update_oferta(path: Path, achado, hoje_str, hoje: date):
    text = path.read_text(encoding="utf-8")
    data, body = parse_frontmatter(text)
    visto_ultimo_anterior = str(data.get("visto_ultimo", ""))
    status_anterior = str(data.get("status", "ativa"))
    ja_visto_hoje = visto_ultimo_anterior == hoje_str

    gw = gateway_slug(achado["gateway"])
    retornou = False

    if not ja_visto_hoje:
        # Foi vista AGORA -> status sempre volta a "ativa" (a funcao de decaimento por
        # ausencia serve para o job separado que varre quem NAO apareceu, nao para quem
        # acabou de aparecer). "Retornou" e so uma comparacao com o status anterior.
        if status_anterior in ("esfriando", "morta"):
            retornou = True
        data["status"] = "ativa"
        data["rodadas_vista"] = int(data.get("rodadas_vista", 0) or 0) + 1
        data["visto_ultimo"] = hoje_str

    data["ra_reclamacoes"] = max(int(data.get("ra_reclamacoes", 0) or 0), achado.get("mencoes", 0))
    data["ra_checado"] = hoje_str
    plataformas = list(data.get("ra_plataformas", []) or [])
    if gw not in plataformas:
        plataformas.append(gw)
    data["ra_plataformas"] = plataformas
    gws = list(data.get("gateways_detectados", []) or [])
    if gw not in gws:
        gws.append(gw)
    data["gateways_detectados"] = gws
    # scores (s_ticket/s_lucro/s_replica/s_saturacao) e demais campos de mineracao funda
    # NAO sao tocados aqui — preservados como estao, por design (ver docstring do modulo).

    novo_texto = serialize_frontmatter(data) + "\n" + body
    marcador = f"## Rodada {hoje_str}"
    if marcador not in novo_texto:
        linha = (f"\n{marcador}\n\n"
                 f"{achado.get('mencoes', 0)} mencao(oes) nesta varredura (gateway {achado['gateway']}). "
                 f"{achado.get('descricao', '').strip()}\n\n"
                 f"Evidencia: {achado.get('evidencia_url', '')}\n")
        novo_texto = novo_texto.rstrip("\n") + "\n" + linha
    path.write_text(novo_texto, encoding="utf-8")
    return data, ja_visto_hoje, retornou


def ensure_observacao(obs_dir: Path, slug, achado, hoje_str, nova: bool):
    fname = obs_dir / f"{hoje_str} -- {slug}.md"
    if fname.exists():
        return False
    lo, hi = parse_faixa_preco(achado.get("faixa_preco", ""))
    data = {
        "tipo": "observacao",
        "data": hoje_str,
        "slug": slug,
        "oferta": f"[[{slug}]]",
        "criativos_ativos": 0,
        "dias_no_ar": 0,
        "ticket_frente": achado.get("ticket_frente", lo or 0),
        "preco_mudou": False,
        "angulo_novo": nova,
        "fonte": "reclame-aqui",
        "ra_reclamacoes": achado.get("mencoes", 0),
        "criativos_novos": 0,
    }
    linhas = [serialize_frontmatter(data, OBSERVACAO_FIELD_ORDER), ""]
    if nova:
        linhas.append(f"Primeira vez vista. {achado.get('descricao', '').strip()}")
    else:
        linhas.append(f"{achado.get('mencoes', 0)} mencao(oes) na varredura de hoje. {achado.get('descricao', '').strip()}")
    fname.write_text("\n".join(linhas) + "\n", encoding="utf-8")
    return True


def sync_radar_note(radar_dir: Path, hoje_str: str, novas_slugs, movimento_slugs, retornaram_slugs, sumiram_slugs, leitura: str, fontes, ofertas_vistas_delta, novas_delta, retornaram_delta):
    fname = radar_dir / f"{hoje_str}.md"
    if fname.exists():
        data, body = parse_frontmatter(fname.read_text(encoding="utf-8"))
    else:
        data = {}
        body = f"""
# Radar {hoje_str}

## Novas
<!-- [[slug]] — nicho — ticket — por que entrou -->

## Movimento
<!-- quem acelerou (criativos_delta > 0), quem esfriou, quem mudou preco -->

## Retornaram
<!-- estavam esfriando/mortas e voltaram — investigue o porque -->

## Sumiram
Nao avaliado por esta automacao — ela cobre so PerfectPay/Cakto (poucas paginas por rodada),
nao o vault inteiro. Decair status por ausencia aqui confundiria "fora do escopo desta skill"
com "mercado esfriando" (ver _meta/Scoring.md). Fica para a Etapa 1/3b do Pipeline.md completo.

## Leitura da rodada
<!-- 3 linhas -->
"""

    data["tipo"] = "radar"
    data["data"] = hoje_str
    data["ofertas_vistas"] = int(data.get("ofertas_vistas", 0) or 0) + ofertas_vistas_delta
    data["novas"] = int(data.get("novas", 0) or 0) + novas_delta
    data["retornaram"] = int(data.get("retornaram", 0) or 0) + retornaram_delta
    data["sumiram"] = int(data.get("sumiram", 0) or 0) + len(sumiram_slugs)
    fontes_existentes = set(data.get("fontes", []) or [])
    fontes_existentes.update(fontes)
    data["fontes"] = sorted(fontes_existentes)
    data["duracao_min"] = int(data.get("duracao_min", 0) or 0)

    def append_bullets(section_header, slugs):
        nonlocal body
        if not slugs:
            return
        pattern = re.compile(rf"(## {re.escape(section_header)}\n)(.*?)(\n## |\Z)", re.DOTALL)
        m = pattern.search(body)
        if not m:
            return
        existentes = m.group(2)
        novas_linhas = []
        for slug, nota in slugs:
            if f"[[{slug}]]" not in existentes:
                novas_linhas.append(f"- [[{slug}]] — {nota}")
        if novas_linhas:
            novo_bloco = existentes.rstrip("\n") + "\n" + "\n".join(novas_linhas) + "\n"
            body = body[:m.start(2)] + novo_bloco + body[m.end(2):]

    append_bullets("Novas", novas_slugs)
    append_bullets("Movimento", movimento_slugs)
    append_bullets("Retornaram", retornaram_slugs)
    append_bullets("Sumiram", sumiram_slugs)

    if leitura:
        pattern = re.compile(r"(## Leitura da rodada\n)(.*)", re.DOTALL)
        body = pattern.sub(lambda m: m.group(1) + "\n" + leitura.strip() + "\n", body)

    if not body.startswith("\n"):
        body = "\n" + body
    fname.write_text(serialize_frontmatter(data, RADAR_FIELD_ORDER) + body, encoding="utf-8")
    return data


def aplicar_decaimento(ofertas_dir: Path, slugs_tocados_hoje: set, hoje: date, hoje_str: str,
                        gateways_cobertos: set):
    """Para ofertas NAO vistas nesta rodada: recalcula status por ausencia, MAS SO para
    quem esta dentro do escopo real desta automacao (checkout/ra_plataformas batendo com
    os gateways efetivamente varridos hoje, ex: perfectpay/cakto). Uma oferta de outro
    gateway, ou de um nicho descoberto por Ads Library/busca manual (danca, material
    pedagogico etc.), nunca vai ser "vista" por esta automacao de qualquer forma — decair
    o status dela por ausencia seria confundir falta de cobertura com o mercado esfriando
    (o mesmo erro que o _meta/Scoring.md do vault documenta e corrige em varios adendos).
    Portanto: NAO aplica decaimento nenhum por padrao. Fica registrado aqui, comentado e
    documentado, para o dia em que a skill cobrir todos os gateways do vault e essa
    decisao puder ser revisitada com seguranca."""
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("achados_json")
    ap.add_argument("--vault", default=".")
    ap.add_argument("--leitura", default="")
    ap.add_argument("--data", default="", help="YYYY-MM-DD para popular retroativamente (default: hoje)")
    args = ap.parse_args()

    vault = Path(args.vault).resolve()
    ofertas_dir = vault / "Ofertas"
    obs_dir = vault / "Observacoes"
    radar_dir = vault / "Radar"
    for d in (ofertas_dir, obs_dir, radar_dir):
        d.mkdir(exist_ok=True)

    payload = json.loads(Path(args.achados_json).read_text(encoding="utf-8"))
    achados = payload["achados"]
    fontes = [g["nome"].lower().replace(" ", "-") for g in payload.get("gateways", [])] or ["reclame-aqui"]

    if args.data:
        y, m, d = [int(x) for x in args.data.split("-")]
        hoje = date(y, m, d)
    else:
        hoje = date.today()
    hoje_str = hoje.isoformat()

    novas_slugs, movimento_slugs, retornaram_slugs = [], [], []
    ofertas_vistas_delta = novas_delta = retornaram_delta = 0
    log = []

    for achado in achados:
        slug_candidato = slugify(achado["produto"])
        if achado["tipo"] == "angulo" and not slug_candidato.startswith("angulo-"):
            slug_candidato = f"angulo-{slug_candidato}"

        existente = find_existing_slug(ofertas_dir, achado["produto"], slug_candidato)
        path = ofertas_dir / f"{(existente or slug_candidato)}.md"

        if existente:
            slug = existente
            data, ja_visto_hoje, retornou = update_oferta(path, achado, hoje_str, hoje)
            nova = False
            if not ja_visto_hoje:
                ofertas_vistas_delta += 1
                if retornou:
                    retornaram_delta += 1
                    retornaram_slugs.append((slug, f"{achado.get('nicho','')} — reapareceu ({achado.get('mencoes',0)} mencao(oes))"))
                else:
                    movimento_slugs.append((slug, f"ra_reclamacoes atualizado para {data['ra_reclamacoes']}"))
            log.append(f"  ~ {slug} (existente) — atualizado" if not ja_visto_hoje else f"  = {slug} (ja visto hoje nesta rodada)")
        else:
            slug = slug_candidato
            texto = build_new_oferta(achado, hoje_str, slug)
            path.write_text(texto, encoding="utf-8")
            nova = True
            ofertas_vistas_delta += 1
            novas_delta += 1
            novas_slugs.append((slug, f"{achado.get('nicho','')} — {achado.get('faixa_preco','?')} — {truncar_frase(achado.get('descricao',''), 140)}"))
            log.append(f"  + {slug} (NOVA)")

        ensure_observacao(obs_dir, slug, achado, hoje_str, nova)

    # Decaimento so deve ignorar quem foi de fato visto HOJE (qualquer passada) — le direto
    # do disco em vez de reconstruir da lista de achados, porque cobre tambem "ja visto hoje
    # nesta rodada" (2a+ passada do dia, que nao gera bullet mas ja tem visto_ultimo == hoje).
    slugs_com_visto_hoje = set()
    for f in ofertas_dir.glob("*.md"):
        try:
            d, _ = parse_frontmatter(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        if str(d.get("visto_ultimo", "")) == hoje_str:
            slugs_com_visto_hoje.add(f.stem)

    gateways_cobertos = {gateway_slug(g["nome"]) for g in payload.get("gateways", [])}
    mudancas_decaimento = aplicar_decaimento(ofertas_dir, slugs_com_visto_hoje, hoje, hoje_str, gateways_cobertos)
    sumiram_slugs = [(slug, f"{de} -> {para}") for slug, de, para in mudancas_decaimento]

    radar_data = sync_radar_note(
        radar_dir, hoje_str, novas_slugs, movimento_slugs, retornaram_slugs, sumiram_slugs,
        args.leitura, fontes, ofertas_vistas_delta, novas_delta, retornaram_delta,
    )

    print(f"Vault: {vault}")
    print(f"Radar/{hoje_str}.md — ofertas_vistas={radar_data['ofertas_vistas']} novas={radar_data['novas']} retornaram={radar_data['retornaram']} sumiram(decairam)={len(sumiram_slugs)}")
    print("\n".join(log))
    if mudancas_decaimento:
        print("Decaimento por ausencia:")
        for slug, de, para in mudancas_decaimento:
            print(f"  - {slug}: {de} -> {para}")


if __name__ == "__main__":
    main()
