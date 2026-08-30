---
tipo: oferta
classe: oferta
slug: portal-do-mei-brasil
nome: "Portal do MEI Brasil"
nicho: servicos-empresariais
sub_nicho: taxa-sobre-servico-publico-gratuito
idioma: pt-BR
pais: BR
plataforma_ads: [google]
checkout: desconhecido
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=abrir%20mei%20online&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.95
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 0
s_lucro: 10
s_replica: 4
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-30
visto_ultimo: 2026-08-30
rodadas_vista: 1
dias_no_ar: 210
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/portal-do-mei-brasil"
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 889
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-30
veredito: observar
prioridade: 3
tags: [oferta, lowticket, servicos-empresariais, taxa-servico-gratuito]
---

# Portal do MEI Brasil

**O maior volume ja medido no vault, e o unico com cadencia diaria.** 889 reclamacoes
ativas — 5x a [[alfabetinho]], que detinha o teto desde ontem — e, ao contrario da
Alfabetinho, **nao e volume historico: esta chegando agora.**

## Os numeros

| Medida | Valor |
|---|---|
| **M** — ativas hoje | **889** |
| **N** — recebidas 01/02–31/07 | **362** (~60/mes) |
| Reclamacoes na ultima semana | **5 nas primeiras 5 linhas** (ha 1, 2, 3, 4 e 4 dias) |
| Reputacao | **Bom, 7,1/10** |
| Resposta | 100%, media de **14 horas** |
| Resolvidas | 78,9% · 213 avaliadas · 48,8% voltariam |

As cinco linhas da primeira pagina cobrem **quatro dias**. Nenhuma outra pagina de produtor
minerada ate hoje devolveu isso: a [[alfabetinho]] tinha a mais recente ha dois meses, a
[[certifica-brasil]] ha tres dias com apenas 13 ativas no total. Aqui sao ~60/mes sustentados
por seis meses.

## `dias_no_ar: 210` — o primeiro medido, e como foi medido

`M − N = 527`. Se agosto rodou na mesma taxa da janela (~60), sobram **~467 reclamacoes
anteriores a 01/02/2026**. Ou seja: a operacao ja existia quando a janela de seis meses abriu.
O piso conservador e a propria abertura da janela — **01/02/2026, 210 dias atras**.

Isto **nao** e generalizavel para qualquer produtor: ver o adendo que abri hoje no
`Pipeline.md`. So vale quando `M − N` e muito maior que a taxa mensal. Na [[certifica-brasil]],
`M − N = 5` com ~5 chegadas em agosto — ali o mesmo calculo daria zero informacao sobre idade.

Ainda assim, e a **primeira nota do vault com `dias_no_ar` derivado de medicao em vez de
acaso**, e ela existe sem Biblioteca de Anuncios.

## A mecanica

Cobrar por um servico que o governo presta de graca. O comprador busca "como abrir MEI" no
Google, cai num portal que **parece** o canal oficial, preenche o formulario inteiro de
abertura, paga por Pix — e recebe **um guia em PDF**.

> "Entrei nesse site e respondi todo o formulario de abertura do Mei, em momento algum
> disseram que estava pagando por um Guia PDF. La esta escrito que esta sendo aberto o Mei."
> — ID 257468219, 26/08/2026

O entregavel e literalmente um infoproduto. O que se vende nao e o PDF: e a **intencao
capturada no momento exato** — quem digitou "abrir MEI" ja decidiu, ja esta com o CPF na mao
e nao sabe que o processo e gratuito. Custo de aquisicao baixissimo por ser busca, nao
interrupcao. Isso explica os 60/mes.

Distribuicao dos problemas: **cobranca indevida (150), propaganda enganosa (101), estorno
(94)**. Todos derivam da mesma coisa — o comprador nao sabia o que estava comprando.

## O que a resposta da empresa entrega de graca

Duas coisas uteis, ambas na replica do ID 257468219:

1. **Operam atendimento de verdade** — 14h de resposta, 78,9% resolvido, reputacao Bom. Uma
   operacao que estorna nao morre de chargeback. E a diferenca entre isto e o
   [[retrato-da-alma-gemea]], que tem 206 reclamacoes de nao-entrega e 0% de resposta.
2. **Denunciam os proprios clones:** *"temos identificado situacoes em que terceiros utilizam
   indevidamente o nome e elementos de identificacao do Portal do MEI Brasil, inclusive por
   meio de paginas e enderecos eletronicos semelhantes"*. Traduzindo para o vault: **a mecanica
   ja esta sendo copiada em escala por terceiros**, o que e a confirmacao mais barata possivel
   de que ela paga. Tambem e o motivo de `s_saturacao: 3`.

## Por que nao passa no corte, e por que isso importa

Score **5,15**. Nao passa. E o motivo **nao** e o `dias_no_ar` faltando — pela primeira vez
ele esta la.

| Eixo | Nota | Por que |
|---|---|---|
| `s_lucro` | **10** | 210+ dias medidos, ~60/mes, chegada de ontem |
| `s_ticket` | **0** | sentinela: o valor foi redigido pelo RA em todos os corpos lidos |
| `s_replica` | **4** | o funil so converte porque o comprador **nao sabe** que o servico e gratuito |
| `s_saturacao` | **3** | clones admitidos pela propria empresa, mais 4 operadores no mesmo angulo |

`s_replica: 4` e o eixo que decide, e e uma decisao de conteudo, nao de dado faltando.
**A conversao vem da confusao com o canal oficial.** Tirar a confusao — dizer no criativo que
a abertura e gratuita e que se cobra pela assessoria — e um negocio legitimo e possivel, mas e
outro negocio, com outro CPA. O que da para copiar aqui e a **leitura de intencao de busca**:
achar um processo publico gratuito, chato e mal documentado, e vender o atalho **com o preco
na frente**. Isso replica; a ambiguidade nao.

**Correcao a leitura de ontem.** O Painel de 29/08 concluiu que o corte esta vazio porque falta
`dias_no_ar`. Esta nota e o contraexemplo: com `s_lucro` no maximo e idade medida, ela ainda
para em 5,15. A tese de ontem estava certa sobre a causa **media** do vault e errada como
explicacao unica — quando a idade aparece, `s_ticket` sentinela e `s_replica` de nicho
ambiguo assumem o freio.

## Estado dos dados

- **Confirmado:** volume (889/362), cadencia diaria, mecanica, entregavel (PDF), atendimento,
  existencia de clones, piso de idade.
- **Faltando:** ticket (redigido pelo RA — tentar corpo com valor nao redigido), gateway,
  URL da pagina, criativos.
- **Proximo passo:** o `s_ticket: 0` esta segurando 1,4 ponto de score. Um corpo com valor
  visivel resolve. Alternativa: a propria pagina de vendas, que ainda nao foi localizada.

Pagina do produtor: https://www.reclameaqui.com.br/empresa/mei-brasil-online/lista-reclamacoes/

Angulo: [[angulo-taxa-sobre-servico-gratuito]]

## Historico

```base
filters:
  and:
    - 'note.tipo == "observacao"'
    - 'note.slug == this.slug'
views:
  - type: table
    name: Snapshots
    order:
      - note.data
      - note.ra_reclamacoes
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
