---
tipo: meta
---

# Dashboard do Radar — o site na Vercel

O site mostra tudo o que o radar já minerou: visão geral, tabela de ofertas com busca e
filtros, a nota completa de cada oferta, as rodadas (com a saúde de cada passada da tarefa
agendada) e a qualidade dos dados. Ele lê **só** `dashboard/data/`, que é gerado a partir das
notas — o vault continua sendo a fonte da verdade. Nada aqui é editado à mão.

## Como uma mineração chega na tela

```
passada da mineração (tarefa agendada ou sessão)
  → python3 _meta/publicar.py --achados <json>
       grava Ofertas/, Observacoes/, Radar/ e Radar/rodadas/   (sync_vault.py)
       gera dashboard/data/*.json                              (exportar_dados.py)
       commit no git
  → push pro GitHub            (Obsidian Git no Mac, ou Publicar.command)
  → Vercel republica           (~1 min, automático a cada push)
  → painel aberto se atualiza  (confere a cada minuto; mostra "Dados atualizados")
```

Editou uma nota à mão no Obsidian? O hook de pre-commit (instalado pelo `publicar.py`)
regenera `dashboard/data/` em todo commit, inclusive nos automáticos do Obsidian Git.

## Publicar na Vercel (uma vez)

1. vercel.com → **Add New… → Project** → importe o repositório `LucasRobs/lowticketswiki`.
2. Em **Root Directory**, escolha `dashboard`. O resto já vem do `vercel.json`
   (sem build, sem dependências, dados fora da pasta pública).
3. Recomendado: **Environment Variables** → `DASHBOARD_SENHA` = uma senha sua.
   Com ela, o painel pede senha e os dados só saem da API para quem entrou.
   Sem ela, o painel fica aberto (o rodapé avisa "Acesso aberto").
4. **Deploy.** A partir daí, cada push no `main` republica sozinho.

> O repositório no GitHub está **público**: o vault inteiro pode ser lido lá, com ou sem
> senha no painel. Para fechar de verdade: GitHub → Settings → Danger Zone → Change
> visibility → Private. A Vercel continua funcionando com repositório privado da sua conta.

## Deixar o envio pro GitHub automático (Mac)

O agente que minera roda num ambiente que não alcança o GitHub: ele grava e commita no vault,
e quem envia é o Mac. Duas formas:

**Obsidian Git (recomendado — envia sozinho enquanto o Obsidian estiver aberto)**

1. Obsidian → Configurações → Plugins da comunidade → Procurar → **Git** (Vinzent03) → Instalar → Ativar.
2. Nas opções do plugin:
   - *Advanced → Custom base path (Git repository path)*: `lowticket`
   - *Auto commit-and-sync interval (minutes)*: `10`
   - *Pull on startup*: ligado · *Push on commit-and-sync*: ligado
3. Primeira vez: o Mac precisa ter permissão de push. No Terminal:
   `cd ~/Documents/"Obsidian Vault"/lowticket && git push`. Se pedir senha, use um token do
   GitHub (Settings → Developer settings → Fine-grained tokens → só este repositório →
   *Contents: Read and write*). O macOS guarda no Keychain e não pergunta de novo.

**Publicar.command (manual)** — dois cliques em `_meta/Publicar.command` no Finder: exporta,
commita, junta o que tiver no GitHub e envia.

## Rodar localmente (opcional)

```
cd dashboard
node dev/servidor.js     # http://localhost:3000  (DASHBOARD_SENHA=x para testar a senha)
node dev/testar.js       # 20 verificações da API e dos dados
```

Não precisa de `npm install` — não há dependências. Se um dia instalar algo aqui, adicione
`lowticket/dashboard/node_modules` em *Configurações → Arquivos e links → Arquivos excluídos*
do Obsidian, senão ele indexa milhares de arquivos.

## O que tem aqui

| Caminho | O que é |
|---|---|
| `public/` | o site: `index.html`, `assets/estilo.css`, `assets/app.js` e `assets/js/` (JS puro, sem build) |
| `api/dados.js` | entrega os JSON de `data/` (só depois de checar a sessão) |
| `api/sessao.js` + `lib/sessao.js` | senha opcional (`DASHBOARD_SENHA`), cookie assinado de 30 dias |
| `data/` | **gerado** por `_meta/exportar_dados.py` — `versao.json`, `painel.json`, `rodadas.json`, `ofertas/<slug>.json` |
| `dev/` | servidor local e testes |
| `vercel.json` | configuração do deploy |
