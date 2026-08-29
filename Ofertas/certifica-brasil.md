---
tipo: oferta
classe: oferta
slug: certifica-brasil
nome: "Certifica Brasil — prova online, certificado pago"
nicho: certificacao
sub_nicho: taxa-para-liberar-certificado
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=certifica%20brasil&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.95
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 0
s_lucro: 8
s_replica: 5
s_saturacao: 4
status: nova
visto_primeiro: 2026-08-29
visto_ultimo: 2026-08-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/certifica-brasil"
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 13
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-29
veredito: observar
prioridade: 2
tags: [oferta, lowticket, certificacao]
---

# Certifica Brasil — prova online, certificado pago

**A unica coisa quente encontrada hoje.** Tres reclamacoes nos ultimos cinco dias (ha 2, ha 3, ha 5 dias) numa pagina de produtor que so tem 13 ativas no total. Todas nao respondidas.

## Contador de velocidade

| Numero | Valor |
|---|---|
| **N** — recebidas em 01/02-31/07 | 8 |
| **M** — ativas hoje | 13 |
| **M − N** | ~5 chegadas depois de 01/08 |

8 em seis meses = **1,3/mes**. ~5 so em agosto = **~5/mes**. Aceleracao de **~3,8x** — o mesmo formato de sinal que a [[google-captcha-tw]] deu ontem (4,6x), pela mesma medicao de uma requisicao so.

O reforco e a cadencia: as tres mais recentes sao de 2, 3 e 5 dias. Nenhum outro produtor minerado hoje tem reclamacao da ultima semana.

**0% de resposta, 0 avaliadas.** Perfil de operacao que nao trata reembolso — o oposto da [[alfabetinho]] e igual ao da `joyce-roberts`. Nesta rotina isso e sinal positivo de `s_lucro`: quem esta escalando nao gasta atendimento.

## A mecanica

Nao e curso com certificado. E **prova com certificado**: o comprador faz uma prova online e paga para receber o certificado digital — "Fiz a prova, passei e nao recebi meu certificado. Fiz o pagamento para obter o certificado digital". Outro cita carteirinha junto do certificado.

Isso e mais enxuto que o padrao do [[angulo-taxa-do-certificado]]: **nao ha nem curso para entregar.** O custo marginal e um PDF gerado. Margem estimada 0,95.

## O freio: `s_replica: 5`

Uma reclamacao de ha 2 dias pede **2a via de certificado de reservista** — documento militar emitido pela Uniao. Vender intermediacao de documento oficial e outra categoria de risco, nao e infoproduto. Some a isso "propaganda enganosa" como problema mais frequente (4 de 13) e emissao de certificado com valor declarado.

Pela regra do `Scoring.md` — nicho regulado tem teto — `s_replica: 5`. A mecanica e trivial de copiar tecnicamente; o que nao e replicavel com seguranca e a promessa de validade do documento. **Copiar a mecanica sem copiar a promessa** e o unico caminho: prova + certificado de conclusao proprio, sem alegar equivalencia oficial.

## Estado dos dados

- **Confirmado:** aceleracao (M−N), cadencia recente, mecanica, ausencia de atendimento.
- **Faltando:** ticket (nenhum corpo lido citou valor — `s_ticket: 0` e sentinela), gateway, `dias_no_ar`, pagina de vendas.
- **Proximo passo barato:** abrir o corpo de `pagamento-efetuado-para-certificado-digital...` para capturar valor e gateway. Um fetch.

Pagina do produtor: https://www.reclameaqui.com.br/empresa/certifica-brasil/lista-reclamacoes/

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
