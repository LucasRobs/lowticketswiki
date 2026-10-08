---
tipo: oferta
classe: oferta
slug: ms-green-premium
nome: "MS GREEN PREMIUM"
nicho: saude-estetica-fitness
sub_nicho: suplemento-emagrecimento
idioma: pt-BR
pais: BR
plataforma_ads: []
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=MS%20Green%20Premium&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [fisico]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 2
s_saturacao: 5
status: esfriando
visto_primeiro: 2026-09-22
visto_ultimo: 2026-09-26
rodadas_vista: 5
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/ms-green-premium"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-09-26
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# MS GREEN PREMIUM

## Angulo
Suplemento (provavel emagrecimento/saude), formato fisico — entrega logistica, nao digital.

## Funil
anuncio -> pagina -> compra -> reclamante alega propaganda enganosa, arrependimento.

## Por que funciona
Ainda nao avaliado — uma mencao apenas, sinal fraco.

## O que copiar / o que evitar
Produto fisico com logistica real: teto baixo de `s_replica` por padrao do vault (produto fisico penaliza replicabilidade). Nao e prioridade de clonagem.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout (PerfectPay), 1 mencao em amostra parcial (15 paginas) de 22/09.
- **Faltando:** quase tudo — sinal unico (`fria`), sem Etapa 1. Manter em observacao passiva.
- **Nota de metodo:** mesma limitacao de `boss-ia-trade` — captura via skill sincronizada, sem dedup por URL/ID.

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

## Rodada 2026-09-22

3 mencao(oes) nesta varredura (gateway PerfectPay). Produto de saúde/suplemento com propaganda enganosa. Não cumpre promessas. Mecânica: descrição agressiva, produto inútil.

Evidencia: https://www.reclameaqui.com.br/perfectpay/arrependimento-de-compra-do-produto-ms-green-premium-por-propaganda-enganosa_Lu8Q8rmMewVHD1IR/

## Rodada 2026-09-23

1 mencao(oes) nesta varredura (gateway PerfectPay). Propaganda enganosa, não cumpre o que promete.

Evidencia: https://www.reclameaqui.com.br/perfectpay/arrependimento-de-compra-do-produto-ms-green-premium-por-propaganda-enganosa_Lu8Q8rmMewVHD1IR/

## Rodada 2026-09-24

1 mencao(oes) nesta varredura (gateway PerfectPay). Avistada 04h41 e 14h12. Propaganda enganosa, vendedor inacessivel.

Evidencia: [[2026-09-24 -- 0441]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-25

1 mencao(oes) nesta varredura (gateway PerfectPay). Aparece com a variacao 'Master Betano 1.0' (previsoes de aposta) - pode ser mais de um produto sob o mesmo vendedor.

Evidencia: [[2026-09-25 -- 0600]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-26

1 mencao(oes) nesta varredura (gateway PerfectPay). Listada como ainda ativa na passada das 06h00.

Evidencia: [[2026-09-26 -- 0600]] (rodada agendada; sem URL individual de reclamacao)
