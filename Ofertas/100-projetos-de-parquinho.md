---
tipo: oferta
classe: oferta
slug: 100-projetos-de-parquinho
nome: "+100 Projetos de Parquinho"
nicho: cursos-de-oficio
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=100%20projetos%20de%20parquinho&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 25.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 25.9
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 4
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-10-02
visto_ultimo: 2026-10-02
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/100-projetos-de-parquinho"
gateways_detectados: [wiapy]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [wiapy]
ra_primeira_reclamacao: 
ra_checado: 2026-10-02
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# +100 Projetos de Parquinho

## Angulo
Pacote de projetos de marcenaria infantil em PDF, R$ 25,90 no Pix (260567601, 01/10). Na Lowify aparece o mesmo formato: 'Modelos de Arquitetura Infantil + 100 projetos de carrinhos de madeira' (260207349, 28/09). PLR de marcenaria em gateways de ticket baixo.

## Funil
anuncio -> pagina -> checkout wiapy -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-02 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/wiapy/lista-reclamacoes/ (ID 260567601)

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
