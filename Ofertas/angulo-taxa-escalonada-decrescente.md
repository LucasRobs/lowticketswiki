---
tipo: oferta
slug: angulo-taxa-escalonada-decrescente
nome: "Escada de taxas decrescentes no pos-compra (nome nao capturado)"
nicho: mecanica-de-checkout
sub_nicho: taxa-para-liberar
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=curso%20taxa%20de%20libera%C3%A7%C3%A3o&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 27.9
ticket_bump: 12.9
ticket_upsell: 5.9
ticket_medio_est: 46.7
margem_est: 0.9
modelo: [direct]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 5
s_lucro: 3
s_replica: 8
s_saturacao: 7
status: ativa
visto_primeiro: 2026-08-27
visto_ultimo: 2026-08-29
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/angulo-taxa-escalonada-decrescente"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 2026-08-27
ra_checado: 2026-08-29
veredito: observar
prioridade: 2
tags: [oferta, lowticket]
---

# Escada de taxas decrescentes no pos-compra (nome nao capturado)

PerfectPay, ID 257581811, carimbo **27/08/2026 as 19h59**. Tiangua - CE. Produto nao nomeado — pelo adendo de 23/08 do `Pipeline.md`, a mecanica vale nota mesmo sem o nome.

## A mecanica
Tres cobrancas em sequencia, **decrescentes**:

| Degrau | Valor | Pretexto |
|---|---|---|
| 1 | R$ 27,90 | o curso |
| 2 | R$ 12,90 | "confirmacao" |
| 3 | R$ 5,90 | "liberacao" |

Total R$ 46,70. O comprador pagou os tres.

## Por que isso e diferente do que o vault ja tem
O vault ja cataloga tres formas do degrau invisivel: upsell escondido ([[lowzap]], [[love-pix]]), downsell forcado ([[desafio-anamnese-plano-alimentar]]) e custo transferido para a infra da vitima ([[renderizador-imagem-recarga-google]]). **Esta e a quarta: o degrau decrescente.**

A ordem e o produto. Cada cobranca e menor que a anterior, entao a resistencia cai a cada passo em vez de subir — o comprador que ja pos R$ 27,90 nao briga por R$ 5,90, e a soma quase dobra o ticket de frente. E o oposto do upsell classico, que pede mais depois de pedir muito.

## O que copiar / o que evitar
**Copiar:** a curva decrescente aplicada a entregas reais — bump de R$ 12,90 e complemento de R$ 5,90 sobre um produto que existe. `s_replica: 8`, e mecanica de checkout, nao de produto.
**Evitar:** a versao daqui, em que os tres degraus nao entregam nada. Isso nao e funil, e fraude, e queima gateway.

Evidencia: https://www.reclameaqui.com.br/perfectpay/compra-de-curso-com-cobrancas-adicionais-e-falta-de-retorno-da-plataforma_0xpgksbL0G11mhgE/
