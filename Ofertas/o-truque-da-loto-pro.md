---
tipo: oferta
classe: oferta
slug: o-truque-da-loto-pro
nome: "O Truque da Loto PRO"
nicho: apostas-loteria
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: payt
url_pagina: 
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Truque%20da%20Loto&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 4
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 252.78
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 10
s_lucro: 2
s_replica: 0
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-03
visto_ultimo: 2026-10-26
rodadas_vista: 6
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/o-truque-da-loto-pro"
gateways_detectados: [payt]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 10
ra_plataformas: [payt]
ra_primeira_reclamacao: 
ra_checado: 2026-10-26
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# O Truque da Loto PRO

## Angulo
Achado novo e o mais chamativo da passada: funil de 4 produtos amarrados (O Truque da Loto PRO, Lovable.app, Blindagem Anti-Erro do Apostador, Comunidade Truque da Loto) vendendo 'método' de previsão de loteria. Cobrança não autorizada clara, suporte bloqueou os pedidos de reembolso e só saiu com escalada direto na Payt.

## Funil
anuncio -> pagina -> checkout payt -> ver evidencia.

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 1 mencao(oes) na varredura de 2026-10-03 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Sentinela (nao medido ainda):** dias_no_ar, criativos_ultima, s_replica, s_saturacao — dependem da Etapa 1 (Biblioteca de Anuncios) / Etapa 2 (unFunnelizer), que a automacao 6x/dia nao roda.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/payt/fui-cobrado-indevidamente-por-4-servicos-pela-payt-que-nao-comprei_o4e7nq1Fi06vnQrG/

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

## Rodada 2026-10-05

4 mencao(oes) nesta varredura (gateway Payt). Operacao de loteria/apostas com upsell muito pesado: uma unica reclamacao lista 4 produtos cobrados do mesmo produtor na mesma venda (Blindagem Anti-Erro do Apostador, Comunidade Truque da Loto, Truque da Loto PRO, Truque da Loto), somando R$623,24. Estrutura de order bump agressiva, acabou de aparecer via gateway rotativo Payt - forte candidato a modelar o funil.

Evidencia: https://www.reclameaqui.com.br/payt/fui-cobrado-indevidamente-por-4-servicos-pela-payt-que-nao-comprei_o4e7nq1Fi06vnQrG/

## Rodada 2026-10-19

6 mencao(oes) nesta varredura (gateway Payt). 2 IDs novos na Payt (4 -> 6): 261749815, 261641399. Voltou depois de esfriar.

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/

## Rodada 2026-10-21

7 mencao(oes) nesta varredura (gateway Payt). Retorno com 1 ID novo (6 -> 7): 262243473, compra em 17/10 depois de 'ouvir o entrevistador' (VSL em formato de entrevista): R$ 149 no Pix, R$ 172,62 no cartao e uma terceira cobranca de R$ 177 tentada. Escada de tres cobrancas no mesmo dia.

Evidencia: https://www.reclameaqui.com.br/payt/fui-cobrado-indevidamente-por-venda-enganosa-e-nao-consigo-contato-com-o-suporte_mBBAvG1uc8BBOYDO/

## Rodada 2026-10-23

9 mencao(oes) nesta varredura (gateway Payt). 2 IDs novos (7 -> 9): 262368523 (segunda cobranca no cartao que o titular diz nao ter feito, 'Produto: O Truque da Loto') e 262265883 (app nao recebido, 'dizia que tinha que efetuar' mais um pagamento).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (IDs 262368523, 262265883)

## Rodada 2026-10-26

10 mencao(oes) nesta varredura (gateway Payt). 1 ID novo (9 -> 10): 262552743 (Payt, Pix de R$ 149 para acesso e logo outro pagamento gerado).

Evidencia: https://www.reclameaqui.com.br/empresa/payt/lista-reclamacoes/ (ID 262552743)
