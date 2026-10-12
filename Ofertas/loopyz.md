---
tipo: oferta
classe: oferta
slug: loopyz
nome: "Loopyz"
nicho: lives-interativas
sub_nicho: ferramenta-live-tiktok
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: "https://loopyz.com.br/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Loopyz&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 97
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 150
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: true
s_ticket: 10
s_lucro: 5
s_replica: 4
s_saturacao: 8
status: ativa
visto_primeiro: 2026-08-16
visto_ultimo: 2026-10-10
rodadas_vista: 9
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/loopyz"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-10
veredito: observar
prioridade: 2
tags: [oferta, lowticket, marca]
---

# Loopyz

## Angulo
Ferramenta/overlay para live no TikTok. Reclamacao registrada as 11h de hoje - e trafego rodando agora.

## Funil
anuncio -> pagina -> checkout Cakto -> suporte via produtor, nao via plataforma.

## Por que funciona
O nicho de live interativa esta em expansao rapida e com poucos players. s_saturacao 8 e o mais alto da rodada entre as marcas.

## O que copiar / o que evitar
Copiar: o nicho, nao necessariamente o produto. Vale mapear os concorrentes na Biblioteca de Anuncios com 'live interativa tiktok'.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/cakto-pay/dificuldade-para-obter-reembolso-de-ferramenta-comprada-para-live-no-tiktok_8ByKgtxdl-o8n54i/

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

## Correção 2026-08-21 — é recorrência, não low ticket

Página localizada: **`loopyz.com.br`**, checkout Cakto. Preços visíveis:
**R$ 97/mês · R$ 197/trimestre · R$ 497 vitalício.**

A estimativa anterior de R$ 47 estava errada por uma categoria inteira. `s_ticket` sobe
de 5 para **10** (a rubrica dá 9-10 para qualquer valor com recorrência) e
`tem_recorrencia` vira `true`. Score: 5,15 → 6,15.

O que trava a nota continua sendo `s_replica: 4` — é software de live, não PDF.

## Rodada 2026-09-27

0 mencao(oes) nesta varredura (gateway Cakto Pay). Plataforma de educação. Reclamação RESOLVIDA: reembolso foi efetuado conforme resposta da Cakto.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-recebi-meu-reembolso-da-loopyz-e-o-produtor-me-removeu-do-grupo_7xTu0t7hJOtnBwjw/

## Rodada 2026-09-28

1 mencao(oes) nesta varredura (gateway Cakto Pay). Plataforma de educação online. Reclamação sobre cobrança recorrente após cancelamento. ATUALIZADA - já aparecia em 27/09.

Evidencia: 

## Rodada 2026-10-04

1 mencao(oes) nesta varredura (gateway Cakto). Ferramenta para lives interativas no TikTok. Reclamação de arrependimento (R$ 88,29) confirma que a oferta, já registrada no vault, segue ativa via Cakto.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/exerco-meu-direito-de-arrependimento-e-solicito-reembolso-do-loopyz_Z1Tp7RIznG2K2I6T/

## Rodada 2026-10-05

1 mencao(oes) nesta varredura (gateway Cakto). Ferramenta para lives interativas no TikTok. Já tracked no vault; reconfirmado nesta passada com valor R$88,29.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/exerco-meu-direito-de-arrependimento-e-solicito-reembolso-do-loopyz_Z1Tp7RIznG2K2I6T/

## Rodada 2026-10-06

1 mencao(oes) nesta varredura (gateway Cakto). Reconfirmado mais uma vez via Cakto - direito de arrependimento solicitado.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/exerco-meu-direito-de-arrependimento-e-solicito-reembolso-do-loopyz_Z1Tp7RIznG2K2I6T/

## Rodada 2026-10-09

1 mencao(oes) nesta varredura (gateway Cakto). Ferramenta de lives interativas no TikTok, ja confirmada no vault (slug loopyz) com reconfirmacoes em varios dias desde 09/2026. Esta e uma evidencia_url nova (reclamacao de cancelamento/reembolso datada de 12/08/2026, pagina profunda do gateway), nao a mesma ja registrada - soma ao historico sustentado da oferta.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/solicitacao-formal-de-cancelamento-e-reembolso-do-produto-loopyz-live_V0h6y6-kild6pbKr/

## Rodada 2026-10-10

1 mencao(oes) nesta varredura (gateway Cakto). Ferramenta de lives/engajamento, entrega via 'Cakto Members'. Vendedor mascarado no RA. Ja registrado no vault (slug loopyz); reaparece em dia distinto.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/solicitacao-formal-de-cancelamento-e-reembolso-do-produto-loopyz-live_V0h6y6-kild6pbKr/

## Rodada 2026-10-11

3 mencao(oes) nesta varredura (gateway Cakto). 2 reclamacoes com ID novo na Cakto (261213595 e 261161015, reembolso negado dentro do prazo). Primeira mencao desde 21/08.

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/ (IDs 261213595, 261161015)
