---
tipo: oferta
slug: angulo-material-pedagogico
nome: "Material pedagogico e apostilas imprimiveis"
nicho: material-pedagogico
sub_nicho: alfabetizacao-e-planos-de-aula
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: wiapy
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=atividades%20imprimiveis%20professor&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 27
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 30
margem_est: 0.85
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 4
s_lucro: 8
s_replica: 9
s_saturacao: 5
status: morta
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-material-pedagogico"
gateways_detectados: [wiapy, kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 5
ra_plataformas: [wiapy, kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: observar
prioridade: 3
tags: [oferta, lowticket, angulo]
---

# Material pedagogico e apostilas imprimiveis

## Angulo
Kits de material didatico, alfabetizacao, apostilas e pacotes educativos. Nomes vistos na Kirvano: Horinha da Leitura, Aulinhas de Matematica.

## Funil
anuncio -> pagina -> checkout Wiapy/Kirvano -> entrega de PDF por link/email.

## Por que funciona
Cinco reclamacoes em duas plataformas diferentes (Wiapy e Kirvano) na mesma amostra. Multi-gateway e o sinal mais confiavel de que o nicho tem volume real, nao uma operacao unica. Confirma o nicho de [[kit-300-aulas-edfisica]].

## O que copiar / o que evitar
Copiar: o nicho ja esta validado por duas rodadas independentes. O padrao de falha e sempre entrega (link quebrado, arquivo incompleto) - quem entregar direito tem vantagem estrutural de reembolso baixo.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (5 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/wiapy/compra-de-material-de-alfabetizacao-nao-entregue-apos-pagamento-via-pix_52imFDU1Cf7zGdCq/

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
