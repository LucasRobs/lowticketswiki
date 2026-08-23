---
tipo: oferta
slug: lowzap
nome: "Lowzap (+ upsell Low Scale)"
nicho: ganhar-dinheiro
sub_nicho: whatsapp-ferramentas
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=lowzap&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 197
ticket_medio_est: 97
margem_est: 0.85
modelo: [vsl]
formato_entrega: [curso, app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 6
s_replica: 5
s_saturacao: 3
status: ativa
visto_primeiro: 2026-08-21
visto_ultimo: 2026-08-23
rodadas_vista: 3
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: [kirvano, hubla]
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 2
ra_plataformas: [kirvano, hubla]
ra_primeira_reclamacao: 2026-08-21
ra_checado: 2026-08-23
veredito: observar
prioridade: 1
tags: [oferta, lowticket, zap]
---

# Lowzap (+ upsell Low Scale)

## Ângulo
Ferramenta de WhatsApp com escada nomeada: **Lowzap** na frente, **Low Scale** no upsell.
Marca própria em dois degraus é sinal de operação estruturada, não de teste.

## Funil
`Lowzap → upsell Low Scale (recusável no checkout)`. A reclamação de hoje na Kirvano diz
que o comprador **recusou** o Low Scale no site e foi cobrado mesmo assim, e que o cartão
ficou salvo sem autorização. Isso é one-click upsell mal implementado — ou implementado
de propósito. Registrar como risco de replicação: o mecanismo é copiável, a execução não
deve ser.

## Estado dos dados
- **Confirmado:** existe, vende, gateway Kirvano, reclamação de 2026-08-21.
- **Provisório:** todos os tickets. `ticket_medio_est: 67` é estimativa por categoria.
- **Faltando:** preços reais, página, tempo no ar, criativos.

`s_replica: 5` — é software mais curso, não ebook. `s_saturacao: 3` — ferramenta de zap
para ganhar dinheiro é o leilão mais disputado que o vault mapeia. Cluster:
[[zap-radar]], [[teacher-zap]], [[loopyz]].

## Correcao 2026-08-22 — o upsell tem preco e tem outro gateway

Releitura do corpo da mesma reclamacao de 21/08/2026 (ID 257028189). A rodada anterior
registrou o nome do upsell (Low Scale) e o fato de ele ser cobrado apos recusa. **Faltavam
os dois dados que mudam o score:**

- O Low Scale custa **R\$ 197,00**. `ticket_upsell` sai de 0 e `ticket_medio_est` de 67 para 97.
- A cobranca nao passa pela Kirvano: o cartao foi salvo **na plataforma Hubla**, sem
  autorizacao. O funil atravessa dois gateways — Kirvano na frente, Hubla no upsell.

O segundo achado importa mais que o primeiro. Um funil que troca de gateway entre a frente
e o upsell **quebra a busca por gateway**: procurar "Lowzap" no Reclame Aqui da Kirvano
acha a frente e perde a escada, e procurar na Hubla acharia a escada sem o nome do produto.
O vault nunca varreu a Hubla. Ela nao esta na lista de plataformas do `Pipeline.md`.

`ra_reclamacoes` permanece 1 — e a mesma reclamacao, lida com mais cuidado.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/cobranca-indevida-de-curso-nao-solicitado-e-salvamento-nao-autorizado-de-dados-do-cartao_DZBZe48yfNcvRiBo/

## Rodada 2026-08-23

Kirvano, ha 5h: o upsell **Low Scale** foi cobrado mesmo depois do comprador RECUSAR a oferta na pagina, e os dados do cartao ficaram salvos sem autorizacao. Isso reclassifica o degrau: nao e upsell escondido, e cobranca contra recusa explicita. Terceira rodada consecutiva.
