---
tipo: oferta
classe: oferta
slug: green-stalker
nome: "Green Stalker"
nicho: espionagem-rastreamento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=green%20stalker&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 67
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 67
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 8
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-29
visto_ultimo: 2026-10-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/green-stalker"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 4
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Green Stalker

## Angulo
Estreia com 4 IDs na PerfectPay: 262754247 (R$ 67, 27/10) e 262770617 (27/10, 'toda hora tinha que add credito e fazer pix', grafado 'Green Staker'), somados aos dois da fila de 26/10 (262561045 e 262559131), lidos e nunca contados. App de 'monitoramento' com escada de creditos, a mecanica do angulo-taxa-escalonada-decrescente. 'green stalker' (frase exata) nao devolve nada na Biblioteca.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 4 mencao(oes) na varredura de 2026-10-29 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/nao-recebi-o-servico-green-staker-que-prometeu-e-solicito-reembolso_idXqZoAP0eqoXcQa/

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
