---
tipo: painel
atualizado: 2026-08-28
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-28

**5 ofertas vistas · 1 nova · 0 retornaram · 22 mudancas de status · 0 no corte de replicacao**

Oitava rodada, com cobertura deliberadamente estreita: so PerfectPay e Kiwify, porque o adendo
de cadencia de 27/08 diz que com um dia de intervalo apenas esses dois giram a primeira pagina
rapido o bastante. Dez linhas lidas, oito repeticoes, dois IDs ineditos, **uma nota nova**.
Biblioteca de Anuncios e unFunnelizer fora pelo oitavo dia. O vault fecha em **84 ofertas**.

**A rodada achou uma fonte, e ela ataca o gargalo que esta pagina nomeou ontem.** Uma reclamacao
listada na PerfectPay tinha, dentro do corpo, um bloco de empresa que **nao era a PerfectPay** —
era `TW EMPREENDIMENTOS DIGITAIS`, com pagina propria no Reclame Aqui. O gateway reatribui a
reclamacao ao produtor e ela fica listada nos dois lugares; ha ate uma reclamacao vizinha
intitulada *"PERFECT PAY MOVENDO RECLAMACAO PRA OUTRA EMPRESA"*. A diferenca entre as duas fontes
e de natureza: a lista do gateway e **larga e rasa** (centenas de ofertas, cinco linhas,
`ra_reclamacoes` travado em 1); a pagina do produtor e **estreita e funda** — uma oferta so, 39
reclamacoes ativas, a mais antiga carimbada em 29/06. Isso deu **60 dias de idade medida** para a
[[google-captcha-tw]], a primeira vez em oito rodadas que uma nota recebe `dias_no_ar` real sem
Biblioteca de Anuncios. Virou a Etapa 3b do `Pipeline.md`.

**A oferta em si e o contraponto exato do achado de ontem.** A [[google-captcha-tw]] cobra uma
escada de taxas **ascendente e sem teto** — comeca em R$ 50, chega a R$ 795, um comprador somou
R$ 4.666,49 — enquanto o [[angulo-taxa-escalonada-decrescente]] fecha em tres degraus decrescentes
e R$ 46,70. O que segura a escada ascendente e uma pessoa: a *"gestora do GOOGLE CAPTCHA"* que
reabre a conversa a cada falha de acesso e converte o atrito no gancho da cobranca seguinte. Duas
escadas em duas rodadas, e a divisao util nao e a direcao — e o que sustenta o degrau. **As que
rodam sozinhas no checkout sao replicaveis; as que precisam de gente no WhatsApp nao sao.** Dai o
`s_replica: 2` e o score de 5,65, apesar do `s_lucro: 8`, o maior ja atribuido aqui.

**Onze ofertas morreram hoje — as primeiras do vault.** Todas com `visto_ultimo: 2026-08-16`,
sete rodadas de ausencia, cruzando o limiar do `Scoring.md`. Mas `morta` aqui quer dizer "saiu do
campo de visao do instrumento", nao "saiu do ar": nenhuma das onze foi procurada por nome desde
16/08, porque a rotina so le as primeiras paginas dos gateways. Distribuicao final: **55 esfriando
· 17 ativa · 11 morta · 1 nova**.

**Oitava rodada com zero no corte, e o topo do Ranking parado pela terceira vez.**
[[angulo-diagnostico-isca]] segue em 7,35 contra corte de 7,50, o mesmo numero de 24/08 e 27/08.
Nada mudou porque nada podia mudar: as seis notas do pelotao de cima ja tem `s_replica` 8 ou 9 e
todas tem `s_lucro` de proxy magro. **A proxima rodada deve gastar o tempo de outro jeito** — em
vez de reler a primeira pagina dos nove gateways, procurar pagina de produtor para as seis do topo.
Se alguma tiver, o `s_lucro` delas sai do palpite, e e isso, nao mais uma oferta nova, que tira o
vault do zero. Proxima rodada em **30/08 ou 31/08**.
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
