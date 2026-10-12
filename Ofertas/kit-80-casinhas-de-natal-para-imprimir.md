---
tipo: oferta
classe: oferta
slug: kit-80-casinhas-de-natal-para-imprimir
nome: "Kit +80 Casinhas de Natal para Imprimir"
nicho: artesanato
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=casinhas%20de%20natal&search_type=keyword_unordered&media_type=all"
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
s_lucro: 3
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-05
visto_ultimo: 2026-10-05
rodadas_vista: 1
dias_no_ar: 12
criativos_ultima: 2
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/kit-80-casinhas-de-natal-para-imprimir"
gateways_detectados: [wiapy]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [wiapy]
ra_primeira_reclamacao: 
ra_checado: 2026-10-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Kit +80 Casinhas de Natal para Imprimir

## Angulo
Kit digital de +80 casinhas de Natal para imprimir, recortar e montar. Na Biblioteca, o anunciante Denis Sah esta no ar desde 23/09 com 2 anuncios. A reclamacao 260786429 (04/10) diz que o arquivo chega mas faltam instrucoes e partes. Produto sazonal do cluster de papel/imprimivel.

## Funil
anuncio -> pagina -> checkout wiapy -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-05 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/wiapy/lista-reclamacoes/ (ID 260786429)

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

## Medicao 2026-10-05 (Biblioteca de Anuncios)

A busca "casinhas de natal" devolve ~110 resultados, quase todos de decoracao fisica e tecido. O infoproduto aparece em **Denis Sah**: 2 anuncios com o mesmo criativo, no ar desde **23/09** (12 dias). O texto diz "+80 modelos, arquivos prontos para imprimir, 100% digital". `s_lucro: 3` corresponde a faixa de 7-20 dias com poucos criativos. Ha um irmao provavel na Ateliê Lulu Arts (`site.acmprodutosdigitais.com`, desde 21/09), que nao foi aberto. Encosta no cluster de papel/imprimivel ([[kit-mundinho-de-papel]], [[bonecas-papel-maria-criativa]]). E a versao sazonal desse cluster, com prazo de validade ate dezembro.
