---
tipo: oferta
slug: cinefy-tv
nome: "Cinefy TV"
nicho: streaming-e-acesso
sub_nicho: catalogo-series
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lowify
url_pagina: "https://app.cinefytv.site/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Cinefy&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 20
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 20
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 3
s_lucro: 6
s_replica: 3
s_saturacao: 5
status: ativa
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-21
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/cinefy-tv"
gateways_detectados: [lowify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [lowify]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Cinefy TV

## Angulo
Acesso a catalogo de series/filmes. Familia de marcas na mesma operacao Lowify: Cinefy TV, CineShort, Bleff.App, Reliquia Games.

## Funil
anuncio -> pagina -> checkout Lowify -> acesso ao catalogo (frequentemente com erro de formato/login).

## Por que funciona
A Lowify concentra um cluster inteiro de catalogo pirata sob marcas diferentes. Volume real, mas o ativo e conteudo de terceiros.

## O que copiar / o que evitar
Nao replicar: direito autoral. Registrado porque o cluster explica o perfil da Lowify como gateway.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (2 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/lowify-tecnologia/cinefy-tv-nao-cumpre-o-que-promete_Hb4uPnPCVeMoMjSC/

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

## Correção 2026-08-21 — dois espelhos ativos, operação Lowify

Domínios ativos: **`app.cinefytv.site`** e **`appcine.site`** (com página de registro em
`/register`). A empresa por trás aparece no Reclame Aqui como **Lowify Tecnologia**.

Mecânica registrada na reclamação: vendido como "pagamento único e vitalício", vira
assinatura recorrente depois. É bump pós-compra, o mesmo padrão de [[wiapy-foto-com-pet]].
