---
tipo: oferta
classe: angulo
slug: angulo-bonecas-de-papel-imprimivel
nome: "Angulo — bonecas e cenarios de papel imprimiveis"
nicho: comportamento-infantil
sub_nicho: imprimivel-brincadeira
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: desconhecido
url_pagina: ""
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=bonecas%20de%20papel&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 0
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 0
margem_est: 0.9
modelo: [direct]
formato_entrega: [ebook]
tem_recorrencia: false
s_ticket: 0
s_lucro: 8
s_replica: 10
s_saturacao: 2
status: nova
visto_primeiro: 2026-08-31
visto_ultimo: 2026-08-31
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: ""
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-31
veredito: observar
prioridade: 2
tags: [oferta, lowticket, angulo]
---

# Angulo — bonecas e cenarios de papel imprimiveis

**Sete operadores ativos medidos numa unica consulta.** Este e o primeiro angulo do vault cuja
saturacao foi *contada*, nao estimada.

| Operador | Dominio | Inicio do anuncio | Dias | Preco |
|---|---|---|---|---|
| Camila Andrade — [[bonecas-papel-maria-criativa]] | `bonecasdepapel28.lovable.app` | 08/07 | 54 | 17,90 / 27,90 |
| Carla Menezes — [[kit-mundinho-de-papel]] | `bibliotecainterativa.com` | 08/07 | 54 | 10,00 |
| Prof.a Juliana Gamon — [[casinha-dos-sonhos]] | `casinhadossonhos.com.br` | 20/07 | 42 | 10,00 |
| Rebeca Flores | (sem link no criativo) | 24/07 | 38 | 10,90 |
| Jessica Alencar | `bonecas-de-papel.vercel.app` | 03/08 | 28 | — |
| Escola Pequena Estilista — [[pequenas-estilistas]] | `pequenasestilistas.com` | 12/08 | 19 | 27,90 |
| [[papel-magico-bonecas]] | `papelmagicobr.netlify.app` | — | — | 12,90 / 24,90 |

## Correcao da shortlist de 30/08

A nota de ontem colocou a [[papel-magico-bonecas]] em primeiro lugar e escreveu **"campo
aberto"**. Com a Biblioteca de Anuncios de volta, isso esta errado: o campo tem sete operadores,
tres deles com mais de 40 dias de anuncio, e a Papel Magico e uma entre pares — nao a dona do
angulo.

`s_saturacao` das notas do angulo cai para **2**. A conclusao pratica de ontem (o ativo e 100%
gerave por IA, `s_replica: 10`) continua valendo e e justamente **por que** o campo lotou.

**A licao de metodo:** sem Etapa 1, "campo aberto" nunca foi medicao — era ausencia de dado
lida como ausencia de concorrente. Onze rodadas produziram esse vies em silencio, e ele so
apareceu quando a fonte voltou.

## A ancoragem circula pronta

[[papel-magico-bonecas]] e [[bonecas-papel-maria-criativa]] ancoram **nos mesmos valores ao
centavo**: R$ 47,90 no basico e R$ 143,50 no completo, com os mesmos sete bonus na mesma ordem.
Operadores diferentes, dominios diferentes, gateways diferentes (Lowify e Kirvano), oferta
identica. O kit de venda deste angulo esta sendo distribuido pronto — provavelmente por um
infoproduto de "como vender imprimiveis".

**Consequencia para replica:** copiar este funil e copiar o setimo clone. O que ainda tem espaco
e o **reenquadramento** — [[pequenas-estilistas]] cobra 2,3x com o mesmo ativo — e o **publico
espelho** (acervo so de meninos, que os sete tratam como bonus de 20 pecas).

## Padroes estaveis do angulo

1. **Host gratuito** (Netlify, Vercel, Lovable) em 5 dos 7. Custo de infra zero.
2. **Persona feminina com nome proprio** em 5 dos 7. Nao ha marca — ha "Camila", "Carla",
   "Rebeca", "Jessica".
3. **Abertura por nostalgia dirigida a mae**, nao por beneficio para a filha.
4. **Faixa de preco R$ 10 a R$ 27,90.** Piso duro em R$ 10.

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
