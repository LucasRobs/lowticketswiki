---
tipo: oferta
slug: angulo-streaming-doramas-turcas
nome: "Novelas turcas, doramas e mini dramas"
nicho: streaming-e-acesso
sub_nicho: catalogo-novelas
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lowify
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=novelas%20turcas%20dubladas&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 10
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 20
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: true
s_ticket: 3
s_lucro: 8
s_replica: 3
s_saturacao: 6
status: esfriando
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-20
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-streaming-doramas-turcas"
gateways_detectados: [lowify, cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 8
ra_plataformas: [lowify, cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-08-20
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# Novelas turcas, doramas e mini dramas

## Angulo
Acesso vitalicio a catalogo de novelas turcas, doramas, mini dramas e desenhos classicos. Ticket de R$10 a R$20.

## Funil
anuncio -> pagina -> Pix -> link/login para o catalogo.

## Por que funciona
Seis mencoes em dois gateways (Lowify e Cakto). Volume alto e ticket baixissimo - e o nicho de streaming que a taxonomia marca como pouco explorado por infoprodutor.

## O que copiar / o que evitar
Nao replicar como esta: o catalogo e conteudo de terceiros. O que vale e a leitura de demanda - o publico de novela turca compra por impulso a R$10 e nao pede reembolso por preco, so por acesso.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (6 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/cakto-pay/pagamento-efetuado-mas-sem-acesso-as-novelas-e-series-turcas_L1Hr6fNcsbhS8Sxe/

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

## Rodada 2026-08-20 — recorrência confirmada

Duas reclamações novas na lista da Lowify, ambas de um dia atrás. Uma delas nomeia os
planos com precisão:

> "assinatura Dorama VIP vitalícia" e "de 1 mês"

A oferta tem **trilho de assinatura mensal** além do vitalício — `tem_recorrencia`
corrigido para `true`. Pela rubrica de `s_ticket`, recorrência puxaria a nota para 9-10;
não aplico o ajuste porque o valor da mensalidade não foi citado e a mecânica aqui é
tipicamente de R$10 a R$20. Registro a pendência em vez de inflar o score.

Oito menções em dois gateways é o segundo maior volume do vault, atrás só de
[[treino-trinca]]. O veredito segue `descartar`: o produto é catálogo de terceiro. O que
vale continua sendo a leitura de demanda.
