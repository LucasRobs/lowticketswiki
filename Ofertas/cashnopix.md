---
tipo: oferta
slug: cashnopix
nome: "Cashnopix / Cash no Pix"
nicho: renda-celular-cashback
sub_nicho: cashback-pix
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 39
ticket_bump: 67
ticket_upsell: 0
ticket_medio_est: 107
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 8
s_replica: 3
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/cashnopix"
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Cashnopix / Cash no Pix

## Angulo
Ganhe avaliando produtos / assistindo videos, com saldo acumulado em cashback via Pix. Grafias: Cashnopix, Cash no Pix, Cash Pix.

## Funil
anuncio -> app -> saldo acumula -> saque bloqueado -> taxa de liberacao -> segunda taxa -> terceira. Um reclamante somou R$107,80 em dois Pix.

## Por que funciona
Cinco reclamacoes em 50 amostradas, todas descrevendo a mesma cascata de taxas. Volume alto e recorrente na PerfectPay.

## O que copiar / o que evitar
Registrado como referencia de mecanica, nao como candidata. O modelo depende de nunca pagar o saque - nao ha versao honesta disso para replicar.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (5 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/perfectpay/cobranca-para-liberacao-de-saldo-e-propaganda-enganosa-no-cashnopix_-Av-lIMQePl-aZU2/

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
