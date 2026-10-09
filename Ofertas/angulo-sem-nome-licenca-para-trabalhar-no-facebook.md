---
tipo: oferta
classe: angulo
slug: angulo-sem-nome-licenca-para-trabalhar-no-facebook
nome: "sem nome - licenca para trabalhar no Facebook"
nicho: emprego-e-renda-falsa
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=licenca%20para%20trabalhar%20pelo%20facebook&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 48
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 48
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-09
visto_ultimo: 2026-10-09
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-sem-nome-licenca-para-trabalhar-no-facebook"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-10-09
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# sem nome - licenca para trabalhar no Facebook

## Angulo
Golpe de 'licenca'/cadastro pago para supostamente trabalhar no Facebook (moderacao, gestao de paginas) sem acesso liberado depois do pagamento. Ticket de entrada baixo (R$48). Angulo distinto do golpe de 'ganhar dinheiro avaliando produtos' ja tracked no vault - aqui a vitima paga para comecar a trabalhar, nao para liberar saque.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-09 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fui-cobrado-por-licenca-para-trabalhar-no-facebook-e-nao-recebi-acesso_SjRnw3sciDBftCQg/

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
