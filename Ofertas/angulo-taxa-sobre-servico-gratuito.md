---
tipo: oferta
classe: angulo
slug: angulo-taxa-sobre-servico-gratuito
nome: "Angulo — cobrar pelo servico publico que e gratuito"
nicho: servicos-empresariais
sub_nicho: taxa-sobre-servico-publico-gratuito
idioma: pt-BR
pais: BR
plataforma_ads: [google]
checkout: desconhecido
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=abrir%20mei%20segunda%20via%20certidao&search_type=keyword_unordered&media_type=all"
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
s_lucro: 9
s_replica: 4
s_saturacao: 4
status: nova
visto_primeiro: 2026-08-30
visto_ultimo: 2026-08-30
rodadas_vista: 1
dias_no_ar: 210
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-30
veredito: observar
prioridade: 2
tags: [oferta, lowticket, angulo, servicos-empresariais]
---

# Angulo — cobrar pelo servico publico que e gratuito

**A isca nao e o produto, e a busca.** O comprador digita "abrir MEI", "segunda via de
certidao", "2a via do IPVA" — um processo que o Estado presta de graca, mas que e chato, mal
documentado e assustador o suficiente para ele pagar pelo atalho. O portal aparece na busca,
parece oficial, cobra por Pix e entrega **um PDF**.

E a mesma familia do [[angulo-taxa-do-certificado]], com uma diferenca que muda a economia:
ali a taxa vem **depois** do tempo investido no curso; aqui ela vem **no pico da intencao**,
antes de qualquer investimento. Nao ha nada para produzir e nao ha nada para entregar alem do
guia — o produto e o formulario.

## Operadores

Nasce com um operador **medido** e quatro leads da mesma busca:

| Operador | Ativas (M) | Janela 6m (N) | Estado |
|---|---|---|---|
| [[portal-do-mei-brasil]] | **889** | **362** | **vivo, ~60/mes, chegada de ontem** |
| Certidao Online Brasil | nao medido | — | fila |
| Cartorio Brasil | nao medido | — | fila |
| RECEBIMENTOS IPVA | nao medido | — | fila |
| Postnet | nao medido | — | fila |

Um operador medido nao faz padrao confirmado — pela regra do `Scoring.md`, angulo com um
operador ainda e hipotese forte, nao padrao. **Mas ha uma confirmacao de segunda ordem:** o
proprio Portal do MEI Brasil declara em replica publica que terceiros clonam suas paginas e
enderecos. Quem esta sendo clonado esta pagando as contas.

Medir os quatro da fila e a tarefa de menor custo e maior retorno da proxima rodada: quatro
fetches, e o angulo sai de hipotese para padrao confirmado ou morre.

## Onde procurar mais

O gerador de operadores aqui e a **lista de processos publicos gratuitos com atrito alto**:
abertura e baixa de MEI, DAS em atraso, certidao negativa, segunda via de documento, consulta
de FGTS, agendamento de INSS, CadUnico, Bolsa Familia, titulo de eleitor, antecedentes
criminais. Cada item dessa lista e uma busca no RA por pagina de produtor.

## O teto: `s_replica: 4`

O funil converte porque o comprador **acha que esta no canal oficial**. Retire a ambiguidade e
a conversao cai — nao um pouco, e o mecanismo inteiro. E o mesmo diagnostico do
[[retrato-da-alma-gemea]], por caminho diferente: **o que faz a oferta funcionar e exatamente
o que nao se pode copiar.**

A replica legitima existe e e mais chata: assessoria com preco na frente, dizendo no criativo
que o processo e gratuito e que se cobra pelo acompanhamento. Vira servico, nao infoproduto,
com CPA maior e ticket maior. Contabilidade online vive disso ha anos.

**Nao confundir com o vizinho de vitrine.** A busca por "taxa de saque" e "liberacao de premio"
na mesma rodada devolveu Viva Sorte, Play Videos Premiados, Roleta Pix e Mangofy — mecanica
parecida, categoria diferente: la nao ha entregavel nenhum, so a taxa. A [[play-videos-premiados]]
foi medida e esta morta (M=106, N=0, mais recente ha 7 meses). Este angulo tem PDF; aquele nao
tem nada, e o vault nao vai catalogar fraude pura como oferta replicavel.

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
