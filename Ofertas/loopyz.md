---
tipo: oferta
slug: loopyz
nome: "Loopyz"
nicho: lives-interativas
sub_nicho: ferramenta-live-tiktok
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 47
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 47
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 5
s_lucro: 5
s_replica: 4
s_saturacao: 8
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/loopyz"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 2
tags: [oferta, lowticket, marca]
---

# Loopyz

## Angulo
Ferramenta/overlay para live no TikTok. Reclamacao registrada as 11h de hoje - e trafego rodando agora.

## Funil
anuncio -> pagina -> checkout Cakto -> suporte via produtor, nao via plataforma.

## Por que funciona
O nicho de live interativa esta em expansao rapida e com poucos players. s_saturacao 8 e o mais alto da rodada entre as marcas.

## O que copiar / o que evitar
Copiar: o nicho, nao necessariamente o produto. Vale mapear os concorrentes na Biblioteca de Anuncios com 'live interativa tiktok'.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/cakto-pay/dificuldade-para-obter-reembolso-de-ferramenta-comprada-para-live-no-tiktok_8ByKgtxdl-o8n54i/

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
