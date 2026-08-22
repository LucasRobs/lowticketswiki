---
tipo: painel
atualizado: 2026-08-22
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-22

**16 ofertas vistas · 6 novas · 3 retornaram · 5 correções de score · 0 no corte de replicação**

Quarta rodada. Biblioteca de Anúncios fora pelo quarto dia e unFunnelizer fora por falta de
grant de desktop, então a rodada inteira saiu do Reclame Aqui — desta vez em **oito
gateways**, com Lastlink e PerfectPay entrando pela primeira vez como fonte de descoberta.
O vault fecha em **70 ofertas**. A tabela **Acelerando** segue vazia pelo quarto dia, pela
mesma razão de sempre: ela mede `criativos_delta`, e `criativos_delta` não tem de onde vir.

**O corpo da reclamação passou a entregar tempo no ar, que era o dado que faltava.** Três
ofertas citaram data de compra hoje: [[teacher-zap]] em março, [[unlovable]] em 27/03,
[[curso-massagem-tantrica]] em 12/08. Isso não mede o anúncio, mede a oferta — que é
exatamente o que `s_lucro` pergunta, e é proxy melhor que contagem de reclamações.
[[teacher-zap]] subiu para `s_lucro: 8` com cinco meses de venda **medidos**, não estimados;
[[unlovable]] para 7 com ~148 dias. Enquanto o browser estiver fora, procurar data de
compra no corpo deveria ser etapa explícita do `Pipeline.md`.

**Ampliar de cinco para oito gateways produziu mais sinal do que qualquer refinamento de
rubrica.** As cinco requisições novas em Lastlink e PerfectPay devolveram três retornos e
duas ofertas. E as três que "voltaram" nunca esfriaram de verdade — o radar é que não
olhava para onde elas estavam. Enquanto a cobertura de fontes mudar a cada rodada,
`esfriando` continua medindo o instrumento e não o mercado.

**O padrão do degrau invisível fechou em seis casos e agora é regra.** [[love-pix]] cobra
duas taxas de R$ 10 dentro do app depois dos R$ 25,90 da entrada; [[app-do-paizao]] oferece
o plano anual de R$ 250 depois da primeira mensalidade de R$ 50; [[lowzap]] cobra o upsell
de R$ 197 **através da Hubla**, não da Kirvano; [[unlovable]] roda Pix Automático que
sobrevive ao reembolso da primeira parcela; mais [[wiapy-foto-com-pet]] e [[cinefy-tv]]. Em
todos, o degrau caro é pós-compra e não está no DOM da página de vendas — o Brute Mode, que
o `Pipeline.md` chama de "a etapa que mais muda o score", não acharia nenhum. O Reclame Aqui
acha todos, porque é onde o comprador vai reclamar da cobrança que não esperava. Para funis
com escada pós-compra, a Etapa 3 é melhor que a Etapa 2, não complemento dela.

**A melhor descoberta de ontem não sobreviveu à leitura de hoje.** O [[app-do-paizao]], que
esta seção chamou em 21/08 de "o melhor achado, e não está no topo do ranking", entrega
treinos, dietas, comunidade e promessa de personal. É assinatura de fitness; a paternidade é
o recorte de público, não o produto. `s_replica` cai de 6 para 3 (saúde tem teto 4 no
`Scoring.md`), `s_saturacao` de 8 para 4, **score de 6,55 para 5,05**. A tese sobre o
público continua de pé — um ebook de R$ 27 falando com o pai segue sendo campo aberto — mas
não era esta oferta que a provava. Registrar o erro importa mais que corrigi-lo: a nota de
ontem foi escrita a partir do título da reclamação, e o corpo estava a uma requisição de
distância.

**Zero no corte pela quarta rodada, e o topo não se mexeu.** [[angulo-diagnostico-isca]] e
[[angulo-desintoxicacao-telas]] seguem empatadas em 7,35, abaixo do corte de 7,5. Vale dizer
o incômodo com todas as letras: **nenhuma das duas foi vista em rodada alguma além da de
estreia.** Elas lideram porque foram pontuadas por hipótese de ângulo em vez de evidência de
venda, e hipótese não decai. As duas correções pendentes desde 16/08 — curva de sino em
`s_lucro`, média geométrica no lugar da soma — continuam sem implementação, e hoje apareceu
uma terceira: 35 das 70 notas ainda estão com `status: nova` porque o `Scoring.md` não diz o
que fazer com uma oferta ausente por exatamente uma rodada. **Quatro rodadas, zero
candidatas: a essa altura o instrumento já foi diagnosticado três vezes e não foi
consertado nenhuma.**

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
