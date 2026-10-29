---
tipo: oferta
classe: oferta
slug: tokscale-ia
nome: "TokScale IA"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=tokscale&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 0
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-29
rodadas_vista: 9
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/tokscale-ia"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 34
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# TokScale IA

## Angulo
Plataforma de videos com IA para TikTok Shop, vendida como assinatura (261202955, contratada em 25/09). 6 reclamacoes na Payt em 08-11/10 (261367965, 261093565, 261202955, 261154757, 261154719, 261118633), todas de reembolso sem resposta. Mesmo cluster do ShopMiner: ferramenta de video de produto para quem vende em marketplace.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 6 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (6 IDs)

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

## Rodada 2026-10-14

8 mencao(oes) nesta varredura (gateway Payt). 2 reclamacoes com ID novo, ambas de reembolso prometido e nao pago: 261490049 (compra em 05/10) e 261435023.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261490049, 261435023)

## Rodada 2026-10-19

15 mencao(oes) nesta varredura (gateway Payt). 7 IDs novos na Payt desde 14/10 17h38 (8 -> 15), 5 deles em 15/10: 261998569, 261795969, 261769737, 261742929, 261704329, 261691071, 261680751.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-20

19 mencao(oes) nesta varredura (gateway Payt). 4 IDs novos na Payt (15 -> 19): 262075729 (comprado em 14/10), 262039609, 262026209 (comprado em 14/10), 262022817 ('plataforma de criar videos e imagens de IA'). Tres das quatro citam compra de 14/10, a mesma semana das cinco de 15/10 lidas ontem.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-21

20 mencao(oes) nesta varredura (gateway Payt). 1 ID novo na Payt (19 -> 20): 262153937 (fatura em nome de 'paytcc'). Fora da conta: 261887749 ('Quero reembolso da Tok Scale'), ID antigo com carimbo de 20/10 — carimbo movido.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-23

23 mencao(oes) nesta varredura (gateway Payt). 3 IDs novos (20 -> 23): 262437537 (vendido por influenciador), 262345895, 262264385.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262437537, 262345895, 262264385)

## Rodada 2026-10-26

28 mencao(oes) nesta varredura (gateway Payt). 5 IDs novos (23 -> 28), todos na Payt: 262619207, 262600761, 262570047 (R$ 297 no cartao, 17/10), 262559217 ('divulgada pela influenciadora Fernanda', 25/10), 262476031. O vendedor manda cancelar em outro canal.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262619207 ... 262476031)

## Rodada 2026-10-27

33 mencao(oes) nesta varredura (gateway Payt). 5 IDs novos em ~24h (28 -> 33), todos na Payt: 262695961, 262689375 (assinatura anual), 262674929 (comprou 20/10, pediu reembolso 22/10), 262656533 (reembolso ja autorizado e nao pago), 262636017 (anual R$ 297 no cartao, 19/10). O 262631047 (mesmo texto de R$ 297/19/10, 16h37 de 26/10) ficou fora por ter ID abaixo do maior lido na rodada anterior.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262695961 ... 262636017)

## Rodada 2026-10-29

34 mencao(oes) nesta varredura (gateway Payt). 1 ID novo (33 -> 34): 262869727. O 262738929 ficou fora: e o mesmo comprador do 262689375, ja contado em 27/10, reabrindo o caso.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/
