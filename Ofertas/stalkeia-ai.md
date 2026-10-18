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
visto_ultimo: 2026-10-17
rodadas_vista: 20
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/stalkeia-ai"
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 28
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-10-17
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

11 mencao(oes) nesta varredura (gateway PerfectPay). 3 reclamacoes nomeadas em 05/10, as primeiras com ID desde 256618461: 260841477 (app simula a interface do Instagram e inventa conversas), 260836685 (R$ 155,70 em 3 transacoes) e 260834783 (R$ 232,64 em 3 Pix no mesmo dia). Uma quarta (260833211, 'Stalker app', taxas sucessivas) provavelmente e a mesma operacao e nao foi contada. Taxa escalonada: tres cobrancas por compra.

Evidencia: https://www.reclameaqui.com.br/perfectpay/realizei-3-pagamentos-via-pix-para-e-o-produto-e-propaganda-enganosa_U29fQmXatOKQJ4w8/ (IDs 260841477, 260836685, 260834783)

## Rodada 2026-10-06

1 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram/celular. Reconfirmado mais uma vez via PerfectPay, 4 pix pro dominio stalkeia.com. Grafias: Stalkea.ai, Stalkeia.com.

Evidencia: https://www.reclameaqui.com.br/perfectpay/fiz-4-pix-para-app-que-e-editado-pelo-reclame-aqui_GbZOb-kvBPPM7FLa/

## Rodada 2026-10-08

15 mencao(oes) nesta varredura (gateway PerfectPay). 4 reclamacoes com ID novo em 07-08/10: 261105725 e 261102589 ('Stalkea AI - Acesso Completo 2.0'), 261061359 e 261044525 ('Stalkeia.com', R$ 47,90 e R$ 39,90). Aparece um nome de produto novo, 'Acesso Completo 2.0'.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 261105725, 261102589, 261061359, 261044525)

## Rodada 2026-10-10

3 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram. Grafias: Stalkea.ai, Stalkea APP. 3 reclamações novas publicadas hoje (10/10) só na primeira página da PerfectPay — oferta com o maior volume sustentado do radar (134+ menções no histórico do vault).

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicito-reembolso-por-propaganda-enganosa-do-app-stalkeia_n4cG4M9Agu_uGags/

## Rodada 2026-10-11

28 mencao(oes) nesta varredura (gateway PerfectPay). 13 reclamacoes com ID novo de 08 a 11/10, todas acima de 261105725: 261382501, 261382373, 261347677, 261293029, 261292483, 261292285, 261288369, 261253637 ('Acesso Completo 2.0'), 261204241, 261147273 (stalkeia.website), 261144399, 261114367 (taxas extras para liberar) e 261110827. Maior volume da nota desde a estreia.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (13 IDs de 261110827 a 261382501)

## Rodada 2026-10-13

2 mencao(oes) nesta varredura (gateway PerfectPay). Segue ativo: 2 reclamacoes novas em 11/10, cobrancas de R$55,35 (9x) e R$44,80 (7x) nao reembolsadas. PerfectPay nega venda direta. Recorrente no radar ha semanas.

Evidencia: https://www.reclameaqui.com.br/perfectpay/comprei-um-app-de-espionagem-falso-e-fui-cobrado-indevidamente_qyYRcGho51TUmHXq/

## Rodada 2026-10-14

34 mencao(oes) nesta varredura (gateway PerfectPay). 6 reclamacoes nomeadas com ID novo na PerfectPay: 261503107, 261446151, 261445633, 261441547, 261414905, 261408091. Nao contadas: 261491319 ('Stalkeria', tres cobrancas de R$ 162), 261557075 (R$ 47,90 + 39,90 sem acesso, sem nome) e 261464561 (quatro Pix, sem nome).

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 261503107, 261446151, 261445633, 261441547, 261414905, 261408091)

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram. Mesma reclamacao da passada anterior ainda ativa na pagina 1 -- sem novidade, so confirma presenca continua na PerfectPay.

Evidencia: https://www.reclameaqui.com.br/perfectpay/stalkeia-ia-nao-cumpre-o-que-promete_1qOOSCnIR45PgPXH/

## Rodada 2026-10-16

1 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram, mesma familia Stalkeia/Stalkea. Reclamacao desta rodada: 'comprei servico enganoso no stalkea.ai e quero estorno'. Presenca constante ha semanas, confirma oferta sustentada.

Evidencia: 

## Rodada 2026-10-17

1 mencao(oes) nesta varredura (gateway PerfectPay). App de espionar WhatsApp/Instagram, grafias Stalkeia/Stalkea. Mesma reclamacao da rodada anterior (21:46) -- zero novidade, apenas confirma presenca continua.

Evidencia: https://www.reclameaqui.com.br/perfectpay/comprei-servico-enganoso-no-e-quero-estorno_1K5fva5lYbNP8xmH/
