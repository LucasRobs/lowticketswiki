---
tipo: oferta
classe: oferta
slug: crie-ai
nome: "Crie AI"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=crie%20ai&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 297.99
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 297.99
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-10-19
visto_ultimo: 2026-10-19
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/crie-ai"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 6
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-19
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Crie AI

## Angulo
Gerador de sites com IA vendido como 'criacao ilimitada' e plano vitalicio de R$ 297,99 na Cakto; na pratica limita o numero de sites e cobra creditos de IA a parte (261809083: 'venda casada de creditos'), com garantia de 15 dias recusada por Termos de Uso. 4 IDs nesta rodada (261982681, 261893289, 261843291, 261809083) + 2 em 11-14/10 (CrieAI, na fila). Compras de 03 a 13/10. Biblioteca: 'crie.ai' so devolve ruido (~5.500 resultados genericos). Nao confundir com [[criaai]] (Ticto, 1 mencao).

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 6 mencao(oes) na varredura de 2026-10-19 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/solicitei-reembolso-de-plano-vitalicio-dentro-do-prazo-e-negaram_U8ORNFtBw7wlqMf2/

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
