---
tipo: oferta
classe: oferta
slug: fornece-up
nome: "Fornece Up"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=forneceup&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 12
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 12
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 2
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-31
rodadas_vista: 10
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/fornece-up"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 30
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-31
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Fornece Up

## Angulo
Plataforma de fornecedores por assinatura parcelada em 12x (261367699). 8 reclamacoes na PerfectPay em 08-11/10, quase todas com o mesmo texto 'nao consigo cancelar a compra da ForneceUp' (261316209, 261316083, 261280965, 261236057, 261183451, 261168583, 261121611): cancelamento travado e o que move o volume.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 8 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (8 IDs de 261121611 a 261367699)

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

## Rodada 2026-10-12

1 mencao(oes) nesta varredura (gateway PerfectPay). Plataforma de fornecedores por assinatura parcelada (ja mapeada como estreia na rodada anterior, 8 mencoes). Nova reclamacao no mesmo padrao: cancelamento/reembolso dentro do prazo de 7 dias, produtor sem resposta. Continua ativa poucas horas depois da ultima passada.

Evidencia: https://www.reclameaqui.com.br/perfectpay/quero-cancelar-minha-compra-e-ser-reembolsado-em-r-31554_liRRdrRGZL9uTLus/

## Rodada 2026-10-13

2 mencao(oes) nesta varredura (gateway PerfectPay). Assinatura de acesso a fornecedores/revenda, recorrente desde 25/09 e marcada quente na rodada anterior (debutou 11/10 com 8 IDs). Hoje mais 2 pedidos de estorno (um deles via Pix). Uma reclamação cita taxas de R$97-250 cobradas pra liberar um saldo de R$17.658 -- mecânica de order bump/upsell pesada pra travar saque.

Evidencia: https://www.reclameaqui.com.br/perfectpay/nao-recebi-o-estorno-da-fornece-up-apos-cancelamento-em-7-dias_nK2G6qUC6C7nWEIi/

## Rodada 2026-10-14

15 mencao(oes) nesta varredura (gateway PerfectPay). 7 reclamacoes com ID novo, todas de cancelamento/estorno travado: 261541275, 261533037, 261507661, 261502437, 261471517, 261467633 (R$ 175), 261389195 (R$ 315,54). Biblioteca, busca 'forneceup': nenhum anuncio da operacao.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 261541275, 261533037, 261507661, 261502437, 261471517, 261467633, 261389195)

## Rodada 2026-10-19

21 mencao(oes) nesta varredura (gateway PerfectPay). 5 IDs novos na PerfectPay desde 14/10 17h38 (16 -> 21; a nota estava em 8 por regressao no merge de 18/10): 261966411, 261909311, 261895127, 261738361, 261702913.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/

## Rodada 2026-10-21

23 mencao(oes) nesta varredura (gateway PerfectPay). 2 IDs novos na PerfectPay (21 -> 23): 262167639 ('ForneceUP - Pro', compra 11/10, estorno nao feito) e 262141861 (produtor nao responde e-mail).

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/

## Rodada 2026-10-23

25 mencao(oes) nesta varredura (gateway PerfectPay). 2 IDs novos (23 -> 25): 262382111 (plano Premium sem reembolso) e 262300725 ('Forneceup - Vitalicio').

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 262382111, 262300725)

## Rodada 2026-10-26

27 mencao(oes) nesta varredura (gateway PerfectPay). 2 IDs novos (25 -> 27): 262530413 (comprado 21/10) e 262470121 ('teste por 7 dias' sem onde cancelar).

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 262530413, 262470121)

## Rodada 2026-10-29

28 mencao(oes) nesta varredura (gateway PerfectPay). 1 ID novo (27 -> 28) na PerfectPay: 262806429 (cancelamento pedido em 15/10; pagamento processado pela 'Applyfy').

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/

Complemento 21h26: 1 ID novo, 262943461 (29/10 18h01, 'centenas de influenciadores no TikTok fazendo lives'). Os 262641247 e 262722243 tambem estao na lista com carimbo de 29/10, mas os IDs sao de 26-27/10 (carimbo movido por resposta): nao contados.

Evidencia: https://www.reclameaqui.com.br/perfectpay/forneceup-e-propaganda-enganosa-quero-meu-dinheiro-de-volta_xqtXb5Q7E70ov2Xo/

## Rodada 2026-10-31

30 mencao(oes) nesta varredura (gateway PerfectPay). Rodada 31/10: 1 ID novo, 263068407 (31/10 10h57): comprado em 11/10 pela PerfectPay, produtos cadastrados na plataforma sem nenhuma venda; pede estorno no cartao.

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-forneceup-quero-meu-reembolso-por-desacordo-comercial_f32yTcf_wpnDr436/
