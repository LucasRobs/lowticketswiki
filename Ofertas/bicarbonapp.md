---
tipo: oferta
classe: oferta
slug: bicarbonapp
nome: "BicarbonApp"
nicho: emagrecimento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=bicarbonapp&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-20
visto_ultimo: 2026-10-29
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/bicarbonapp"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 7
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# BicarbonApp

## Angulo
App de 'receita de emagrecimento' com bicarbonato, com uma 'Dra Ana' na frente. 3 IDs, todos nesta rodada e em dois gateways: Payt 262073561 (compra de 19/10 no Pix) e 262044977 (2 compras em 16/10, 'site nao confiavel'), Kirvano 262052053 ('aplicativo Bicarbonepp com Dra Ana', acesso nao chegou). Na Biblioteca, 'bicarbonato app' so devolveu ruido.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-20 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

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

## Rodada 2026-10-23

4 mencao(oes) nesta varredura (gateway Payt). 1 ID novo (3 -> 4): 262422749, pacotes BicarbonApp + 'Cola Egipcia', app 'amador' que nao libera o conteudo.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (ID 262422749)

## Rodada 2026-10-27

5 mencao(oes) nesta varredura (gateway Payt). 1 ID novo (4 -> 5): 262639857 (Payt, comprado 25/10, sem opcao de reembolso no app).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (ID 262639857)

## Rodada 2026-10-29

7 mencao(oes) nesta varredura (gateway Payt). 2 IDs novos (5 -> 7) na Payt: 262773631, 262745461.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/
