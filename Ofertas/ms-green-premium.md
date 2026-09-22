---
tipo: oferta
classe: oferta
slug: ms-green-premium
nome: "MS GREEN PREMIUM"
nicho: suplementacao-saude
sub_nicho: suplemento-emagrecimento
idioma: pt-BR
pais: BR
plataforma_ads: []
checkout: perfectpay
url_pagina: ""
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=MS%20Green%20Premium&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [fisico]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 2
s_saturacao: 5
status: nova
visto_primeiro: 2026-09-22
visto_ultimo: 2026-09-22
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/ms-green-premium"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [perfectpay]
ra_primeira_reclamacao:
ra_checado: 2026-09-22
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# MS GREEN PREMIUM

## Angulo
Suplemento (provavel emagrecimento/saude), formato fisico — entrega logistica, nao digital.

## Funil
anuncio -> pagina -> compra -> reclamante alega propaganda enganosa, arrependimento.

## Por que funciona
Ainda nao avaliado — uma mencao apenas, sinal fraco.

## O que copiar / o que evitar
Produto fisico com logistica real: teto baixo de `s_replica` por padrao do vault (produto fisico penaliza replicabilidade). Nao e prioridade de clonagem.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout (PerfectPay), 1 mencao em amostra parcial (15 paginas) de 22/09.
- **Faltando:** quase tudo — sinal unico (`fria`), sem Etapa 1. Manter em observacao passiva.
- **Nota de metodo:** mesma limitacao de `boss-ia-trade` — captura via skill sincronizada, sem dedup por URL/ID.

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
