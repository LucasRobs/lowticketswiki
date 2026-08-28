---
tipo: oferta
slug: cafe-premium-barista-academy
nome: "Cafe Premium — Barista Academy"
nicho: gastronomia-profissional
sub_nicho: barista-cafeteria
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Cafe%20Premium%20Barista%20Academy&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.85
modelo: [vsl]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 0
s_lucro: 4
s_replica: 7
s_saturacao: 8
status: ativa
visto_primeiro: 2026-08-24
visto_ultimo: 2026-08-27
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/cafe-premium-barista-academy"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 2026-08-22
ra_checado: 2026-08-27
veredito: observar
prioridade: 1
tags: [oferta, lowticket]
---

# Cafe Premium — Barista Academy

Kirvano, reclamacao de 22/08/2026 as 20h54 (ID 257141113). Guarulhos - SP.

**Nicho novo no vault, e o mais limpo que apareceu ate agora.** Cafe/barista nao tem regulacao, nao tem estigma, nao depende de rosto e nao aparece em nenhuma das 78 outras notas. `s_saturacao: 8`.

## O que o corpo entrega

Compra em **12/08/2026** — 12 dias de venda medidos, e a medida e da oferta, nao do anuncio. O comprador comprou **para presentear**, cancelou em menos de 24h sem sequer criar acesso, teve o reembolso aprovado por e-mail e 10 dias depois o valor ainda constava pendente no cartao.

Dois sinais laterais uteis:

- **Compra como presente** e um angulo de criativo que o vault ainda nao tinha visto. Muda o publico-alvo do anuncio: nao e quem quer aprender, e quem quer dar de presente. Datas comemorativas viram sazonalidade previsivel.
- **Reembolso aprovado mas nao liquidado** e problema de gateway, nao de produtor. Nao penaliza `s_lucro`.

## Score

`s_replica: 7` — curso digital, sem regulacao, sem figura publica citada, produzivel com equipamento domestico. `s_lucro: 4` — 12 dias medidos e uma unica reclamacao; ainda e pouco para dizer que escala. `s_ticket: 0` — o valor nao aparece no corpo; sentinela, nao avaliacao.

**Esta e a nota que chega mais perto do corte com o perfil certo.** Se a captura de ticket mostrar um medio de R$ 60+, o score passa de 4,7 para perto de 6,2 sem que nada mais mude. Vale prioridade na fila de captura.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/problemas-com-reembolso-apos-cancelamento_SY1AHl8f7g_2efjL/


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
