---
tipo: oferta
classe: oferta
slug: little-genius
nome: "Little Genius — Kit de 235+ atividades educativas"
nicho: material-pedagogico
sub_nicho: estimulacao-cognitiva
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kiwify
url_pagina: "https://www.thelittlegenius.com.br"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=little%20genius&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 162
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 162
margem_est: 0.85
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 10
s_lucro: 7
s_replica: 7
s_saturacao: 7
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 76
criativos_ultima: 1
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/little-genius"
gateways_detectados: [kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-31
veredito: observar
prioridade: 3
tags: [oferta, lowticket, material-pedagogico]
---

# Little Genius — 235 atividades a R$ 162

**Score 7,60 com `s_replica: 7`. E a primeira nota de `classe: oferta` a cruzar o corte de
decisao do `Scoring.md` — o teto anterior era 6,95 ([[treino-trinca]]).**

Antes de comemorar, leia a secao de ressalvas: o cruzamento depende de dois numeros que **nao
foram confirmados em checkout aberto**, e de um julgamento de `s_replica` que e discutivel.

## O que ela quebra

O vault inteiro assume que material imprimivel infantil e um mercado de R$ 10 a R$ 47. Doze das
treze ofertas medidas hoje vivem nessa faixa; a mediana da rodada e **R$ 17,90**. A Little Genius
cobra **R$ 162** pelo mesmo formato — PDF de atividades — e sustenta isso ha **76 dias de
anuncio ativo**.

Se o preco esta certo, a leitura e dura e util: **o piso de R$ 10 e escolha dos operadores, nao
limite do mercado.** Os R$ 12 da [[colecao-caligrafia-cursiva]] e os R$ 10 da
[[mundo-criativo-caligrafia]] nao sao o que a mae aceita pagar — sao o que o vendedor achou que
ela aceitaria.

## Funil

Anuncio (video 1min) -> LP em dominio proprio -> checkout em **dois** dominios distintos:
`checkout.thelittlegenius.com.br/85623611` e `checkout.aprendendobrincando.com.br/99880857`.

Dois dominios de checkout apontando para a mesma oferta e o mesmo padrao de
[[parabolas-kids]] e da [[colecao-caligrafia-cursiva]]: **teste paralelo com verba**, nao site
duplicado. Sinal de operacao com metodo.

Promessa: *"Treine o cerebro da crianca enquanto ela brinca"* — 235 atividades de raciocinio
logico, matematica e resolucao de desafios. "Aprendendo Brincando" no segundo dominio sugere
marca guarda-chuva com mais de uma oferta.

## Ressalvas que o score nao mostra

1. **`ticket_frente: 162` nao foi lido num checkout aberto.** A pagina cita R$ 162 e tambem
   "de R$ 222,00". Pode ser o preco cheio de uma oferta parcelada, ou ancoragem mal lida. **Ate
   abrir o checkout, trate `s_ticket: 10` como hipotese**, e a hipotese sozinha vale 2,0 pontos
   do score composto.
2. **`s_replica: 7` e julgamento, nao medicao.** 235 atividades de qualidade e um acervo
   consideravel; a rubrica pode defender 6 ("producao media e alguma expertise"). Com
   `s_replica: 6` o score cai para **7,30 e a oferta sai do corte.** O cruzamento e por margem
   estreita e depende de uma casa decimal de opiniao.
3. **`criativos_ultima: 1`.** Um unico criativo ativo visto. 76 dias com um criativo e
   estabilidade, nao escala — nao confundir com a aceleracao da [[colecao-caligrafia-cursiva]].

## Proxima acao

Abrir os dois checkouts e confirmar o valor. **E o unico fetch da fila que muda um veredito.**
Se R$ 162 se confirmar, esta e a oferta mais importante do vault: prova que da para vender
imprimivel infantil a 10x o preco de mercado, e a estrutura toda (LP, PDF, checkout) e a mesma
que ja esta catalogada aqui treze vezes.

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
