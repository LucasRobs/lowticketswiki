---
tipo: oferta
slug: arquitetos-do-pensamento
nome: "Arquitetos do Pensamento — Projetando Realidades"
nicho: desenvolvimento-pessoal
sub_nicho: reprogramacao-mental
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: "https://arquitetos-do-pensamento.netlify.app/"
url_ads: 
moeda: BRL
ticket_frente: 27
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 27
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 3
s_lucro: 5
s_replica: 8
s_saturacao: 2
status: nova
visto_primeiro: 2026-08-20
visto_ultimo: 2026-08-20
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/arquitetos-do-pensamento"
gateways_detectados: [hotmart]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-20
veredito: descartar
prioridade: 0
tags: [oferta, lowticket]
---

# Arquitetos do Pensamento

Descartada: score 5,05. `s_saturacao` 2 sozinho mata a oferta — ebook de reprogramação
mental a R$27 é o produto mais copiado do mercado brasileiro.

## Ângulo
Psicologia + física quântica + fé, 45 capítulos, 112 páginas. R$27 ancorado em R$97.
Autor com nome e rosto: Matheus Bento.

## O detalhe que vale a nota
Logo abaixo do primeiro botão, em destaque:

> "autor real, sem pseudônimo, sem capa gerada por IA"

**A oferta se posiciona contra a própria categoria.** Isso é um dado de mercado, não de
copy: quando um vendedor precisa jurar que é humano, é porque o comprador já foi queimado
por ebooks de IA o suficiente para desconfiar por padrão.

Registro isso como sinal, não como oferta. Se essa objeção já entrou na cabeça do
comprador de infoproduto barato, ela vai contaminar todo o vault — inclusive as ofertas
de `s_replica` alto, que são justamente as mais fáceis de gerar automaticamente. Vale
acompanhar se outras páginas começam a fazer a mesma promessa.

## Funil
Página única → `pay.hotmart.com/N102194416L`. Dois bônus (guia de afirmações, áudios
binaurais), garantia de 7 dias, 3× de R$9,64. Sem bump ou upsell visíveis.

Rodapé marca © 2025: a página não é nova, apesar de anunciar "oferta de lançamento".

## Estado dos dados
- **Confirmado:** preço, gateway, ID do produto, estrutura de bônus, autoria.
- **Provisório:** `s_lucro` 5 sem dado de anúncio nem reclamação.
- **Faltando:** tudo de biblioteca de anúncios; bump e upsell dependem de Brute Mode.

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
