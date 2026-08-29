---
tipo: painel
atualizado: 2026-08-29
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-29 (segunda passada)

**88 notas · 73 ofertas · 15 angulos · 3 novas nesta passada · 0 no corte de replicacao**

A tarefa disparou de novo no mesmo dia. Em vez de repetir a varredura — que menos de 24h depois nao produziria sinal, e sobrescreveria os snapshots de hoje — esta passada executou a ordem que a rodada da manha tinha deixado: **mexer no instrumento antes de minerar mais.**

**O campo `classe` separou oferta de angulo, e o vies era real: 1,1 ponto de score e 1,6 de `s_replica`** a favor da abstracao (angulo 6,55 / 7,86 contra oferta 5,43 / 6,28). O criterio e a tag, nao o prefixo do slug — [[angulo-taxa-escalonada-decrescente]] tem nome de angulo mas gateway, ticket e ID de reclamacao, entao ficou como oferta. `tipo` continua `oferta` nas duas para nao quebrar Bases e Dataview.

**Mas separar nao destravou o corte, e essa e a correcao que importa.** O Painel de ontem culpava os angulos por nove rodadas de zero-no-corte. Nenhum angulo cruzava: o melhor marca 7,35, abaixo de 7,5. Tirar os angulos nao promoveu ninguem — revelou que **o teto das ofertas reais e 6,95** ([[treino-trinca]]). A causa e um campo faltando: **`dias_no_ar` esta zerado em 66 das 71 ofertas (93%)**, e ele alimenta `s_lucro`, que tem peso 35. Fixando `s_lucro = 10` e mantendo o resto, **24 ofertas cruzariam o corte**. Ou seja: **zero-no-corte nao e leitura do mercado, e o eco da rubrica rodando sem o insumo principal** — e nao deve mais ser reportado como diagnostico.

**Do garimpo, tres notas novas, todas de uma busca so.** [[certifica-brasil]] e o unico achado quente: M=13 contra N=8 na janela de seis meses, ~5 chegadas em agosto, **aceleracao de ~3,8x**, com reclamacoes de 2, 3 e 5 dias atras — o unico produtor com movimento na ultima semana. Mecanica de prova online com certificado pago, sem curso a entregar. [[certificado-curso-online]] e o oposto: 58 ativas mas so 3 em seis meses, parada, e a unica com **ticket capturado (R$ 139,90)**. O par ilustra o defeito do score melhor que o Diagnostico abaixo: a morta marca 5,30 e a viva 4,90, porque uma teve ticket capturado por acaso. Das duas nasceu o [[angulo-taxa-do-certificado]] — primeiro angulo do vault a **nascer com operador nomeado**, com cinco encontrados de uma vez.

**O limite da porta de fora tambem ficou claro:** "artesanato + moldes" devolveu seis lojas de material fisico e nenhum infoproduto. **A busca por produtor funciona quando o termo descreve a mecanica ("certificado", "taxa"), nao o produto.** Proxima rodada em **01/09**: abrir o corpo da reclamacao de pagamento da [[certifica-brasil]] (um fetch destrava ticket e gateway da unica oferta acelerando) e varrer por mecanica — "taxa de saque", "liberacao de premio", "segunda via". Distribuicao final: **62 esfriando · 17 morta · 5 ativa · 4 nova**.

---

## Ranking — ofertas reais

Só `classe: oferta`. Ângulo tem tabela própria mais abaixo: ele não tem produtor, gateway
nem ticket, então não pode disputar o corte de replicação com uma oferta concreta.

```base
filters:
  and:
    - note.tipo == "oferta"
    - note.classe == "oferta"
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

## Padrões (ângulos)

Nota de ângulo é **padrão sem dono**. A métrica útil aqui não é o score composto — é quantas
ofertas nomeadas já foram ligadas ao padrão. Zero operador = hipótese. Dois ou mais = padrão
confirmado, e aí a próxima rodada procura produtor *no nicho* dele (Etapa 3b, porta de fora).

```base
filters:
  and:
    - note.tipo == "oferta"
    - note.classe == "angulo"
formulas:
  score: (note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100
properties:
  file.name:
    displayName: Ângulo
  formula.score:
    displayName: Score
views:
  - type: table
    name: Padroes
    order:
      - file.name
      - formula.score
      - nicho
      - sub_nicho
      - s_replica
      - s_saturacao
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
    - 'note.classe == "oferta"'
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
    - 'note.classe == "oferta"'
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
