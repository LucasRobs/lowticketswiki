---
tipo: oferta
classe: oferta
slug: direct-line-app
nome: "Direct Line (app)"
nicho: app-assinatura
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Direct%20Line%20app&search_type=keyword_unordered&media_type=all"
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
visto_primeiro: 2026-10-06
visto_ultimo: 2026-10-16
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/direct-line-app"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-16
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Direct Line (app)

## Angulo
App vendido por assinatura via Cakto. Comprador relata bugs e dificuldade para encontrar opção de cancelamento dentro do app. Estreia nesta passada.

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-06 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/quero-cancelar-minha-assinatura-do-app-direct-line-que-nao-gostei_2y3V-K7WaLzqRGhL/

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

## Rodada 2026-10-06

1 mencao(oes) nesta varredura (gateway Cakto). 2a reclamacao sobre o app por assinatura Direct Line (estreou as 00:50). Usuario quer cancelar a assinatura por insatisfacao com o app.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/quero-cancelar-minha-assinatura-do-app-direct-line-que-nao-gostei_2y3V-K7WaLzqRGhL/

## Rodada 2026-10-14

1 mencao(oes) nesta varredura (gateway Cakto). 6ª aparição cumulativa na página 1 da Cakto. Mesma reclamação da rodada das 03:45, zero novidade.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-meu-reembolso-da-direct-line-e-o-servico-nao-cumpriu-o-prometido_Usq2R4tN11f3MoW5/

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway Cakto). App com assinatura dificil de cancelar, cobrado via Cakto. Pouca informacao sobre o que o app faz -- nome novo, mencao unica.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-consigo-cancelar-o-app-direct-line-e-a-assinatura_qrkw52eRA-a1OUvG/

## Rodada 2026-10-16

1 mencao(oes) nesta varredura (gateway Cakto). App por assinatura, reclamacao recorrente de dificuldade pra cancelar a assinatura -- sinal de cobranca recorrente mal explicada no checkout.

Evidencia: 
