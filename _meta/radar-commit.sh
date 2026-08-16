#!/usr/bin/env bash
# Commita a rodada do dia. Rode DEPOIS que a skill terminar de escrever.
# Uso: ./_meta/radar-commit.sh [YYYY-MM-DD]
set -euo pipefail

VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$VAULT"
DIA="${1:-$(date +%F)}"

git add -A

if git diff --cached --quiet; then
  echo "nada mudou em $DIA — sem commit"
  exit 0
fi

NOVAS=$(git diff --cached --name-only --diff-filter=A -- 'Ofertas/' | wc -l | tr -d ' ')
ALTER=$(git diff --cached --name-only --diff-filter=M -- 'Ofertas/' | wc -l | tr -d ' ')
SNAPS=$(git diff --cached --name-only --diff-filter=A -- 'Observacoes/' | wc -l | tr -d ' ')

git commit -q -m "radar $DIA: +${NOVAS} novas, ${ALTER} atualizadas, ${SNAPS} snapshots"
git tag -f "radar-$DIA" -m "rodada $DIA" >/dev/null 2>&1 || true
echo "commit: radar $DIA (+${NOVAS} novas, ${ALTER} atualizadas, ${SNAPS} snapshots)"
