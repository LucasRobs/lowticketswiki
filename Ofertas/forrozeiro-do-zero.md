---
tipo: oferta
classe: oferta
slug: forrozeiro-do-zero
nome: "Forrozeiro do Zero (nome comercial nao confirmado)"
nicho: danca
sub_nicho: forro
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: "https://quiz.forrozeirodozero.com.br/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=aprender%20forr%C3%B3&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.85
modelo: [quiz]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 6
s_saturacao: 6
status: nova
visto_primeiro: 2026-09-06
visto_ultimo: 2026-09-06
rodadas_vista: 1
dias_no_ar: 8
criativos_ultima: 2
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/forrozeiro-do-zero"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 
veredito: observar
prioridade: 1
tags: [oferta, danca, forro, quiz]
---

# Forrozeiro do Zero

Anunciante `matheuscasbri`, dois criativos com varias versoes, no ar desde 29/08. O criativo e o
melhor texto de danca da varredura:

> "O segredo que esta ensinando homens a dancar forro do zero sem passar vergonha na festa.
> Nao importa se voce trava quando alguem te chama pra dancar. Nao importa se acha que nao tem
> ritmo. Nao importa se nao tem par pra treinar. 7 dias. Do zero. Na sua casa."

Cartao de link: **"Crie seu Plano"** com "+1.200 Alunos recomendam". Destino
`quiz.forrozeirodozero.com.br` — funil de **quiz**, unico da varredura de danca.

## Por que registrar mesmo sem preco

O angulo e a peca replicavel, nao o produto. Tres objecoes nomeadas na ordem certa (ritmo,
vergonha, falta de par) e a terceira e a que nenhuma escola presencial consegue responder — e
exatamente por isso que a versao online vence ali. Ver o mesmo mecanismo de diagnostico em
[[angulo-diagnostico-isca]] e [[angulo-quiz-retrato-ia]].

## Estado dos dados

`s_ticket: 0` e **sentinela**, nao avaliacao: a pagina de quiz retorna so um shell JS e o preco
so aparece no fim do fluxo. Pelo `Pipeline.md`, nota com `s_ticket: 0` nao deve ser comparada com
as outras no Ranking ate a captura. Primeiro item da fila para a proxima rodada.

## Criativos (Biblioteca de Anuncios)

Anunciante: **matheuscasbri** — `facebook.com/100068510731647`
Pagina de vendas: <https://quiz.forrozeirodozero.com.br>

| Criativo | Veiculacao iniciada | Nota |
|---|---|---|
| [1064507922644275](https://www.facebook.com/ads/library/?id=1064507922644275) | 29/08/2026 | varias versoes |
| [1871711103791552](https://www.facebook.com/ads/library/?id=1871711103791552) | 29/08/2026 | varias versoes |

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
