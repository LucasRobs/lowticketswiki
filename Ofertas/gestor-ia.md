---
tipo: oferta
slug: gestor-ia
nome: "Gestor IA"
nicho: ferramentas-ia
sub_nicho: automacao-negocio
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: "https://gestoria.site/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Gestor%20IA&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 29.98
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 50
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: true
s_ticket: 9
s_lucro: 6
s_replica: 5
s_saturacao: 5
status: esfriando
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-21
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/gestor-ia"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 1
tags: [oferta, lowticket, marca]
---

# Gestor IA

## Angulo
Assistente de IA para gestao de negocio. Duas reclamacoes distintas em 50 amostradas da Kirvano.

## Funil
Nao capturado.

## Por que funciona
Aparece duas vezes na amostra, o que ja separa de ruido. Nicho de IA com assinatura e o que mais cresce na Kirvano.

## O que copiar / o que evitar
Vale abrir na Biblioteca de Anuncios antes de decidir - a amostra e pequena demais para concluir.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (2 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/solicitacao-de-reembolso-para-o-produto-gestor-ia-nao-respondida_QJGMkxMpN1_RSAma/

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

## Correção 2026-08-21 — assinatura mensal, checkout Kirvano

Página localizada: **`gestoria.site`** (agregador de 60+ ferramentas de IA), checkout
**Kirvano** (`pay.kirvano.com`). Planos: R$ 29,98 (Pro) · R$ 38,96 (Premium) ·
R$ 76,95 (Ultra) por mês; anual de R$ 69 a R$ 139/mês.

`s_ticket` sobe de 5 para 9 por causa da recorrência. Score: 5,35 → 6,10.
Bate com as reclamações de "Gestor IA Premium +60 Modelos de IAs" via Kirvano.
