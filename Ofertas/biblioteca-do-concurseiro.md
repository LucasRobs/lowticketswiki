---
tipo: oferta
slug: biblioteca-do-concurseiro
nome: "Biblioteca do Concurseiro"
nicho: concursos
sub_nicho: acervo-pdf
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: "https://bibliotecadoconcurseiro.site/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Biblioteca%20do%20Concurseiro&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 27
margem_est: 0.9
modelo: [vsl]
formato_entrega: [pdf]
tem_recorrencia: false
s_ticket: 3
s_lucro: 7
s_replica: 9
s_saturacao: 3
status: esfriando
visto_primeiro: 2026-08-20
visto_ultimo: 2026-08-20
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/biblioteca-do-concurseiro"
gateways_detectados: [hotmart, lowify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [hotmart, lowify]
ra_primeira_reclamacao: 2026-04-11
ra_checado: 2026-08-20
veredito: observar
prioridade: 2
tags: [oferta, lowticket, concursos]
---

# Biblioteca do Concurseiro

Descoberta pelo caminho que o `Pipeline.md` previu: a lista de reclamações da Lowify como
**fonte de descoberta**, não só de validação. Uma reclamação de dois dias atrás citava o
nome do produto; o nome levou a uma página própria no Reclame Aqui.

## Ângulo
Acervo curado de apostilas, resumos, mapas mentais, simulados e questões para concursos,
militares, ENEM e vestibular, organizado por concurso, banca e disciplina. A promessa é
**economia de tempo de garimpo**, não conteúdo exclusivo: "evitando que o aluno perca
tempo procurando conteúdo na internet".

## Funil
anúncio → página → checkout → link de site → link de Google Drive.

Produtor na Hotmart: **WAU Digital LTDA**, produto `G104367321C`. Também aparece na
Lowify, o que indica operação em mais de um gateway ao mesmo tempo.

## Sinal de volume
Cinco reclamações no total: quatro na página própria, uma na lista da Lowify. O número
absoluto é baixo, mas **a distribuição é o que importa** — 11/04, 25/04, 15/05, 01/07 e
18/08. Reclamação em cinco meses distintos não é pico de lançamento, é venda contínua.
Está no Reclame Aqui há 4 meses, com 0% de resposta.

## Rotação de domínio
O mesmo padrão de [[kit-300-aulas-edfisica]], em outro nicho:

| Domínio | Estado |
|---|---|
| `bibliotecadoconcurseiro.site` | contato oficial no Reclame Aqui |
| `acesso.bibliotecadoconcurseiro.com` | área de acesso |
| `aluno-concurseiro.netlify.app` | **vazia na leitura de hoje** — página queimada ou em troca |

Duas ofertas independentes com a mesma arquitetura reforça a hipótese do Painel: contar
deploys distintos da mesma oferta merece virar métrica própria do radar.

## O que copiar / o que evitar

**Copiar:** o eixo de organização. O valor declarado não é o PDF — é a curadoria por
banca. Isso é replicável com material que já circula de graça.

**Evitar:** entrega por link de Google Drive. Três das cinco reclamações são exatamente
isso — link que não abre, conteúdo que não está lá. É onde a operação está sangrando, e
é barato de resolver com área de membros de verdade.

**Cuidado de direito autoral:** "materiais curados" em concursos costuma significar
apostila de terceiro redistribuída. Modelar a estrutura, não o acervo.

## Estado dos dados
- **Confirmado:** existência, produtor, dois gateways, histórico de reclamações datado.
- **Provisório:** `ticket_medio_est` 27 é estimativa de categoria. A página de marketplace
  da Hotmart não expõe preço e a landing não abriu. `s_ticket` cai junto se estiver errado.
- **Faltando:** preço real, tempo no ar, criativos, bump e upsell.

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
