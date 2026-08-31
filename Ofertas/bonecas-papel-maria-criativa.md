---
tipo: oferta
classe: oferta
slug: bonecas-papel-maria-criativa
nome: "+150 Bonecas de Papel — Maria Criativa"
nicho: comportamento-infantil
sub_nicho: imprimivel-brincadeira
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: "https://bonecasdepapel28.lovable.app"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=bonecas%20de%20papel&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 17.9
ticket_bump: 0
ticket_upsell: 27.9
ticket_medio_est: 24
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 3
s_lucro: 8
s_replica: 10
s_saturacao: 2
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 54
criativos_ultima: 9
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/bonecas-papel-maria-criativa"
gateways_detectados: [kirvano]
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

# +150 Bonecas de Papel — Maria Criativa

Concorrente direta da [[papel-magico-bonecas]], e a comparacao lado a lado e o achado: **as duas
ofertas tem a mesma estrutura de degraus, os mesmos sete bonus e a mesma promessa.** Basico
R$ 17,90 (de R$ 47,90), Completo R$ 27,90 (de R$ 143,50) — a Papel Magico cobra R$ 12,90 e
R$ 24,90 com ancoragem **identica** de R$ 47,90 e R$ 143,50.

Ancoragem identica ao centavo nao e coincidencia. **Uma copiou a outra, ou as duas copiaram a
mesma fonte.** Isso e a evidencia mais forte que o vault ja teve de que o ativo deste angulo
circula pronto — o que confirma `s_replica: 10` e derruba `s_saturacao`.

## Funil

Anuncio -> LP em `lovable.app` (host gratuito) -> Kirvano, dois links de checkout:
`pay.kirvano.com/1c26a88d-...` (basico) e `pay.kirvano.com/fbdbc67e-...` (completo).

Bonus: 12 Casinhas (R$ 27) · +50 Pets (R$ 27) · +50 Itens de Camarim (R$ 27) · +30 Comidinhas
(R$ 27) · +30 Bebes (R$ 17,90) · Mini Kit Irmao (R$ 17,90). Garantia **30 dias**.

## O criativo e melhor que o produto

O texto que roda ha 54 dias e nostalgia pura, dirigida a mae e nao a filha:

> "Lembra das bonecas de papel que sua mae te dava nos anos 90? Aquele momento na mesa da sala,
> tesoura na mao... Aquela infancia voltou. E agora voce pode dar pra sua filha."

Nao vende brinquedo. Vende **devolver a propria infancia** — e depois entrega um PDF de R$ 17,90.
Confirma a regra 1 da shortlist de 30/08: o produto parece ser sobre a crianca e nao e.

## O que copiar / o que evitar

**Copiar:** a garantia de 30 dias (a Papel Magico tambem tem; num ticket de R$ 20 o custo de
reembolso e menor que o ganho de conversao) e a escada basico/completo, que e upsell sem pagina
de upsell — o degrau esta no proprio checkout.

**Evitar:** entrar por "bonecas de papel" generico. Sao no minimo **seis operadores ativos** no
mesmo termo hoje (ver [[angulo-bonecas-de-papel-imprimivel]]). O leilao esta caro e os criativos
sao intercambiaveis.

## Estado dos dados

- **Medido hoje:** `dias_no_ar: 54` (veiculacao iniciada 08/07/2026), 9 criativos ativos da mesma
  anunciante ("Camila Andrade") entre 08/07 e 10/08, precos, checkouts, bonus, garantia.
- **Nao medido:** downsell de saida (a Papel Magico tem um de R$ 17,90; aqui nao foi testado
  abandono de checkout).

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
