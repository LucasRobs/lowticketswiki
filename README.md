# Radar Low Ticket — manual de operação

Vault de inteligência de mercado para ofertas low ticket. Roda todo dia, compara com o
histórico e mostra **movimento**, não só uma lista.

## O modelo de dados (leia isto antes de mudar qualquer coisa)

O vault separa duas coisas que quase todo sistema de radar mistura — e é essa separação
que permite medir tendência:

| Pasta | O que é | Muda? |
|---|---|---|
| `Ofertas/` | **Entidade.** Uma nota por oferta, para sempre. Guarda o estado atual e os scores. | Sim, é atualizada a cada rodada |
| `Observacoes/` | **Fato datado.** Um snapshot por oferta por dia. O que foi visto naquele dia. | Nunca. É append-only |
| `Radar/` | **Rodada.** Uma nota por dia com o resumo da varredura e o diff. | Nunca |

Se você só tivesse `Ofertas/`, saberia *o que existe*. Com `Observacoes/` você sabe
*o que está acelerando* — que é a informação que vale dinheiro.

## Ciclo diário

1. A tarefa agendada (6x/dia) roda a skill `radar-low-ticket` e minera o mercado.
2. Ela grava os achados em `Radar/dados/achados-AAAA-MM-DD-HHMM.json` e roda **um comando só**:
   `python3 _meta/publicar.py --achados Radar/dados/achados-AAAA-MM-DD-HHMM.json`
   - já existe em `Ofertas/`? → atualiza `visto_ultimo`, `rodadas_vista`, `ra_*`, `status`
   - é nova? → cria a nota de oferta (mesmo contrato de `Templates/T-Oferta.md`)
   - sempre → grava um snapshot novo em `Observacoes/` e a nota da passada em `Radar/rodadas/`
   - regenera `dashboard/data/` e commita (no Mac, também envia pro GitHub)
3. Ofertas não vistas hoje: `status` decai (ver `_meta/Scoring.md`) — hoje só em passada de manutenção.
4. A nota do dia fica em `Radar/YYYY-MM-DD.md`, com a lista das passadas.
5. O push pro GitHub republica o **dashboard** na Vercel. O `git diff` entre dois dias continua
   sendo o relatório de movimento mais honesto que existe (`_meta/radar-diff.sh`).

## Onde olhar

Comece por [[Inicio]] — o mapa do vault.

**Dashboard (site na Vercel)** — tudo o que já foi minerado, com busca, filtros, a nota de
cada oferta, as rodadas e a qualidade dos dados; atualiza sozinho a cada mineração publicada.
Como publicar e como funciona: [[dashboard/README|dashboard/README]].


Abra `Bases/` — quatro visões:

- **Ofertas.base** — tudo, ranqueado por score composto
- **Replicaveis.base** — o funil de decisão: só o que passa no corte de replicabilidade
- **Movimento.base** — quem acelerou, quem esfriou, quem sumiu
- **Radar-Log.base** — histórico das rodadas

> Bases é plugin **core** do Obsidian. Se as views não abrirem:
> Configurações → Plugins principais → ative **Bases**.

## Contratos

- `_meta/Schema.md` — as propriedades exatas que a skill deve gravar
- `_meta/Scoring.md` — a rubrica dos 4 eixos e como o score é calculado

## Outras pastas

| Pasta | O que tem |
|---|---|
| `Analises/` | Análises avulsas e shortlists (`tipo: shortlist`) — top ofertas, quick reference, igreen, shortlists de LPs/infantil/dança |
| `Radar/rodadas/` | Uma nota por passada da tarefa agendada (`tipo: rodada`, `YYYY-MM-DD -- HHMM.md`), com gateways, páginas e se a coleta funcionou. A nota do dia em `Radar/` consolida as passadas |
| `Radar/exports/` | CSV, favoritos e painéis HTML gerados pela skill a cada rodada. A planilha acumulada fica em `Radar/radar-low-ticket.xlsx`; o JSON bruto em `Radar/dados/` |
| `Nichos/` | Notas de nicho |
| `Ativos/` | Ativos capturados pelo unFunnelizer |
| `Claude outputs/` | Planilhas e HTMLs entregues fora da rodada diária |
| `dashboard/` | O site (Vercel, Root Directory = `dashboard`). `dashboard/data/` é **gerado** do vault — não editar |
| `_meta/` | Contratos (Schema, Scoring, Pipeline) e scripts: `publicar.py` (comando único do pipeline), `exportar_dados.py` (vault → dashboard + validação), `vault.py` (parser/formato canônico), `sync_vault.py`, `collect_complaints.py`, `radar-commit.sh`, `radar-diff.sh`, `hooks/pre-commit`, `Publicar.command` (Mac) |
| `_arquivo/mineracao-2026-08/` | Scripts, JSONs e debug da mineração manual de ago/set. Só histórico — nada do ciclo diário depende disso |
| `_arquivo/exports-antigos/` | Exports avulsos substituídos pelo dashboard (`ofertas-export`, `export-planilha`) |
| `_to_delete/` | Quarentena (fora do git). Esvaziada em 27/09; pode apagar de novo quando encher |

## Comandos

| Quero… | Rodar (na pasta `lowticket`) |
|---|---|
| Gravar uma passada de mineração e publicar | `python3 _meta/publicar.py --achados Radar/dados/achados-….json` |
| Só atualizar o dashboard e commitar o que mudou | `python3 _meta/publicar.py` |
| Validar o vault (vocabulário, datas, slugs, regra do s_lucro) | `python3 _meta/publicar.py --verificar` |
| Padronizar frontmatter vindo de outra ferramenta | `python3 _meta/vault.py normalizar --aplicar` |
| Enviar pro GitHub pelo Finder | dois cliques em `_meta/Publicar.command` |
| Ver o site localmente | `cd dashboard && node dev/servidor.js` |
