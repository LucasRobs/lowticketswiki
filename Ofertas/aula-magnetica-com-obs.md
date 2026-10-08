---
tipo: oferta
classe: oferta
slug: aula-magnetica-com-obs
nome: "Aula Magnética Com OBS"
nicho: a-identificar
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: ticto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Aula%20Magnetica%20OBS&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 38
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 38
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-08
visto_ultimo: 2026-10-08
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/aula-magnetica-com-obs"
gateways_detectados: [ticto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [ticto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-08
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Aula Magnética Com OBS

## Angulo
Achado novo no vault. Curso de R$38 via Pix, comprador pede devolucao por insatisfacao com material e falta de suporte. Provavel curso de uso do software OBS para criacao de conteudo/lives.

## Funil
anuncio -> pagina -> checkout ticto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-08 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/ticto/cancelamento-de-curso-aula-magnetica-com-obs-devido-a-insatisfacao-com-o-material-e-falta-de-suporte-com-solicitacao-de-devolucao-do-valor-pago-via-pix_augBSUhCbG-a60Ou/

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
