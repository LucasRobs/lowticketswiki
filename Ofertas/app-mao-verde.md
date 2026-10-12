---
tipo: oferta
classe: oferta
slug: app-mao-verde
nome: "App Mão Verde"
nicho: nao-classificado
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kiwify
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=app%20mao%20verde&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 9.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 23.45
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 4
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-05
visto_ultimo: 2026-10-05
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/app-mao-verde"
gateways_detectados: [kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kiwify]
ra_primeira_reclamacao: 
ra_checado: 2026-10-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# App Mão Verde

## Angulo
Jardinagem fatiada em microprodutos: APP Mao Verde R$ 37, SOS Fungos R$ 14,90, Segredo da Floracao R$ 9,90 e Adeus Mato R$ 9,90, todos comprados no mesmo dia (260758569, 01/10). Escada de bumps de R$ 9,90-14,90.

## Funil
anuncio -> pagina -> checkout kiwify -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-05 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/kiwify/lista-reclamacoes/ (ID 260758569)

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
