---
tipo: oferta
classe: oferta
slug: date-nights-cristao
nome: "Date Nights Cristão"
nicho: religioso
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Date%20Nights%20Cristão&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 42
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 42
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-02
visto_ultimo: 2026-10-02
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/date-nights-cristao"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-02
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Date Nights Cristão

## Angulo
Kit digital de encontros para casais cristaos, R$ 42 em 2x R$ 21 (compra de 21/09). Duas reclamacoes em 01/10 (260597223, 260601271): conteudo menor que o anunciado e vendedor sem resposta. Biblioteca: busca exata sem anuncio ativo em 02/10.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) na varredura de 2026-10-02 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/payt/lista-reclamacoes/ (ID 260597223)

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
