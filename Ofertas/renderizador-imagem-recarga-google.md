---
tipo: oferta
classe: oferta
slug: renderizador-imagem-recarga-google
nome: "Renderizador de imagem com recarga na Google (nome nao capturado)"
nicho: ferramentas-ia-design
sub_nicho: renderizador-wrapper-api
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kiwify
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=renderizador%20de%20imagem%20IA&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.95
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 3
s_replica: 9
s_saturacao: 6
status: esfriando
visto_primeiro: 2026-08-24
visto_ultimo: 2026-08-24
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/renderizador-imagem-recarga-google"
gateways_detectados: [kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kiwify]
ra_primeira_reclamacao: 2026-08-22
ra_checado: 2026-08-24
veredito: observar
prioridade: 1
tags: [oferta, lowticket]
---

# Renderizador de imagem com recarga na Google (nome nao capturado)

Kiwify, reclamacao de 22/08/2026 as 11h31 (ID 257114401). Fortaleza - CE.

**A mecanica e o achado, e ela e nova no vault: o custo de operacao foi transferido para o comprador depois da compra.**

O comprador diz, textualmente, que na compra "nao avisava que precisava fazer recargas no Google para poder usar o renderizador". Ou seja: o produto vendido e um **wrapper de API de imagem**. O que ele entrega e uma interface. O processamento roda na conta do proprio comprador, que precisa criar credencial na Google e por credito la — e isso so aparece depois do pagamento.

## Por que isso importa

Ate hoje o vault vinha catalogando duas formas do degrau invisivel:

1. **Upsell escondido** — cobrar de novo o que o comprador nao viu ([[lowzap]], [[love-pix]], [[stalkeia-ai]]).
2. **Downsell forcado** — cobrar o que o comprador ja recusou ([[desafio-anamnese-plano-alimentar]]).

Esta e uma terceira: **nao cobrar mais nada e ainda assim nao pagar nada.** O vendedor nao tem custo de inferencia, nao tem custo de servidor, nao tem custo de suporte tecnico — a infraestrutura e da vitima. `margem_est: 0.95` nao e otimismo, e o modelo.

## O que copiar / o que evitar

**Copiar:** a arquitetura. Um wrapper de API onde a chave e do comprador tem margem quase perfeita e escala sem custo marginal. `s_replica: 9` — funil de duas paginas, entrega digital trivial, criativo de antes/depois de render e generico e abundante.

**Evitar:** omitir a recarga na pagina de vendas. E exatamente essa omissao que gera a reclamacao, o reembolso e, em volume, a derrubada da conta de anuncio. A versao honesta do mesmo produto — "voce usa sua propria chave, veja aqui como criar" — mantem a margem e mata o passivo.

## Estado dos dados

- **Confirmado:** existencia, gateway (kiwify), a mecanica de recarga, data da reclamacao.
- **Faltando:** nome comercial, valor pago, pagina de vendas, dias no ar, criativos. `s_ticket: 0` e sentinela, nao avaliacao — a nota nao deve ser comparada no Ranking ate a captura.

Evidencia: https://www.reclameaqui.com.br/kiwify/solicitacao-de-cancelamento-e-estorno-de-renderizador-de-imagem-com-propaganda-enganosa_hbtJFlNyD_C0teyQ/


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
