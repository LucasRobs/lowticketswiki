---
tipo: oferta
classe: oferta
slug: velix
nome: "Velix"
nicho: ferramentas-ecommerce
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=velix&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 296
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 387.16
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 10
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-27
visto_ultimo: 2026-10-27
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/velix"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-27
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Velix

## Angulo
Ferramenta/assinatura que promete ajudar a vender produtos digitais e em marketplace (Mercado Livre/Shopee), vendida pelo TikTok de 'Julio Gabriel'. 3 IDs na PerfectPay: 262719823 (R$ 296, comprada 27/10 09h50, suporte e robo), 262615033 (R$ 478,32, 26/10) e 262601455 (estorno de assinatura nao pago); os dois ultimos estavam na fila de 26/10. Biblioteca: 'velix' devolve outros anunciantes (Velix-Core, laser Vellix), nenhum desta oferta.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-27 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/nao-recebi-ajuda-do-suporte-da-velix-e-solicito-reembolso_IIQUfbnvGhCSQyZN/

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
