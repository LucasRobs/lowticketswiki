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

1. A skill `radar-low-ticket` roda e minera o mercado.
2. Para cada oferta encontrada:
   - já existe em `Ofertas/`? → atualiza `visto_ultimo`, `rodadas_vista`, `criativos_*`, recalcula `status`
   - é nova? → cria a nota de oferta a partir de `Templates/T-Oferta.md`
   - sempre → grava um snapshot novo em `Observacoes/`
3. Ofertas não vistas hoje: `status` decai (ver `_meta/Scoring.md`).
4. Grava a nota da rodada em `Radar/YYYY-MM-DD.md`.
5. `_meta/radar-commit.sh` commita tudo — o `git diff` entre dois dias é o relatório
   de movimento mais honesto que existe.

## Onde olhar

Comece por [[Inicio]] — o mapa do vault.


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

# lowticketswiki

## Outras pastas

| Pasta | O que tem |
|---|---|
| `Analises/` | Análises avulsas e shortlists (`tipo: shortlist`) — top ofertas, quick reference, igreen, shortlists de LPs/infantil/dança |
| `Radar/rodadas/` | Uma nota por passada da tarefa agendada (`tipo: rodada`, `YYYY-MM-DD -- HHMM.md`), com gateways, páginas e se a coleta funcionou. A nota do dia em `Radar/` consolida as passadas |
| `Radar/exports/` | CSV, favoritos e painéis HTML gerados pela skill a cada rodada. A planilha acumulada fica em `Radar/radar-low-ticket.xlsx`; o JSON bruto em `Radar/dados/` |
| `Nichos/` | Notas de nicho |
| `Ativos/` | Ativos capturados pelo unFunnelizer |
| `Claude outputs/` | Planilhas e HTMLs entregues fora da rodada diária |
| `_meta/` | Contratos (Schema, Scoring, Pipeline) e scripts ativos: `sync_vault.py`, `collect_complaints.py`, `radar-commit.sh`, `radar-diff.sh` |
| `_arquivo/mineracao-2026-08/` | Scripts, JSONs e debug da mineração manual de ago/set. Só histórico — nada do ciclo diário depende disso |
| `_to_delete/` | Quarentena (fora do git). Esvaziada em 27/09; pode apagar de novo quando encher |
