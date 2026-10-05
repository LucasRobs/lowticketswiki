---
tipo: moc
tags: [moc]
atualizado: 2026-10-05
---
# Início — mapa do vault

Porta de entrada. A leitura do dia está no [[Painel]]; como o vault funciona está no [[README]].

## Operação diária
- **[[dashboard/README|Dashboard]]** — o site na Vercel com todas as ofertas mineradas, ao vivo (fonte: este vault)
- [[Painel]] — leitura consolidada + rankings vivos
- Rodadas: `Radar/YYYY-MM-DD.md` (última: [[2026-10-05]]) · cada passada da tarefa agendada em `Radar/rodadas/` (tabela no fim desta nota) · exports da skill em `Radar/exports/` · planilha acumulada `Radar/radar-low-ticket.xlsx`
- Contratos: [[Schema]] · [[Scoring]] · [[Pipeline]] · publicar uma passada: `python3 _meta/publicar.py --achados <json>` · prompts das tarefas agendadas: [[Tarefa-agendada]] (passadas 6x/dia) · [[Tarefa-diaria]] (rodada diária 23h30)

## Visões (Bases)
- [[Ofertas.base|Ofertas]] — tudo, ranqueado por score
- [[Replicaveis.base|Replicáveis]] — o que passa no corte
- [[Movimento.base|Movimento]] — quem acelerou / esfriou / sumiu
- [[Radar-Log.base|Radar-Log]] — histórico das rodadas
- [[Observacoes.base|Observações]] · [[Mineracao.base|Mineração]]

## Análises e shortlists
- **[[2026-09-27 -- novidades-22-a-26-09]] — tudo que as rodadas de 22 a 26/09 acharam, separado pelo que fazer**
- [[2026-09-26 -- ofertas-escaladas]] — ranking de escala + anúncios conferidos em 26/09
- [[2026-09-24 -- ofertas-mais-escaladas]] — quem provou escala (tempo no ar, criativos, RA)
- [[2026-09-14 -- shortlist-lps-replicaveis]] — 10 LPs pra replicar
- [[2026-09-13 -- pdf-clonaveis]] — ofertas de arquivo que um agente de IA produz de ponta a ponta
- [[2026-09-06 -- shortlist-danca]]
- [[2026-08-31 -- shortlist-infantil-replicaveis]]
- [[2026-08-30 -- shortlist-infantil]]
- [[2026-08-21 -- shortlist-replicaveis]]
- [[analise_top_ofertas]] · [[quick_reference_ofertas]] · [[igreen-paginas-criativos]]

## Nichos
- [[alma-gemea]] · [[mulher-crista-saude-mental]]

## Ideias e modelos
- [[IDEA]]
- Templates: [[T-Oferta]] · [[T-Observacao]] · [[T-Radar-Diario]]

## Shortlists (automático)
```base
filters:
  and:
    - 'note.tipo == "shortlist"'
views:
  - type: table
    name: Shortlists
    order:
      - file.name
      - note.data
      - note.titulo
    sort:
      - property: note.data
        direction: DESC
```

## Passadas da tarefa agendada (automático)
```base
filters:
  and:
    - 'note.tipo == "rodada"'
views:
  - type: table
    name: Passadas
    order:
      - file.name
      - note.data
      - note.hora
      - note.gateways
      - note.paginas
      - note.coleta
    sort:
      - property: file.name
        direction: DESC
```
