---
tipo: oferta
classe: angulo
slug: angulo-pendrive-anunciado-entrega-so-acesso-online
nome: "angulo pendrive anunciado entrega so acesso online"
nicho: a-identificar
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=curso%20pendrive&search_type=keyword_unordered&media_type=all"
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
visto_primeiro: 2026-10-16
visto_ultimo: 2026-10-18
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-pendrive-anunciado-entrega-so-acesso-online"
gateways_detectados: [hotmart, perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 4
ra_plataformas: [hotmart, perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-18
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# angulo pendrive anunciado entrega so acesso online

## Angulo
Angulo de propaganda enganosa classico: anuncio promete pen-drive fisico com o conteudo, comprador recebe so acesso online. Produto e produtor nao identificados nesta reclamacao, mas o mecanismo (bait-and-switch fisico->digital) e recorrente em varios nichos de infoproduto e vale monitorar.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-16 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/fui-enganado-com-propaganda-de-pen-drive-e-recebi-apenas-acesso-online_q7WBMk5ZvwKDD5Ay/

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

## Rodada 2026-10-17

1 mencao(oes) nesta varredura (gateway Hotmart). Mecanismo classico de propaganda enganosa (pendrive fisico anunciado, so acesso online entregue). Mesma reclamacao de 16/10, agora confirmada em segundo dia diferente -- sobe de fria para morna.

Evidencia: https://www.reclameaqui.com.br/hotmart/fui-enganado-com-propaganda-de-pen-drive-e-recebi-apenas-acesso-online_q7WBMk5ZvwKDD5Ay/

## Rodada 2026-10-18

4 mencao(oes) nesta varredura (gateway PerfectPay). Mesmo mecanismo de bait-and-switch fisico->digital ja catalogado (3 ocorrencias na Hotmart), agora com evidencia nova em outro gateway (PerfectPay): compradora diz ter comprado pensando ser produto fisico e descoberto depois que era curso. Confirma que o angulo nao e exclusivo de um gateway. 4a ocorrencia, sobe para quente.

Evidencia: https://www.reclameaqui.com.br/perfectpay/quero-reembolso-de-curso-que-comprei-pensando-ser-produto-fisico_3dLpxOdBfBZHiROG/
