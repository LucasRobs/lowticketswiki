---
tipo: oferta
classe: oferta
slug: captchas-no-google
nome: "Captchas no Google"
nicho: servicos-diversos
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Captchas%20Google&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 17500
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 17500
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-09-29
visto_ultimo: 2026-09-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/captchas-no-google"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-09-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Captchas no Google

## Angulo
Serviço de recebimento de captchas. Taxa paga (R$ 17.500 — valor extremo, pode ser formatação) mas serviço não entregue nem reembolso processado. Suspeita de fraude ou erro de entrada.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-09-29 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/paguei-taxa-para-receber-captchas-no-google-e-nao-recebi-nem-o-valor-nem-a-devolucao_EPc68aBY7XP5R0hz/

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
