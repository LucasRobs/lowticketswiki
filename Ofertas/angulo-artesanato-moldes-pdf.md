---
tipo: oferta
slug: angulo-artesanato-moldes-pdf
nome: "Artesanato, moldes e PDF criativo"
nicho: artesanato-e-pdf
sub_nicho: moldes-e-croche
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 25
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 25
margem_est: 0.85
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 3
s_lucro: 8
s_replica: 10
s_saturacao: 4
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-artesanato-moldes-pdf"
gateways_detectados: [wiapy, cakto, lastlink, lowify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 6
ra_plataformas: [wiapy, cakto, lastlink, lowify]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 2
tags: [oferta, lowticket, angulo]
---

# Artesanato, moldes e PDF criativo

## Angulo
Moldes, croche, bordado, figurinhas, bonecas de papel. Marca nomeada na amostra: 160 Moldes Pra Personalizacao de Tenis.

## Funil
anuncio -> pagina -> checkout -> PDF.

## Por que funciona
Seis reclamacoes espalhadas por QUATRO gateways diferentes (Wiapy, Cakto, Lastlink, Lowify). E o angulo mais difuso da rodada, o que significa muitos produtores pequenos rodando em paralelo - mercado com demanda, nao operacao unica.

## O que copiar / o que evitar
Copiar: producao trivial, s_replica 10. O contra e o ticket de R$25 - so fecha conta com bump. O '160 moldes' mostra o padrao vencedor: quantidade no nome do produto.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (6 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/wiapy/reembolso-do-material-160-moldes-pra-personalizacao-de-tenis_93lTucSVR8kCltMT/

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
