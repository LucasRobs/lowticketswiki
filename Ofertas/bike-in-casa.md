---
tipo: oferta
classe: oferta
slug: bike-in-casa
nome: "Bike in Casa"
nicho: saude-bemestar
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: ticto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Bike%20in%20Casa%20assinatura&search_type=keyword_unordered&media_type=all"
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
visto_primeiro: 2026-10-04
visto_ultimo: 2026-10-08
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/bike-in-casa"
gateways_detectados: [ticto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 4
ra_plataformas: [ticto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-08
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Bike in Casa

## Angulo
Primeira aparicao. Assinatura de treino/bike em casa, cancelamento solicitado sem retorno.

## Funil
anuncio -> pagina -> checkout ticto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-04 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/ticto/solicitacao-de-cancelamento-de-assinatura-e-reembolso-de-bike-in-casa_wagDYadhO7DBU-a2/

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

## Rodada 2026-10-06

2 mencao(oes) nesta varredura (gateway Ticto). Assinatura de bike indoor com periodo de teste de 30 dias. Duas reclamacoes em dias diferentes (04/10 e 05/10) pedindo cancelamento/reembolso, ambas dizendo que a plataforma nao oferece opcao de cancelar - mecanica de assinatura recorrente dificil de sair, sinal de order bump/retencao forcada.

Evidencia: https://www.reclameaqui.com.br/ticto/nao-consigo-cancelar-minha-assinatura-do-bike-in-casa-dentro-do-prazo-de-teste_uc_bma5xDzkUi_F2/

## Rodada 2026-10-07

2 mencao(oes) nesta varredura (gateway Ticto). Reaparece pela terceira varredura em dias diferentes (04/10, 06/10, 07/10). Duas reclamacoes nesta passada pedindo cancelamento/reembolso da assinatura de bike indoor dentro do periodo de teste; mecanica de assinatura recorrente dificil de cancelar continua o padrao ja visto.

Evidencia: https://www.reclameaqui.com.br/ticto/quero-cancelar-minha-compra-do-bike-in-casa-e-pedir-reembolso_lmbt8XwzPjBUpeSr/

## Rodada 2026-10-08

4 mencao(oes) nesta varredura (gateway Ticto). Assinatura de treino indoor com periodo de teste dificil de cancelar. 4ª rodada em dias diferentes (04/10, 06/10, 07/10, agora 08/10) -- mecanica de retencao forcada continua sem correcao.

Evidencia: https://www.reclameaqui.com.br/ticto/nao-consigo-cancelar-minha-assinatura-do-bike-in-casa-dentro-do-prazo-de-teste_uc_bma5xDzkUi_F2/
