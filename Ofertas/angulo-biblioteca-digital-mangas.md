---
tipo: oferta
classe: angulo
slug: angulo-biblioteca-digital-mangas
nome: "Biblioteca Digital (mangas)"
nicho: streaming-e-acesso
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=biblioteca%20digital%20mangas&search_type=keyword_unordered&media_type=all"
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
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: esfriando
visto_primeiro: 2026-10-17
visto_ultimo: 2026-10-26
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-biblioteca-digital-mangas"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 4
ra_plataformas: [cakto]
ra_primeira_reclamacao: 
ra_checado: 2026-10-26
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# Biblioteca Digital (mangas)

## Angulo
Produto digital vendido como catalogo/'Biblioteca Digital' de mangas; comprador diz que o conteudo nao veio no formato anunciado (MOBI/EPUB). Produtor/vendedor nao identificado no relato, so o nome do site e a Cakto como gateway.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-17 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/cakto-pay/comprei-mangas-que-nao-vieram-em-mobiepub-como-anunciado_3wvdlv2SHEprZOeh/

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

## Rodada 2026-10-20

3 mencao(oes) nesta varredura (gateway Cakto). 1 ID novo na Cakto: 262113587 (Biblioteca Digital, R$ 37,90 no Pix, para ler mangas e outras historias pela internet, acesso nao chegou). Soma com as 2 mencoes da fila de 19/10 (Cakto, IDs nao registrados): 3. Primeiro preco e primeiro gateway desta nota.

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/

## Rodada 2026-10-26

4 mencao(oes) nesta varredura (gateway Cakto). Retorno com 1 ID (3 -> 4): 262566211 (Cakto, 'pacote de HQs e mangas na biblioteca digital', reembolso sem resposta). Outro ID da Cakto (262472579, 'biblioteca digital tm') nao cita mangas e ficou fora.

Evidencia: https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/ (ID 262566211)
