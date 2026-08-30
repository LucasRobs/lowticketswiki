---
tipo: oferta
classe: oferta
slug: alfabetinho
nome: "Alfabetinho — pacotes de atividades imprimiveis"
nicho: material-pedagogico
sub_nicho: alfabetizacao-e-educacao-especial
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: "https://www.alfabetinho.com.br/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=alfabetinho&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.85
modelo: [direct]
formato_entrega: [ebook, curso]
tem_recorrencia: false
s_ticket: 0
s_lucro: 7
s_replica: 7
s_saturacao: 4
status: ativa
visto_primeiro: 2026-08-29
visto_ultimo: 2026-08-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/alfabetinho"
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 177
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-29
veredito: observar
prioridade: 2
tags: [oferta, lowticket, material-pedagogico]
---

# Alfabetinho — pacotes de atividades imprimiveis

**177 reclamacoes ativas.** E o maior volume medido do vault — 4,5x a [[google-captcha-tw]], que ate ontem era o teto. E o operador nomeado por tras do [[angulo-material-pedagogico]], que estava no vault ha treze dias como padrao sem dono.

Nao veio de lista de gateway. Veio de **busca direta por pagina de produtor**, o que e o achado de metodo desta rodada: `reclameaqui.com.br/empresa/alfabetinho/lista-reclamacoes/`.

## O que a pagina entrega

| Campo | Valor |
|---|---|
| Reclamacoes ativas | **177** (36 paginas) |
| Recebidas em 01/02-31/07 | 24 |
| Reputacao | **Bom, 7,7/10** |
| Tempo de resposta | 11 horas |
| Resolvidas | 90% |
| Mais recente | ~2 meses atras |

## A leitura: volume sem aceleracao

As duas metades do numero dizem coisas opostas e as duas importam.

**177 ativas** e prova de operacao grande e de anos — nenhum produtor acumula isso vendendo pouco. O catalogo confirma: pacotes por disciplina e por ano ("pacote 2026 de ciencias"), "350 atividades para a educacao especial", "planejamentos anuais prontos", bonus com planos semanais e mensais, gabarito, area do aluno, promessa de acesso vitalicio. Isso e uma escada de produto, nao um ebook.

**24 na janela de seis meses, mais recente ha 2 meses** diz que o volume e historico. Compare com a [[google-captcha-tw]]: 22 na mesma janela mas 39 ativas, ou seja ~17 chegaram so em agosto. A Alfabetinho nao mostra esse degrau. `s_lucro: 7` — grande, provada, **nao esquentando agora**.

## Por que a reputacao Bom e informacao, nao ruido

Reputacao Bom, 11h de resposta, 90% resolvido: e o perfil oposto ao da `joyce-roberts` (Nao Recomendada, 0% respondida). Entrega de verdade e trata reembolso. Duas consequencias praticas: as reclamacoes sao sobre **expectativa** ("material de qualidade inferior ao que promete", "propaganda enganosa" com 58 ocorrencias), nao sobre nao-entrega; e o padrao de falha replicavel e o de sempre neste nicho — o criativo promete mais do que o PDF cumpre.

## O que copiar

O recorte de **educacao especial** e o mais interessante do catalogo: "350 atividades para a educacao especial" conecta este operador direto com [[kit-so-escola-autismo]], [[kit-so-escola-tdah]] e [[angulo-tea-kit-imprimivel]]. Um so publico — professora de sala regular com aluno de inclusao e sem material — comprando de tres angulos diferentes do vault.

O que **nao** copiar: o modelo de catalogo anual. Pacote "2026 de ciencias" obriga a refazer o produto todo ano e cria a divida de suporte (gabarito, bonus, area do aluno) que gera as 177. Um kit unico imprimivel nao tem esse passivo.

## Estado dos dados

- **Confirmado:** existencia, volume (177), reputacao, catalogo, cadencia de reclamacao.
- **Faltando:** ticket (nenhum corpo citou valor — `s_ticket: 0` e sentinela, ver `Pipeline.md` item 6), gateway de checkout, `ra_primeira_reclamacao`.
- **Bloqueio conhecido:** `ra_primeira_reclamacao` exigiria a pagina 36 da lista, e URL com `?pagina=` nao passa no filtro de proveniencia do fetch. Sem browser, **a Etapa 3b entrega `ra_reclamacoes` mas nao `dias_no_ar`.**

Pagina do produtor: https://www.reclameaqui.com.br/empresa/alfabetinho/lista-reclamacoes/

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
