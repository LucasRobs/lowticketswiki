---
tipo: oferta
slug: lottoapp
nome: "LottoApp / LotteApp PRO"
nicho: apostas-e-sinais
sub_nicho: loteria
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: 
moeda: BRL
ticket_frente: 197
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 197
margem_est: 0.85
modelo: [vsl]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 9
s_lucro: 6
s_replica: 4
s_saturacao: 6
status: nova
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/lottoapp"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 1
tags: [oferta, lowticket, marca]
---

# LottoApp / LotteApp PRO

## Angulo
App que promete numeros/oportunidades de loteria. Trafego vindo do YouTube, nao do Meta.

## Funil
anuncio YouTube -> pagina -> checkout Kirvano R$197,99 -> versao PRO.

## Por que funciona
Ticket de R$197,99 num app de loteria e o maior valor unitario visto na rodada. Se sustenta CPA nesse preco, a margem por comprador e alta.

## O que copiar / o que evitar
Copiar: o ticket. Vale checar na Biblioteca de Anuncios se o volume no YouTube justifica o preco. Evitar: promessa de resultado em jogo de azar.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (2 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/solicitacao-de-estorno-do-valor-pago-pelo-aplicativo-lottoapp_fXSACeAM35sNCqQm/

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
