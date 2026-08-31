---
tipo: oferta
classe: oferta
slug: missa-em-atividades
nome: "Missa em Atividades — kit catolico infantil imprimivel"
nicho: comportamento-infantil
sub_nicho: catequese-infantil
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: ""
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=missa%20em%20atividades&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 0
s_lucro: 5
s_replica: 9
s_saturacao: 9
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 35
criativos_ultima: 3
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/missa-em-atividades"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-31
veredito: replicar
prioridade: 3
tags: [oferta, lowticket, imprimivel]
---

# Missa em Atividades — o cruzamento mais vazio do vault

35 dias no ar, 3 criativos ativos, +200 recursos imprimiveis em PDF sobre a Santa Missa: partes
da celebracao, objetos liturgicos, cores, gestos e respostas da assembleia. Publico declarado:
pais, catequistas, educadores, paroquias e escolas catolicas.

## Por que `s_saturacao: 9`

O vault tem **dois clusters grandes que nunca se tocaram**: material pedagogico imprimivel
([[alfabetinho]], [[kit-so-escola-tdah]], [[clube-da-pedagogia]], [[angulo-material-pedagogico]])
e devocional cristao ([[desafio-romanos-12-2]], [[hinario-em-movimento]],
[[renovacao-da-mente-mulheres-no-secreto]], [[desafio-30-dias-com-deus]]).

Esta oferta e a **primeira interseccao observada em campo**, e esta praticamente sozinha nela.
A [[parabolas-kids]] chega perto mas entra por formacao de carater com a Biblia como veiculo;
esta entra por **liturgia**, que e vocabulario catolico especifico e nao tem concorrente medido.

## Por que o publico e melhor do que parece

Nao e so a mae. E a **catequista** — que compra material para vinte criancas, tem verba de
paroquia e nao pede reembolso de R$ 30. O mesmo deslocamento de comprador que a shortlist de
30/08 anotou na [[coletanea-regulacao-emocional]] (mae -> psicologa infantil), aqui ja resolvido
pelo proprio anunciante.

E o problema que ele nomeia e observavel toda semana:

> "Muitas criancas vao a Missa, sentam, levantam, ajoelham e respondem... mas ainda nao entendem
> o que esta acontecendo."

## O que falta

`ticket_frente: 0` e **sentinela, nao avaliacao** (`Pipeline.md`, item 6): o anuncio nao declara
preco e a LP nao foi capturada — o link do criativo nao apareceu no texto da Biblioteca. Com
`s_ticket: 0`, o score de 5,80 esta sistematicamente subestimado e **nao deve ser comparado com
as outras notas da rodada** ate a captura.

Prioridade 3 apesar do score: `s_saturacao: 9` com `s_replica: 9` e a combinacao mais rara do
vault, e o ativo (PDF ilustrado sobre um roteiro fixo e publico) e integralmente gerave por IA.

## Fila

Achar a LP pela pagina do anunciante na Biblioteca de Anuncios e capturar preco e gateway.

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
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
