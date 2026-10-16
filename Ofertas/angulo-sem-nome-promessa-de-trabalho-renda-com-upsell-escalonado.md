---
tipo: oferta
classe: angulo
slug: angulo-sem-nome-promessa-de-trabalho-renda-com-upsell-escalonado
nome: "sem nome - promessa de trabalho/renda com upsell escalonado"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=trabalho%20de%20casa%20renda%20extra&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 49
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 374.5
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-16
visto_ultimo: 2026-10-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-sem-nome-promessa-de-trabalho-renda-com-upsell-escalonado"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-16
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# sem nome - promessa de trabalho/renda com upsell escalonado

## Angulo
Reclamante relata 16 compras distintas entre 09/10 e 15/10 (R$49,90 a R$700,00, total ~R$4.136), todas dentro de uma promessa de trabalho/renda, sem nome de produto nem produtor identificados. Padrao de upsell/order bump muito agressivo e escalonado -- sinal forte de funil com multiplas ofertas em sequencia no mesmo gateway.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-16 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fui-enganado-com-promessa-de-trabalho-e-solicito-reembolso-dos-valores-pagos_-VYBfAbViU5o7AfK/

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

1 mencao(oes) nesta varredura (gateway PerfectPay). Mesma reclamacao ja conhecida (16 compras entre 09/10 e 15/10, total ~R$4.136), zero novidade.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fui-enganado-com-promessa-de-trabalho-e-solicito-reembolso-dos-valores-pagos_-VYBfAbViU5o7AfK/
