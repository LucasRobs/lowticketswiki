---
tipo: oferta
classe: oferta
slug: a-renda-da-fortuna
nome: "A Renda da Fortuna"
nicho: renda-celular-cashback-pix
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Renda%20da%20Fortuna&search_type=keyword_unordered&media_type=all"
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
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-08
visto_ultimo: 2026-10-15
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/a-renda-da-fortuna"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-15
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# A Renda da Fortuna

## Angulo
Achado novo, mencao unica. 'Pacote' vendido parcelado (comprador cita opcoes de 12x e 5x), nome do produto parcialmente censurado pelo Reclame Aqui. Reclamante pede estorno no cartao; nao descreve o que o pacote entrega. Angulo tipico de renda-extra/promessa de dinheiro, mas vendedor nao identificado -- vale confirmar pagina antes de priorizar.

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

Evidencia: https://www.reclameaqui.com.br/payt/quero-estorno-do-pacote-a-renda-da-fortuna-que-e-editado-pelo-reclame-aqui_1FU059K8Nun7mHif/

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

## Rodada 2026-10-10

1 mencao(oes) nesta varredura (gateway Payt). Pacote de 'renda extra', parcelado em 12x e 5x conforme reclamante. Vendedor nao identificado. Ja registrado no vault; reaparece em dia distinto.

Evidencia: https://www.reclameaqui.com.br/payt/quero-estorno-do-pacote-a-renda-da-fortuna-que-e-editado-pelo-reclame-aqui_1FU059K8Nun7mHif/

## Rodada 2026-10-14

1 mencao(oes) nesta varredura (gateway Payt). Pacote ja catalogado, continua sendo vendido via Payt. Reclamante pede estorno de duas parcelas ocultas, produtor nao identificado na reclamacao.

Evidencia: https://www.reclameaqui.com.br/payt/quero-estorno-do-pacote-a-renda-da-fortuna-que-e-editado-pelo-reclame-aqui_1FU059K8Nun7mHif/

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway Payt). Mesma reclamacao de 07/10 ainda na pagina 1 da Payt -- pacote pago em parcelas (12x e 5x, valores mascarados pelo Reclame Aqui). Zero novidade genuina, mas confirma oferta sustentada desde 08/10.

Evidencia: https://www.reclameaqui.com.br/payt/quero-estorno-do-pacote-a-renda-da-fortuna-que-e-editado-pelo-reclame-aqui_1FU059K8Nun7mHif/
