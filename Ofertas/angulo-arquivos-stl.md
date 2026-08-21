---
tipo: oferta
slug: angulo-arquivos-stl
nome: "Arquivos STL para impressao 3D"
nicho: artesanato-e-pdf
sub_nicho: impressao-3d
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=arquivos%20STL%20impressao%203D&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 30
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 30
margem_est: 0.85
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 4
s_lucro: 6
s_replica: 8
s_saturacao: 8
status: esfriando
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-arquivos-stl"
gateways_detectados: [wiapy]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 2
ra_plataformas: [wiapy]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: replicar
prioridade: 2
tags: [oferta, lowticket, angulo]
---

# Arquivos STL para impressao 3D

## Angulo
Pacotes de arquivos STL prontos para quem tem impressora 3D. Publico com equipamento comprado e sede de conteudo.

## Funil
anuncio -> pagina -> checkout Wiapy -> download dos arquivos.

## Por que funciona
Duas mencoes na amostra da Wiapy e nenhum player conhecido. Publico auto-qualificado (ja gastou em impressora), entrega e arquivo, saturacao baixa. s_saturacao 8.

## O que copiar / o que evitar
Copiar: a logica 'quem comprou o equipamento precisa de conteudo pra ele' vale para impressora 3D, plotter de recorte, maquina de bordar e Cricut. Evitar: arquivo com defeito - foi exatamente a reclamacao.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (2 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/wiapy/arquivos-stl-com-defeito-e-diferentes-do-anunciado_xdSqNJPFhMT7qKV7/

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
