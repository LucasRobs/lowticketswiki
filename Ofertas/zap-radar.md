---
tipo: oferta
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
visto_ultimo: 2026-08-21
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/zap-radar"
gateways_detectados: [perfectpay]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
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
