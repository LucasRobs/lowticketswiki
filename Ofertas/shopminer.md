---
tipo: oferta
classe: oferta
slug: shopminer
nome: "ShopMiner"
nicho: ferramentas-ecommerce
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=ShopMiner&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 297
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 297
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 9
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-03
visto_ultimo: 2026-10-26
rodadas_vista: 8
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/shopminer"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 58
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-26
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# ShopMiner

## Angulo
Ferramenta de pesquisa de produtos pra loja online que não entrega as funcionalidades anunciadas na compra.

App que 'minera' produtos de e-commerce e gera imagens e videos deles, vendido em live com plano vitalicio de R$ 297 (261213933). 11 reclamacoes na Payt em 08-11/10 (261378247 a 261112515), quase todas 'nao gera videos / nao funciona'. Nao aparece na Biblioteca pelo nome: o canal e a live.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-03 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/payt/solicito-reembolso-pois-o-aplicativo-nao-cumpre-o-prometido_fPPuZWKCyL9FUzp3/

- **Confirmado:** existencia, 11 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261378247, 261371209, 261356113, 261303597, 261293905, 261248881, 261213933, 261148849, 261148545, 261134853, 261112515)

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

## Rodada 2026-10-05

1 mencao(oes) nesta varredura (gateway Payt). Ferramenta/app vendida via Payt, aplicativo nao cumpriu o prometido. Nome de produto incomum nesse gateway - Payt costuma ser overflow de operacoes que saem de outros gateways, vale checar se roda tambem em PerfectPay/Cakto.

Evidencia: https://www.reclameaqui.com.br/payt/solicito-reembolso-pois-o-aplicativo-nao-cumpre-o-prometido_fPPuZWKCyL9FUzp3/

## Rodada 2026-10-14

20 mencao(oes) nesta varredura (gateway Payt). 9 reclamacoes com ID novo na Payt: 261557535, 261517005, 261488385 (app so trava), 261426601, 261425543, 261417585 ('acesso vitalicio ao ShopMiner (Shop Flix)', comprado em 02/10), 261409511 (comprado durante live), 261404929, 261400543 (nao gera o conteudo prometido). Biblioteca, busca 'shopminer': zero anuncios — confirma que o canal de venda e a live.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261557535, 261517005, 261488385, 261426601, 261425543, 261417585, 261409511, 261404929, 261400543)

## Rodada 2026-10-19

31 mencao(oes) nesta varredura (gateway Payt). 10 IDs novos na Payt desde 14/10 17h38 (21 -> 31): 261985647, 261983013, 261956671, 261913993, 261907365, 261861193 ('ShopMine'), 261836405, 261756631, 261742137, 261664933. Biblioteca nao consultada nesta rodada (zero anuncio em 14/10: canal e live).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-20

33 mencao(oes) nesta varredura (gateway Payt). 2 IDs novos na Payt (31 -> 33): 262079945 ('Shopeminer', comprado em 15/10 por link) e 262067709 (contratado em 15/10 no cartao). Ritmo caiu de ~2/dia para 2 em 23h.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-21

35 mencao(oes) nesta varredura (gateway Payt). 2 IDs novos na Payt (33 -> 35): 262187991 (comprou em 20/10 no cartao, arrependimento) e 262125411 (produtos 'atualizados todos os dias' nao se atualizam).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-23

46 mencao(oes) nesta varredura (gateway Payt). 11 IDs novos entre 21/10 16h e 23/10 16h (35 -> 46): 262441225, 262439191, 262438373, 262419457 (comprado em live no TikTok), 262369743 (R$ 297 no Pix em 21/10), 262361165, 262339837, 262334469, 262311037 ('Short Shop Miner', comprado 22/10 09h45), 262310243, 262299849 (vendido por influenciadora). Quase todas: nao gera os videos prometidos e o estorno nao sai. Canal de venda continua sendo live e influenciador.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262441225 ... 262299849)

## Rodada 2026-10-26

58 mencao(oes) nesta varredura (gateway Payt). 12 IDs novos entre 23/10 16h e 26/10 16h50 (46 -> 58), todos na Payt: 262614303, 262596929 ('Shop Mimer'), 262590077, 262581891, 262578409 (R$ 297 Pix, compra 19/10), 262574281, 262562787 (comprado para vender como afiliada), 262500927, 262492807 (R$ 297 Pix), 262475877, 262474605, 262451265. Mesma queixa: o app de videos com IA nao entrega e o estorno nao sai; o vendedor manda pedir o reembolso na Payt (262614303).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262614303 ... 262451265)
