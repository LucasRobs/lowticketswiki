---
tipo: oferta
classe: oferta
slug: atmoz
nome: "Atmoz"
nicho: ganhar-dinheiro
sub_nicho: 
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina: "https://inteligenciajohn.com"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=atmoz&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 297.99
ticket_bump: 0
ticket_upsell: 997
ticket_medio_est: 647.5
margem_est: 0.8
modelo: [webinar]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 10
s_lucro: 4
s_replica: 3
s_saturacao: 0
status: ativa
visto_primeiro: 2026-10-29
visto_ultimo: 2026-10-31
rodadas_vista: 2
dias_no_ar: 13
criativos_ultima: 120
criativos_delta: 10
unfunnelizer_capturado: false
ativos_pasta: "Ativos/atmoz"
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 3
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 
ra_checado: 2026-10-31
veredito: observar
prioridade: 0
tags: [oferta, lowticket, marca]
---

# Atmoz

## Angulo
Estreia, 3 IDs na Kirvano em ~24h, tres compradores diferentes: 262837843 (app Atmoz R$ 297,99 no Pix em 28/10; para usar, pedem 'investimento' de R$ 997), 262880843 (tres cobrancas no cartao em 28/10: R$ 366,30 + R$ 369,99 + R$ 858,30, 'o Sr Jhon da plataforma Atmoz'), 262908177 (escada ATMOZ -> ATMOZ PRO -> CARTEIRA JOHN, 'sem esse nao iria funcionar'). Biblioteca: ~110 anuncios ativos de um unico anunciante, 'John Atmoz Rodrigues', LP inteligenciajohn.com ('Aula Gratuita | JOHN'), o mais antigo carregado de 18/10 e 13 deles de 27-29/10. Funil de aula gratuita -> app -> 'carteira'.

## Funil
Anuncio Meta de "John Atmoz Rodrigues" ("Aula Gratuita | JOHN", "a maior oportunidade dos ultimos tempos") -> aula em inteligenciajohn.com -> app Atmoz R$ 297,99 (Pix ou cartao, Kirvano) -> ATMOZ PRO -> CARTEIRA JOHN ("sem esse nao iria funcionar") -> "investimento" de R$ 997. Um comprador pagou R$ 366,30 + R$ 369,99 + R$ 858,30 no mesmo dia (262880843).

## Por que funciona
<!-- preencher com leitura humana -->

## O que copiar / o que evitar
<!-- preencher com leitura humana -->

## Estado dos dados
- **Confirmado:** existencia, 3 mencao(oes) na varredura de 2026-10-29 (radar-low-ticket automatico, WebFetch por titulo de lista — sem abrir todas as paginas).
- **Medido na Biblioteca (2026-10-29):** ~110 anuncios ativos para "atmoz", 29 de 30 carregados de um so anunciante (John Atmoz Rodrigues), datas de 18/10 a 29/10 -> `dias_no_ar: 11`, `criativos_ultima: 110`. `s_lucro` 4 (faixa 7-20 dias; delta de criativos ainda sem segunda leitura). `s_replica` 3: rosto proprio + promessa financeira (teto 4 do Scoring.md).
- **Sentinela (nao medido ainda):** s_saturacao — a busca foi por marca, que devolve um operador so e nao mede o angulo.
- **Estimado, nao confirmado:** ticket_medio_est a partir da faixa de preco citada na(s) reclamacao(oes); s_lucro travado no teto 6 (Scoring.md) por falta de dias_no_ar.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/quero-o-ressarcimento-do-meu-pagamento-via-pix-de-r29799-pelo-app-atmoz_L13cNF59br2DCVd3/

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

## Rodada 2026-10-31

3 mencao(oes) nesta varredura (gateway Kirvano). So Biblioteca (nenhum ID novo nas 5 linhas da Kirvano): ~120 anuncios ativos para 'atmoz' (eram ~110 em 29/10), todos os carregados de John Atmoz Rodrigues, LP inteligenciajohn.com/atmoz ('Aula Gratuita | JOHN'). Mais antigo carregado 18/10 (13 dias), 5 iniciados em 29/10 e 1 em 30/10: a verba continua entrando.

Evidencia: https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=atmoz&search_type=keyword_unordered&media_type=all
- **Medido na Biblioteca (2026-10-31):** ~120 anuncios ativos para "atmoz" (eram ~110 em 29/10), todos os carregados de John Atmoz Rodrigues, LP `inteligenciajohn.com/atmoz`. Mais antigo carregado 18/10 -> `dias_no_ar: 13`; 5 iniciados em 29/10 e 1 em 30/10 -> `criativos_ultima: 120`, `criativos_delta: +10`. Primeira segunda leitura: a verba segue subindo. `s_lucro` mantido em 4 (faixa 7-20 dias; delta positivo numa leitura so ainda nao e "aquecendo", que pede 2+ rodadas).
