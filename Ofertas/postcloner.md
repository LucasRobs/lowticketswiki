---
tipo: oferta
classe: oferta
slug: postcloner
nome: "PostCloner"
nicho: social-media-marketing
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=PostCloner&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 59.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 59.9
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-09-27
visto_ultimo: 2026-11-06
rodadas_vista: 5
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/postcloner"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 10
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-11-06
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# PostCloner

## Angulo
Ferramenta de automação para redes sociais. Reclamação: reembolso solicitado dentro do prazo.

## Funil
anuncio -> pagina -> checkout cakto -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-09-27 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/solicito-reembolso-do-meu-pedido-postcloner-no-valor-de-r-5990_ouBeMGVURX7lnJfi/

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

## Rodada 2026-10-26

2 mencao(oes) nesta varredura (gateway Cakto). Retorno com 1 ID (1 -> 2): 262568217 (Cakto, sem conseguir pedir reembolso).

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/ (ID 262568217)

## Rodada 2026-10-29

3 mencao(oes) nesta varredura (gateway Cakto). 1 ID novo (2 -> 3) na Cakto: 262779983 (videos duplicados).

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/

## Rodada 2026-11-05

9 mencao(oes) nesta varredura (gateway Cakto). Rodada 05/11: 6 IDs novos (3 -> 9), todos na Cakto: 263110071, 263131651 (tres compras em 31/10), 263188195, 263278263, 263329193 ('Posh Clone'), 263390807 (automacao de redes que parou de funcionar e cobranca indevida). Triplicou em 5 dias.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/contratei-automacao-de-redes-sociais-e-parou-de-funcionar-alem-de-cobranca-indevida_t_tcB738kLDP5N5j/

## Rodada 2026-11-06

10 mencao(oes) nesta varredura (gateway Cakto). Rodada 06/11: 1 ID novo na Cakto, 9 -> 10. 263592245 (14h54): 'Posh Clone' (grafia ja atribuida em 05/11), produto incompleto desde o dia da compra, vendedor sem resposta ha 72h e a Cakto manda falar com o vendedor.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/nao-consigo-cancelar-a-compra-do-posh-clone-e-a-cakto-nao-me-reembolsa_xnBjNissrdmkmPri/
