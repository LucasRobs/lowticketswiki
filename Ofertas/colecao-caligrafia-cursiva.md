---
tipo: oferta
classe: oferta
slug: colecao-caligrafia-cursiva
nome: "Colecao Completa de Caligrafia 1o ao 6o ano — 380 atividades"
nicho: material-pedagogico
sub_nicho: caligrafia
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: cakto
url_pagina: "https://atividade-cursiva.netlify.app"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=caligrafia&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 12
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 12
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 2
s_lucro: 9
s_replica: 9
s_saturacao: 3
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 123
criativos_ultima: 8
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/colecao-caligrafia-cursiva"
gateways_detectados: [cakto]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-31
veredito: replicar
prioridade: 3
tags: [oferta, lowticket, material-pedagogico, imprimivel]
---

# Colecao Completa de Caligrafia — 380 atividades

**123 dias no ar.** E a maior idade de anuncio ja medida no vault, e a primeira medida de
verdade: saiu da Biblioteca de Anuncios, nao de estimativa. Veiculacao iniciada em **30 de abril
de 2026**, ainda ativa hoje.

Ninguem queima verba por quatro meses numa oferta que nao paga. Este e o unico registro do vault
onde `s_lucro` alto e **medicao**, nao palpite conservador.

## Funil

Anuncio (video 44s, criativo de "letra feia") -> LP unica em Netlify -> checkout Cakto
`pay.cakto.com.br/si5amap_922965` -> nenhum bump, nenhum upsell.

| Item | Valor |
|---|---|
| Preco | **R$ 12,00** (ancorado R$ 44,90, economia declarada R$ 32,90) |
| Entrega | 380 paginas em PDF, 6 modulos |
| Garantia | 7 dias, "sem burocracia e sem perguntas" |
| Escassez | timer de 14min59s |

Modulos: Caderno Pratico de Caligrafia · Silabario Cursivo · Frases Cursivas · Producao de
Frases · Coordenacao Motora Fina · Caderno do Alfabeto.

## Os bonus sao precificados mas nao sao produtos

Caderno do Alfabeto (R$ 9,90), Suporte VIP WhatsApp (R$ 14,90), Acesso Vitalicio (R$ 19,90),
Renovacao Gratuita (R$ 12,90). Somam R$ 57,60 de valor declarado e **custam zero**: dois sao
promessas de acesso, um e um canal de WhatsApp, um e um PDF a mais. E a tecnica mais barata de
inflar valor percebido que existe — e a oferta de R$ 12 encosta em R$ 60 de ancoragem sem
produzir nada.

## Por que funciona

**A dor tem testemunha.** Letra feia e o unico problema escolar que a mae ve com os proprios
olhos, todo dia, no caderno. Nao precisa de laudo, nao precisa de professora avisando. O
criativo so precisa mostrar um caderno rabiscado ao lado de um caderno bonito.

**E o inverso do nicho regulado.** Caligrafia nao promete tratamento, nao encosta em diagnostico
e nao reprova no Meta. Compare com [[kit-so-escola-tdah]], que carrega o risco de promessa
clinica: aqui o teto de `s_replica` nao existe.

## O que copiar / o que evitar

**Copiar:** a ancoragem por bonus de custo zero; o timer curto; a LP unica em host gratuito
(Netlify), que e o funil mais barato possivel; e o duplo anunciante — "Universo das Dinamicas" e
"Atividades Cursiva" rodam **o mesmo criativo em duas paginas**, o que dobra o alcance sem dobrar
producao. Ver [[parabolas-kids]], que faz o mesmo com dois dominios.

**Evitar:** competir com o preco. A R$ 12 sem bump nem upsell, o ticket medio e R$ 12 —
`s_ticket: 2`. Quem entrar aqui deve entrar com **bump** (caderno de numeros, R$ 9) e **upsell**
(pacote bastao + cursiva, R$ 27), porque a mesma verba de trafego compra o mesmo clique.

## Estado dos dados

- **Medido hoje:** `dias_no_ar: 123`, preco, gateway, garantia, bonus, escassez.
- **Estimado:** `criativos_ultima: 8` — soma conservadora dos criativos ativos das duas paginas
  (1 + 3 + 4). A contagem exata exige abrir cada anuncio.
- **Ausente:** rastro no Reclame Aqui. Esperado — ver a excecao de nicho no `Pipeline.md`.

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
      - note.criativos_ativos
      - note.dias_no_ar
      - note.ticket_frente
    sort:
      - property: note.data
        direction: DESC
```
