---
tipo: oferta
slug: 
nome: 
nicho: 
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: []
checkout: 
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: []
formato_entrega: []
tem_recorrencia: false
s_ticket: 0
s_lucro: 0
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 
visto_ultimo: 
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
veredito: observar
prioridade: 0
tags: [oferta, lowticket]
---

# {{nome}}

## Ângulo
<!-- Qual é a promessa? Pra quem? Contra qual crença? -->

## Funil
<!-- anúncio → página → checkout → bump → upsell. Uma linha por etapa. -->

## Por que funciona
<!-- Sua leitura. O que essa oferta acerta que as outras erram? -->

## O que copiar / o que evitar

## Histórico
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
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
      - note.angulo_novo
    sort:
      - property: note.data
        direction: DESC
```
