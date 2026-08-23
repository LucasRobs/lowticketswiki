---
tipo: oferta
slug: desafio-anamnese-plano-alimentar
nome: "Desafio de treino com loop de anamnese (nome nao capturado)"
nicho: saude-estetica-fitness
sub_nicho: desafio-com-funil-de-anamnese
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lastlink
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=desafio%20treino%20plano%20alimentar%20anamnese&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 100
ticket_medio_est: 150
margem_est: 0.8
modelo: [quiz]
formato_entrega: [planilha]
tem_recorrencia: false
s_ticket: 10
s_lucro: 4
s_replica: 3
s_saturacao: 5
status: nova
visto_primeiro: 2026-08-23
visto_ultimo: 2026-08-23
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/desafio-anamnese-plano-alimentar"
gateways_detectados: [lastlink]
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 1
ra_plataformas: [lastlink]
ra_primeira_reclamacao: 2026-08-22
ra_checado: 2026-08-23
veredito: observar
prioridade: 0
tags: [oferta, lowticket]
---

# Desafio de treino com loop de anamnese (nome nao capturado)

Descoberta na lista da Lastlink (22/08, 17h33). **A mecanica mais interessante da rodada, e nao tem nome.**

O comprador descreve o funil inteiro sem perceber que esta descrevendo um funil:

1. Compra um "desafio" achando que e planilha de treino. No checkout entram plano alimentar **e um outro produto** - order bump duplo, visivel.
2. Para receber, precisa preencher uma anamnese. A anamnese e uma **interface de falso chat sem opcao de recusar**.
3. Ao terminar, oferta de plano de R$ 200. Nao aceita.
4. Dias depois: "sua anamnese nao esta preenchida". Preenche de novo. Oferta de R$ 200 trimestral. Nao aceita. **Contra-oferta de R$ 100. Aceita.**
5. Dias depois, de novo: anamnese nao preenchida, nova oferta de plano alimentar - e sem comprar, a anamnese nao termina.

A anamnese nao e onboarding: e o mecanismo de downsell. Ela nunca "conclui" porque concluir e o que a oferta esta vendendo. O comprador pagou frente + dois bumps + R$ 100 e nao recebeu nada.

**Por que o score continua baixo mesmo com a mecanica sendo boa:** `s_replica: 3` - nicho de saude tem teto 4 no `Scoring.md`, e o funil depende de uma interface de chat com estado, nao de duas paginas. `s_ticket: 10` pela escada medida. `s_lucro: 4` porque nao ha idade da oferta, so a evidencia de que a escada funcionou pelo menos uma vez.

**O que falta:** o nome. Sem ele nao da para buscar na Biblioteca de Anuncios nem cruzar com outras reclamacoes. `slug` fica congelado; `nome` muda quando for capturado.
