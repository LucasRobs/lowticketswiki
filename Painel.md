---
tipo: painel
atualizado: 2026-08-21
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-21

**9 ofertas vistas · 7 novas · 1 com movimento real · 14 esfriando · 0 no corte de replicação**

Três rodadas gravadas neste dia: o cluster religioso, o cluster de comportamento infantil
(17 notas) e esta varredura de gateways. O vault fecha o dia com **64 ofertas**. A
Biblioteca de Anúncios seguiu fora pela terceira rodada — extensão não conectada — então
`dias_no_ar` e `criativos_ultima` continuam zerados em todas elas, e a tabela
**Acelerando** está vazia pelo terceiro dia. Ela mede `criativos_delta`, e `criativos_delta`
não tem de onde vir.

**A lista de reclamações de gateway virou o método de descoberta mais barato do vault.**
Sete ofertas novas saíram da *primeira página* de cinco gateways — Lowify, Wiapy, Kirvano,
Cakto e Ticto — ao custo de cinco requisições. Nenhuma delas teria aparecido por busca de
nicho ou por domínio netlify, que eram os métodos das rodadas anteriores. Isso reordena o
`Pipeline.md` na prática: enquanto o browser estiver fora, a Etapa 3 deixa de ser
validação final e passa a ser a porta de entrada.

**O corpo da reclamação continua entregando anatomia de funil, e agora com quatro
confirmações.** [[script-da-banca]] revelou a escada inteira num parágrafo — R$ 9,99 na
entrada, upsell de R$ 29,99 ao fim do conteúdo. [[lowzap]] entregou o nome do upsell e o
fato de ele ser cobrado mesmo após recusa no checkout. [[unlovable]] entregou cinco meses
de assinatura ativa numa frase sobre data de compra, que é o sinal de receita mais concreto
que o vault produziu até hoje. [[mounjaro-de-pobre]] entregou a distância deliberada entre
o criativo e o produto. Nada disso está no DOM de uma página de vendas, e nada disso sairia
do Brute Mode. Junto com o PIX oculto da [[wiapy-foto-com-pet]] descoberto em 20/08, são
cinco casos: **o Reclame Aqui é fonte primária de anatomia, não proxy secundário de volume.**

**A correção da rodada é uma armadilha de contagem.** O rótulo "Há X horas" da listagem do
Reclame Aqui marca a última atividade do caso, não a data de abertura. A reclamação do PIX
da [[wiapy-foto-com-pet]] aparecia como "Há 15 horas" e é de 04/08 — a mesma já registrada.
Contar pela listagem infla `ra_reclamacoes`, e `ra_reclamacoes` alimenta `s_lucro`. A regra
agora é abrir o corpo antes de contar; foi ela que evitou registrar uma aceleração
inexistente na Wiapy e que confirmou uma real na Cakto, onde o
[[instalador-robo-pronto-2]] ganhou a segunda reclamação em rodadas diferentes — a primeira
série temporal de verdade do vault.

**O melhor achado não está no topo do ranking.** É o [[app-do-paizao]], com score 6,55.
As dezessete notas do cluster infantil convergiram na leitura de que o nicho vende alívio
de culpa da mãe; o ponto cego dessa leitura é que, se o que converte é falar com o
comprador sobre ele mesmo, existe um discurso de culpa paterna que ninguém está usando. A
única oferta encontrada falando com o pai não vende ebook de R$ 27 — vende **assinatura**.
O cluster inteiro roda sem backend nenhum, e essa roda com recorrência.

**Nada passou no corte de replicação, pela terceira rodada.** A melhor das sete novas é o
[[app-do-paizao]] com 6,55, e o topo do vault inteiro segue empatado em 7,35 entre
[[angulo-diagnostico-isca]] e [[angulo-desintoxicacao-telas]] — ambos abaixo do corte de 7,5. A causa é a mesma que o Diagnóstico abaixo já nomeou e que segue sem
correção: `s_lucro` pesa 35%, é o único eixo que responde "isso está dando lucro agora?", e
é estimado em vez de medido porque a biblioteca de anúncios nunca foi lida. As duas
pendências de método — curva de sino em `s_lucro`, média geométrica no lugar da soma —
estão registradas desde 16/08. **Três rodadas, zero candidatas, é o instrumento falando,
não o mercado.** A quarta rodada vai terminar igual se nada mudar antes dela.

Quatorze ofertas vistas só em 16/08 completaram a segunda ausência e decaíram para
`esfriando`. Nenhuma morreu ainda — `morta` exige sete rodadas — e vale repetir que
`esfriando`, hoje, mede a cobertura do radar e não a saúde da oferta.

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
