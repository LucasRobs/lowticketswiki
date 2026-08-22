---
tipo: oferta
slug: unlovable
nome: "Unlovable"
nicho: ia-ferramentas
sub_nicho: gerador-de-app
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: kirvano
url_pagina:
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=unlovable&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 57
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 114
margem_est: 0.8
modelo: [direct]
formato_entrega: [app]
tem_recorrencia: true
s_ticket: 9
s_lucro: 7
s_replica: 3
s_saturacao: 5
status: ativa
visto_primeiro: 2026-08-21
visto_ultimo: 2026-08-22
rodadas_vista: 2
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta:
gateways_detectados: [kirvano]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 1
ra_plataformas: [kirvano]
ra_primeira_reclamacao: 2026-08-21
ra_checado: 2026-08-22
veredito: observar
prioridade: 1
tags: [oferta, recorrencia, ia]
---

# Unlovable

## Ângulo
**Nome como piada de posicionamento.** "Unlovable" é o anti-Lovable — categoria de
gerador de app por IA, entrada barata contra uma ferramenta cara e conhecida. O mesmo
mecanismo que faz [[mounjaro-de-pobre]] funcionar em emagrecimento: pegar carona no nome
que o mercado já pesquisa e vender a versão acessível.

## Funil
`R$ 57,00 recorrente`. A reclamação de 2026-08-21 é o dado bom: a primeira compra foi em
**27/03** e a cobrança seguia rodando em agosto. **Cinco meses de assinatura ativa** é o
sinal de receita mais concreto que esta rodada produziu — mais confiável que contagem de
reclamação, porque é uma série temporal dentro de um único caso.

## Estado dos dados
- **Confirmado:** R$ 57,00, recorrência, Kirvano, operação viva de março a agosto de 2026.
- **Faltando:** página, tempo no ar, criativos, taxa de churn.

`s_ticket: 9` pela recorrência — a rubrica dá 9-10 para qualquer valor recorrente.
`s_replica: 3` é o que derruba: construir um gerador de app é produção pesada de software.
**O ângulo é replicável, o produto não.**

## Correcao 2026-08-22 — nao e compra unica, e Pix Automatico recorrente

Releitura do corpo da reclamacao de 21/08/2026 (ID 257016211). A rodada anterior leu
"cinco meses de assinatura ativa" e registrou `tem_recorrencia: false`. As duas coisas nao
podem ser verdade ao mesmo tempo.

O que o corpo diz: compra em **27/03** por R\$ 57,00, reembolsada. Nova cobranca de
R\$ 57,00 em **27/05**, e outras depois, somando "mais de R\$ 100,00". O meio de pagamento
e **Pix Automatico** — e a cobranca sobreviveu ao reembolso da primeira parcela.

Tres consequencias:

1. `tem_recorrencia: true`. `ticket_medio_est` sobe de 57 para 114 — dois ciclos sao o
   piso observado, nao a media.
2. `s_lucro` sobe de 6 para 7: a oferta esta viva desde 27/03, sao ~148 dias, e a faixa
   "45-90 dias" do `Scoring.md` ja estava estourada.
3. **Pix Automatico e o achado transferivel.** Recorrencia sem cartao, em ticket baixo,
   num publico que nao tem limite de credito — e o unico jeito de rodar assinatura de
   R\$ 57 no Brasil sem depender de aprovacao de cartao. Nenhuma outra oferta do vault
   usa. Vale checar se [[app-do-paizao]] e [[treino-trinca]] cobram assim.

`ra_reclamacoes` permanece 1.

Evidencia: https://www.reclameaqui.com.br/kirvano-pagamentos/cobranca-indevida-de-produto-apos-solicitacao-de-reembolso-e-cancelamento_w-be-Q3HeN6FdwPQ/
