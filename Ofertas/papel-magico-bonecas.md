---
tipo: oferta
slug: papel-magico-bonecas
nome: "+350 Bonecas de Papel — Papel Mágico"
nicho: imprimiveis-infantil
sub_nicho: tempo-de-tela
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: lowify
url_pagina: "https://papelmagicobr.netlify.app/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=%2B350%20Bonecas%20de%20Papel&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 12.90
ticket_bump: 0
ticket_upsell: 24.90
ticket_medio_est: 21
margem_est: 0.95
modelo: [direct]
formato_entrega: [pdf]
tem_recorrencia: false
s_ticket: 3
s_lucro: 6
s_replica: 10
s_saturacao: 7
status: nova
visto_primeiro: 2026-08-20
visto_ultimo: 2026-08-20
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/papel-magico-bonecas"
gateways_detectados: [lowify]
bump_oculto: false
upsell_oculto: true
ra_reclamacoes: 0
ra_plataformas: []
ra_primeira_reclamacao: 
ra_checado: 2026-08-20
veredito: observar
prioridade: 3
tags: [oferta, lowticket, imprimiveis]
---

# +350 Bonecas de Papel — Papel Mágico

**O achado da rodada.** `s_replica` 10 é a primeira nota máxima do vault nesse eixo.

## Ângulo

> "Sua filha vai largar o celular quando ver isso!"

O produto é boneca de papel imprimível. **A oferta não é sobre boneca — é sobre tempo de
tela.** A headline não vende a atividade, vende o fim da briga diária. É a diferença
entre vender o objeto e vender a saída de um conflito que a mãe já perdeu várias vezes.

A seção "esta coleção é ideal pra você que" tem seis blocos, e cada um nomeia um cenário
específico em vez de um benefício: *já tentou cortar o celular e cedeu na primeira birra*,
*briga com a sogra ou marido que sempre cede*, *tem medo de atraso de fala*. O terceiro é
o mais afiado — usa o conflito familiar, não o da criança, como gatilho.

O objetivo é ser substituição, não proibição: "você não tira nada, você substitui".

## Funil

| Degrau | Preço | Onde |
|---|---|---|
| Plano Básico | **R$ 12,90** (de R$47,90) | 350 bonecas, sem bônus |
| Plano Completo | **R$ 24,90** (de R$143,50) | `pay.lowify.com.br/checkout?product_id=yZauOn` |
| Downsell de saída | **R$ 17,90** | `pay.lowify.com.br/checkout?product_id=DxPp46` |

O **downsell de saída** é o detalhe caro: um pop-up dispara na intenção de sair e oferece
o Completo por R$17,90 em vez de R$24,90. Isso não é funil de iniciante — é alguém que já
mediu abandono e construiu uma segunda chance para ele.

Seis bônus com valor declarado (R$19,90 + R$12,90 × 4 = R$71,50), mais um sétimo bônus de
"atualizações mensais gratuitas" que cria motivo de retorno sem cobrar recorrência.

Entrega por **WhatsApp e e-mail**, garantia de 30 dias (não 7).

## Por que isso está rodando

Custo de produção próximo de zero: ilustração kawaii chibi, formato A4, PDF. Sem rosto,
sem autoridade, sem nicho regulado, sem logística. A página inteira roda em netlify.

O que sustenta a nota: **nada aqui exige o produtor original.** Qualquer pessoa com um
gerador de imagem e uma tarde monta o acervo. É o oposto de [[raio-x-enare-farmacia]],
descoberta na mesma rodada e que depende de dois doutores.

## O que copiar / o que evitar

**Copiar:** o downsell de saída (o vault não tinha nenhum exemplo até hoje); a ancoragem
por unidade — "menos de 4 centavos por boneca" transforma R$12,90 em algo sem comparação;
o "Truque do Dedão", um detalhe de uso trivial que finge ser método proprietário; e a
garantia de 30 dias, que num produto de custo zero é retórica pura.

**Evitar:** os temas nomeados são personagens genéricos (princesa, fada, sereia), mas a
headline promete "personagens favoritos dela". Se a modelagem usar personagem licenciado
de verdade, vira problema de marca. Mantenha genérico como eles mantiveram.

**Melhorar:** eles entregam meninas de 4 a 10 anos. O bônus #6 já admite que existe
demanda de menino e entrega 20 bonecos como consolo. Uma oferta espelho só de meninos é
campo aberto — e o mesmo acervo, redesenhado.

## Estado dos dados
- **Confirmado:** preços dos três degraus, gateway, IDs de produto, estrutura de bônus.
- **Provisório:** `ticket_medio_est` 21 assume mix entre básico e completo. A página afirma
  97% no completo, o que empurraria para 24; não há como verificar, então fica no meio.
- **Faltando:** tempo no ar e contagem de criativos. `s_lucro` 6 é leitura de sofisticação
  do funil, não de dado de anúncio — é o eixo mais frágil desta nota.
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
