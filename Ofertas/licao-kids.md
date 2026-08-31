---
tipo: oferta
classe: oferta
slug: licao-kids
nome: "Licao Kids — loja de atividades imprimiveis"
nicho: material-pedagogico
sub_nicho: acervo-professora
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: "https://licaokids.com.br"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=licao%20kids&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 9.9
ticket_bump: 0
ticket_upsell: 97
ticket_medio_est: 25
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 3
s_lucro: 6
s_replica: 7
s_saturacao: 5
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 50
criativos_ultima: 1
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/licao-kids"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-31
veredito: observar
prioridade: 2
tags: [oferta, lowticket, imprimivel]
---

# Licao Kids — loja, nao funil

Sousa Marketing Digital LTDA · CNPJ 46.941.473/0001-94 · 50 dias no ar.

## A arquitetura e o achado

Nao e uma landing page. E uma **loja com categorias** — Atividades Crista, Caligrafia Cursiva e
Bastao, Combo Premium, Datas Comemorativas, Desenhos para Colorir, Matematica — e mais de 25
produtos entre R$ 9,90 e R$ 10,00.

Tres mecanismos de ticket empilhados sobre um catalogo unico:

1. **Item avulso** a R$ 9,90 / R$ 10,00 (ancorado em R$ 34,90).
2. **Cupom KIDS**: compre 3, ganhe 15% — empurra o carrinho de 1 para 3 itens.
3. **Combo "pague uma vez e tenha acesso a tudo": R$ 97,00**, declarado como 80,6% de desconto
   sobre R$ 500.

O R$ 97 e o mesmo movimento do upgrade de R$ 28 do [[clube-da-pedagogia]], numa escala maior:
**o catalogo inteiro existe para tornar o combo obvio.** Cada produto de R$ 10 e, na pratica,
um anuncio do de R$ 97 hospedado dentro da propria loja.

## Contra o modelo de LP unica

O cluster inteiro do vault e LP unica -> checkout. Esta e a primeira operacao infantil catalogada
que roda **vitrine**. Vantagem: um so trafego alimenta 25 ofertas e a mesma verba testa qual
categoria converte. Desvantagem: exige plataforma de loja, gestao de catalogo e produz atrito de
navegacao que a LP unica nao tem — por isso `s_replica: 7` e nao 9.

## O que copiar

**A categoria "Atividades Crista" dentro de uma loja pedagogica.** E o cruzamento que o vault
persegue em duas notas separadas ([[parabolas-kids]] e [[angulo-material-pedagogico]]) e que aqui
ja esta operando: a mesma professora compra folclore, matematica e devocional infantil no mesmo
carrinho. Um publico, tres nichos, um checkout.

**PIX com entrega na hora** em destaque no topo — no ticket de R$ 10 o PIX nao e forma de
pagamento, e reducao de atrito: nao tem CVV, nao tem parcelamento, nao tem recusa de cartao.

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
