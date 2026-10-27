---
tipo: oferta
classe: oferta
slug: dossie-do-emagrecimento
nome: "Dossiê do Emagrecimento"
nicho: saude-emagrecimento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Dossiê%20do%20Emagrecimento&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-10-06
visto_ultimo: 2026-10-23
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/dossie-do-emagrecimento"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-23
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Dossiê do Emagrecimento

## Angulo
Infoproduto digital de emagrecimento vendido via Payt. Comprador pediu estorno dentro do prazo de arrependimento (7 dias); Payt processou via Pix no dia seguinte. Reclamação de hoje (06/10), sem valor citado.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-06 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/payt/quero-o-estorno-do-dossie-do-emagrecimento-por-arrependimento_vPoBdNpsghuLq8pR/

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

## Rodada 2026-10-21

2 mencao(oes) nesta varredura (gateway Payt). 1 ID novo na Payt (1 -> 2): 262182239 (pagou no Pix e nao recebeu o dossie). Primeira aparicao desde 06/10.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-23

3 mencao(oes) nesta varredura (gateway Payt). 1 ID novo (2 -> 3): 262387755, compra em 22/10 e arrependimento sem canal de cancelamento.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (ID 262387755)
