---
tipo: painel
atualizado: 2026-08-23
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-23

**17 ofertas vistas · 5 novas · 1 retornou · 37 mudancas de status · 0 no corte de replicacao**

Quinta rodada. Biblioteca de Anuncios fora pelo quinto dia e unFunnelizer fora pelo quinto
dia — hoje nao por falta de grant, mas porque pedir o grant exige o Lucas presente e a
rodada e agendada. Tudo saiu do Reclame Aqui, agora em **nove gateways**, com Kiwify e
Hubla estreando. O vault fecha em **75 ofertas**. A tabela **Acelerando** segue vazia pelo
quinto dia, pela mesma razao de sempre.

**A correcao pendente desde 16/08 foi finalmente implementada, e o resultado e
desconfortavel do jeito certo.** O `Scoring.md` nao dizia o que fazer com uma oferta
ausente por exatamente uma rodada, entao 35 das 70 notas estavam presas em `nova` — metade
do vault descrita por um campo que so significava "ninguem recalculou". Com a regra escrita
e aplicada, 37 notas mudaram de status: sobram 5 `nova` e aparecem **53 `esfriando` de 75**.
Isso nao e o mercado esfriando. E o vault admitindo que a maior parte do que ele guarda foi
vista uma vez e nunca mais.

**O topo do ranking agora esta inteiramente em `esfriando`, o que confirma a reclamacao das
duas ultimas rodadas.** [[angulo-diagnostico-isca]] e [[angulo-desintoxicacao-telas]]
lideram em 7,35 com `ra_reclamacoes: 0` e duas rodadas sem serem vistas. Elas pontuam alto
porque foram avaliadas por hipotese de angulo, e ate hoje hipotese nao decaia. Agora o campo
`status` discorda do campo `score` na mesma linha da tabela — o que e progresso, porque
antes os dois concordavam em estar errados.

**Zero no corte pela quinta rodada, mas por um motivo novo e mais util que o anterior.** Nas
quatro primeiras, nada passava porque o score comprimia o sinal. Hoje nada passa porque as
unicas ofertas com evidencia de venda **medida** — [[unlovable]] com 149 dias desde a compra
de 27/03, [[stalkeia-ai]] com 7 reclamacoes e presenca em todas as rodadas, [[treino-trinca]]
com 10 — tem `s_replica` de 3, 4 e 6. E as ofertas com `s_replica` alto nao tem prova de
venda nenhuma. **O vault esta alimentando os dois lados do corte com fontes diferentes:
o Reclame Aqui so encontra o que gera briga, e o que gera briga e software, assinatura e
app — exatamente o que o Lucas nao replica.** Isso nao se conserta com peso nem com media
geometrica. Se conserta com a Biblioteca de Anuncios, que e a unica fonte capaz de dar
evidencia de venda a um ebook de R$ 27.

**O melhor achado da rodada nao tem nome.** [[desafio-anamnese-plano-alimentar]], na
Lastlink: order bump duplo no checkout e depois uma anamnese em interface de falso chat que
nunca conclui — cada tentativa dispara uma oferta de plano (R$ 200, R$ 200 trimestral,
R$ 100 aceita) e sem comprar a anamnese nao termina. A anamnese nao e onboarding, e o
mecanismo de downsell. Junto com o [[lowzap]], cujo upsell **Low Scale** foi cobrado depois
de recusa explicita na pagina, o padrao do degrau invisivel ganha uma versao mais agressiva:
nao e so cobrar o que o comprador nao viu, e cobrar o que ele disse nao. Nenhum dos dois
apareceria no Brute Mode.
---

## Ranking

```base
filters:
  and:
    - note.tipo == "oferta"
formulas:
  score: (note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100
  decisao: if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 7.5 && note.s_replica >= 7, "REPLICAR", if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 6, "observar", "descartar"))
properties:
  file.name:
    displayName: Oferta
  formula.score:
    displayName: Score
  formula.decisao:
    displayName: Decisao
views:
  - type: table
    name: Ranking
    order:
      - file.name
      - formula.score
      - formula.decisao
      - nicho
      - checkout
      - ra_reclamacoes
      - dias_no_ar
      - status
    sort:
      - property: formula.score
        direction: DESC

```

## Acelerando

Quem ganhou criativos desde a rodada anterior. **Esta é a tabela que vale dinheiro** —
o topo do ranking diz o que é bom, esta diz o que está esquentando *agora*.

```base
filters:
  and:
    - 'note.tipo == "oferta"'
    - 'note.criativos_delta > 0'
views:
  - type: table
    name: Acelerando
    order:
      - file.name
      - note.criativos_delta
      - note.criativos_ultima
      - note.dias_no_ar
      - note.nicho
    sort:
      - property: note.criativos_delta
        direction: DESC
```

## Fila de captura

Ofertas com sinal mas sem o unFunnelizer rodado. Enquanto estiverem aqui, os tickets
delas são estimativa.

```base
filters:
  and:
    - 'note.tipo == "oferta"'
    - 'note.unfunnelizer_capturado != true'
views:
  - type: table
    name: Fila
    order:
      - file.name
      - note.url_pagina
      - note.checkout
      - note.ra_reclamacoes
      - note.dias_no_ar
    sort:
      - property: note.ra_reclamacoes
        direction: DESC
```

## Rodadas

```base
filters:
  and:
    - 'note.tipo == "radar"'
views:
  - type: table
    name: Rodadas
    order:
      - file.name
      - note.ofertas_vistas
      - note.novas
      - note.retornaram
      - note.sumiram
    sort:
      - property: note.data
        direction: DESC
    limit: 30
```

---

## Diagnóstico do instrumento

Rodado em 2026-08-16 sobre as 6 primeiras ofertas. **O score composto está compactando
o sinal em vez de separá-lo.**

| Eixo | Amplitude |
|---|---|
| s_ticket | 6,00 |
| s_saturacao | 5,00 |
| s_replica | 4,00 |
| s_lucro | 3,00 |
| **score final** | **0,80** |

Seis ofertas muito diferentes em cada dimensão colapsam entre 6,00 e 6,80. Causa: os
eixos são anticorrelados na prática — ticket alto vem com nicho lotado, replicabilidade
fácil vem com ticket baixo — e a soma ponderada faz eles se anularem.

Correlação de cada eixo com o score final:

| Eixo | Peso | r com o score |
|---|---|---|
| s_replica | 30 | **+0,73** |
| s_saturacao | 15 | +0,33 |
| s_lucro | **35** | **−0,19** |
| s_ticket | 20 | −0,20 |

`s_lucro` tem o maior peso e influência praticamente nula. **Peso só funciona se a
variável variar** — e `s_lucro` ficou espremido entre 5 e 8 porque, sem biblioteca de
anúncios, as seis foram pontuadas pelo mesmo proxy magro.

**Correção proposta:** média geométrica ponderada no lugar da soma. A soma deixa um eixo
forte compensar um eixo quase zerado; a geométrica pune o elo fraco. Nos dados atuais
separa 1,4× melhor e joga `lowify-app-historias` de 3º para último — correto, porque
R$19 em campo lotado não é a terceira melhor oportunidade por mais fácil que seja.

Enquanto a fila de captura não esvaziar, **trate o ranking como ordem de investigação,
não como ordem de decisão.**

## Mesa de Garimpo — links de todas as ofertas (2026-08-21)

Página com as 57 ofertas do vault, cada uma com **página de vendas** e **busca pronta na
Biblioteca de Anúncios**. Filtros por nicho, veredito, "só com página" e "2+ rodadas".

https://claude.ai/code/artifact/a9f45cac-2553-48ec-8e9b-f86fdb7ec13f

Fonte dos dados: `_meta/ofertas-export.json`, gerado a partir do frontmatter das notas de
`Ofertas/`. Reexportar e republicar depois de cada rodada.
