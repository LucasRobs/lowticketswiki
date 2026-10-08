---
tipo: oferta
classe: oferta
slug: lumi-ai
nome: "Lumi.ai"
nicho: ferramentas-de-pagamento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=lumi%20ai&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 99.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 644.74
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-09-22
visto_ultimo: 2026-09-26
rodadas_vista: 5
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/lumi-ai"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-09-26
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Lumi.ai

## Angulo
Plataforma de pagamento eletrônico. Cliente contrata por R$ 1.189,57 (12x), percebe que não atende necessidades, cobra para cancelamento dentro do prazo.

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) na varredura de 2026-09-22 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/cobranca-indevida-apos-cancelamento-dentro-do-prazo-legal-de-arrependimento-na-plataforma__6V948YP9ErQzUms/

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

2 mencao(oes) nesta varredura (gateway Cakto Pay). Plataforma de pagamento eletrônico. Cliente contrata por R$ 1.189,57 (12x), percebe que não atende necessidades, cobra para cancelamento dentro do prazo.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/cobranca-indevida-apos-cancelamento-dentro-do-prazo-legal-de-arrependimento-na-plataforma__6V948YP9ErQzUms/

## Rodada 2026-09-23

1 mencao(oes) nesta varredura (gateway Cakto Pay). Cobrança recorrente após cancelamento. Cliente cancelou dentro de 7 dias mas continuou sendo cobrado.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/cobranca-indevida-apos-cancelamento-dentro-do-prazo-legal-de-arrependimento-na-plataforma__6V948YP9ErQzUms/

## Rodada 2026-09-24

1 mencao(oes) nesta varredura (gateway Cakto). Avistada 04h41 e 14h12. Mesma reclamacao de cobranca apos cancelamento (12x R$ 99,90).

Evidencia: [[2026-09-24 -- 0441]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-25

1 mencao(oes) nesta varredura (gateway Cakto). Mesma reclamacao: cancelou em 29/05 dentro do prazo, cobrancas ate 20/08, resolvido por chargeback.

Evidencia: [[2026-09-25 -- 1300]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-26

1 mencao(oes) nesta varredura (gateway Cakto). Mesma reclamacao antiga (20/08), relida nas passadas 06h00 e 17h00. Nenhuma reclamacao nova de Lumi.ai nesta semana.

Evidencia: [[2026-09-26 -- 0600]] (rodada agendada; sem URL individual de reclamacao)
