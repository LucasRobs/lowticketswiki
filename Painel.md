---
tipo: painel
atualizado: 2026-08-20
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-20

**7 ofertas vistas · 4 novas · 3 com movimento · 0 no corte de replicação**

Segunda rodada, quatro dias depois da primeira. Biblioteca de anúncios e unFunnelizer
seguem fora — extensão não conectada, nenhum aplicativo aprovado para controle de
desktop — então `dias_no_ar` e `criativos_ultima` continuam zerados em todas as 30
ofertas do vault. A tabela **Acelerando**, que o Painel chama de "a que vale dinheiro",
está vazia pela segunda rodada consecutiva. Ela vai continuar vazia até a extensão
conectar: `criativos_delta` não tem de onde vir.

**A busca por domínio netlify se confirmou como o método principal.** Foi ela que trouxe
três das quatro ofertas novas, repetindo o resultado de 16/08. O que era achado virou
procedimento: produtor sem domínio próprio é produtor em fase de teste, e a hospedagem
gratuita entrega essa lista de graça. A quarta oferta nova, a [[biblioteca-do-concurseiro]],
veio da lista de reclamações da Lowify usada como fonte de descoberta — o caminho que o
`Pipeline.md` prescreve e que agora tem duas confirmações.

**O achado da rodada é uma correção de método, não uma oferta.** A
[[wiapy-foto-com-pet]] cobra R$10,90 no Pix *depois* da compra, com 8 horas de espera
pela entrega. Isso não aparece na página de vendas, não aparece no checkout e não
apareceria nem no Brute Mode do unFunnelizer — não está no DOM, está no atendimento
pós-venda. Só quem pagou sabe, e o único lugar onde quem pagou fala é o Reclame Aqui.
A consequência é maior que a oferta: **`ticket_medio_est` está provavelmente subestimado
em todo o vault**, e o Reclame Aqui deixa de ser só proxy de volume para virar fonte
primária de anatomia de funil. Vale acrescentar ao `Pipeline.md` a instrução de ler o
corpo das reclamações procurando valores cobrados, não só contá-las.

**Nada passou no corte de replicação, pela segunda rodada.** O topo do dia é a
[[papel-magico-bonecas]] com score 6,75 e `s_replica` 10 — a primeira nota máxima do
vault nesse eixo, com um downsell de saída que nenhuma outra oferta mapeada tem. Ela
falha no corte por `s_lucro` 6, que é chute educado sobre sofisticação de funil, não
leitura de dado. Isso expõe o mesmo problema que o Diagnóstico já apontou: enquanto
`s_lucro` for estimado em vez de medido, o corte de 7,5 é praticamente inalcançável e o
instrumento está calibrado para não decidir nada. **Duas rodadas, zero candidatas, é
resultado do instrumento — não do mercado.** As duas pendências de método já registradas
(curva de sino em `s_lucro`, média geométrica no lugar da soma) deveriam ser resolvidas
antes da próxima rodada, ou a terceira vai terminar igual.

Nenhuma oferta decaiu: as 23 não vistas hoje estão na primeira ausência, e `esfriando` só
começa na segunda. Vale lembrar que elas não sumiram do mercado — sumiram do alcance de
um radar que, sem biblioteca de anúncios, só reencontra uma oferta quando ela gera
reclamação nova.

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
