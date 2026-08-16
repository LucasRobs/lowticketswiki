---
tipo: painel
atualizado: 2026-08-16
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-16

**2 passadas · 9 ofertas · 0 no corte de replicação**

A rodada teve duas passadas: varredura ampla via Reclame Aqui (6 ofertas) e busca
dirigida ao nicho de educação física via domínio de hospedagem gratuita (3 ofertas).
Biblioteca de anúncios e unFunnelizer seguem fora — extensão Claude in Chrome não
conectada — então `dias_no_ar` e `criativos_ultima` continuam zerados em todas.

**O método mais produtivo foi a busca por domínio netlify.** Uma consulta
`site:netlify.app` com as palavras do nicho devolveu cinco ofertas ativas que nenhuma
busca por palavra-chave comercial tinha encontrado. Produtor sem domínio próprio é
produtor em fase de teste — é a janela que interessa.

**Achado do dia: rotação de domínio como sinal.** O [[kit-300-aulas-edfisica]] existe
em três subdomínios netlify, um já 404, com nome auto-gerado. Página que sobe, roda e
queima é campanha ativa. Vale virar métrica própria: contar deploys distintos da mesma
oferta.

**Teste de um segundo para separar máquina de amador: o botão de compra.** As duas
ofertas boas levam a checkout com link direto (Wiapy, GG Checkout); a descartada leva a
WhatsApp. Venda manual não escala e não tem bump.

**Pendência de método.** A rubrica de `s_lucro` em `_meta/Scoring.md` premia tempo no ar
alto (90+ dias = nota 9-10). A estratégia adotada em 16/08 quer o oposto para o mercado
BR: menos de 35 dias, para não pegar o fim da onda. As duas leituras estão certas para
objetivos diferentes e **a rubrica atual está errada para esta estratégia**. Precisa
virar curva de sino, com pico entre 15 e 35 dias.

---

## Ranking

```base
filters:
  and:
    - 'note.tipo == "oferta"'
formulas:
  score: '(note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100'
  decisao: 'if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 7.5 && note.s_replica >= 7, "REPLICAR", if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 6, "observar", "descartar"))'
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
      - note.nicho
      - note.checkout
      - note.ra_reclamacoes
      - note.dias_no_ar
      - note.status
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
