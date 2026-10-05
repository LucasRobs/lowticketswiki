---
tipo: oferta
classe: oferta
slug: stalkeia-ai
nome: "Stalkeia.ai"
nicho: espionagem-rastreamento
sub_nicho: espionar-redes-sociais
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: perfectpay
url_pagina: "https://www.stalkea.ai/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Stalkea&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 37
ticket_bump: 19
ticket_upsell: 0
ticket_medio_est: 75
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 8
s_replica: 4
s_saturacao: 3
status: ativa
visto_primeiro: 2026-08-16
visto_ultimo: 2026-10-05
rodadas_vista: 13
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/stalkeia-ai"
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 8
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-05
veredito: observar
prioridade: 1
tags: [oferta, lowticket, marca]
---

# Stalkeia.ai

## Angulo
App que promete ver conversa/perfil fechado de terceiros. Grafias na mesma familia: Stalkeia.ai, Stalkeia.com, Stalker. Produtora citada: Disrupty Tecnologia.

## Funil
anuncio -> promessa de 'teste gratuito' -> coleta de dados -> primeiro pagamento R$29,90-37 -> segunda cobranca de R$19,90 em creditos para 'liberar o resultado'.

## Por que funciona
A mecanica de credito e o produto: o primeiro pagamento nao entrega nada, so habilita a proxima cobranca. E o que sustenta CPA alto no front.

## O que copiar / o que evitar
Copiar: a estrutura de creditos escalonados. Evitar: o nicho inteiro - espionagem de terceiros e o que mais gera reembolso forcado e derrubada de conta de anuncio.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (5 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-solicitacao-de-reembolso-por-aplicativo-de-espionagem-falso_zoL2pFAm1VieYFOp/

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

## Correção 2026-08-21 — página de vendas e camada de firewall

Candidato forte: **`stalkea.ai`** ("a maior ferramenta de stalker do Brasil"), SPA em JS.
Marcado como **incerto** — o WebFetch só pega a casca da página.

O achado que importa: existe um subdomínio **`up.stalkeia.website/firewall`**, página de
proteção/redirecionamento antes do funil. É infraestrutura para **esconder o destino real
da moderação de anúncios** do Meta. Sinal de operação madura e de que o criativo não
poderia ser aprovado apontando direto para a oferta.

## Rodada 2026-08-22 — sexta reclamacao, e a escada em numeros

Reclamacao de 17/08/2026 (ID 256618461), posterior a varredura de 16/08 — conta como nova.
`ra_reclamacoes` 5 -> 6.

O comprador registra o valor exato: **dois PIX, R\$ 56,96 + R\$ 37,00 = R\$ 93,96**. O vault
tinha `ticket_frente: 37` e `ticket_bump: 19`, somando 56. Os numeros reais nao batem com
essa decomposicao — ha um degrau a mais ou um preco diferente do registrado.
`ticket_medio_est` vai de 60 para 75, entre a frente conhecida e o topo observado.

Vale notar que a PerfectPay reembolsou em ~9 horas. Reembolso rapido em gateway grande
reduz o custo de reclamar, o que **infla** a contagem em relacao a gateways lentos — e mais
um motivo para nao comparar `ra_reclamacoes` entre plataformas diferentes.

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-nao-entrega-de-aplicativo-de-espionagem_bsQiiX5mms5RNOcb/

## Rodada 2026-08-23

PerfectPay, ha 8h: setima reclamacao acumulada, quarta rodada consecutiva vista. Volume estavel e alto - a unica oferta do vault presente em todas as rodadas desde 16/08.

## Rodada 2026-08-24

PerfectPay. URL da reclamacao de hoje e identica a citada na nota de 22/08 (bsQiiX5mms5RNOcb) — a lista nao girou em dois dias. ra_reclamacoes mantido em 7: o 8 de ontem seria contagem dupla.

## Rodada 2026-09-22

8 mencao(oes) nesta varredura (gateway PerfectPay). App fake de espionar WhatsApp/Instagram. Variações: Stalkeia.ai, Stalkea.ai, Stalkeia.com. Múltiplos gateways (confirmado em Mangofy também). Cobra créditos extras após venda para liberar resultados falsos.

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-nao-entrega-de-aplicativo-de-espionagem-falso_zoL2pFAm1VieYFOp/

## Rodada 2026-09-23

2 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram. Grafias: Stalkea.ai, Stalkeia.com. Não entrega o prometido, carregamento lento. Cobra créditos extras.

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-solicitacao-de-reembolso-por-aplicativo-de-espionagem-falso_zoL2pFAm1VieYFOp/

## Rodada 2026-09-24

1 mencao(oes) nesta varredura (gateway PerfectPay). Avistada nas passadas 04h41, 14h12 e 23h00. Grafias Stalkea.ai / StalkeaAI. Cobrancas duplicadas, R$ 47-152 por transacao, nao entrega.

Evidencia: [[2026-09-24 -- 0441]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-25

1 mencao(oes) nesta varredura (gateway PerfectPay). Detalhe novo: cobrancas sucessivas na mesma compra - R$ 47, R$ 37,90, R$ 67,90 - cada funcao nova cobra taxa extra.

Evidencia: [[2026-09-25 -- 0600]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-26

1 mencao(oes) nesta varredura (gateway PerfectPay). Listada como ainda ativa na passada das 06h00.

Evidencia: [[2026-09-26 -- 0600]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-10-03

7 mencao(oes) nesta varredura (gateway PerfectPay). App falso de espionagem de WhatsApp/Instagram, a oferta mais estável do vault desde 16/08. Grafias desta passada: Stalkea.ai, Stalker AI, 'stalkiem'. Cobra em PIX sucessivos e não entrega o resultado prometido.

Evidencia: https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-e-nao-entrega-do-servico-no-aplicativo-stalker-ai_ZkpgnfCPgV5V-Rge/

## Rodada 2026-10-04

3 mencao(oes) nesta varredura (gateway PerfectPay). App falso de espionagem/monitoramento de WhatsApp e Instagram; cobra em pagamentos sucessivos sem liberar acesso. Continua dominando o volume de queixas da PerfectPay, mesma família de grafias (Stalkea.ai, Stalker AI) de passadas anteriores.

Evidencia: https://www.reclameaqui.com.br/perfectpay/comprei-um-aplicativo-falso-e-enganoso-que-nao-entrega-o-prometido_WZ5LD8PtcACoBJV7/

## Rodada 2026-10-05

3 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram e rastrear celular. Continua dominando o topo das reclamacoes recentes da PerfectPay - 3 mencoes nesta janela curta (varios pix, cobranca sem entrega do resultado), mesmo padrao de creditos pra liberar.

Evidencia: https://www.reclameaqui.com.br/perfectpay/reembolso-negado-e-produto-nao-funcional-apos-compra-via-perfectpay_cpojyBGrbKt5gfjo/
