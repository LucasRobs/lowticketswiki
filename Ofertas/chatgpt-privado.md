---
tipo: oferta
classe: oferta
slug: chatgpt-privado
nome: "ChatGPT Privado"
nicho: ferramentas-ia
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=ChatGPT%20Privado&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 97
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 97
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 7
s_lucro: 2
s_replica: 2
s_saturacao: 2
status: ativa
visto_primeiro: 2026-09-27
visto_ultimo: 2026-10-02
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/chatgpt-privado"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-10-02
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# ChatGPT Privado

## Angulo
Revenda de acesso ao ChatGPT que exige criar e-mail novo todo mes para continuar usando. ID 260135435 (26/09).

## Funil
anuncio -> pagina -> checkout kirvano -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-09-27 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/lista-reclamacoes/ (ID 260135435)

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

## Rodada 2026-10-02

5 mencao(oes) nesta varredura (gateway Kirvano). Quatro reclamacoes novas em 01/10 que nomeiam o produto ou o vendedor Infinity Apps (260547439 'ChatGPT Infinity (privado) acesso anual', 260547549, 260552799 R$ 145,89, 260562241: 'anual' vira Pix automatico mensal). Mais duas provaveis nao contadas (260549007 R$ 97, 260539297 vendedor Gabriel de Jesus). Na Biblioteca, 'chatgpt plus anual' devolve ~120 anuncios, todos iniciados 27-30/09, varios anunciantes a R$ 21,90: coorte nova e lotada.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/lista-reclamacoes/ (ID 260547439)

## Medicao 2026-10-02
- Reclame Aqui (Kirvano), 01/10: 260547439 ("ChatGPT Infinity (privado) acesso anual"), 260547549, 260552799 (Infinity Apps, R$ 145,89), 260562241 (anual que vira Pix automatico mensal). Provaveis, nao contadas: 260549007 (R$ 97, 1 ano), 260539297 (vendedor Gabriel de Jesus, entrega ChatGPT Go).
- Biblioteca, busca "chatgpt plus anual": ~120 anuncios, os carregados todos iniciados entre 27 e 30/09, varios anunciantes (AgenciaDesign, Eu andrade, Daniela Gomes) a R$ 21,90. Coorte nova e lotada: `s_saturacao: 2`. Revenda de acesso a servico de terceiro: `s_replica: 2`.
