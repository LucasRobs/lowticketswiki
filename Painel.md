---
tipo: painel
atualizado: 2026-08-24
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-08-24

**20 ofertas vistas · 4 novas · 0 retornaram · 8 mudancas de status · 0 no corte de replicacao**

Sexta rodada. Biblioteca de Anuncios e unFunnelizer fora pelo sexto dia. Tudo saiu do Reclame
Aqui, nos mesmos nove gateways. A Cakto voltou a ser legivel — o cabecalho hoje diz "Todas as
reclamacoes", sem o `?problema=` que sabotou a leitura de ontem — e foi o unico gateway a
devolver sinal genuinamente novo. O vault fecha em **79 ofertas**. A tabela **Acelerando**
segue vazia pelo sexto dia, pela mesma razao de sempre.

**A descoberta da rodada nao e uma oferta: e que o instrumento esta sendo lido mais rapido do
que ele se atualiza.** Abrindo os corpos datados, a reclamacao da
[[desafio-anamnese-plano-alimentar]] de hoje e a de 22/08 as 17h33, ID 257133061 — a mesma que
originou a nota ontem. E a linha da [[stalkeia-ai]] de hoje aponta para a URL `bsQiiX5mms5RNOcb`,
**a mesma citada como evidencia na nota de 22/08**: ela esteve na primeira pagina em tres
rodadas seguidas e foi contada como sinal novo em duas. Os rotulos relativos ("Ha 8 horas")
mentem — a reclamacao da anamnese aparece como "Ha 21 horas" com carimbo proprio de 43. Das
quarenta e cinco vagas nas nove listas, quarenta repetem a rodada anterior.

**Regra adotada agora:** `ra_reclamacoes` so incrementa quando a data do corpo e posterior a
rodada anterior; aparecer na lista conta como avistamento, nao como sinal. [[stalkeia-ai]] fica
em 7 e nao em 8. A consequencia real e sobre **cadencia, nao rubrica**: rodar diariamente contra
uma fonte que se move a cada dois ou tres dias nao produz serie temporal, produz a mesma
fotografia carimbada com datas diferentes e uma contagem que sobe sozinha. Enquanto a Biblioteca
de Anuncios estiver fora, rodar a cada dois ou tres dias mediria a mesma coisa com um terco do
ruido.

**Zero no corte pela sexta rodada, mas faltou pouco de um jeito novo.**
[[cafe-premium-barista-academy]] tem o perfil que as cinco rodadas anteriores nunca produziram:
`s_replica: 7`, nicho de cafe/barista intocado no vault, sem regulacao, sem estigma, sem rosto,
com doze dias de venda medidos e um angulo lateral inedito (a compra foi para presentear). Ela
para em 4,70 **apenas porque `s_ticket` e sentinela**. Um ticket medio de R$ 60 a levaria a ~6,2
sem que nenhum outro eixo se mexa. E o argumento mais concreto ate agora de que o gargalo do
vault e **captura de ticket, nao descoberta de oferta**.

**O melhor achado de mecanica e o [[renderizador-imagem-recarga-google]].** Ele vende uma
interface e so depois da compra revela que o processamento roda na conta Google do proprio
comprador, que precisa criar credencial e por credito la. E uma terceira forma do degrau
invisivel: o vault ja catalogava o upsell escondido ([[lowzap]], [[love-pix]]) e o downsell
forcado ([[desafio-anamnese-plano-alimentar]]); esta nao cobra mais nada e ainda assim nao paga
nada, porque a infraestrutura e da vitima. `margem_est: 0.95` nao e otimismo, e o modelo — e a
versao honesta do mesmo produto, com a recarga declarada na pagina, mantem a margem e mata o
passivo.

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
