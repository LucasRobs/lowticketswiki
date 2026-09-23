---
tipo: moc
tags: [moc]
atualizado: 2026-09-23
---
# Início — mapa do vault

Porta de entrada. A leitura do dia está no [[Painel]]; como o vault funciona está no [[README]].

## Operação diária
- [[Painel]] — leitura consolidada + rankings vivos
- Rodadas: `Radar/YYYY-MM-DD.md` (última: [[2026-09-23]]) · exports da skill em `Radar/exports/` · planilha acumulada `Radar/radar-low-ticket.xlsx`
- Contratos: [[Schema]] · [[Scoring]] · [[Pipeline]]

## Visões (Bases)
- [[Ofertas.base|Ofertas]] — tudo, ranqueado por score
- [[Replicaveis.base|Replicáveis]] — o que passa no corte
- [[Movimento.base|Movimento]] — quem acelerou / esfriou / sumiu
- [[Radar-Log.base|Radar-Log]] — histórico das rodadas
- [[Observacoes.base|Observações]] · [[Mineracao.base|Mineração]]

## Análises e shortlists
- [[2026-09-14 -- shortlist-lps-replicaveis]] — 10 LPs pra replicar
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
