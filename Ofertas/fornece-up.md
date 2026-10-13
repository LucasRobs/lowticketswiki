---
tipo: oferta
classe: oferta
slug: fornece-up
nome: "Fornece Up"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=forneceup&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 12
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 12
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 2
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-13
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/fornece-up"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 8
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-13
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Fornece Up

## Angulo
Plataforma de fornecedores por assinatura parcelada em 12x (261367699). 8 reclamacoes na PerfectPay em 08-11/10, quase todas com o mesmo texto 'nao consigo cancelar a compra da ForneceUp' (261316209, 261316083, 261280965, 261236057, 261183451, 261168583, 261121611): cancelamento travado e o que move o volume.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 8 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (8 IDs de 261121611 a 261367699)

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

## Rodada 2026-10-12

1 mencao(oes) nesta varredura (gateway PerfectPay). Plataforma de fornecedores por assinatura parcelada (ja mapeada como estreia na rodada anterior, 8 mencoes). Nova reclamacao no mesmo padrao: cancelamento/reembolso dentro do prazo de 7 dias, produtor sem resposta. Continua ativa poucas horas depois da ultima passada.

Evidencia: https://www.reclameaqui.com.br/perfectpay/quero-cancelar-minha-compra-e-ser-reembolsado-em-r-31554_liRRdrRGZL9uTLus/

## Rodada 2026-10-13

2 mencao(oes) nesta varredura (gateway PerfectPay). Assinatura de acesso a fornecedores/revenda, recorrente desde 25/09 e marcada quente na rodada anterior (debutou 11/10 com 8 IDs). Hoje mais 2 pedidos de estorno (um deles via Pix). Uma reclamação cita taxas de R$97-250 cobradas pra liberar um saldo de R$17.658 -- mecânica de order bump/upsell pesada pra travar saque.

Evidencia: https://www.reclameaqui.com.br/perfectpay/nao-recebi-o-estorno-da-fornece-up-apos-cancelamento-em-7-dias_nK2G6qUC6C7nWEIi/
