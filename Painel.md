---
tipo: painel
atualizado: 2026-08-27
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-27

**17 ofertas vistas · 4 novas · 0 retornaram · 4 mudancas de status · 0 no corte de replicacao**

Setima rodada, e a primeira com tres dias de intervalo em vez de um — a cadencia que o adendo
de 24/08 do `Pipeline.md` prescreveu. **Funcionou.** Nas seis rodadas diarias anteriores, cerca
de quarenta das quarenta e cinco vagas nas listas repetiam a rodada anterior. Hoje apareceram
quatro ofertas nomeadas e ineditas, e **duas com carimbo do proprio dia** — coisa que nao tinha
acontecido nenhuma vez em seis rodadas. O instrumento nao estava quebrado; estava sendo lido
rapido demais. Biblioteca de Anuncios e unFunnelizer fora pelo setimo dia. O vault fecha em
**83 ofertas** e a tabela **Acelerando** segue vazia pela mesma razao de sempre.

**Mas a correcao de 24/08 estava incompleta, e a rodada de hoje mostrou onde.** Aquela regra
mandava abrir o corpo e confiar no carimbo. Hoje a reclamacao da
[[desafio-anamnese-plano-alimentar]] apareceu com **ID 257133061** — exatamente o ID que a nota
de 24/08 registra como *"a de 22/08 as 17h33"* — exibindo carimbo de **25/08 as 16h24**. Mesmo
ID, mesmo texto, tres datas em tres leituras: o carimbo se move quando a reclamacao e editada ou
respondida. Sobrou um unico identificador estavel, o **ID**, e ele e monotonico. A anamnese tem o
menor ID de toda a rodada e o segundo carimbo mais recente — ela e a mais antiga, e o carimbo diz
o contrario. **Regra adotada:** deduplicar e ordenar por ID; `ra_reclamacoes` so incrementa com ID
inedito e maior que o maior da rodada anterior. Aplicada, deu **zero incrementos hoje**.

**O melhor achado de mecanica e o [[angulo-taxa-escalonada-decrescente]].** R$ 27,90 pelo curso,
R$ 12,90 de "confirmacao", R$ 5,90 de "liberacao" — os tres pagos, na PerfectPay, carimbados hoje
as 19h59. E a **quarta forma do degrau invisivel** que o vault cataloga, depois do upsell escondido
([[lowzap]], [[love-pix]]), do downsell forcado ([[desafio-anamnese-plano-alimentar]]) e do custo
transferido para a infra da vitima ([[renderizador-imagem-recarga-google]]). A novidade e a direcao:
os degraus **diminuem**, entao a resistencia cai a cada passo em vez de subir, e a soma quase dobra o
ticket de frente. Como mecanica de checkout — nao de produto — ela e replicavel sobre qualquer
entrega real: `s_replica: 8`.

**Setima rodada com zero no corte, e desta vez o topo do Ranking parou de subir.** A melhor nota do
vault segue [[angulo-diagnostico-isca]] com 7,35, o mesmo valor de 24/08, contra um corte de 7,50.
Seis notas estao entre 7,00 e 7,35 e **todas as seis tem `s_replica` 8 ou 9** — o eixo de
replicabilidade ja esta saturado no topo. O que falta nao e achar oferta mais facil de copiar, e
`s_lucro`, que depende de tempo no ar, que depende da Biblioteca de Anuncios. **O gargalo migrou de
captura de ticket para medicao de idade.** Enquanto isso, uma observacao de fonte para a proxima
rodada: a PerfectPay tem 287 mil reclamacoes ativas contra 17 mil da Cakto e 37 mil da Kirvano, e
foi a unica com carimbo do dia. Se a cadencia for diaria, so PerfectPay e Kiwify justificam a
visita; para os outros sete, o intervalo util e de tres dias ou mais.

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
