---
tipo: painel
<<<<<<< HEAD
atualizado: 2026-09-11
=======
atualizado: 2026-08-31
>>>>>>> d5869cd14357e25e4453f7def9fac303c24add30
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

<<<<<<< HEAD
## Leitura atual — 2026-09-11 · parentalidade, TEA e TDAH

**Rodada dirigida: 7 novas ofertas, 3 revisitadas e 10 snapshots.** Relatório: [[2026-09-11]].

Prioridades por aderência: [[31-segredos-pais-tdah]] para TDAH e escola; [[tdah-tod-paula-frati]] para conflitos familiares; [[autismo-para-pais-lacerda]] para organização parental; [[meu-filho-e-unico-horleana]] e [[parentalidade-atipica-sarah-hayden]] para TEA + TDAH.

[[tea-sem-crise]] tem quatro anúncios ativos observados, pelo menos três vídeos distintos e anúncio desde 12/08; frente capturada em R$71. Os dois kits Só Escola responderam nesta consulta, por R$47 (TDAH) e R$37 (autismo). Não são manuais de parentalidade.

A Biblioteca de Anúncios funcionou nesta rodada. Ainda faltam métricas de tráfego para a maioria das ofertas; lucro não foi medido. **Scores e decisões automáticas nas Bases abaixo continuam provisórios quando faltam dados.** As outras ofertas não foram reclassificadas por falta de cobertura. Histórico anterior abaixo preservado como registro, não como leitura atual.

---

## Leitura histórica — 2026-08-29 (segunda passada)
=======
## Leitura atual — 2026-08-31 (segunda passada)
>>>>>>> d5869cd14357e25e4453f7def9fac303c24add30

**110 notas · 91 ofertas · 19 angulos · 0 novas nesta passada · 1 no corte de replicacao**

Duas passadas hoje. A da manha varreu o nicho infantil pela Biblioteca de Anuncios e trouxe quinze
notas; esta executou a fila que ela deixou. **A Etapa 1 nao estava disponivel aqui** — o navegador
interno recusou `facebook.com` duas vezes e o claude-in-chrome segue vazio. O adendo da manha
descreve um procedimento que custa 2-3 aprovacoes por termo, e **aprovacao pressupoe o Lucas na
frente da tela**: a Etapa 1 pelo navegador interno e ferramenta de rodada assistida, nao de rodada
agendada. A cadencia diaria que a manha declarou restaurada vale so para as passadas acompanhadas.

**A correcao que importa: as duas rodadas anteriores relataram o corte sem calcular o corte.** A
manha abriu anunciando o primeiro cruzamento de sempre — [[little-genius]], 7,60. Mas [[soulmate-sketcher]]
(7,85) e [[retrato-da-alma-gemea]] (7,65) ja cruzavam, e as duas nasceram em **30/08** — rodada que
fechou o texto dizendo "decimo dia de zero no corte". O corte e uma formula sobre o frontmatter e
ninguem a estava rodando; a narrativa vinha da memoria do que tinha acabado de ser escrito. Regra
nova de processo: **computar o ranking antes de narrar**, toda rodada.

**Auditadas, as duas caem — e pelo mesmo vicio, nos dois eixos de maior peso.** A soulmate marcava
`s_lucro: 9` com `dias_no_ar: 0`, `criativos_ultima: 0` e `ra_reclamacoes: 0`, e o corpo da nota
escrevendo *"so a Biblioteca de Anuncios mede"* — declarou nao ter instrumento e cravou o maximo do
eixo de peso 35. O retrato marcava `s_saturacao: 8` com a prosa da propria nota dizendo *"ha dezenas
de clones"*; ali nem faltava dado, faltava ler. Corrigidas para 6,10 e 6,40. **Isso inverte o
diagnostico de 29/08:** campo faltando nao empurra o score para baixo, empurra para onde quem
preencheu quis — e quem preenche acabou de gastar meia hora se convencendo de que a oferta e boa.
Hoje **22 ofertas** tem `s_lucro >= 5` sem nenhum insumo de longevidade e **14** tem `s_lucro >= 7`
nas mesmas condicoes, entre elas [[treino-trinca]], a nota que o Painel de 29/08 citou como "o teto
das ofertas reais". O teto era ele proprio um palpite. Regra nova no `Scoring.md`: **`s_lucro >= 7`
exige `dias_no_ar > 0` ou `ra_primeira_reclamacao`; sem isso o teto e 6** — aplicada so onde muda
veredito, para nao trocar um palpite por outro em lote.

**De medicao de campo, o angulo de alma gemea:** tres paginas de produtor no Reclame Aqui,
`retrato-da-alma-gemea` (M=206, N=21, mais recente ha 16 dias), `alma-gemea` (M=19, N=2, ha 3 meses)
e `desenho-da-alma-gemea` (M=16, N=0, ha 1 ano), mais Marcia Sensitiva, Mestre Zion, Aurara Vidal e
Alma Gemea Chay soltos nos corpos. **Seis operadores nomeaveis, um vivo** — e as 206 reclamacoes do
sobrevivente sao de nao-entrega. Mesma forma do achado da manha sobre bonecas de papel: o ativo
circula pronto, os clones sao muitos, e **o que separa vivo de morto nao e a copy, e a entrega.**
Proxima passada precisa ser **assistida**, para os tres itens de browser que ficaram na fila.
Distribuicao final: **52 morta · 29 esfriando · 20 nova · 9 ativa**.
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
