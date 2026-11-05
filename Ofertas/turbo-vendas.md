---
tipo: oferta
classe: oferta
slug: turbo-vendas
nome: "Turbo Vendas"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lastlink
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=turbo%20vendas&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 49
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 49
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-11-05
visto_ultimo: 2026-11-05
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/turbo-vendas"
gateways_detectados: [lastlink]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [lastlink]
ra_primeira_reclamacao: 
ra_checado: 2026-11-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Turbo Vendas

## Angulo
Estreia 05/11 com 3 IDs na Lastlink: 263169683 (videos automaticos a partir de link de produto do TikTok e Shopee, bloqueio por 'muitos acessos' depois do primeiro video), 263278225 (R$ 49,00) e 263343631 (comprado 04/11). Mensalidade.

## Funil
anuncio -> pagina -> checkout lastlink -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-11-05 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/lastlink/solicito-cancelamento-e-reembolso-do-turbo-vendas-por-propaganda-enganosa_YHw8QP9X1rYLFslL/

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
