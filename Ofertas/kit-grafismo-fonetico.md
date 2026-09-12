---
tipo: oferta
classe: oferta
slug: kit-grafismo-fonetico
nome: "Kit Grafismo Fonetico — Leitura Facil"
nicho: material-pedagogico
sub_nicho: alfabetizacao
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: whatsapp
url_pagina: ""
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=grafismo%20fonetico&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 20
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 20
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 2
s_lucro: 7
s_replica: 8
s_saturacao: 4
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 39
criativos_ultima: 10
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/kit-grafismo-fonetico"
gateways_detectados: [whatsapp]
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

# Kit Grafismo Fonetico — venda por conversa, 10 criativos

39 dias no ar e **o maior numero de criativos ativos da rodada**: um bloco de 6 anuncios e outro
de 4, mesmo texto, datas diferentes (23/07 e 14/08). Criativo repetido em volume e o sinal de
`s_lucro` que o `Scoring.md` premia — e aqui ele e visivel sem abrir nada.

`checkout: whatsapp` — nao ha gateway. Mesmo padrao de [[planos-aula-infantil-500]]: venda por
conversa, "menos de R$ 20,00 no Pix", entrega do PDF pelo proprio WhatsApp.

## O que o texto do anuncio entrega de graca

Uma aula inteira de copy defensiva:

- **Numero de mecanismo:** "aprende ate 5x mais rapido" com "apenas 10 minutos por dia" — o mesmo
  par velocidade+cabimento da [[parabolas-kids]].
- **Pseudo-mecanismo neurologico:** "ativando multiplas areas do cerebro". Explica sem prometer.
- **Desqualificacao explicita:** *"Nao indicado para adultos aprenderem a ler."* Parece perda de
  publico; e o contrario. Delimitar quem **nao** deve comprar e prova de honestidade barata, e
  filtra o lead que geraria reembolso.
- **Educacao especial pela porta lateral:** "se voce trabalha com criancas da Educacao Especial,
  esse material pode ser um divisor de aguas" — alcanca o publico de laudo **sem prometer
  tratamento**, que e exatamente o teto de `s_replica` que derruba [[kit-so-escola-tdah]].

## Limite do modelo

WhatsApp elimina taxa de gateway e recupera o carrinho na conversa, mas nao tem order bump,
upsell automatico nem rastreio de conversao — e nao escala sem atendente. `s_ticket: 2` travado
em R$ 20 sem esteira.

**O que copiar e o criativo, nao o checkout.** Os quatro movimentos acima cabem numa LP com
Cakto atras e ticket 3x maior.

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
