---
tipo: oferta
slug: shop-cash-1
nome: "Shop Cash 1.0"
nicho: ganhar-dinheiro
sub_nicho: ia-video-renda-extra
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Shop%20Cash&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 97
margem_est: 0.85
modelo: [vsl]
formato_entrega: [curso, app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 4
s_replica: 4
s_saturacao: 3
status: esfriando
visto_primeiro: 2026-08-22
visto_ultimo: 2026-08-24
rodadas_vista: 3
dias_no_ar: 11
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 2026-08-16
ra_checado: 2026-08-24
veredito: observar
prioridade: 1
tags: [oferta, lowticket, ia]
---

# Shop Cash 1.0

Curso vendido junto com aplicativo proprio: a publicidade promete **criacao de videos por
inteligencia artificial** e "ferramentas disponibilizadas pelo aplicativo". Compra em
12/08/2026.

## Angulo
IA + video + renda extra, os tres gatilhos empilhados. O sufixo "1.0" no nome e escolha
deliberada — sugere produto em evolucao e abre espaco para um "2.0" pago depois, o mesmo
recurso de nomenclatura de [[instalador-robo-pronto-2]].

## Funil
Nao capturado. O relato diz que **nao ha canal de atendimento dentro do sistema** — sem
WhatsApp, sem central. Isso e escolha de arquitetura, nao descuido: suporte ausente
transfere o custo de cancelamento para o gateway.

## Estado dos dados
- **Confirmado:** existe, vende, compra em 12/08/2026, gateway PerfectPay, app trava e nao
  gera os videos, reclamacao de 16/08/2026 (ID 256614755).
- **Provisorio:** ticket (97 estimado), se o app e proprio ou wrapper de API de terceiro.
- **Faltando:** pagina, criativos, dias no ar, bump/upsell.

`s_replica: 4` — a promessa depende de um app que funcione. Refazer o criativo e barato;
refazer o produto nao e.

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicitacao-de-reembolso-e-cancelamento-do-curso-shop-cash-10-por-propaganda-enganosa-e-falhas-no-aplicativo__3_x1jorsFnFaX-D/

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

PerfectPay, ha 11h: compra em 12/08, produto nao corresponde ao anunciado, falhas no aplicativo. Segunda reclamacao. 11 dias de venda medidos.

## Rodada 2026-08-24

PerfectPay, mesma reclamacao com compra em 12/08. Sem alteracao.
