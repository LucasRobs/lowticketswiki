---
tipo: oferta
classe: oferta
slug: spinmaster
nome: "SpinMaster"
nicho: apostas-jogos
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=spinmaster&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 0
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-14
visto_ultimo: 2026-10-14
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/spinmaster"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-10-14
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# SpinMaster

## Angulo
Programa que promete 'acesso a roleta sem pagar mais nada'; depois do pagamento direciona o comprador para casas de apostas onde e preciso depositar — o infoproduto e porta de entrada de afiliacao de bet. 1 reclamacao com ID novo (261544737) mais 2 da rodada de 11/10, registradas como candidatas no Painel.

## Funil
anuncio -> pagina -> checkout kirvano -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-14 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/kirvano-pagamentos/lista-reclamacoes/ (ID 261544737)

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
