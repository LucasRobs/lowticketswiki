---
tipo: oferta
classe: oferta
slug: app-direct-line
nome: "App Direct Line"
nicho: nao-classificado
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=direct%20line%20app&search_type=keyword_unordered&media_type=all"
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
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-14
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/app-direct-line"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-14
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# App Direct Line

## Angulo
Aplicativo vendido por assinatura (plano Pro) com garantia de 7 dias que, segundo os compradores, nao e honrada. 5 reclamacoes na Cakto em 09-11/10 (261380877, 261371245, 261357363, 261239765, 261205833). Funcao do app nao descrita nos corpos.

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 5 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/ (IDs 261380877, 261371245, 261357363, 261239765, 261205833)

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

1 mencao(oes) nesta varredura (gateway Cakto). App por assinatura vendido via Cakto, funcao nao descrita nos corpos. Terceira aparicao em dia diferente (06/10, 11/10 com 5 IDs, agora 13/10) -- mesmo padrao de reclamacao se repetindo (cancelamento dificil / garantia nao honrada).

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-meu-reembolso-da-direct-line-e-o-servico-nao-cumpriu-o-prometido_Usq2R4tN11f3MoW5/

## Rodada 2026-10-14

1 mencao(oes) nesta varredura (gateway Cakto). Mesma reclamacao da rodada de 23:32 (4a aparicao cumulativa no radar, dias diferentes: 06/10, 11/10, 13/10). Nenhuma reclamacao nova nesta janela, mas o padrao de garantia nao honrada persiste sem solucao.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-meu-reembolso-da-direct-line-e-o-servico-nao-cumpriu-o-prometido_Usq2R4tN11f3MoW5/
