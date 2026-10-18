---
tipo: oferta
classe: oferta
slug: oblivium-digital-vendedor-produto-nao-identificado
nome: "Oblivium Digital (vendedor; produto nao identificado)"
nicho: a-identificar
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Oblivium%20Digital&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 4
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 4
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 2
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-10-08
visto_ultimo: 2026-10-17
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/oblivium-digital-vendedor-produto-nao-identificado"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-17
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Oblivium Digital (vendedor; produto nao identificado)

## Angulo
Achado novo, mencao unica. Nome do vendedor/produtor aparece explicito no titulo da reclamacao ('Oblivium Digital'), mas o comprador nao diz o que comprou -- so que nao recebeu o produto, pediu cancelamento e o vendedor parou de responder enquanto as parcelas (4x no cartao) continuam sendo cobradas.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-08 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/payt/compra-pedido-de-cancelamento-nao-respondido-por-vendedor-oblivium-digital-exijo-o-estorno-do-cartao_kc0x3hE-i7qw7H14/

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

1 mencao(oes) nesta varredura (gateway Payt). Vendedor ja catalogado no radar, produto fisico (segundo resposta da Payt) ainda sem nome identificado na reclamacao. Comprador parcelou em 4x e nao teve resposta ao pedido de cancelamento.

Evidencia: https://www.reclameaqui.com.br/payt/compra-pedido-de-cancelamento-nao-respondido-por-vendedor-oblivium-digital-exijo-o-estorno-do-cartao_kc0x3hE-i7qw7H14/

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway Payt). Mesma reclamacao de 07/10 ainda na pagina 1 da Payt -- produto nao identificado, pagamento em 4x. Zero novidade genuina (mesmo problema de volume baixo + bug de paginacao do ZapRadar acima), mas confirma vendedor sustentado ha semanas.

Evidencia: https://www.reclameaqui.com.br/payt/compra-pedido-de-cancelamento-nao-respondido-por-vendedor-oblivium-digital-exijo-o-estorno-do-cartao_kc0x3hE-i7qw7H14/

## Rodada 2026-10-17

1 mencao(oes) nesta varredura (gateway Payt). Vendedor ja catalogado desde 08/10 (3 rodadas vistas), produto ainda nao identificado nos relatos. Reconfirmado via Payt em reclamacao de cancelamento nao respondido (publicada 07/10, capturada agora) -- aparicao em dia distinto (17/10 vs ultimo visto 15/10).

Evidencia: https://www.reclameaqui.com.br/payt/compra-pedido-de-cancelamento-nao-respondido-por-vendedor-oblivium-digital-exijo-o-estorno-do-cartao_kc0x3hE-i7qw7H14/
