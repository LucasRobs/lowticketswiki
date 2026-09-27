#!/bin/bash
# Radar Low Ticket — publica o vault no GitHub (a Vercel republica o dashboard sozinha).
# Dois cliques no Finder. Exporta os dados do dashboard, commita o que estiver pendente,
# junta o que houver de novo no GitHub e envia.
cd "$(dirname "$0")/.." || exit 1
echo "Radar Low Ticket — publicando $(pwd)"
echo
if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 nao encontrado. Instale as ferramentas de linha de comando: xcode-select --install"
else
  python3 _meta/publicar.py "$@"
fi
echo
read -r -p "Pronto. Enter para fechar..." _
