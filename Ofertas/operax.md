---
tipo: oferta
slug: operax
nome: "Operax"
nicho: renda-celular-cashback
sub_nicho: ia-de-avaliacao
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Operax&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 37
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 37
margem_est: 0.85
modelo: [direct]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 4
s_lucro: 5
s_replica: 3
s_saturacao: 3
status: esfriando
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/operax"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Operax

## Angulo
Anuncio no Instagram promete IA que paga por avaliar empresas (Amazon, Google). Entrega e curso de trader com exigencia de deposito.

## Funil
anuncio Instagram -> checkout Kirvano R$37 -> entrega de curso de trading -> pedido de deposito.

## Por que funciona
Isca de 'IA que avalia produtos' com entrega de trading e um bait-and-switch documentado. Interessa como leitura de angulo de captacao, nao como produto.

## O que copiar / o que evitar
Copiar: o angulo de entrada 'IA paga voce para avaliar' esta convertendo. Evitar: a troca de produto na entrega.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/cobranca-indevida-e-propaganda-enganosa-de-ia-de-avaliacao_X7EEuRn9MgpGmt_t/

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

## Rodada 2026-08-21 — página de vendas não localizada

Busca web dedicada não encontrou LP ativa de **Operax**. Ou a oferta já rotacionou de
domínio, ou o nome do criativo difere do nome que o comprador registrou na reclamação.
`url_ads` preenchido com o termo de busca para tentar pela Biblioteca de Anúncios.

