---
tipo: oferta
classe: oferta
slug: play-videos-premiados
nome: "Play Videos Premiados / PremiaPlay"
nicho: renda-extra
sub_nicho: taxa-para-liberar-saque
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: "http://playvideospremiados.com"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=assistir%20videos%20e%20ganhar%20dinheiro&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.95
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: false
s_ticket: 0
s_lucro: 2
s_replica: 2
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-30
visto_ultimo: 2026-08-30
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: []
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 106
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-30
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, renda-extra, morta-na-chegada]
---

# Play Videos Premiados / PremiaPlay

**Medida e descartada na mesma rodada.** Entrou pela busca por mecanica de "taxa para liberacao
de saque" e saiu com o diagnostico mais limpo que o contador `M − N` ja produziu.

| Medida | Valor |
|---|---|
| **M** — ativas | 106 |
| **N** — janela 01/02–31/07 | **0** |
| Mais recente | ha 7 meses |
| Restante da primeira pagina | 1 ano |

`N = 0` com `M = 106` e o caso extremo: volume historico real, **zero atividade na janela**.
Nao e uma oferta esfriando, e uma oferta que **acabou**. `s_lucro: 2`.

## Por que fica registrada mesmo morta

Duas razoes.

1. **Serve de calibragem do `M − N`.** A leitura de 29/08 dizia que "para produtor antigo, N
   baixo com M alto ja denuncia a desaceleracao". Aqui N e zero e o diagnostico e binario. Ter
   um caso de fundo de escala no vault ajuda a ler os intermediarios.
2. **Documenta a fronteira do que o vault cataloga.** A mecanica — pagar taxa atras de taxa
   para liberar um saldo que nunca sai — nao tem entregavel. Um comprador registrou
   **R$ 250,68 em taxas sucessivas**; outro descreve "taxa de manutencao" que vira varias.
   Isso nao e oferta low ticket com margem alta, e uma escada sem produto no fim.

O detalhe que quase a salva: uma reclamacao cita "paguei taxas para **e-books da Disrupty**" —
ou seja, em algum ponto a taxa foi embrulhada como venda de infoproduto. E a costura entre esta
categoria e o [[angulo-taxa-sobre-servico-gratuito]]. Mas embrulho nao muda a entrega: continua
sem produto.

`veredito: descartar`. Nao gasta rodada.

Pagina do produtor: https://www.reclameaqui.com.br/empresa/play-videos-premiados/lista-reclamacoes/

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
