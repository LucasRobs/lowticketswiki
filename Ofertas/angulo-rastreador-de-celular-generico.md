---
tipo: oferta
classe: angulo
slug: angulo-rastreador-de-celular-generico
nome: "Rastreador de celular (generico)"
nicho: espionagem-rastreamento
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=rastrear%20localizacao%20celular&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 3
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 44.35
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 6
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-04
visto_ultimo: 2026-10-04
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-rastreador-de-celular-generico"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-10-04
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# Rastreador de celular (generico)

## Angulo
Duas reclamações hoje sobre apps de rastreamento de celular que não entregam acesso, nenhuma com nome de marca. Uma delas mostra o padrão clássico de 3 cobranças crescentes (R$27,90 + R$19,90 + R$37,90) para 'liberar' o resultado - mesma mecânica da família Stalkeia, mas sem confirmação de que seja o mesmo produto.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 2 mencao(oes) na varredura de 2026-10-04 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fiz-varios-pagamentos-e-nao-recebi-o-servico-de-rastreamento_qSmcZT9snGfN4-CL/

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
