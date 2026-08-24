---
tipo: oferta
slug: love-pix
nome: "Love Pix"
nicho: renda-celular-cashback
sub_nicho: taxa-para-liberar
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Love%20Pix&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 25.9
ticket_bump: 10
ticket_upsell: 10
ticket_medio_est: 56
margem_est: 0.95
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 5
s_lucro: 3
s_replica: 2
s_saturacao: 2
status: ativa
visto_primeiro: 2026-08-22
visto_ultimo: 2026-08-24
rodadas_vista: 3
dias_no_ar: 6
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: true
ra_reclamacoes: 2
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 2026-08-17
ra_checado: 2026-08-24
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, escada-de-taxas]
---

# Love Pix

**A escada de taxas inteira num paragrafo.** R$ 25,90 na entrada, depois mais R$ 10, depois
mais R$ 10 — "totalizando 56 reais" para liberar um saque que nunca chega. Esse e o
mecanismo que o `Pipeline.md` chama de "taxa pra liberar", e e a razao pela qual o nicho
de cashback/PIX continua produzindo reclamacao: o comprador ja pagou tres vezes quando
percebe.

Registrada pela anatomia, nao pela oportunidade. Os dois upsells sao **pos-compra e
ocultos** — nao aparecem no checkout, aparecem depois, dentro do app, cada um com um
pretexto novo. Um Brute Mode na pagina de vendas nunca acharia: eles nao estao no DOM.

## Funil
anuncio -> pagina -> checkout PerfectPay R$ 25,90 -> app -> pedido de taxa 1 (R$ 10) ->
pedido de taxa 2 (R$ 10) -> saque nao liberado.

## Por que nao replicar
O ticket medio de R$ 56 so existe porque o produto nao entrega. Tirar a fraude tira a
escada. `s_replica: 2` e teto, nao estimativa.

## Estado dos dados
- **Confirmado:** valores 25,90 / +10 / +10, gateway PerfectPay, reclamacao 17/08/2026
  (ID 256617879), saque nao pago.
- **Faltando:** pagina, criativos, dias no ar, se ha mais degraus na escada.

Parente proximo de [[cashnopix]] e [[lottoapp]] — mesmo nicho, mesma mecanica, mesmo
veredito.

Evidencia: https://www.reclameaqui.com.br/perfectpay/aplicativo-love-pix-cobra-taxas-sucessivas-e-nao-realiza-o-pagamento-prometido_eiuEX2eJfSf-ipos/

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

## Rodada 2026-08-23

PerfectPay, ha 9h: a escada de taxas aparece completa e literal - "primeiro pediu 25,90 depois pediu mais 10 reais e depois pediu mais 10 reais". Confirma ticket_medio_est de 56 sem precisar de Brute Mode. 6 dias desde a primeira reclamacao.

## Rodada 2026-08-24

PerfectPay, mesma reclamacao com a escada 25,90 + 10 + 10. Sem alteracao.
