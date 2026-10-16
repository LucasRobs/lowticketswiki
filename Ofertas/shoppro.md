---
tipo: oferta
classe: oferta
slug: shoppro
nome: "ShopPro"
nicho: negocio-online-ecommerce
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=ShopPro&search_type=keyword_unordered&media_type=all"
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
status: ativa
visto_primeiro: 2026-10-04
visto_ultimo: 2026-10-16
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/shoppro"
gateways_detectados: [hotmart, kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [hotmart, kiwify]
ra_primeira_reclamacao: 
ra_checado: 2026-10-16
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# ShopPro

## Angulo
Curso de e-commerce/loja online; comprador não se identificou com o conteúdo e teve demora no reembolso apesar de promessa de devolução rápida. Nome extraído do corpo da reclamação (confirmar antes de usar como termo de busca).

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-04 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/solicitacao-de-estorno-de-curso-nao-identificado-apos-promessa-de-reembolso_au-P7Qc2m2tbqQFs/

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

## Rodada 2026-10-16

1 mencao(oes) nesta varredura (gateway Kiwify). Curso/ferramenta de loja com IA vendido via Kiwify; reclamação por reembolso não estornado em 6 dias. Primeira aparição no radar.

Evidencia: https://www.reclameaqui.com.br/kiwify/solicito-reembolso-urgente-do-curso-ia-shop-pro-nao-estornado-em-6-dias_f5Xo90i_9ZrkGn9b/
