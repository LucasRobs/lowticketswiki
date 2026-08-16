#!/usr/bin/env bash
# O que mudou entre duas rodadas.
# Uso: ./_meta/radar-diff.sh 2026-08-14 2026-08-16
#      ./_meta/radar-diff.sh            (ultima rodada vs anterior)
set -euo pipefail
VAULT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$VAULT"

if [ $# -eq 2 ]; then
  A="radar-$1"; B="radar-$2"
else
  A=$(git log --format=%H -n 2 | tail -1)
  B=$(git log --format=%H -n 1)
fi

echo "=== OFERTAS NOVAS ==="
git diff --name-only --diff-filter=A "$A" "$B" -- Ofertas/ | sed 's|Ofertas/||;s|\.md$||'
echo
echo "=== OFERTAS ATUALIZADAS ==="
git diff --name-only --diff-filter=M "$A" "$B" -- Ofertas/ | sed 's|Ofertas/||;s|\.md$||'
echo
echo "=== MUDANCAS DE SCORE / STATUS / CRIATIVOS ==="
git diff -U0 "$A" "$B" -- Ofertas/ \
  | grep -E '^\+\+\+|^[-+](s_|status|criativos_|ticket_|veredito)' \
  | sed 's|^+++ b/Ofertas/|\n## |;s|\.md$||'
