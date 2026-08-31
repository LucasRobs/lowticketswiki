---
tipo: meta
---

# Rubrica de score

Quatro eixos, 0-10 cada. O score composto é o que ranqueia as Bases.

```
score = (s_lucro*35 + s_replica*30 + s_ticket*20 + s_saturacao*15) / 100
```

**Por que esses pesos.** Sinal de lucro pesa mais porque é o único eixo que responde à
pergunta que importa — *isso está funcionando agora?*. Replicabilidade vem logo atrás
porque uma oferta ótima que você não consegue executar vale zero. Ticket é importante
mas enganoso isolado: ticket alto com criativo parado é oferta morrendo. Saturação
entra com o menor peso porque é o eixo mais fácil de contornar com ângulo novo.

---

## `s_lucro` — sinal de que está dando lucro (peso 35)

Você não vê o faturamento. Vê os proxies de que alguém está pagando pra manter aquilo no ar.

| Nota | Sinal |
|---|---|
| 0-2 | < 7 dias no ar, poucos criativos, sem histórico |
| 3-4 | 7-20 dias, criativos estáveis mas poucos |
| 5-6 | 20-45 dias, criativos crescendo devagar |
| 7-8 | 45-90 dias **ou** `criativos_delta` fortemente positivo |
| 9-10 | 90+ dias no ar com criativos ainda subindo — está escalando |

Regra prática: **tempo no ar é o proxy mais confiável.** Ninguém queima verba por 60
dias numa oferta que não paga.

## `s_replica` — facilidade de replicar (peso 30)

| Nota | Sinal |
|---|---|
| 0-2 | Depende de autoridade/rosto específico, ou produto físico com logística |
| 3-4 | Produção pesada: curso longo, software, comunidade ativa |
| 5-6 | Exige produção média e alguma expertise real no nicho |
| 7-8 | Ebook/planilha/mini-curso, ângulo claro, criativo simples de refazer |
| 9-10 | Entrega digital trivial, funil de 2 páginas, criativo genérico |

Penalize sem dó: marca registrada, licenciamento, figura pública, nicho regulado
(saúde, financeiro) → teto de 4.

## `s_ticket` — ticket e margem (peso 20)

Considere o **ticket médio estimado**, não o de frente. Uma oferta de R$27 com bump de
R$19 e upsell de R$97 é uma oferta de ~R$50.

| Nota | `ticket_medio_est` (BRL) |
|---|---|
| 0-2 | < 20 |
| 3-4 | 20-35 |
| 5-6 | 35-60 |
| 7-8 | 60-120 |
| 9-10 | > 120, ou qualquer valor com recorrência |

Ajuste: `margem_est` < 0.6 → tire 2 pontos.

## `s_saturacao` — campo livre (peso 15, **invertido**)

10 é bom. Você está medindo espaço, não concorrência.

| Nota | Sinal |
|---|---|
| 0-2 | Dezenas de players no mesmo ângulo, criativos idênticos |
| 3-4 | 5-15 players, ângulo batido |
| 5-6 | Alguns players, ainda há variação de ângulo |
| 7-8 | 2-4 players, ângulo com espaço |
| 9-10 | Player único, ou nicho/idioma ainda intocado |

---

## Ciclo de vida — como `status` muda

A skill recalcula a cada rodada:

| Status | Condição |
|---|---|
| `nova` | primeira rodada em que apareceu |
| `aquecendo` | `criativos_delta` > 0 por 2+ rodadas seguidas |
| `ativa` | vista na rodada de hoje, sem tendência clara |
| `esfriando` | não vista por 2-6 rodadas, ou `criativos_delta` < 0 por 3 seguidas |
| `morta` | não vista por 7+ rodadas |

Oferta que volta de `esfriando`/`morta` conta como **retorno** — sinalize na nota da
rodada. Retorno costuma significar que o dono resolveu um gargalo e voltou a escalar:
vale mais atenção do que uma oferta nova.

## Corte de decisão

- `score >= 7.5` **e** `s_replica >= 7` → candidata a replicar
- `score >= 6` → observar, revisar semanalmente
- `s_lucro <= 3` após 3 rodadas → descartar, não gasta mais atenção

---

## Adendo — ausencia de exatamente uma rodada (2026-08-23)

A tabela de ciclo de vida acima tinha um buraco: `nova` so descrevia a rodada de estreia
e `esfriando` so comecava em 2 rodadas de ausencia. Uma oferta ausente por **exatamente
uma rodada** nao se encaixava em nenhuma linha, entao a skill nao mexia no status e ela
ficava `nova` para sempre. Em 22/08 isso tinha 35 das 70 notas travadas — metade do vault
descrita por um campo que so significava "ninguem recalculou".

**Regra:** `nova` vale apenas na rodada de estreia. A partir da rodada seguinte, o status
e funcao da ausencia, sempre:

| Rodadas sem ver | Status |
|---|---|
| 0 (vista hoje) | `ativa` (ou `aquecendo`, se `criativos_delta` > 0 por 2+ rodadas) |
| 1 | `ativa` — ausencia de uma rodada nao e sinal, e cobertura |
| 2-6 | `esfriando` |
| 7+ | `morta` |

A contagem e em **rodadas**, nao em dias: o radar nao roda todo dia e datas de calendario
mentiriam sobre a frequencia de observacao.

**Efeito colateral que era o ponto:** aplicada em 23/08, a regra moveu 37 notas e deixou
53 das 75 em `esfriando`. Isso nao e o mercado esfriando, e o vault admitindo que a maior
parte do que ele guarda foi visto uma vez e nunca mais. Enquanto a Biblioteca de Anuncios
estiver fora, essa e a leitura correta.

---

## Adendo — o corte so vale para `classe: oferta` (2026-08-29, segunda passada)

O corte de decisao acima (`score >= 7,5` **e** `s_replica >= 7`) foi desenhado para achar
oferta replicavel, nao padrao. Com a introducao de `classe` no `Schema.md`:

**O corte de replicacao se aplica apenas a `classe: oferta`.** Angulo nao entra: ele nao
tem produtor para copiar, gateway para conferir nem ticket para validar — o que se replica
de um angulo e a ideia, e isso e insumo de criativo, nao decisao de negocio.

Para `classe: angulo` a leitura util nao e o score composto e sim **quantas ofertas nomeadas
o angulo ja tem ligadas a ele**. Angulo com zero operador identificado e hipotese; com dois
ou mais, e padrao confirmado. Ver [[angulo-material-pedagogico]] → [[alfabetinho]].

### Correcao importante: separar angulo NAO destravou o corte

A leitura de 28/08 atribuia nove rodadas de zero-no-corte ao fato de os angulos ocuparem o
topo do Ranking. **A separacao provou que essa explicacao estava errada.** Nem os angulos
cruzavam: o melhor deles marca 7,35, abaixo de 7,5. Tirar os angulos da tabela nao promoveu
ninguem — apenas revelou que o teto das ofertas reais e **6,95** ([[treino-trinca]]).

A causa real e outra, e e mensuravel:

| Campo | Ofertas reais sem o dado |
|---|---|
| `dias_no_ar` == 0 | **66 de 71 (93%)** |
| `unfunnelizer_capturado` != true | 71 de 71 (100%) |
| `s_ticket` == 0 (sentinela) | 11 de 71 |
| `ra_reclamacoes` == 0 | 23 de 71 |

`dias_no_ar` e o insumo principal de `s_lucro`, que tem **peso 35** — o maior da rubrica.
Com o campo zerado em 93% das notas, `s_lucro` vira palpite conservador em quase todo o
vault, e o palpite conservador e o que segura o score abaixo do corte.

**Teste do contrafactual:** fixando `s_lucro = 10` e mantendo todo o resto,
**24 ofertas cruzariam o corte** — entre elas [[desafio-romanos-12-2]] (8,25),
[[hinario-em-movimento]] (8,20) e [[renovacao-da-mente-mulheres-no-secreto]] (7,90).
Ou seja: **o corte nao esta vazio porque o mercado e ruim. Esta vazio porque falta um
campo.** Enquanto a Etapa 1 estiver fora e a Etapa 3b nao entregar idade, zero-no-corte
e o resultado esperado da rubrica, nao uma leitura do mercado — e nao deve ser reportado
como se fosse.

---

## Adendo — teto de `s_lucro` sem insumo de longevidade (2026-08-31, segunda passada)

O Painel de 29/08 diagnosticou que campo faltando **derruba** o score: `dias_no_ar` zerado
em 93% do vault fazia `s_lucro` virar palpite conservador e segurava todo mundo abaixo do
corte. O diagnostico estava certo sobre a causa e **errado sobre a direcao**. Campo faltando
nao empurra para baixo nem para cima — empurra para onde quem preencheu quis.

Medido em 31/08, sobre `classe: oferta`:

| Condicao | Notas |
|---|---|
| `s_lucro >= 5` com `dias_no_ar: 0` **e** `ra_reclamacoes: 0` | **22** |
| `s_lucro >= 7` sem `dias_no_ar` **e** sem `ra_primeira_reclamacao` | **14** |

O caso que provocou o adendo: [[soulmate-sketcher]] entrou em 30/08 com **`s_lucro: 9`**,
`dias_no_ar: 0`, `criativos_ultima: 0`, `ra_reclamacoes: 0` — e a propria nota escrevendo,
no corpo, *"so a Biblioteca de Anuncios mede"*. Ou seja: a nota declarava nao ter instrumento
e mesmo assim atribuiu a nota maxima do eixo de maior peso. Resultado: score 7,85,
`veredito: replicar`, `prioridade: 3` — **o topo do Ranking, construido sobre nada medido.**

### A regra

As faixas 7-8 e 9-10 de `s_lucro` sao definidas **exclusivamente em tempo no ar**. Nao ha
como argumentar por elas sem um insumo de longevidade. Portanto:

> **`s_lucro >= 7` exige `dias_no_ar > 0` ou `ra_primeira_reclamacao` preenchida.**
> Sem nenhum dos dois, o teto e **6**.

Faixas 0-6 continuam podendo ser argumentadas por sinal mole (mecanica, escada de ofertas,
qualidade da pagina) — o que nao se pode e alegar escala sem ter medido escala.

### Escopo da aplicacao nesta passada

Aplicada **apenas onde muda veredito**: [[soulmate-sketcher]], `s_lucro` 9 → 4, score 7,85 →
6,10, `veredito` replicar → observar. As outras 13 violacoes estao todas abaixo de 7,5 e o
teto so as reordena no meio da tabela — ficam na fila para quando a Etapa 1 medir, em vez de
serem rescoradas em lote por um numero que tambem seria palpite.

**Vale registrar quem mais viola**, porque uma delas sustentava a tese do Painel: 
[[treino-trinca]] tem `s_lucro: 9` sem medicao nenhuma, e foi ela que o Painel de 29/08 citou
como *"o teto das ofertas reais e 6,95"*. O teto era ele proprio um palpite.

### Corolario — `s_saturacao` alto contra corpo de nota que diz o contrario

O mesmo vicio, no eixo invertido. [[retrato-da-alma-gemea]] carregava `s_saturacao: 8`
("2-4 players, angulo com espaco") enquanto o **corpo da propria nota** listava seis avatares
intercambiaveis e escrevia, ao pe da letra, *"o angulo esta lotado"* e *"ha dezenas de clones"*.
Corrigido para **2** em 31/08.

Esse erro e mais barato de achar que o de `s_saturacao` por falta de Etapa 1: **nao precisa de
browser, precisa de ler a nota.** Vale uma varredura de contradicao interna antes de qualquer
rodada de garimpo — campo otimista contra prosa pessimista, na mesma nota.
