---
tipo: oferta
classe: oferta
slug: cursos-gratis-online
nome: "Cursos Gratis Online"
nicho: certificacao
sub_nicho: taxa-para-liberar-certificado
idioma: pt-BR
pais: BR
plataforma_ads: [meta, google]
checkout: desconhecido
url_pagina: "http://cursosgratisonline.com.br"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=cursos%20gratis%20online%20certificado&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 79.9
ticket_bump: 0
ticket_upsell: 99
ticket_medio_est: 90
margem_est: 0.9
modelo: [direct]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 7
s_lucro: 7
s_replica: 5
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-30
visto_ultimo: 2026-08-30
rodadas_vista: 1
dias_no_ar: 210
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/cursos-gratis-online"
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 114
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-30
veredito: observar
prioridade: 2
tags: [oferta, lowticket, certificacao]
---

# Cursos Gratis Online

Estava na fila do [[angulo-taxa-do-certificado]] como *"nao medido"* desde ontem. Medida hoje:
**114 reclamacoes ativas, 9 na janela de seis meses**, mais recente ha tres meses.

## Os numeros

| Medida | Valor |
|---|---|
| **M** — ativas | 114 |
| **N** — janela 01/02–31/07 | 9 (~1,5/mes) |
| Mais recente | ha ~3 meses |
| Reputacao | Sem reputacao definida (so 2 avaliadas) |
| Resposta | **100%**, media de **1 dia e 11 horas** |

`M − N = 105` contra taxa de 1,5/mes: a esmagadora maioria e anterior a janela. Operacao
**antiga e viva, mas desacelerando** — mesma assinatura da [[alfabetinho]]. Pelo criterio que
abri hoje no `Pipeline.md`, `dias_no_ar >= 210` (piso conservador).

## Ticket — o segundo capturado no angulo

Dois valores lidos em corpo, o que torna esta a nota mais bem instrumentada do nicho:

- **R$ 79,90** pelo certificado de um curso de extensao (auxiliar fiscal; tambem ABA),
  pago **via Pix**
- **R$ 99,00 por um combo de 5 certificados** — e o combo gerou reclamacao propria: o
  comprador entendeu que escolheria os cinco cursos e a empresa e que escolhia quatro deles

O combo e o achado comercial. Ele transforma um ticket de R$ 79,90 em R$ 99 e, de quebra,
**resolve o problema de catalogo**: cursos que ninguem escolheria sozinho saem empacotados. E
o mesmo movimento de pilha de bonus que o [[soulmate-sketcher]] usa em nicho totalmente
diferente.

Junto com os R$ 139,90 do [[certificado-curso-online]], o angulo agora tem faixa medida:
**R$ 80 a R$ 140**.

## Esta e a variante limpa da mecanica

O contraste com a [[certifica-brasil]] e o que essa nota adiciona ao vault:

| | [[certifica-brasil]] | Cursos Gratis Online |
|---|---|---|
| Resposta a reclamacao | **0%** | **100%**, 1d11h |
| Reclamacoes resolvidas | nenhuma | resolve, com nota 10 |
| Entrega | prova + PDF, nao chega | curso real + certificado, chega |
| Parceiro emissor | nenhum citado | **Fasul** (faculdade) |
| Cadencia | 3 dias | 3 meses |

A operacao que **entrega** tem um vigesimo da velocidade da que **nao entrega**. Isso e o
padrao mais desconfortavel que o vault ja mediu, e vale registrar sem suavizar: neste angulo,
a friccao de fazer certo (curso real, emissor real, atendimento real) custa volume.

O que **nao** se conclui dai e que a replica limpa nao funciona — se conclui que ela e um
negocio de margem menor e ritmo menor. `veredito: observar`.

## Score 5,80

`s_lucro: 7` (antiga e provada, sem aceleracao — nada nos ultimos tres meses).
`s_ticket: 7` (medio estimado ~R$ 90, dentro da faixa 60-120).
`s_replica: 5`, herdado do angulo: a promessa de validade do certificado encosta em area
regulada mesmo na variante limpa.
`s_saturacao: 3`.

Pagina do produtor: https://www.reclameaqui.com.br/empresa/cursos-online-gratis/lista-reclamacoes/

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
