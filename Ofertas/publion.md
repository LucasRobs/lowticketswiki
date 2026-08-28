---
tipo: oferta
slug: publion
nome: "PubliOn"
nicho: renda-celular-cashback
sub_nicho: app-de-tarefas
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lastlink
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Publion&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 62
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 62
margem_est: 0.85
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 7
s_lucro: 5
s_replica: 3
s_saturacao: 4
status: morta
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/publion"
gateways_detectados: [lastlink]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [lastlink]
ra_primeira_reclamacao: 
ra_checado: 2026-08-16
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# PubliOn

## Angulo
Plataforma de tarefas com saldo minimo para saque. R$62,80 de entrada.

## Funil
anuncio -> plataforma -> tarefas -> saldo minimo atingido -> saldo zerado sem pagamento.

## Por que funciona
Mesma mecanica do Cashnopix num gateway diferente, o que confirma que o modelo esta rodando em mais de uma operacao.

## O que copiar / o que evitar
Referencia de mecanica. Mesmo problema estrutural do Cashnopix.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (1 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/lastlink/solicitacao-de-estorno-de-valor-pago-por-produto-editado-pelo-reclame-aqui-publion_OTETZNuOH0HHYKWE/

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

## Rodada 2026-08-21 — página de vendas não localizada

Busca web dedicada não encontrou LP ativa de **Publion**. Ou a oferta já rotacionou de
domínio, ou o nome do criativo difere do nome que o comprador registrou na reclamação.
`url_ads` preenchido com o termo de busca para tentar pela Biblioteca de Anúncios.

