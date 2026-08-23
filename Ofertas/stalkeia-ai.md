---
tipo: oferta
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
visto_ultimo: 2026-08-23
rodadas_vista: 4
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/stalkeia-ai"
gateways_detectados: [perfectpay]
bump_oculto: true
upsell_oculto: false
ra_reclamacoes: 7
ra_plataformas: [perfectpay]
ra_primeira_reclamacao: 
ra_checado: 2026-08-23
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
