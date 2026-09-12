---
tipo: oferta
classe: angulo
slug: angulo-material-pronto-para-quem-ensina-danca
nome: "Angulo — material pronto para quem ENSINA danca"
nicho: danca
sub_nicho: material-para-professor
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=coreografias%20prontas&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 19.9
ticket_bump: 12
ticket_upsell: 0
ticket_medio_est: 30
margem_est: 0.92
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 4
s_lucro: 4
s_replica: 9
s_saturacao: 5
status: nova
visto_primeiro: 2026-09-06
visto_ultimo: 2026-09-06
rodadas_vista: 1
dias_no_ar: 10
criativos_ultima: 19
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: 
gateways_detectados: [ggcheckout, kiwify, payt, onprofit, hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 
veredito: replicar
prioridade: 3
tags: [oferta, lowticket, angulo, danca, imprimivel]
---

# Angulo — material pronto para quem ENSINA danca

**A metade replicavel do mercado de danca nao vende danca. Vende planejamento de aula.**

Quem compra nao e a aluna: e a professora de ballet, a lider de ministerio, o professor de
educacao fisica. Eles ja tem a obrigacao — ha uma turma esperando na quarta-feira — e o que falta
e repertorio. Por isso o produto pode ser **PDF**: ninguem precisa ver alguem dancando bonito,
precisa de uma sequencia escrita que funcione na sala.

E o mesmo deslocamento de comprador que o vault ja catalogou em [[angulo-material-pedagogico]]
(mae -> professora) e em [[missa-em-atividades]] (mae -> catequista). A novidade aqui e que ele
resolve o problema estrutural do nicho de danca: **danca normalmente obriga video, e video obriga
talento.** Este angulo nao obriga nenhum dos dois.

## Os operadores medidos em 06/09/2026

| Oferta | Comprador | Ticket | Entrega | Dias no ar |
|---|---|---|---|---|
| [[cantigas-da-bailarina]] | professora de Baby Class | R$ 19,90 + 7 bumps | PDF + audios | 9 |
| [[250-dinamicas-de-ballet]] | professora de ballet | R$ 10 / R$ 19,90 | PDF imprimivel | 9 |
| [[movimentos-de-adoracao]] | lider de ministerio | R$ 19,90 + bump R$ 9,90 | PDF | 4 |
| [[dicionario-em-movimento]] | lider de ministerio | R$ 67 | PDF + QR para video | nao medido |
| [[aerobico-ritmado]] | professor de ed. fisica | R$ 67 + certificado | video + PDF | 10 |

Cinco operadores, **quatro deles com menos de dez dias de anuncio**. Isso nao e um angulo maduro:
e uma coorte se formando agora.

## Por que `s_saturacao: 5` e nao 8

O reflexo seria chamar de campo aberto — o vault nunca tinha visto nenhuma dessas notas. O adendo
de 31/08 do `Pipeline.md` existe exatamente para impedir isso: **cobertura do radar nao e
concorrencia de mercado.** Cinco operadores ativos e a faixa 5-15 players, ainda com variacao de
angulo. Cinco.

O que sustenta o 5 e nao o 3: os cinco atacam **denominacoes diferentes de comprador** (ballet
infantil, ballet adulto, gospel, educacao fisica) e nenhum deles cobre mais de uma. Ha espaco
lateral, nao ha espaco frontal.

## A escada que ninguem monta

Tres camadas de ticket foram medidas no mesmo comprador gospel, por tres operadores diferentes:

- R$ 19,90 — coreografia pronta ([[movimentos-de-adoracao]])
- R$ 67 — vocabulario de movimento ([[dicionario-em-movimento]])
- R$ 40/mes ou R$ 397 — formacao tecnica ([[brumdance-3em1]])

**Nenhum dos tres vende os outros dois.** Sao estagios sequenciais do mesmo comprador, operados
por gente que nao se conhece. Quem montar as tres camadas sob um funil so captura a escada inteira
com um CPA.

## O que copiar

1. **O catalogo no checkout** de [[cantigas-da-bailarina]] — sete PDFs do mesmo nicho como bump,
   sem LP, sem criativo, sem trafego proprio. E o multiplicador de ticket mais barato do vault.
2. **O bump em bloco** de [[movimentos-de-adoracao]] — quatro PDFs por R$ 9,90 em vez de quatro
   ofertas separadas. Menos atrito, mesma margem.
3. **A prova social institucional** — depoimento com cargo e instituicao (pastora, coordenadora,
   professora), nao corpo dancando. Mantem o criativo fora do escrutinio estetico.

## O que evitar

Entrar a R$ 10 sem bump, como [[250-dinamicas-de-ballet]]. O CPA e o mesmo do concorrente de
R$ 19,90 com sete bumps; o faturamento por comprador nao e.

## Ofertas ligadas

[[cantigas-da-bailarina]] · [[250-dinamicas-de-ballet]] · [[movimentos-de-adoracao]] ·
[[dicionario-em-movimento]] · [[aerobico-ritmado]] · [[brumdance-3em1]]

Cinco ofertas nomeadas ligadas na estreia. Pelo adendo de 29/08 do `Scoring.md`, angulo com dois
ou mais operadores identificados e **padrao confirmado**, nao hipotese.

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
