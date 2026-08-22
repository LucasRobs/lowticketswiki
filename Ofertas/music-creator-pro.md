---
tipo: oferta
slug: music-creator-pro
nome: "Music Creator Pro"
nicho: musica-producao
sub_nicho: pacote-arquivos
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Music%20Creator%20Pro&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 40
margem_est: 0.95
modelo: [direct]
formato_entrega: [pdf]
tem_recorrencia: false
s_ticket: 5
s_lucro: 3
s_replica: 8
s_saturacao: 7
status: nova
visto_primeiro: 2026-08-22
visto_ultimo: 2026-08-22
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: [wiapy]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [wiapy]
ra_primeira_reclamacao: 2026-08-22
ra_checado: 2026-08-22
veredito: observar
prioridade: 1
tags: [oferta, lowticket]
---

# Music Creator Pro

Descoberta na primeira página da Wiapy em 2026-08-22. Reclamação ID 257113387, aberta
às 11:15 e **reembolsada às 11:57** — 42 minutos. Esse tempo de resposta é ele próprio um
dado: a Wiapy resolve rápido demais para que o volume de reclamações vire proxy confiável
de faturamento nesse gateway.

## Angulo
Nome em inglês com sufixo "Pro" vendendo ferramenta de criação musical. O comprador
esperava **aulas explicativas de como usar**; recebeu "só arquivos em word".

## Funil
Nao capturado. A frase "so tem arquivos em word" e a peca de anatomia: o produto é um
pacote de documentos vendido com promessa de software/curso. Mesmo mecanismo de
[[kit-convites-casamento]] — a promessa é a ferramenta, a entrega é o arquivo.

## Estado dos dados
- **Confirmado:** existe, vende, roda em Wiapy, reclamacao de 22/08/2026, entrega em .doc.
- **Provisorio:** ticket (nao citado; 40 e estimativa da faixa Wiapy), nicho exato.
- **Faltando:** pagina de vendas, anunciante, dias no ar, criativos, bump/upsell.

`s_replica: 8` — pacote de arquivos é entrega digital trivial. `s_lucro: 3` é o piso
honesto: uma reclamação, zero dias no ar medidos.

Evidencia: https://www.reclameaqui.com.br/wiapy/solicitacao-de-devolucao-de-produto-digital-music-creator-pro-por-falta-de-aulas-explicativas-e-baixa-qualidade_TH51Fb94-jPtDoTQ/

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
