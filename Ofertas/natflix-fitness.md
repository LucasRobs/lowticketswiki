---
tipo: oferta
classe: oferta
slug: natflix-fitness
nome: "Natflix Fitness"
nicho: saude-fitness
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Natflix%20Fitness&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 79.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 79.9
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 8
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-09
visto_ultimo: 2026-10-09
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/natflix-fitness"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [hotmart]
ra_primeira_reclamacao: 
ra_checado: 2026-10-09
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Natflix Fitness

## Angulo
App/catálogo de treinos com nome que remete a streaming ('Natflix'). Reembolso pedido no mesmo dia da compra, aprovado pela Hotmart em 20/09. 1ª aparição no radar.

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-09 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/reembolso-nao-realizado_MgZ5OmIsDjuB1_E2/

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
