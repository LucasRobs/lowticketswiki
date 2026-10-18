---
tipo: oferta
classe: oferta
slug: minha-historinha
nome: "Minha Historinha"
nicho: educacao-infantil
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Minha%20Historinha&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 29
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 4
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-09-29
visto_ultimo: 2026-09-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/minha-historinha"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-09-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Minha Historinha

## Angulo
Livro infantil digital. Problema: não recebimento de link de acesso após pagamento (PIX confirmado em 22/09, sem entrega até 29/09).

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-09-29 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-o-link-do-livro-minha-historinha-apos-pagamento-via-pix_U7wp_PH9c4g5gNH7/

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

## Rodada 2026-09-29

1 mencao(oes) nesta varredura (gateway cakto-pay). Livro infantil digital. Não recebimento de link: compra 22/09 → reclamação 29/09 (7 dias sem entrega). Pode ser problema técnico ou negligência deliberada.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-o-link-do-livro-minha-historinha-apos-pagamento-via-pix_U7wp_PH9c4g5gNH7/
