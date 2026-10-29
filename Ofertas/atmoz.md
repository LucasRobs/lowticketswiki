---
tipo: oferta
classe: oferta
slug: atmoz
nome: "Atmoz"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=atmoz&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 297.99
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 647.5
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 10
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-29
visto_ultimo: 2026-10-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/atmoz"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-10-29
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Atmoz

## Angulo
Estreia, 3 IDs na Kirvano em ~24h, tres compradores diferentes: 262837843 (app Atmoz R$ 297,99 no Pix em 28/10; para usar, pedem 'investimento' de R$ 997), 262880843 (tres cobrancas no cartao em 28/10: R$ 366,30 + R$ 369,99 + R$ 858,30, 'o Sr Jhon da plataforma Atmoz'), 262908177 (escada ATMOZ -> ATMOZ PRO -> CARTEIRA JOHN, 'sem esse nao iria funcionar'). Biblioteca: ~110 anuncios ativos de um unico anunciante, 'John Atmoz Rodrigues', LP inteligenciajohn.com ('Aula Gratuita | JOHN'), o mais antigo carregado de 18/10 e 13 deles de 27-29/10. Funil de aula gratuita -> app -> 'carteira'.

## Funil
anuncio -> pagina -> checkout kirvano -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-29 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/quero-o-ressarcimento-do-meu-pagamento-via-pix-de-r29799-pelo-app-atmoz_L13cNF59br2DCVd3/

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
