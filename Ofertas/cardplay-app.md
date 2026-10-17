---
tipo: oferta
classe: oferta
slug: cardplay-app
nome: "CardPlay (app)"
nicho: app-assinatura
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=CardPlay%20app&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-16
visto_ultimo: 2026-10-17
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/cardplay-app"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-17
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# CardPlay (app)

## Angulo
Nome novo. App que o comprador ja usava e pagou de novo (atualizacao) via Pix em 14/10; diz que o app segue com problema e a empresa nao responde no WhatsApp, pede estorno. Primeira vez que aparece no radar.

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-16 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/quero-estorno-do-valor-pago-via-pix-pelo-app-cardplay_E52u_fjCj_6DS34k/

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

1 mencao(oes) nesta varredura (gateway Cakto). App cobrado via PIX com renovacao automatica; reclamante pede estorno da renovacao de um app que ja tinha vencido. Nome novo no radar, natureza exata do app (cartao virtual/financas) nao confirmada pela reclamacao.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/quero-estorno-do-valor-pago-via-pix-pelo-app-cardplay_E52u_fjCj_6DS34k/

## Rodada 2026-10-17

1 mencao(oes) nesta varredura (gateway Cakto). App de cartao virtual, reclamacao pedindo estorno via Pix. Mesma reclamacao de 16/10, agora confirmada em segundo dia diferente (16/10 e 17/10) -- sobe de fria para morna.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/quero-estorno-do-valor-pago-via-pix-pelo-app-cardplay_E52u_fjCj_6DS34k/
