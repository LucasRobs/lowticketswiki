---
tipo: oferta
classe: oferta
slug: mentoria-thiago-lobos
nome: "Mentoria Thiago Lobos"
nicho: marketing-faca-como-eu
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
status: esfriando
visto_primeiro: 2026-10-06
visto_ultimo: 2026-10-07
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/mentoria-thiago-lobos"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [hotmart]
ra_primeira_reclamacao: 
ra_checado: 2026-10-07
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Mentoria Thiago Lobos

## Angulo
Estreia. Mentoria parcelada; aluno relata que os primeiros dias foram so slides/conversa, depois pediram para gravar videos promovendo produtos que nao existem. Reembolso negado e nome enviado ao SPC/SERASA - pratica predatoria a observar, ticket mais alto que o low ticket tipico.

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) nas varreduras de 2026-10-06 e 2026-10-07 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas). Reclamacao de 2026-10-07 (publicada 05/10) confirma que a oferta segue ativa e gerando atrito pos-venda: https://www.reclameaqui.com.br/hotmart/nao-consigo-cancelar-cobranca-indevida-da-pages-e-quero-estorno_fR8DvfLnBkBVRnGq/
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/quero-a-devolucao-da-primeira-parcela-e-a-exclusao-do-meu-nome-do-spcserasa_1jlhwqELYQOHxjmO/

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
