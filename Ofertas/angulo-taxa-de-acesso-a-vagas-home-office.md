---
tipo: oferta
classe: angulo
slug: angulo-taxa-de-acesso-a-vagas-home-office
nome: "Taxa de acesso a vagas home office"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=vagas%20home%20office&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 37.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 38.9
margem_est: 0.8
modelo: [direct]
formato_entrega: []
tem_recorrencia: false
s_ticket: 6
s_lucro: 5
s_replica: 0
s_saturacao: 0
status: nova
visto_primeiro: 2026-11-05
visto_ultimo: 2026-11-05
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-taxa-de-acesso-a-vagas-home-office"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-11-05
veredito: observar
prioridade: 0
tags: [oferta, lowticket, angulo]
---

# Taxa de acesso a vagas home office

## Angulo
Angulo sem dono, 5 IDs na PerfectPay em 5 dias (263117123, 263126143, 263156513, 263285893, 263400811): paga-se uma 'taxa unica' de R$ 37,90-39,90 por acesso a vagas de trabalho remoto; depois do cadastro o saque exige novo pagamento, ou chega um 'cursinho' no lugar da vaga. Familia 'taxa para liberar'.

## Funil
anuncio -> pagina -> checkout (nao mapeado) -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 5 mencao(oes) na varredura de 2026-11-05 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fui-enganado-com-editado-pelo-reclame-aqui-vaga-de-emprego-e-quero-meu-dinheiro-de-volta_W1rvo9fJEqg6VCEk/

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
