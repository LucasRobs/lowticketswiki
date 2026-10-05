---
tipo: oferta
classe: oferta
slug: achados-da-ellen
nome: "Achados da Ellen"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kiwify
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Achados%20da%20Ellen&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 67
ticket_bump: 0
ticket_upsell: 49.9
ticket_medio_est: 117
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: true
s_ticket: 8
s_lucro: 6
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-02
visto_ultimo: 2026-10-02
rodadas_vista: 1
dias_no_ar: 62
criativos_ultima: 2
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/achados-da-ellen"
gateways_detectados: [kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [kiwify]
ra_primeira_reclamacao: 
ra_checado: 2026-10-02
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Achados da Ellen

## Angulo
Perfil de achadinhos (comenta 'eu quero' e recebe o link) que vende 'Treinamento da Ellen' (R$ 67, vendedor Lucas Caiafa) e o 'Grupo dos Achados da Ellen 3' por assinatura em Pix automatico (R$ 49,90). Duas reclamacoes em 01/10 (260601503, 260601331). Biblioteca: anuncio ativo desde 01/08, 2 anuncios no mesmo criativo.

## Funil
anuncio -> pagina -> checkout kiwify -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) na varredura de 2026-10-02 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/kiwify/exijo-reembolso-do-treinamento-da-ellen-comprado-em-1509_diz9w1dMxNow_wCb/

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

## Medicao 2026-10-02
- Biblioteca de Anuncios, busca "achados da ellen": ~3 resultados, anuncio ativo mais antigo iniciado em 01/08/2026 (62 dias), 2 anuncios usam o mesmo criativo. O anuncio vende o achadinho (organizador de roupa de bebe, "comenta eu quero"), nao o treinamento: a oferta de R$ 67 e o grupo de R$ 49,90/mes ficam atras do perfil.
- `s_lucro: 6` e nao 7: 62 dias de anuncio, mas de um perfil de achadinhos com poucos criativos, nao da oferta em si.
