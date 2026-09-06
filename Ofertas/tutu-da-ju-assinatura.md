---
tipo: oferta
classe: oferta
slug: tutu-da-ju-assinatura
nome: "Tutu da Ju — assinatura de ballet classico online"
nicho: danca
sub_nicho: ballet-adulto
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: "https://conteudos.tutudaju.com/assinatura-de-aulas-tutu-da-ju"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=aulas%20de%20ballet&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 50
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 150
margem_est: 0.85
modelo: [direct]
formato_entrega: [curso, comunidade]
tem_recorrencia: true
s_ticket: 9
s_lucro: 7
s_replica: 3
s_saturacao: 7
status: nova
visto_primeiro: 2026-09-06
visto_ultimo: 2026-09-06
rodadas_vista: 1
dias_no_ar: 137
criativos_ultima: 1
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/tutu-da-ju-assinatura"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 
veredito: observar
prioridade: 1
tags: [oferta, danca, ballet, recorrencia]
---

# Tutu da Ju — assinatura

R$ 50/mes sem fidelidade, Hotmart, 170+ aulas gravadas com aula nova toda semana, grupo de
WhatsApp. Publico: mulher adulta que quer fazer ballet e nao vai a uma escola. **137 dias no ar**
(anuncio de 22/04/2026), um criativo so.

## A leitura util

E a unica oferta de danca da varredura com **recorrencia** — `s_ticket: 9` por isso. Um criativo
sustentando 137 dias e sinal de CPA baixo e churn administravel, nao de operacao parada.

`s_replica: 3`: 170 aulas gravadas e aula nova por semana e uma esteira de producao permanente.
Nao e um produto, e um emprego. Fica no vault como referencia de **teto de modelo** no nicho:
mostra que existe recorrencia de R$ 50 sustentavel em danca, o que e insumo para pensar o backend
das ofertas de R$ 19,90 — ver [[angulo-material-pronto-para-quem-ensina-danca]].

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
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
