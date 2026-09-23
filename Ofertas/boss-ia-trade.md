---
tipo: oferta
classe: oferta
slug: boss-ia-trade
nome: "BOSS IA TRADE"
nicho: trading-automatizado
sub_nicho: robo-trading
idioma: pt-BR
pais: BR
plataforma_ads: []
checkout: perfectpay
url_pagina: ""
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=BOSS%20IA%20TRADE&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 3
s_replica: 3
s_saturacao: 5
status: nova
visto_primeiro: 2026-09-22
visto_ultimo: 2026-09-22
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/boss-ia-trade"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [perfectpay]
ra_primeira_reclamacao:
ra_checado: 2026-09-22
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# BOSS IA TRADE

## Angulo
App de "IA de trading" — promete operar/automatizar trades. Nicho de trading + IA, mesmo cluster de Luna IA e Trendy IA vistos em rodadas anteriores no Projeto Claude (não capturadas como notas individuais ainda).

## Funil
anuncio -> app -> cliente relata que app nao funciona, pede reembolso via Pix.

## Por que funciona
Ainda nao avaliado — captura de hoje veio so do Reclame Aqui (Etapa 3), sem Biblioteca de Anuncios.

## O que copiar / o que evitar
Registrar e observar. Nicho de trading tem risco regulatorio (CVM) — atencao no s_replica se confirmado.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout (PerfectPay), 2 mencoes em amostra parcial (15 paginas) de 22/09.
- **Faltando:** dias no ar, criativos, ticket, pagina de vendas — nenhuma Etapa 1 (Biblioteca de Anuncios) rodou nesta captura. `s_lucro` no teto 6 conforme regra do Scoring.md (sem dias_no_ar).
- **Nota de metodo:** esta captura usou a skill sincronizada `radar-low-ticket` (WebFetch por pagina, sem extracao de URL individual por reclamacao) — mais leve que o pipeline padrao do vault (`_meta/Pipeline.md`). Contagem de mencoes e estimativa por titulo, nao deduplicada por ID de reclamacao.

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
