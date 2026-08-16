#!/usr/bin/env bash
# Commita a rodada do dia. Rode DEPOIS que a skill terminar de escrever.
# Uso: ./_meta/radar-commit.sh [YYYY-MM-DD]
set -uo pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$VAULT"
DIA="${1:-$(date +%F)}"

# --- Sanea locks orfaos -------------------------------------------------
# Quando o git roda por um agente na nuvem (device_bash), ele nao consegue
# apagar os proprios .lock e o commit seguinte trava com "Another git process
# seems to be running". rm falha, mv funciona: varremos por mv.
sweep_locks() {
  local n=0
  while IFS= read -r -d '' lock; do
    mv -f "$lock" "$VAULT/_to_delete/$(basename "$lock").$$.$RANDOM" 2>/dev/null \
      && n=$((n+1)) || rm -f "$lock" 2>/dev/null
  done < <(find .git -name '*.lock' -print0 2>/dev/null)
  [ "$n" -gt 0 ] && echo "(limpei $n lock(s) orfao(s))"
  # objetos temporarios abandonados: mesmo tratamento
  find .git/objects -name 'tmp_obj_*' -exec mv -f {} "$VAULT/_to_delete/" \; 2>/dev/null \
    || find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null
  return 0
}

mkdir -p "$VAULT/_to_delete"
sweep_locks

git add -A 2>/dev/null

if git diff --cached --quiet; then
  echo "nada mudou em $DIA — sem commit"
  sweep_locks
  exit 0
fi

NOVAS=$(git diff --cached --name-only --diff-filter=A -- 'Ofertas/' | wc -l | tr -d ' ')
ALTER=$(git diff --cached --name-only --diff-filter=M -- 'Ofertas/' | wc -l | tr -d ' ')
SNAPS=$(git diff --cached --name-only --diff-filter=A -- 'Observacoes/' | wc -l | tr -d ' ')

git commit -q -m "radar $DIA: +${NOVAS} novas, ${ALTER} atualizadas, ${SNAPS} snapshots" 2>/dev/null
RC=$?
git tag -f "radar-$DIA" -m "rodada $DIA" >/dev/null 2>&1
sweep_locks

if [ "$RC" -eq 0 ]; then
  echo "commit: radar $DIA (+${NOVAS} novas, ${ALTER} atualizadas, ${SNAPS} snapshots)"
else
  echo "FALHA no commit — rode 'git status' no vault"; exit 1
fi
