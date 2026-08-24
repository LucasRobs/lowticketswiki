---
tipo: oferta
slug: curso-aiva
nome: "Curso AIVA"
nicho: ia-ferramentas
sub_nicho: curso-de-ia
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=curso%20AIVA&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.85
modelo: [vsl]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 0
s_lucro: 6
s_replica: 5
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-24
visto_ultimo: 2026-08-24
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/curso-aiva"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 2026-08-23
ra_checado: 2026-08-24
veredito: observar
prioridade: 0
tags: [oferta, lowticket]
---

# Curso AIVA

Kirvano, reclamacao lida em 24/08. Compra em **18/06/2026** — **67 dias de venda medidos**, a segunda maior idade medida do vault depois de [[unlovable]] (149 dias).

Sessenta e sete dias e o sinal aqui. Pelo `Scoring.md`, tempo no ar e o proxy mais confiavel de lucro, e 67 dias de operacao com cancelamento pedido "dentro do prazo legal" indica um funil que continua rodando. `s_lucro: 6`.

O que derruba: `s_saturacao: 3` — curso de IA e o nicho mais lotado do momento — e `s_replica: 5`, porque curso de IA exige atualizacao constante para nao ficar obsoleto em semanas, o que e producao continua, nao entrega unica.

`s_ticket: 0`: valor nao citado. Sentinela.

Nota de cautela: "AIVA" tambem e nome de ferramenta de musica com IA de terceiro. Antes de tratar como oferta propria, confirmar se nao e mais um caso de revenda de assinatura alheia — mesmo padrao de [[capcut-pro-revenda]], descoberto na mesma lista da Kirvano hoje.


## Historico
```base
filters:
  and:
    - 'note.tipo == "observacao"'
    - 'note.slug == this.slug'
views:
  - type: table
    name: Snapshots
    order:
      - note.data
      - note.ra_reclamacoes
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
