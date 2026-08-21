---
tipo: oferta
slug: raio-x-enare-farmacia
nome: "Raio-X ENARE Farmácia — Tática Farmacêutica"
nicho: concursos
sub_nicho: residencia-farmacia
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: "https://raioxenarefarmacia2026.netlify.app/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Raio-X%20ENARE%20Farmacia&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 59.90
ticket_bump: 15.90
ticket_upsell: 79.90
ticket_medio_est: 65
margem_est: 0.9
modelo: [direct]
formato_entrega: [pdf]
tem_recorrencia: false
s_ticket: 7
s_lucro: 4
s_replica: 4
s_saturacao: 9
status: nova
visto_primeiro: 2026-08-20
visto_ultimo: 2026-08-20
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/raio-x-enare-farmacia"
gateways_detectados: [hotmart, kiwify]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-20
veredito: descartar
prioridade: 0
tags: [oferta, lowticket, concursos]
---

# Raio-X ENARE Farmácia

**Descartada pela rubrica, guardada pela estrutura.** Score 5,35 e `s_replica` 4: Lucas
não replica isso. Mas a escada de preços é a mais bem construída que o vault viu, e vale
como modelo para um nicho que ele consiga executar.

## Ângulo

> "Pare de estudar tudo. Estude o que cai."

Vende **priorização**, não conteúdo. O argumento central é um número: 47% da prova está
em 4 dos 18 eixos. Todo o resto da página existe para sustentar esse número — 6 edições
analisadas, 317 questões rastreadas por ano e banca.

O bônus principal, "Raio-X dos Editais", é o movimento mais inteligente da oferta:
*"em vez de mais conteúdo para ler, ele entrega inteligência sobre o conteúdo que você já
vai estudar"*. Bônus que não aumenta a carga de trabalho do comprador.

## Funil — escada de quatro degraus

| Produto | Preço | Papel |
|---|---|---|
| Simulado (100 questões inéditas) | **R$ 15,90** | entrada / bump |
| Super-Combo (2 tabelas + bônus) | **R$ 29,90** | degrau intermediário |
| Raio-X principal (317 questões) | **R$ 59,90** (de R$79,90) | produto central |
| Kit Completo | **R$ 79,90** (de R$99,90) | topo, ancorado contra a soma das partes |

Complementares avulsos (Antimicrobianos, Quimioterápicos) vendidos separados alimentam
os dois combos. **Cada preço avulso existe para justificar o combo** — o Kit a R$79,90
custa menos que principal + simulado somados.

Dois gateways lado a lado no mesmo botão (Hotmart e Kiwify), sem preferência declarada.

Isca de topo: plano de estudos gratuito em Google Docs editável. Amostra de degustação
em Drive antes da compra.

## Por que `s_replica` é 4
317 questões comentadas em quatro camadas, escritas por dois doutores da UFPA com nome,
titulação e vínculo na página. A rubrica penaliza dependência de autoridade e produção
pesada, e aqui são as duas coisas ao mesmo tempo. Não há atalho: o produto *é* o trabalho.

## O que copiar
A arquitetura de escada, aplicada a qualquer nicho de prova com edital público. A parte
transportável é o método de construir o argumento: pegar N edições anteriores, contar
incidência por tema e vender o recorte. Isso funciona para concurso, OAB, ENEM, CFC,
residência de qualquer área — e a contagem pode ser automatizada.

Sazonalidade a favor: prova em 13/09/2026. Menos de um mês. Se houver reposição de verba,
é agora.

## Estado dos dados
- **Confirmado:** todos os preços, os dois gateways, autoria, estrutura de combos.
- **Provisório:** `s_lucro` 4 é conservador por ausência total de dado de anúncio e de
  reclamação. Produto de nicho estreito e recém-lançado pode simplesmente não ter gerado
  reclamação ainda — o falso negativo que o `Pipeline.md` alerta.
- **Faltando:** tempo no ar, criativos.

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
