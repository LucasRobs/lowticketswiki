---
tipo: oferta
slug: angulo-biblia-free-shipping
nome: "Biblia gratis, so paga o frete"
nicho: free-shipping
sub_nicho: brinde-religioso
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=biblia%20gratis%20frete&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 9
ticket_bump: 12
ticket_upsell: 7
ticket_medio_est: 30
margem_est: 0.85
modelo: [direct]
formato_entrega: [fisico]
tem_recorrencia: false
s_ticket: 4
s_lucro: 5
s_replica: 6
s_saturacao: 5
status: esfriando
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-biblia-free-shipping"
gateways_detectados: [cakto]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 1
tags: [oferta, lowticket, angulo]
---

# Biblia gratis, so paga o frete

## Angulo
Biblia de brinde com pagamento apenas do frete, seguido de cobrancas em cascata.

## Funil
anuncio -> 'gratis, so o frete' -> Pix R$12,89 (frete R$9,90 + taxa) -> segundo Pix R$7,57 (NF-e) -> terceiro Pix R$9,90 tentado. Total cobrado: R$30,36.

## Por que funciona
Documenta a cascata completa de um free+shipping: cada etapa tem uma justificativa plausivel (frete, taxa, nota fiscal) e o ticket medio triplica o valor anunciado.

## O que copiar / o que evitar
Copiar: a logica de decompor o preco em etapas justificadas eleva o ticket medio sem elevar a barreira de entrada. Evitar: cobrar 'nota fiscal' como etapa - foi o que disparou a reclamacao.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/cakto-pay/cobrancas-sucessivas-e-propaganda-enganosa-em-brinde-de-biblia_CgSGYZQgT8L3Wv83/

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
