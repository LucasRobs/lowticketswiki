---
tipo: oferta
classe: oferta
slug: app-start
nome: "App Start"
nicho: negocio-online
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=App%20Start&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-10-04
visto_ultimo: 2026-10-05
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/app-start"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [hotmart]
ra_primeira_reclamacao: 
ra_checado: 2026-10-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# App Start

## Angulo
Curso/app vendido como assinatura; cobrança anual não autorizada e sem opção funcional de cancelamento.

## Funil
anuncio -> pagina -> checkout hotmart -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-04 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/hotmart/fui-cobrado-indevidamente-pelo-curso-app-start-e-nao-consigo-cancelar_09P5M-oNHCyoBOmm/

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

## Rodada 2026-10-04

1 mencao(oes) nesta varredura (gateway Hotmart). Primeira aparicao, achado so pelo titulo. Curso cobrado indevidamente, reclamante nao consegue cancelar.

Evidencia: https://www.reclameaqui.com.br/hotmart/fui-cobrado-indevidamente-pelo-curso-app-start-e-nao-consigo-cancelar_09P5M-oNHCyoBOmm/

## Rodada 2026-10-05

3 mencao(oes) nesta varredura (gateway Hotmart). Tres reclamacoes diferentes nesta mesma passada sobre cobranca/renovacao automatica nao autorizada de cursos (App Start, Comunidade Pulsar, curso de Isabela Schonorr) - padrao recorrente de assinatura recorrente sem aviso claro no checkout.

Evidencia: https://www.reclameaqui.com.br/hotmart/fui-cobrado-indevidamente-pelo-curso-app-start-e-nao-consigo-cancelar_09P5M-oNHCyoBOmm/
