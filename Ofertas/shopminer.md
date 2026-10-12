---
tipo: oferta
classe: oferta
slug: shopminer
nome: "ShopMiner"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=shopminer&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 5
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 151
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 10
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-11
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/shopminer"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 11
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-11
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# ShopMiner

## Angulo
App que 'minera' produtos de e-commerce e gera imagens e videos deles, vendido em live com plano vitalicio de R$ 297 (261213933). 11 reclamacoes na Payt em 08-11/10 (261378247 a 261112515), quase todas 'nao gera videos / nao funciona'. Nao aparece na Biblioteca pelo nome: o canal e a live.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 11 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261378247, 261371209, 261356113, 261303597, 261293905, 261248881, 261213933, 261148849, 261148545, 261134853, 261112515)

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
