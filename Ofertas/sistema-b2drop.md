---
tipo: oferta
classe: oferta
slug: sistema-b2drop
nome: "Sistema B2Drop"
nicho: ecommerce-dropshipping
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: braip
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=B2Drop&search_type=keyword_unordered&media_type=all"
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
visto_ultimo: 2026-10-05
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/sistema-b2drop"
gateways_detectados: [braip]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [braip]
ra_primeira_reclamacao: 
ra_checado: 2026-10-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Sistema B2Drop

## Angulo
Sistema de dropshipping/assinatura, reembolso não recebido. Reclamação removida, nome confirmado só pelo título/URL.

## Funil
anuncio -> pagina -> checkout braip -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-04 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/braip/nao-recebimento-da-reembolso-da-assinatura-do-sistema-b2drop_lri1CUtfg9MUm7ro/

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

## Rodada 2026-10-05

1 mencao(oes) nesta varredura (gateway Braip). Sistema de dropshipping nacional vendido por Gilson Vaz da Costa; assinatura sem reembolso processado.

Evidencia: https://www.reclameaqui.com.br/braip/nao-recebi-o-reembolso-da-assinatura-do-sistema-b2drop_lri1CUtfg9MUm7ro/
