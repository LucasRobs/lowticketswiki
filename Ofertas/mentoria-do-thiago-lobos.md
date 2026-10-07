---
tipo: oferta
classe: oferta
slug: mentoria-do-thiago-lobos
nome: "Mentoria do Thiago Lobos"
nicho: mentoria-comunidade
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Thiago%20Lobos%20mentoria&search_type=keyword_unordered&media_type=all"
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
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: morta
visto_primeiro: 2026-10-07
visto_ultimo: 2026-10-07
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/mentoria-do-thiago-lobos"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: [hotmart]
ra_primeira_reclamacao: 
ra_checado: 2026-10-07
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Mentoria do Thiago Lobos

> **DUPLICATA — corrigido manualmente.** Esta nota nasceu de um erro de nomenclatura da rodada 2026-10-07 13:48 ("Mentoria do Thiago Lobos" em vez de "Mentoria Thiago Lobos"), o que impediu o merge automatico. A mencao e a evidencia desta reclamacao foram incorporadas a [[mentoria-thiago-lobos]]. Nao conte esta nota nas estatisticas — mantida apenas porque este ambiente nao pode apagar arquivos.

## Angulo
Reaparece em nova reclamação (publicada 05/10/2026) sobre cobrança indevida referente à mentoria — reforça que a oferta segue ativa e gerando atrito pós-venda.

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-07 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/nao-consigo-cancelar-cobranca-indevida-da-pages-e-quero-estorno_fR8DvfLnBkBVRnGq/

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
