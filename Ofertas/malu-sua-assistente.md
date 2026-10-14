---
tipo: oferta
classe: oferta
slug: malu-sua-assistente
nome: "Malu - Sua Assistente"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Malu%20sua%20assistente&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 24
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 30.95
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 4
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-08
visto_ultimo: 2026-10-14
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/malu-sua-assistente"
gateways_detectados: [wiapy, perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 8
ra_plataformas: [wiapy, perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-14
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Malu - Sua Assistente

## Angulo
Assistente para postar na loja da Shopee, R$ 37,90 no Pix; depois da compra pede mais R$ 24 'da API' para funcionar. 2 reclamacoes: 260944511 (compra 14/09) e 261076971 (07/10).

## Funil
anuncio -> pagina -> checkout wiapy -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) na varredura de 2026-10-08 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/wiapy/lista-reclamacoes/ (IDs 261076971, 260944511)

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

## Rodada 2026-10-11

6 mencao(oes) nesta varredura (gateway Wiapy). 4 reclamacoes com ID novo em TRES gateways: 261345175 (Wiapy, R$ 37,90 em 10/10, cobrado duas vezes), 261360035 (Cakto, R$ 38,89), 261250055 e 261215079 (PerfectPay, compra de 03/09). O mesmo produto roda em Wiapy, Cakto e PerfectPay.

Evidencia: https://www.reclameaqui.com.br/empresa/wiapy/lista-reclamacoes/ (261345175) + cakto-pay (261360035) + perfectpay (261250055, 261215079)

## Rodada 2026-10-14

8 mencao(oes) nesta varredura (gateway PerfectPay). 2 reclamacoes com ID novo na PerfectPay: 261544735 (nao recebeu o app; dentro da area havia outros produtos) e 261422993 ('robo de IA Malu').

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 261544735, 261422993)
