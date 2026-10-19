---
tipo: oferta
classe: oferta
slug: anunciaie
nome: "Anunciaie"
nicho: marketing-digital-trafego
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Anunciaie&search_type=keyword_unordered&media_type=all"
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
visto_primeiro: 2026-10-14
visto_ultimo: 2026-10-19
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/anunciaie"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 4
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-19
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Anunciaie

## Angulo
Nome novo nesta passada. Comprador pede reembolso e suporte nao responde; vendedor nao identificado na reclamacao. Parece produto/ferramenta ligada a anuncios/trafego pago, a confirmar.

## Funil
anuncio -> pagina -> checkout perfectpay -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-14 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/quero-reembolso-do-anunciaie-e-o-suporte-nao-responde_sS-zUGnDMziS12YO/

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

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway PerfectPay). Reembolso pedido sem resposta do suporte. Mesma reclamacao da passada anterior (21:46) ainda visivel -- 2o dia seguido aparecendo, promovido a quente por isso.

Evidencia: https://www.reclameaqui.com.br/perfectpay/quero-reembolso-do-anunciaie-e-o-suporte-nao-responde_sS-zUGnDMziS12YO/

## Rodada 2026-10-17

1 mencao(oes) nesta varredura (gateway PerfectPay). Curso sobre anúncios/tráfego, vendedor não identificado. Reclamação nomeia a grafia com acento 'Anunciaê'. Reaparece em 3o dia diferente (14/10, 15/10, agora 16-17/10) -- sobe pra quente.

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicito-devolucao-do-curso-da-anunciae-por-nao-atender-expectativas_jA77jZ0Mj7G2Gl1s/

## Rodada 2026-10-19

4 mencao(oes) nesta varredura (gateway PerfectPay). 2 IDs novos na PerfectPay (2 -> 4): 261882487 (plataforma Anunciae), 261864239 (curso da Anunciae).

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/
