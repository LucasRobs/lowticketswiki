---
tipo: oferta
classe: oferta
slug: portovian
nome: "Portovian"
nicho: ecommerce-fisico
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: yampi
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Portovian&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 265.05
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 265.05
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-05
visto_ultimo: 2026-10-13
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/portovian"
gateways_detectados: [yampi]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [yampi]
ra_primeira_reclamacao: 
ra_checado: 2026-10-13
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Portovian

## Angulo
Loja de produto físico (não é infoproduto) com não entrega via Correios. Fica registrado por aparecer no mesmo pedágio, mas é e-commerce, não low ticket digital.

## Funil
anuncio -> pagina -> checkout yampi -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-05 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/yampi/nao-recebi-meu-pedido-da-portovian-e-quero-o-cancelamento-e-estorno_r0yLd7lwixZPXOtn/

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

## Rodada 2026-10-13

1 mencao(oes) nesta varredura (gateway Yampi). Produto físico de e-commerce, recorrente desde 05/10 (3 menções anteriores). Hoje mais 1 pedido de cancelamento/estorno.

Evidencia: https://www.reclameaqui.com.br/yampi/nao-recebi-meu-pedido-da-portovian-e-quero-o-cancelamento-e-estorno_r0yLd7lwixZPXOtn/
