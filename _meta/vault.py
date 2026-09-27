#!/usr/bin/env python3
"""
vault.py — biblioteca comum do Radar Low Ticket.

Tudo que le ou escreve nota do vault passa por aqui: sync_vault.py, exportar_dados.py
e publicar.py. Um parser so, um formato canonico so, uma formula de score so.

Stdlib pura, compativel com Python 3.8+ (o python3 do macOS vem das Command Line Tools
e pode ser 3.9). Nada de pyyaml: o frontmatter do vault e um subconjunto pequeno e
estavel de YAML, e este parser cobre os dois estilos que existem no vault:

  - estilo canonico (o que o sync_vault.py grava): listas inline `[a, b]`,
    strings com aspas duplas, vazio = campo sem valor;
  - estilo PyYAML (notas vindas de outras ferramentas, ex. rodada de 11/09):
    listas em bloco (`- item`), aspas simples, `null`.

Uso direto (manutencao):
    python3 _meta/vault.py normalizar            # mostra quem esta fora do formato canonico
    python3 _meta/vault.py normalizar --aplicar  # reescreve so o frontmatter dessas notas
"""

import json
import re
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

# Fortaleza nao tem horario de verao desde 2019: offset fixo evita depender de tzdata
# (o VM do Cowork roda em UTC; uma passada das 22h em Fortaleza ja e "amanha" em UTC).
TZ_FORTALEZA = timezone(timedelta(hours=-3), "America/Fortaleza")


def agora_local() -> datetime:
    return datetime.now(TZ_FORTALEZA)


def hoje_local() -> date:
    return agora_local().date()


# ---------------------------------------------------------------------------
# Contrato (espelha _meta/Schema.md — se mudar la, muda aqui)
# ---------------------------------------------------------------------------

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

OBSERVACAO_FIELD_ORDER = [
    "tipo", "data", "slug", "oferta", "criativos_ativos", "dias_no_ar",
    "ticket_frente", "preco_mudou", "angulo_novo", "fonte",
    "ra_reclamacoes", "criativos_novos",
]

RADAR_FIELD_ORDER = ["tipo", "data", "ofertas_vistas", "novas", "retornaram", "sumiram",
                     "fontes", "duracao_min"]

RODADA_FIELD_ORDER = ["tipo", "data", "hora", "gateways", "paginas", "coleta", "radar", "origem"]

QUOTE_KEYS = {"nome", "url_pagina", "url_ads", "ativos_pasta", "ra_primeira_reclamacao",
              "oferta", "hora", "radar", "origem", "titulo"}
BARE_KEYS = {"slug", "nicho", "sub_nicho", "idioma", "pais", "checkout", "status", "veredito",
             "moeda", "tipo", "classe", "coleta", "fonte"}

# Vocabulario controlado (Schema.md, adendos de 22/08, 31/08 e 06/09)
GATEWAYS = [
    "perfectpay", "cakto", "kirvano", "lastlink", "wiapy", "lowify", "kiwify", "hotmart",
    "ticto", "monetizze", "eduzz", "hubla", "ggcheckout", "payt", "onprofit", "stripe",
    "clickbank", "whatsapp", "proprio", "desconhecido",
]
STATUS = ["nova", "aquecendo", "ativa", "esfriando", "morta"]
VEREDITOS = ["replicar", "observar", "descartar", "replicando", "replicada"]
CLASSES = ["oferta", "angulo"]
MODELOS = ["vsl", "quiz", "advertorial", "tsl", "webinar", "direct"]
FORMATOS = ["ebook", "curso", "comunidade", "planilha", "fisico", "app",
            # em uso no vault, ainda fora da lista original do Schema:
            "pdf", "servico-digital", "area-membros"]
COLETAS = ["ok", "parcial", "sem-coleta"]

CAMPOS_NUMERICOS = [
    "ticket_frente", "ticket_bump", "ticket_upsell", "ticket_medio_est", "margem_est",
    "s_ticket", "s_lucro", "s_replica", "s_saturacao", "rodadas_vista", "dias_no_ar",
    "criativos_ultima", "criativos_delta", "ra_reclamacoes", "prioridade",
]
CAMPOS_LISTA = ["plataforma_ads", "modelo", "formato_entrega", "gateways_detectados",
                "ra_plataformas", "tags"]
CAMPOS_DATA = ["visto_primeiro", "visto_ultimo", "ra_primeira_reclamacao", "ra_checado"]
CAMPOS_BOOL = ["tem_recorrencia", "unfunnelizer_capturado", "bump_oculto", "upsell_oculto"]

RE_DATA = re.compile(r"^\d{4}-\d{2}-\d{2}$")
RE_SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


# ---------------------------------------------------------------------------
# Score e decisao (Scoring.md — mesma formula das Bases do Painel)
# ---------------------------------------------------------------------------

def num(v, padrao=0.0):
    if isinstance(v, bool):
        return float(v)
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return float(str(v).strip())
    except (TypeError, ValueError):
        return padrao


def score(o: dict) -> float:
    s = (num(o.get("s_lucro")) * 35 + num(o.get("s_replica")) * 30
         + num(o.get("s_ticket")) * 20 + num(o.get("s_saturacao")) * 15) / 100
    return round(s, 2)


def decisao(o: dict) -> str:
    """REPLICAR / observar / descartar — o corte so vale para classe oferta (adendo 29/08)."""
    if o.get("classe") == "angulo":
        return "padrao"
    s = score(o)
    if s >= 7.5 and num(o.get("s_replica")) >= 7:
        return "replicar"
    if s >= 6:
        return "observar"
    return "descartar"


# ---------------------------------------------------------------------------
# Parser de frontmatter
# ---------------------------------------------------------------------------

RE_FM = re.compile(r"^﻿?---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(?:\r?\n|$)(.*)$", re.DOTALL)
RE_CHAVE = re.compile(r"^([A-Za-z0-9_\-]+)[ \t]*:(.*)$")


def _tirar_comentario(v: str) -> str:
    """Remove ` # comentario` fora de aspas (ex.: `dias_no_ar: 0  # nao derivavel`)."""
    dentro = None
    for i, ch in enumerate(v):
        if dentro:
            if ch == dentro:
                dentro = None
        elif ch in ("'", '"'):
            if i == 0 or v[i - 1] in " \t[,":
                dentro = ch
        elif ch == "#" and i > 0 and v[i - 1] in " \t":
            return v[:i].rstrip()
    return v


def _split_inline(inner: str):
    itens, atual, dentro = [], [], None
    for ch in inner:
        if dentro:
            atual.append(ch)
            if ch == dentro:
                dentro = None
        elif ch in ("'", '"'):
            dentro = ch
            atual.append(ch)
        elif ch == ",":
            itens.append("".join(atual))
            atual = []
        else:
            atual.append(ch)
    itens.append("".join(atual))
    return [i.strip() for i in itens if i.strip()]


def _escalar(v: str):
    v = v.strip()
    if v == "":
        return ""
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        try:
            return json.loads(v)
        except ValueError:
            return v[1:-1]
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1].replace("''", "'")
    if v in ("null", "Null", "NULL", "~"):
        return None
    if v in ("true", "True", "TRUE"):
        return True
    if v in ("false", "False", "FALSE"):
        return False
    if v.startswith("[") and v.endswith("]"):
        return [_escalar(i) for i in _split_inline(v[1:-1])]
    if re.fullmatch(r"-?\d+", v):
        try:
            return int(v)
        except ValueError:
            return v
    if re.fullmatch(r"-?\d+\.\d+", v):
        try:
            return float(v)
        except ValueError:
            return v
    return v


def parse_frontmatter(texto: str):
    """Devolve (dados, corpo, info). info = {"tem_fm": bool, "estilo": str, "erros": [..]}.

    estilo: "canonico" | "pyyaml" (listas em bloco, aspas simples ou null) | "sem-fm".
    Nunca levanta excecao: linha que nao entende vira erro em info["erros"].
    """
    m = RE_FM.match(texto)
    if not m:
        return {}, texto, {"tem_fm": False, "estilo": "sem-fm", "erros": []}
    fm_txt, corpo = m.group(1), m.group(2)
    dados, erros = {}, []
    estilo = "canonico"
    chave_lista = None          # chave vazia que pode estar abrindo uma lista em bloco
    provisorias, com_itens = set(), set()
    for n, linha in enumerate(fm_txt.splitlines(), start=2):
        if not linha.strip() or linha.lstrip().startswith("#"):
            continue
        item = re.match(r"^[ \t]*-(?:[ \t]+(.*))?$", linha)
        if item and chave_lista is not None:
            dados[chave_lista].append(_escalar(_tirar_comentario(item.group(1) or "")))
            com_itens.add(chave_lista)
            estilo = "pyyaml"
            continue
        mk = RE_CHAVE.match(linha)
        if not mk:
            erros.append("linha %d nao reconhecida: %s" % (n, linha.strip()[:80]))
            continue
        chave, bruto = mk.group(1), _tirar_comentario(mk.group(2).strip())
        if bruto == "":
            dados[chave] = []
            provisorias.add(chave)
            chave_lista = chave
            continue
        chave_lista = None
        valor = _escalar(bruto)
        if valor is None or bruto[:1] == "'":
            estilo = "pyyaml"
        dados[chave] = valor
    # chave vazia sem itens abaixo e campo sem valor, nao lista vazia
    for k in provisorias - com_itens:
        dados[k] = ""
    return dados, corpo, {"tem_fm": True, "estilo": estilo, "erros": erros}


# ---------------------------------------------------------------------------
# Serializacao canonica (identica a do sync_vault.py)
# ---------------------------------------------------------------------------

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
        return "[" + ", ".join(_item_lista(v) for v in val if v not in (None, "")) + "]"
    s = str(val)
    if key in QUOTE_KEYS:
        return json.dumps(s, ensure_ascii=False)
    if key in BARE_KEYS and re.fullmatch(r"[A-Za-z0-9_\-./]+", s):
        return s
    if re.search(r'[:#\[\]{}",\']', s) or " " in s or s[:1] in "-&*!|>%@`":
        return json.dumps(s, ensure_ascii=False)
    return s


def _item_lista(v):
    s = str(v).lower() if isinstance(v, bool) else str(v)
    if re.search(r"[,\[\]{}\"':#]", s) or s != s.strip():
        return json.dumps(s, ensure_ascii=False)
    return s


def serialize_frontmatter(dados: dict, ordem=None) -> str:
    ordem = list(ordem or [])
    chaves = [k for k in ordem if k in dados] + [k for k in dados if k not in ordem]
    linhas = ["---"]
    for k in chaves:
        v = yaml_value(k, dados[k])
        linhas.append(("%s: %s" % (k, v)).rstrip() if v != "" else "%s: " % k)
    linhas.append("---")
    return "\n".join(linhas)


def ordem_para(tipo: str):
    return {
        "oferta": FIELD_ORDER,
        "observacao": OBSERVACAO_FIELD_ORDER,
        "radar": RADAR_FIELD_ORDER,
        "rodada": RODADA_FIELD_ORDER,
    }.get(tipo)


def normalizar_dados(dados: dict) -> dict:
    """Coage tipos do contrato: listas sao listas, numeros sao numeros, datas sem aspas."""
    d = dict(dados)
    for k in CAMPOS_LISTA:
        if k in d:
            v = d[k]
            if v in (None, ""):
                d[k] = []
            elif not isinstance(v, list):
                d[k] = [v]
    for k in CAMPOS_NUMERICOS:
        if k in d and d[k] not in (None, "") and not isinstance(d[k], bool):
            n = num(d[k], None)
            if n is not None:
                d[k] = int(n) if float(n).is_integer() else n
    for k in list(d):
        if d[k] is None:
            d[k] = ""
    return d


# ---------------------------------------------------------------------------
# Leitura do vault
# ---------------------------------------------------------------------------

PASTAS_IGNORADAS = {"_arquivo", "_to_delete", "Templates", "dashboard", ".git", ".obsidian",
                    ".trash", "node_modules"}


def ler_nota(caminho: Path):
    texto = caminho.read_text(encoding="utf-8", errors="replace")
    dados, corpo, info = parse_frontmatter(texto)
    return dados, corpo, info


def notas(vault: Path, pasta: str, recursivo=False):
    base = vault / pasta
    if not base.is_dir():
        return []
    it = base.rglob("*.md") if recursivo else base.glob("*.md")
    return sorted(p for p in it if not any(part in PASTAS_IGNORADAS for part in p.relative_to(vault).parts[:-1]))


def reescrever_frontmatter(caminho: Path, dados: dict, ordem=None) -> bool:
    """Troca so o bloco de frontmatter, preservando o corpo byte a byte."""
    texto = caminho.read_text(encoding="utf-8")
    m = RE_FM.match(texto)
    corpo = m.group(2) if m else texto
    novo = serialize_frontmatter(dados, ordem) + "\n" + corpo
    if novo == texto:
        return False
    escrever_texto(caminho, novo)
    return True


def escrever_texto(caminho: Path, texto: str):
    """Escrita por truncamento. No VM do Cowork, unlink/rename sobre arquivo existente pode
    ser negado; abrir com 'w' (O_TRUNC) sempre funciona."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as f:
        f.write(texto)


# ---------------------------------------------------------------------------
# CLI de manutencao
# ---------------------------------------------------------------------------

def _cmd_normalizar(vault: Path, aplicar: bool):
    alvos = []
    for pasta in ("Ofertas", "Observacoes", "Radar", "Radar/rodadas"):
        for p in notas(vault, pasta):
            dados, corpo, info = ler_nota(p)
            if not info["tem_fm"]:
                continue
            tipo = dados.get("tipo")
            ordem = ordem_para(tipo)
            if ordem is None:
                continue
            canon = serialize_frontmatter(normalizar_dados(dados), ordem)
            atual = RE_FM.match(p.read_text(encoding="utf-8"))
            bloco_atual = "---\n" + atual.group(1) + "\n---" if atual else ""
            if info["estilo"] != "canonico" or info["erros"]:
                alvos.append((p, dados, ordem, info))
            elif bloco_atual.strip() != canon.strip() and info["estilo"] == "pyyaml":
                alvos.append((p, dados, ordem, info))
    for p, dados, ordem, info in alvos:
        rel = p.relative_to(vault)
        extra = (" | erros: " + "; ".join(info["erros"])) if info["erros"] else ""
        if aplicar:
            reescrever_frontmatter(p, normalizar_dados(dados), ordem)
            print("normalizado: %s (%s)%s" % (rel, info["estilo"], extra))
        else:
            print("fora do formato canonico: %s (%s)%s" % (rel, info["estilo"], extra))
    if not alvos:
        print("todas as notas ja estao no formato canonico")
    elif not aplicar:
        print("\n%d nota(s). Rode com --aplicar para reescrever so o frontmatter." % len(alvos))


def main(argv=None):
    import argparse
    ap = argparse.ArgumentParser(description="Manutencao do vault Radar Low Ticket")
    sub = ap.add_subparsers(dest="cmd")
    n = sub.add_parser("normalizar", help="reescreve frontmatter fora do formato canonico")
    n.add_argument("--aplicar", action="store_true")
    n.add_argument("--vault", default=str(Path(__file__).resolve().parent.parent))
    args = ap.parse_args(argv)
    if args.cmd == "normalizar":
        _cmd_normalizar(Path(args.vault).resolve(), args.aplicar)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
