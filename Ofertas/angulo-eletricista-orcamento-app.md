---
tipo: oferta
slug: angulo-eletricista-orcamento-app
nome: "App de orcamento para eletricista + imprimiveis"
nicho: cursos-de-oficio
sub_nicho: eletrica-residencial
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=orcamento%20eletricista%20app&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 27
ticket_bump: 32
ticket_upsell: 0
ticket_medio_est: 60
margem_est: 0.85
modelo: [direct]
formato_entrega: [planilha, ebook]
tem_recorrencia: false
s_ticket: 7
s_lucro: 5
s_replica: 9
s_saturacao: 8
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-eletricista-orcamento-app"
gateways_detectados: [wiapy]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [wiapy]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: replicar
prioridade: 3
tags: [oferta, lowticket, angulo]
---

# App de orcamento para eletricista + imprimiveis

## Angulo
Ferramenta de orcamento para eletricista autonomo, empacotada com materiais imprimiveis. Vende utilidade profissional, nao curso.

## Funil
anuncio -> pagina -> checkout Wiapy R$27,99 -> app + imprimiveis -> cobranca adicional de R$32,90 para liberar o restante.

## Por que funciona
O melhor eixo de replicabilidade da rodada. Entrega e planilha/PDF, o publico e classe C profissional, o criativo nao precisa de rosto nem de autoridade, e o ticket medio chega a R$60 com o bump. s_replica 9.

## O que copiar / o que evitar
Copiar: o formato 'ferramenta de trabalho + imprimiveis' aplicado a qualquer oficio - encanador, ar-condicionado, pintor, marceneiro. O bump de R$32,90 sobre um front de R$27,99 quase dobra o ticket medio. Evitar: travar o produto principal atras do bump; cobre o bump como extra de verdade.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/wiapy/produto-nao-funciona-e-exige-pagamento-adicional_tyL1dL9FWDAZypkJ/

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
