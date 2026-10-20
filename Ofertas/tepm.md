---
tipo: oferta
classe: oferta
slug: tepm
nome: "TEPM"
nicho: a-identificar
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=curso%20TEPM&search_type=keyword_unordered&media_type=all"
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
visto_primeiro: 2026-10-14
visto_ultimo: 2026-10-15
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/tepm"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [hotmart]
ra_primeira_reclamacao: 
ra_checado: 2026-10-15
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# TEPM

## Angulo
Primeira aparicao no radar. Curso TEPM da Prof. Juliana Souza via Hotmart, comprado por volta de outubro/2025 -- compradora perdeu acesso e suporte nao ajuda. Ticket alto pro radar, mas volume de reclamacao de suporte/acesso e recorrente nesse tipo de curso.

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-14 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/nao-consigo-acessar-meu-curso-tepm-e-o-suporte-nao-me-ajuda_d3jlEZGMKJc1-MUZ/

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

## Rodada 2026-10-14

1 mencao(oes) nesta varredura (gateway Hotmart). 2ª passada seguida com a mesma reclamação -- curso de ticket alto com problema de acesso/suporte, produtora Prof. Juliana Souza.

Evidencia: https://www.reclameaqui.com.br/hotmart/nao-consigo-acessar-meu-curso-tepm-e-o-suporte-nao-me-ajuda_d3jlEZGMKJc1-MUZ/

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway Hotmart). Curso TEPM, acesso bloqueado e suporte sem resposta. Mesma reclamacao da passada anterior ainda ativa na pagina 1 -- sem novidade.

Evidencia: https://www.reclameaqui.com.br/hotmart/nao-consigo-acessar-meu-curso-tepm-e-o-suporte-nao-me-ajuda_d3jlEZGMKJc1-MUZ/
