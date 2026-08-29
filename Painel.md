---
tipo: painel
atualizado: 2026-08-29
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-29

**4 ofertas vistas · 1 nova · 0 retornaram · 21 mudancas de status · 0 no corte de replicacao**

Nona rodada. Biblioteca de Anuncios e unFunnelizer fora pelo nono dia. O Painel de ontem deu uma
ordem explicita — *procurar pagina de produtor para as seis do topo do Ranking* — e a rodada
executou. **Ela falhou como escrita, funcionou reformulada, e a diferenca entre as duas coisas e o
achado do dia.** O vault fecha em **85 ofertas**.

**A ordem nao podia ser cumprida porque cinco das seis notas do topo sao angulos, e angulo nao tem
produtor.** Nao e detalhe de execucao: e o Ranking admitindo um vies. Angulo pontua alto porque
abstracao nao tem defeito — uma oferta real tem ticket que nao aparece, gateway que queima,
produtor que sumiu; um angulo tem so a ideia, e ideia sempre parece replicavel. O corte
(`score >= 7,5` **e** `s_replica >= 7`) foi desenhado para achar oferta, nao padrao. **Nove rodadas
de zero no corte com angulos ocupando as seis primeiras posicoes e o sintoma disso, nao do
mercado.**

**A reformulacao rendeu a maior nota de volume do vault.** Procurar produtor *no nicho* do angulo,
em vez de *do* angulo, achou a [[alfabetinho]]: **177 reclamacoes ativas**, 4,5x a
[[google-captcha-tw]] que ontem era o teto. E o operador nomeado por tras do
[[angulo-material-pedagogico]], catalogado ha treze dias como padrao sem dono — a primeira vez que
uma nota de angulo daqui ganha nome proprio. Mas o numero tem duas metades: 177 ativas contra
apenas 24 recebidas na janela de seis meses, com a mais recente ha dois meses. **Volume historico,
sem aceleracao.** Reputacao Bom, 11h de resposta, 90% resolvido — entrega de verdade. `s_lucro: 7`:
grande, provada, nao esquentando agora.

**O achado de metodo e que a Etapa 3b tem duas portas, e a de fora e melhor.** Ontem se chegava a
pagina do produtor por dentro, esperando a reclamacao certa cair nas cinco linhas do gateway. Hoje
ficou claro que ela e pesquisavel direto por nicho, o que inverte a economia da rodada: **a primeira
pagina da PerfectPay nao mudou nada em 24h — os tres IDs eram todos de rodadas anteriores — enquanto
uma unica busca por nicho devolveu cinco produtores ineditos.** Isso tambem corrige a tabela de
cadencia de 27/08: a PerfectPay tem 287.431 reclamacoes ativas e mesmo assim nao girou, ou seja
volume da empresa nao prediz giro da primeira pagina. O preco e que `dias_no_ar` continua fora de
alcance — paginacao nao passa no filtro de proveniencia do fetch, entao sem browser a Etapa 3b
entrega volume, nao idade. O substituto que funcionou e o contador `M - N`: mostrou que a
[[google-captcha-tw]] acelerou ~4,6x em agosto e que a [[alfabetinho]] desacelerou, em uma
requisicao cada.

**Nona rodada com zero no corte e o topo parado em 7,35 pela quarta vez.** Nao adianta esperar que
uma oferta nova resolva: o corte esta parado porque a rubrica compara angulo com oferta na mesma
tabela. **A proxima rodada deve mexer no instrumento antes de minerar mais** — marcar `tipo: angulo`
no frontmatter ou separar as Bases, para que o corte volte a olhar so o que tem produtor, ticket e
gateway. Depois disso, continuar a varredura de produtores por nicho: comportamento infantil,
artesanato e cursos de oficio ainda nao tiveram os seus procurados por fora. Distribuicao final:
**62 esfriando · 17 morta · 5 ativa · 1 nova** — cinco ativas em 85 e o alcance do instrumento
falando, nao o mercado, e `esfriando` com 62 notas ja nao separa nada.

Proxima rodada em **01/09**, sem varrer gateway.

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
