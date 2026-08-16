---
tipo: oferta
slug: robo-produtor-criativos
nome: "Robo Produtor de Criativos"
nicho: ferramentas-ia
sub_nicho: criativos-ia
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 97
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 97
margem_est: 0.85
modelo: [vsl]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 6
s_replica: 5
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/robo-produtor-criativos"
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

# Robo Produtor de Criativos

## Angulo
Ferramenta de IA que gera criativos de anuncio prontos. Publico e o proprio infoprodutor.

## Funil
anuncio -> pagina -> checkout Kirvano parcelado em 3x.

## Por que funciona
Vender pa para garimpeiro. Parcelamento em 3x indica ticket acima de R$97.

## O que copiar / o que evitar
Copiar: o parcelamento como forma de subir ticket sem subir a barreira. Evitar: o nicho de marketing esta saturado - so entra com angulo novo.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (2 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/propaganda-enganosa-no-robo-produtor-de-criativos_iVsYlIi3WkBaFgNM/

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
