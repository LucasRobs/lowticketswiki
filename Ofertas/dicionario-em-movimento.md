---
tipo: oferta
classe: oferta
slug: dicionario-em-movimento
nome: "Dicionario em Movimento — 90 movimentos para ministracao"
nicho: danca
sub_nicho: danca-gospel-ministerio
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: onprofit
url_pagina: "https://dicionarioemmovimento.site/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=minist%C3%A9rio%20de%20dan%C3%A7a&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 67
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 67
margem_est: 0.88
modelo: [direct]
formato_entrega: [ebook, curso]
tem_recorrencia: false
s_ticket: 7
s_lucro: 3
s_replica: 7
s_saturacao: 5
status: nova
visto_primeiro: 2026-09-06
visto_ultimo: 2026-09-06
rodadas_vista: 1
dias_no_ar: 12
criativos_ultima: 3
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/dicionario-em-movimento"
gateways_detectados: [onprofit]
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 
veredito: observar
prioridade: 2
tags: [oferta, lowticket, danca, gospel]
---

# Dicionario em Movimento

**A ponte entre PDF e video sem pagar o custo de uma area de membros.** O produto e um PDF
interativo com mais de 90 "palavras" (movimentos); cada verbete tem um QR Code que abre um video
curto do movimento. O comprador imprime e coloca num fichario. Nao ha plataforma, nao ha aula,
nao ha turma.

R$ 67,00 a vista ou 8x R$ 8,80, checkout **OnProfit** (`pay.onprofit.com.br`) — gateway ainda
nao registrado no vocabulario do `Schema.md` antes desta rodada.

## Por que e relevante para o vault

E a versao de **ticket tres vezes maior** do mesmo comprador de [[movimentos-de-adoracao]]: lider
de ministerio de danca. Enquanto a oferta de R$ 19,90 vende coreografias prontas para copiar, esta
vende o **vocabulario** para montar as proprias. Duas camadas do mesmo nicho, sem competir de
frente.

A pagina menciona "packs adicionais" futuros a partir do "Pack Essencial 1.0" — upsell declarado
mas nao capturado. Marcado `upsell_oculto: true`.

## O custo real

Noventa videos curtos de um movimento cada. Nao e uma producao de curso, mas tambem nao e PDF
puro: e o teto natural de `s_replica: 7`. Some-se a isso a autoridade declarada da autora
(Victoria Mofato, "20 anos", ministerio "um dos mais influentes do pais") — replicar a oferta e
facil, replicar a credibilidade nao.

## Estado dos dados

- **`dias_no_ar: 12` e sentinela, nao medicao.** O dominio apareceu nos links da consulta por
  "ministerio de danca", mas a atribuicao do anuncio ao anunciante correto nao foi confirmada —
  havia tres paginas gospel na mesma tela. Nao datar pelo palpite.
- Sem `dias_no_ar`, `s_lucro` fica travado no teto 6 pelo adendo de 31/08 do `Scoring.md`.
  Atribuido 3.

## Criativos (Biblioteca de Anuncios)

Anunciante: **Escola de Danca Louvor na Terra**
Pagina de vendas: <https://dicionarioemmovimento.site>

| Criativo | Veiculacao iniciada | Nota |
|---|---|---|
| [1401478468587799](https://www.facebook.com/ads/library/?id=1401478468587799) | 25/08/2026 | 5 anuncios usam esse criativo |
| [3514532285389014](https://www.facebook.com/ads/library/?id=3514532285389014) | 25/08/2026 | 5 anuncios usam esse criativo |
| [1769707290732626](https://www.facebook.com/ads/library/?id=1769707290732626) | 31/08/2026 | 4 anuncios, varias versoes |

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
