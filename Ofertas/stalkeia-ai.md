---
tipo: oferta
slug: stalkeia-ai
nome: "Stalkeia.ai"
nicho: espionagem-rastreamento
sub_nicho: espionar-redes-sociais
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 37
ticket_bump: 19
ticket_upsell: 0
ticket_medio_est: 60
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 8
s_replica: 4
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/stalkeia-ai"
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 1
tags: [oferta, lowticket, marca]
---

# Stalkeia.ai

## Angulo
App que promete ver conversa/perfil fechado de terceiros. Grafias na mesma familia: Stalkeia.ai, Stalkeia.com, Stalker. Produtora citada: Disrupty Tecnologia.

## Funil
anuncio -> promessa de 'teste gratuito' -> coleta de dados -> primeiro pagamento R$29,90-37 -> segunda cobranca de R$19,90 em creditos para 'liberar o resultado'.

## Por que funciona
A mecanica de credito e o produto: o primeiro pagamento nao entrega nada, so habilita a proxima cobranca. E o que sustenta CPA alto no front.

## O que copiar / o que evitar
Copiar: a estrutura de creditos escalonados. Evitar: o nicho inteiro - espionagem de terceiros e o que mais gera reembolso forcado e derrubada de conta de anuncio.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (5 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-solicitacao-de-reembolso-por-aplicativo-de-espionagem-falso_zoL2pFAm1VieYFOp/

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
