---
tipo: oferta
classe: oferta
slug: receitas-sem-pensar
nome: "Receitas Sem Pensar"
nicho: emagrecimento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=receitas%20sem%20pensar&search_type=keyword_unordered&media_type=all"
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
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-11
visto_ultimo: 2026-10-14
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/receitas-sem-pensar"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-14
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Receitas Sem Pensar

## Angulo
App de receitas da nutricionista Renata Brugnera. 3 reclamacoes na Payt em 10-11/10 (261356291, 261343035, 261315463); a 261343035 descreve o mecanismo: as receitas de marmita (Marmitas Pro) que motivaram a compra exigem pagamento extra dentro do app.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-11 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261356291, 261343035, 261315463)

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

5 mencao(oes) nesta varredura (gateway Payt). 2 reclamacoes com ID novo: 261529383 e 261454839 (assinatura; receitas diferentes do que e postado no Instagram).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 261529383, 261454839)
