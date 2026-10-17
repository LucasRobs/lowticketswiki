---
tipo: oferta
classe: oferta
slug: zap-radar
nome: "ZAP Radar"
nicho: espionagem-rastreamento
sub_nicho: busca-whatsapp
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: "https://whatsradar.com/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=WhatsRadar&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 97
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 97
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 8
s_lucro: 5
s_replica: 4
s_saturacao: 3
status: ativa
visto_primeiro: 2026-08-16
visto_ultimo: 2026-10-16
rodadas_vista: 19
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/zap-radar"
gateways_detectados: [perfectpay, payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 26
ra_plataformas: [perfectpay, payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-16
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# ZAP Radar

## Angulo
Busca/rastreio de numero de WhatsApp. R$97 de entrada, o dobro do padrao do nicho.

## Funil
anuncio -> pagina -> checkout PerfectPay R$97 -> resultado da busca nao e exibido.

## Por que funciona
Mesmo nicho da Stalkeia mas com ticket de entrada 2,6x maior. Interessa como referencia de precificacao do nicho, nao como oferta.

## O que copiar / o que evitar
Registro de faixa de preco. Nicho com o mesmo problema regulatorio da Stalkeia.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar_OoS-eZ01DAQS7Dyn/

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

## Correção 2026-08-21 — checkout é Payt, e há dois domínios

Dois domínios com a mesma headline ("Clone o WhatsApp do seu Parceiro em 5 minutos"):
**`whatsradar.com`** e **`zapradar.shop`**. Checkout **Payt**, não PerfectPay.

**Não confundir** com `zapradar.com.br` e `zapradar.alualab.com` — são um CRM de WhatsApp
legítimo, produto completamente diferente com nome colidente.

## Rodada 2026-09-22

4 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de análise que promete resultados de busca mas não entrega acesso. Propaganda enganosa clara. Cobra upfront sem entrega.

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar_OoS-eZ01DAQS7Dyn/

## Rodada 2026-09-23

1 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de análise que não funciona. R$ 97 upfront, zero acesso. Propaganda enganosa direta.

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar_OoS-eZ01DAQS7Dyn/

## Rodada 2026-09-24

1 mencao(oes) nesta varredura (gateway PerfectPay). Avistado 14h12 e 23h00. Pagamento sem acesso aos resultados das buscas.

Evidencia: [[2026-09-24 -- 1412]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-25

1 mencao(oes) nesta varredura (gateway PerfectPay). 'Nao da opcoes para ver o resultado das buscas' - reembolso concedido (reclamacao de 10/08).

Evidencia: [[2026-09-25 -- 1700]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-26

1 mencao(oes) nesta varredura (gateway PerfectPay). Listada como ainda ativa na passada das 06h00.

Evidencia: [[2026-09-26 -- 0600]] (rodada agendada; sem URL individual de reclamacao)

## Rodada 2026-09-27

1 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de análise/prospecção (SaaS). Cobrança sem acesso aos resultados. Persistente de 26/09.

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar_OoS-eZ01DAQS7Dyn/

## Rodada 2026-09-28

1 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de automação/radar de vendas. Cobrança efetuada sem acesso aos resultados. NOVA - primeira menção.

Evidencia: 

## Rodada 2026-09-29

1 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de análise/monitoramento. Problema: acesso negado aos resultados após pagamento.

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar/

## Rodada 2026-10-02

5 mencao(oes) nesta varredura (gateway Payt). Reclamacao nova 260598927 (01/10) na Payt: app comprado no cartao nao entrega o prometido. Primeira vez que a oferta aparece no RA da Payt (antes so PerfectPay).

Evidencia: https://www.reclameaqui.com.br/payt/lista-reclamacoes/ (ID 260598927)

## Rodada 2026-10-03

2 mencao(oes) nesta varredura (gateway PerfectPay). Ferramenta de busca de número de WhatsApp (checkout real é Payt, não PerfectPay nesta amostra). Cobra R$97 upfront e não exibe resultado da busca. Mesmo nicho da Stalkeia, ticket ~2,6x maior.

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicitacao-de-reembolso-do-produto-zap-radar-cobrado-pela-perfect-pay_rBXZmMzd8LiU2oqK/

## Rodada 2026-10-04

2 mencao(oes) nesta varredura (gateway PerfectPay). App que promete monitorar WhatsApp de terceiros; pagamento via PerfectPay sem liberação de resultados. Reaparece de novo nesta passada confirmando o mesmo padrão de queixa dos rounds anteriores.

Evidencia: https://www.reclameaqui.com.br/perfectpay/pagamento-efetuado-sem-acesso-aos-resultados-no-zap-radar_OoS-eZ01DAQS7Dyn/

## Rodada 2026-10-05

1 mencao(oes) nesta varredura (gateway PerfectPay). App de rastreamento/busca por WhatsApp (whatsradar.com). Já tracked no vault; reconfirmado com valor exato R$97,09 nesta passada.

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicitacao-de-reembolso-do-produto-zap-radar-cobrado-pela-perfect-pay_rBXZmMzd8LiU2oqK/

8 mencao(oes) nesta varredura (gateway Payt). 3 reclamacoes novas em 04/10. Uma descreve cinco Pix diferentes, um por etapa, sem liberar nada (260770355); outra diz que qualquer numero consultado devolve as mesmas fotos e mensagens (260761095).

Evidencia: https://www.reclameaqui.com.br/payt/lista-reclamacoes/ (IDs 260782901, 260770355, 260761095)

## Rodada 2026-10-06

1 mencao(oes) nesta varredura (gateway PerfectPay). App de rastreamento/espionagem. Reconfirmado via PerfectPay (ja tambem visto no Payt), operacao multi-gateway continua ativa.

Evidencia: https://www.reclameaqui.com.br/perfectpay/solicitacao-de-reembolso-do-produto-zap-radar-cobrado-pela-perfect-pay_rBXZmMzd8LiU2oqK/

## Rodada 2026-10-08

1 mencao(oes) nesta varredura (gateway Payt). App de rastreio/espionagem de WhatsApp ja catalogado no vault (14+ rodadas desde 16/08, multi-gateway PerfectPay+Payt). Nova reclamacao direta na Payt em 08/10: usuario nao consegue abrir o app, login sempre 'incorreto', alega propaganda enganosa. Confirma que a oferta segue ativa e com acesso quebrado/credencial que nao funciona.

Evidencia: https://www.reclameaqui.com.br/payt/nao-consigo-abrir-o-app-zapradar-e-solicito-estorno-por-propaganda-enganosa_D00TBxYjXmHPp3Dy/

10 mencao(oes) nesta varredura (gateway PerfectPay). 2 reclamacoes com ID novo em 07/10 na PerfectPay: 261048565 (acesso nao liberado) e 261039867 (cobraram mais para entregar o produto). Mesma taxa para liberar.

Evidencia: https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/ (IDs 261048565, 261039867)

## Rodada 2026-10-10

1 mencao(oes) nesta varredura (gateway Payt). App de rastreamento/busca no WhatsApp; reclamante nao conseguiu abrir o app apos a compra, pede estorno por propaganda enganosa. Ja registrado no vault.

Evidencia: https://www.reclameaqui.com.br/payt/nao-consigo-abrir-o-app-zapradar-e-solicito-estorno-por-propaganda-enganosa_D00TBxYjXmHPp3Dy/

## Rodada 2026-10-11

26 mencao(oes) nesta varredura (gateway Payt). 16 reclamacoes com ID novo de 08 a 11/10: 12 na Payt (261365841 R$ 137, 261361005 R$ 97 + cobranca para abrir as mensagens, 261345285, 261336883, 261329737, 261290247, 261263781, 261254081, 261228271, 261226587, 261223171, 261191197 com varias cobrancas no cartao) e 4 na PerfectPay (261240537 'Zap Radar / WhatsSpy', 261202867, 261202463, 261107973). O volume migrou para a Payt. Biblioteca 'zap radar': nenhum anuncio da operacao (so ruido de outros anunciantes).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (12 IDs) + perfectpay (4 IDs)

## Rodada 2026-10-14

1 mencao(oes) nesta varredura (gateway Payt). Primeira aparicao no radar. App que o comprador nao conseguiu abrir, reclamacao de propaganda enganosa com pedido de estorno via Payt -- nome sugere app de rastreamento/espionagem de WhatsApp.

Evidencia: https://www.reclameaqui.com.br/payt/nao-consigo-abrir-o-app-zapradar-e-solicito-estorno-por-propaganda-enganosa_D00TBxYjXmHPp3Dy/

## Rodada 2026-10-15

1 mencao(oes) nesta varredura (gateway Payt). Payt estava sem varredura desde 14/10 17:14 (+24h), mas a pagina 1 trouxe a mesma reclamacao de 08/10 contra o app de rastreamento de WhatsApp -- indica que o volume de reclamacoes novas da Payt e baixo e o bug de paginacao (ver nota da passada) impede ver qualquer coisa mais recente. Zero novidade genuina, mas confirma oferta multi-dia (vista em 08, 10, 14 e agora 15/10).

Evidencia: https://www.reclameaqui.com.br/payt/nao-consigo-abrir-o-app-zapradar-e-solicito-estorno-por-propaganda-enganosa_D00TBxYjXmHPp3Dy/

## Rodada 2026-10-16

1 mencao(oes) nesta varredura (gateway Payt). App de rastreamento de WhatsApp, oferta mais antiga e mais recorrente do vault (18+ rodadas desde 16/08). Mesma reclamacao ja conhecida ainda na pagina 1 da Payt -- zero novidade, so confirma presenca continua.

Evidencia: https://www.reclameaqui.com.br/payt/nao-consigo-abrir-o-app-zapradar-e-solicito-estorno-por-propaganda-enganosa_D00TBxYjXmHPp3Dy/
