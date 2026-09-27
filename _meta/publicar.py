#!/usr/bin/env python3
"""
publicar.py — o comando unico do pipeline do Radar Low Ticket.

Toda mineracao termina aqui. Ele grava no vault, atualiza os dados do dashboard e
commita — e, no Mac, ja envia pro GitHub (a Vercel republica o site sozinha).

    python3 _meta/publicar.py --achados Radar/dados/achados-2026-09-27-1300.json
        grava a passada: sync_vault.py (Ofertas/, Observacoes/, Radar/) + nota em
        Radar/rodadas/ + dados do dashboard + commit (+ push no Mac)

    python3 _meta/publicar.py
        so atualiza os dados do dashboard e commita o que estiver pendente (+ push no Mac)

    python3 _meta/publicar.py --verificar      valida o vault e lista erros/avisos, sem gravar
    python3 _meta/publicar.py --instalar       (re)instala o hook de pre-commit

Opcoes: --sem-git (nao commita), --sem-push, --push (tenta push mesmo fora do Mac),
        --mensagem "texto do commit", --leitura "texto" (reescreve a Leitura do dia; so manual)

Formato do --achados: o JSON da skill radar-low-ticket (data_varredura, gateways, achados)
com um bloco opcional "passada" — ver _meta/Schema.md, adendo de 27/09:

    "passada": {"hora": "13:00", "gateways": ["perfectpay", "cakto"], "paginas": 12,
                "coleta": "ok", "relatorio": "markdown curto: Quentes / Mornas / Leitura"}

Onde roda:
  - no Mac (Terminal, Publicar.command, hook do Obsidian Git): commit + push;
  - no VM do Cowork (tarefa agendada / sessao assistida): commit local. O VM nao alcanca o
    GitHub; quem envia e o Obsidian Git (ou o Publicar.command) no Mac.
"""

import argparse
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parent
sys.path.insert(0, str(AQUI))
import vault as V  # noqa: E402
import exportar_dados as E  # noqa: E402

NO_MAC = platform.system() == "Darwin"


def log(msg):
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# Git
# ---------------------------------------------------------------------------

def _env():
    env = dict(os.environ)
    env.update(GIT_OPTIONAL_LOCKS="0", LOWTICKET_SEM_HOOK="1", LC_ALL="C")
    # No Mac, rodando num Terminal (Publicar.command), o git pode pedir usuario/token do GitHub
    # na primeira vez; o macOS guarda no Keychain. Fora disso (VM, hook, agendada), nunca pergunta.
    if not (NO_MAC and sys.stdin.isatty()):
        env["GIT_TERMINAL_PROMPT"] = "0"
    return env


# No VM do Cowork o git nao consegue apagar arquivo: cria objeto por rename (em vez de
# link + unlink, que deixa tmp_obj_* para tras) e nao roda manutencao automatica.
GIT_VM = [] if NO_MAC else ["-c", "core.createObject=rename", "-c", "maintenance.auto=false", "-c", "gc.auto=0"]


def git(*args, timeout=90):
    try:
        r = subprocess.run(["git", *GIT_VM, *args], cwd=str(RAIZ), env=_env(), capture_output=True,
                           text=True, timeout=timeout)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except subprocess.TimeoutExpired:
        return 124, "timeout"
    except FileNotFoundError:
        return 127, "git nao encontrado"
    finally:
        if not NO_MAC:
            varrer_locks()


def varrer_locks(idade_min=0.0):
    """No VM do Cowork o git nao consegue apagar os proprios .lock (unlink negado) e o
    comando seguinte trava com 'Another git process seems to be running'. mv funciona.
    No Mac so removemos lock velho (orfao de uma rodada do VM), nunca um lock vivo."""
    gitdir = RAIZ / ".git"
    if not gitdir.is_dir():
        return 0
    quarentena = RAIZ / "_to_delete"
    n = 0
    agora = time.time()
    alvos = list(gitdir.rglob("*.lock")) + list((gitdir / "objects").rglob("tmp_obj_*"))
    for p in alvos:
        try:
            if idade_min and agora - p.stat().st_mtime < idade_min * 60:
                continue
        except OSError:
            continue
        try:
            p.unlink()
            n += 1
            continue
        except OSError:
            pass
        try:
            quarentena.mkdir(exist_ok=True)
            shutil.move(str(p), str(quarentena / ("%s.%d.%d" % (p.name, os.getpid(), n))))
            n += 1
        except OSError:
            pass
    return n


def instalar_hook(silencioso=False):
    origem = AQUI / "hooks" / "pre-commit"
    destino = RAIZ / ".git" / "hooks" / "pre-commit"
    if not origem.exists() or not (RAIZ / ".git").is_dir():
        return False
    conteudo = origem.read_text(encoding="utf-8")
    atual = destino.read_text(encoding="utf-8") if destino.exists() else None
    if atual != conteudo:
        if atual is not None and "Radar Low Ticket" not in atual:
            log("aviso: .git/hooks/pre-commit ja existe e nao e nosso — nao sobrescrevi")
            return False
        V.escrever_texto(destino, conteudo)
        if not silencioso:
            log("hook de pre-commit instalado (.git/hooks/pre-commit)")
    try:
        os.chmod(str(destino), 0o755)
    except OSError:
        pass
    return True


def contar_staged():
    def n(filtro, pasta):
        _, out = git("diff", "--cached", "--name-only", "--diff-filter=" + filtro, "--", pasta)
        return len([l for l in out.splitlines() if l.strip()])
    return n("A", "Ofertas/"), n("M", "Ofertas/"), n("A", "Observacoes/")


def commitar(mensagem=None, dia=None, hora=None, tag=True, coleta=None):
    rc, _ = git("rev-parse", "--is-inside-work-tree")
    if rc != 0:
        log("git: esta pasta nao e um repositorio — pulei o commit")
        return False
    git("add", "-A")
    rc, _ = git("diff", "--cached", "--quiet")
    if rc == 0:
        log("git: nada novo para commitar")
        return False
    novas, alteradas, snaps = contar_staged()
    dia = dia or V.hoje_local().isoformat()
    if not mensagem:
        if hora and coleta == "sem-coleta":
            mensagem = "radar %s %s: passada sem coleta" % (dia, hora)
        elif hora:
            mensagem = "radar %s %s: +%d novas, %d atualizadas, %d snapshots" % (dia, hora, novas, alteradas, snaps)
        else:
            _, nomes = git("diff", "--cached", "--name-only")
            n_notas = len([l for l in nomes.splitlines() if l.endswith(".md")])
            mensagem = "vault %s: %d nota(s) alterada(s) + dados do dashboard" % (
                V.agora_local().strftime("%Y-%m-%d %H:%M"), n_notas)
    rc, out = git("commit", "-q", "-m", mensagem)
    if rc != 0:
        log("git: FALHA no commit — rode 'git status' na pasta lowticket\n" + out.strip()[-800:])
        return False
    if tag:
        git("tag", "-f", "radar-%s" % dia, "-m", "rodada %s" % dia)
    log("git: commit '%s'" % mensagem)
    return True


def enviar(forcar=False):
    """Push. Se o GitHub tiver commit que o Mac nao tem, faz merge (nunca rebase) e tenta de novo."""
    if not (NO_MAC or forcar):
        rc, out = git("rev-list", "--count", "@{u}..HEAD")
        pend = out.strip() if rc == 0 else "?"
        log("git: push fica para o Mac (%s commit(s) aguardando; o Obsidian Git ou o Publicar.command envia)" % pend)
        return False
    rc, out = git("push", "-q", "origin", "HEAD:main", timeout=300)
    if rc == 0:
        git("fetch", "-q", "origin", "main", timeout=60)
        log("git: enviado para o GitHub — a Vercel publica em ~1 min")
        return True
    if re.search(r"rejected|fetch first|non-fast-forward", out):
        log("git: o GitHub tem commits que este Mac nao tem — juntando (merge)...")
        rc2, out2 = git("pull", "--no-rebase", "--no-edit", "-q", "origin", "main", timeout=120)
        if rc2 != 0:
            git("merge", "--abort")
            log("git: conflito ao juntar com o GitHub. Nada foi perdido; resolva com 'git pull' no Terminal.\n"
                + out2.strip()[-600:])
            return False
        rc, out = git("push", "-q", "origin", "HEAD:main", timeout=300)
        if rc == 0:
            log("git: enviado para o GitHub (apos merge) — a Vercel publica em ~1 min")
            return True
    log("git: push falhou (%s). O commit ficou local; tente de novo mais tarde.\n%s"
        % ("sem rede ou sem credencial" if rc in (124, 128) else "rc=%d" % rc, out.strip()[-500:]))
    return False


# ---------------------------------------------------------------------------
# Passada (nota em Radar/rodadas/) e ingestao dos achados
# ---------------------------------------------------------------------------

def carregar_achados(caminho: Path):
    try:
        payload = json.loads(caminho.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        raise SystemExit("achados invalidos (%s): %s" % (caminho, e))
    if not isinstance(payload, dict) or not isinstance(payload.get("achados", []), list):
        raise SystemExit("achados invalidos: esperado objeto com lista 'achados'")
    faltando = []
    for i, a in enumerate(payload.get("achados", [])):
        for campo in ("produto", "tipo", "gateway"):
            if not str(a.get(campo, "")).strip():
                faltando.append("achados[%d].%s" % (i, campo))
        if a.get("tipo") not in (None, "", "marca", "angulo"):
            faltando.append("achados[%d].tipo deve ser marca|angulo" % i)
    if faltando:
        raise SystemExit("achados invalidos — campos faltando: " + ", ".join(faltando[:12]))
    return payload


def escrever_passada(payload: dict, dia: str, hora: str, origem: str):
    p = payload.get("passada") or {}
    achados = payload.get("achados") or []
    gateways = p.get("gateways")
    if not gateways:
        gateways = [_sv().gateway_slug(g.get("nome", "")) for g in payload.get("gateways", []) if g.get("nome")]
    gateways = [str(g).strip().lower() for g in gateways if str(g).strip()]
    paginas = p.get("paginas")
    if paginas in (None, ""):
        paginas = sum(int(V.num(g.get("paginas_varridas"))) for g in payload.get("gateways", []))
    coleta = p.get("coleta") or ("ok" if achados else "sem-coleta")
    if coleta not in V.COLETAS:
        coleta = "parcial"
    hhmm = hora.replace(":", "")
    destino = RAIZ / "Radar" / "rodadas" / ("%s -- %s.md" % (dia, hhmm))
    if destino.exists():
        log("passada: %s ja existe — mantive (append-only)" % destino.relative_to(RAIZ))
        return destino, coleta, gateways
    fm = {
        "tipo": "rodada", "data": dia, "hora": hora, "gateways": gateways, "paginas": int(V.num(paginas)),
        "coleta": coleta, "radar": "[[%s]]" % dia, "origem": origem,
    }
    relatorio = str(p.get("relatorio") or "").strip()
    if not relatorio:
        linhas = []
        for a in achados[:25]:
            link = a.get("slug_vault") or ""
            nome = "[[%s]]" % link if link else a.get("produto", "")
            linhas.append("- %s — %s · %s" % (nome, a.get("gateway", ""), E.truncar(str(a.get("descricao", "")).strip(), 160)))
        relatorio = "\n".join(linhas) if linhas else "Nenhum achado nesta passada."
    dd, mm, aaaa = dia[8:10], dia[5:7], dia[:4]
    corpo = ("> Registro da passada. Consolidado do dia: [[%s]].\n\n# Rodada — %s/%s/%s · %s Fortaleza\n\n"
             "**Gateways:** %s · **Páginas:** %s · **Coleta:** %s · **Achados:** %d\n\n%s\n"
             % (dia, dd, mm, aaaa, hora, ", ".join(gateways) or "—", fm["paginas"], coleta, len(achados), relatorio))
    V.escrever_texto(destino, V.serialize_frontmatter(fm, V.RODADA_FIELD_ORDER) + "\n" + corpo)
    log("passada: %s (%s, %d achado(s))" % (destino.relative_to(RAIZ), coleta, len(achados)))
    return destino, coleta, gateways


def registrar_no_dia(dia: str, hora: str, coleta: str, n_achados: int, gateways, resumo: str):
    """Acrescenta a passada em '## Passadas do dia' da nota Radar/<dia>.md, se ela existir.
    Passada sem coleta nao cria nota do dia (senao a Radar-Log.base contaria uma rodada vazia)."""
    nota = RAIZ / "Radar" / ("%s.md" % dia)
    if not nota.exists():
        return
    texto = nota.read_text(encoding="utf-8")
    link = "[[%s -- %s]]" % (dia, hora.replace(":", ""))
    if link in texto:
        return
    desc = "%s - %s - %s" % (link, ", ".join(gateways) or "—",
                             ("**sem coleta**" if coleta == "sem-coleta" else "%d achado(s)" % n_achados))
    if resumo:
        desc += " - " + E.truncar(resumo, 140)
    if "## Passadas do dia" in texto:
        m = re.search(r"(## Passadas do dia\n)(.*?)(\n## |\Z)", texto, re.DOTALL)
        bloco = m.group(2).rstrip("\n") + "\n- " + desc + "\n"
        texto = texto[:m.start(2)] + bloco + texto[m.end(2):]
    else:
        texto = texto.rstrip("\n") + "\n\n## Passadas do dia\n- " + desc + "\n"
    V.escrever_texto(nota, texto)


def ingerir(achados_path: Path, leitura: str):
    payload = carregar_achados(achados_path)
    dia = str(payload.get("data_varredura") or "") or V.hoje_local().isoformat()
    if not V.RE_DATA.match(dia):
        raise SystemExit("data_varredura invalida: %r (use AAAA-MM-DD)" % dia)
    p = payload.get("passada") or {}
    hora = str(p.get("hora") or V.agora_local().strftime("%H:%M"))
    if not re.match(r"^\d{2}:\d{2}$", hora):
        raise SystemExit("passada.hora invalida: %r (use HH:MM)" % hora)
    achados = payload.get("achados") or []
    coleta = p.get("coleta") or ("ok" if achados else "sem-coleta")
    origem = str(p.get("origem") or "tarefa agendada")

    if achados and coleta != "sem-coleta":
        cmd = [sys.executable, str(AQUI / "sync_vault.py"), str(achados_path), "--vault", str(RAIZ), "--data", dia]
        if leitura:
            cmd += ["--leitura", leitura]
        r = subprocess.run(cmd, capture_output=True, text=True)
        saida = (r.stdout or "") + (r.stderr or "")
        if r.returncode != 0:
            raise SystemExit("sync_vault.py falhou:\n" + saida[-1500:])
        for linha in saida.strip().splitlines():
            log("sync: " + linha)
        # liga os achados aos slugs que o sync gravou (para a nota da passada linkar certo)
        for a in achados:
            slug = _slug_de(a)
            if slug and (RAIZ / "Ofertas" / ("%s.md" % slug)).exists():
                a["slug_vault"] = slug
    _, coleta_final, gateways = escrever_passada(payload, dia, hora, origem)
    registrar_no_dia(dia, hora, coleta_final, len(achados), gateways, str(p.get("resumo") or ""))
    return dia, hora, coleta_final


_SV = None


def _sv():
    """sync_vault.py carregado como modulo (para reusar slugify, dedup e gateway_slug)."""
    global _SV
    if _SV is None:
        import importlib.util
        spec = importlib.util.spec_from_file_location("sync_vault", str(AQUI / "sync_vault.py"))
        _SV = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(_SV)
    return _SV


def _slug_de(achado: dict):
    # mesma regra do sync_vault: slugify(produto), prefixo angulo- para angulo; dedup por nome
    sv = _sv()
    cand = sv.slugify(achado.get("produto", ""))
    if achado.get("tipo") == "angulo" and not cand.startswith("angulo-"):
        cand = "angulo-" + cand
    return sv.find_existing_slug(RAIZ / "Ofertas", achado.get("produto", ""), cand) or cand


# ---------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="Pipeline do Radar Low Ticket: grava, exporta, commita, envia")
    ap.add_argument("--achados", help="JSON de achados da passada (formato da skill radar-low-ticket)")
    ap.add_argument("--leitura", default="", help="reescreve a 'Leitura da rodada' do dia (uso manual)")
    ap.add_argument("--mensagem", default="", help="mensagem do commit")
    ap.add_argument("--verificar", action="store_true", help="so valida o vault")
    ap.add_argument("--instalar", action="store_true", help="(re)instala o hook de pre-commit e sai")
    ap.add_argument("--sem-git", action="store_true")
    ap.add_argument("--sem-push", action="store_true")
    ap.add_argument("--push", action="store_true", help="tenta push mesmo fora do Mac")
    args = ap.parse_args(argv)

    if args.verificar:
        resumo, rel = E.exportar(RAIZ, RAIZ / "dashboard" / "data", verificar=True)
        E.imprimir(resumo, rel, detalhar=True)
        return 1 if rel.erros else 0

    if NO_MAC:
        varrer_locks(idade_min=10)
    else:
        varrer_locks()
    instalar_hook(silencioso=not args.instalar)
    if args.instalar:
        return 0

    dia = hora = coleta = None
    if args.achados:
        caminho = Path(args.achados)
        if not caminho.is_absolute():
            caminho = (Path.cwd() / caminho) if (Path.cwd() / caminho).exists() else RAIZ / caminho
        dia, hora, coleta = ingerir(caminho, args.leitura)

    resumo, rel = E.exportar(RAIZ, RAIZ / "dashboard" / "data")
    E.imprimir(resumo, rel)

    if args.sem_git:
        return 0
    commitar(args.mensagem or None, dia=dia, hora=hora, tag=bool(args.achados), coleta=coleta)
    if not args.sem_push:
        enviar(forcar=args.push)
    return 0


if __name__ == "__main__":
    sys.exit(main())
