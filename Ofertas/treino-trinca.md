---
tipo: oferta
classe: oferta
slug: treino-trinca
nome: "Treino Trinca (Pedro Lotz)"
nicho: saude-estetica-fitness
sub_nicho: treino-em-casa
idioma: pt-BR
pais: BR
plataforma_ads: [meta]
checkout: hotmart
url_pagina: "https://treinotrinca.com.br/"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=Treino%20Trinca&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 37
ticket_bump: 0
ticket_upsell: 220
ticket_medio_est: 74
margem_est: 0.85
modelo: [quiz]
formato_entrega: [curso, comunidade]
tem_recorrencia: true
s_ticket: 7
s_lucro: 8
s_replica: 6
s_saturacao: 4
status: ativa
visto_primeiro: 2026-08-16
visto_ultimo: 2026-10-08
rodadas_vista: 7
dias_no_ar: 58
criativos_ultima: 210
criativos_delta: -20
unfunnelizer_capturado: false
ativos_pasta: "Ativos/treino-trinca"
gateways_detectados: [lastlink]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 41
ra_plataformas: [lastlink]
ra_primeira_reclamacao: 
ra_checado: 2026-10-08
veredito: observar
prioridade: 3
tags: [oferta, lowticket, marca]
---

# Treino Trinca (Pedro Lotz)

## Angulo
Desafio de treino em casa com rosto e nome do produtor (Pedro Lotz). Promessa de acesso completo por R$37 no criativo.

## Funil
anuncio -> VSL -> checkout Lastlink R$37 -> conteudo parcial entregue -> cobranca adicional para liberar o restante -> comunidade/assinatura com renovacao automatica.

## Por que funciona
O sinal mais forte da rodada inteira: 10 das 50 reclamacoes da Lastlink amostradas sao desta unica oferta, com grafias variadas (Treino Trinca, Projeto Trinca, Comunidade Trinca, Trica). Isso e volume de trafego pago real, nao ruido de suporte.

## O que copiar / o que evitar
Copiar: o corte de R$37 no front com o resto do conteudo atras de um segundo pagamento nao anunciado, e a renovacao automatica como terceira camada. Evitar: prometer 'acesso completo' no criativo se o acesso e parcelado - e o que gera a reclamacao e o chargeback.

## Estado dos dados
- **Confirmado:** existencia, gateway de checkout, contagem de reclamacoes em amostra de 10 paginas (10 mencao/mencoes).
- **Provisorio:** tickets e `s_ticket` quando o reclamante nao citou valor; `s_lucro` usa repeticao no Reclame Aqui como proxy, nao tempo no ar.
- **Faltando:** dias no ar, contagem de criativos, bump e upsell ocultos (unFunnelizer).

Evidencia: https://www.reclameaqui.com.br/lastlink/propaganda-enganosa-e-cobranca-adicional-no-treino-trinca-pedro-lotz_0Par4HkgvA-egMHX/

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

## Correção 2026-08-21 — dois produtores com o mesmo nome

Candidato: **`treinotrinca.com.br`** ("Trinca Turbo — Ative seu modo turbo em 4 semanas"),
listado na Hotmart como "Trinca Turbo – Nikolai Miranda"
(`hotmart.com/pt-br/marketplace/produtos/treino-trinca/U102658517X`).

Mas as reclamações no Reclame Aqui citam **"Treino Trinca Pedro Lotz"** com gateway
**Lastlink**. Ou a marca trocou de dono/gateway, ou são duas operações com o mesmo nome.
Marcado como **incerto** até abrir a página. Instagram: `@treinotrinca`.

## Rodada 2026-08-22 — o funil e quiz, nao venda direta

Reclamacao de 14/08/2026 (ID 256520497), dentro da janela ja amostrada em 16/08.
`ra_reclamacoes` permanece 10 — nao da para saber se estava na amostra de 10 paginas, e a
regra e nao contar sem certeza.

O que e novo e a anatomia: *"fiz a compra do treino trinca e **preenchi a avaliacao**, me
falaram que o treino estaria disponivel **apos 24 horas**"*. Ou seja:

    anuncio -> pagina -> checkout Lastlink -> formulario de avaliacao -> entrega em 24h

`modelo` corrigido de `[vsl]` para `[quiz]`. A avaliacao pos-compra faz duas coisas ao
mesmo tempo: justifica a promessa de personalizacao (e por isso permite ticket maior que
um PDF generico) e **compra 24 horas** antes de qualquer entrega, o que empurra parte dos
arrependimentos para fora da janela de impulso.

E o item mais copiavel do dia. Nao exige app, nao exige backend: e um Google Form entre o
checkout e o e-mail de entrega. Serve para qualquer oferta do vault que hoje entrega PDF
na hora — [[kit-so-escola-tdah]], [[planos-aula-infantil-500]], [[coletanea-regulacao-emocional]].

O que segura `treino-trinca` fora do corte de replicacao continua sendo `s_replica: 6`:
a oferta tem rosto (Pedro Lotz) e o rosto e parte da conversao.

Evidencia: https://www.reclameaqui.com.br/lastlink/atraso-na-liberacao-do-treino-e-falta-de-suporte_Pl3cl-kkgs0wZIsO/

## Rodada 2026-09-27

12 mencao(oes) nesta varredura (gateway Lastlink). Duas reclamacoes novas em 26/09 (IDs 260142269 e 260143667, acima do maior ID anterior 256520497); uma descreve a escada cobrada: R$ 110 + 67 + 37. Biblioteca de Anuncios em 27/09: ~91 anuncios ativos de Pedro Lotz (LP ltz.pedrolotz.online), o mais antigo carregado de 08/08.

Evidencia: https://www.reclameaqui.com.br/lastlink/quero-o-reembolso-do-programa-treino-trinca_d3v8u5FiwbakOPEJ/

## Medicao 2026-09-27 (rodada diaria, Biblioteca de Anuncios + RA Lastlink)
- Busca exata "treino trinca": **~91 anuncios ativos** de Pedro Lotz, LP `ltz.pedrolotz.online`, dois textos ("Participe do Desafio Treino Trinca... 28 dias" e "a metodologia que as famosas estao usando"). Das 30 carregadas, a mais antiga e de **08/08/2026** → `dias_no_ar: 50` (limite inferior; as outras 61 nao foram carregadas). Criativos novos de 17 a 23/09: esta escalando agora.
- Reclamacoes novas na Lastlink: IDs **260142269** e **260143667** (26/09), acima do maior ID anterior (256520497) → `ra_reclamacoes` 10 → 12. Uma descreve a escada efetivamente cobrada: **R$ 110 + 67 + 37**.
- `s_lucro` 9 → **8**: agora medido (45-90 dias, criativos subindo), mas 9-10 exige 90+ dias. O 9 anterior era palpite (ver adendo de 31/08 do Scoring.md).
- As reclamacoes estao na Lastlink, nao na Hotmart do `checkout`; nao troquei o `checkout` sem abrir a LP.

## Rodada 2026-10-02

17 mencao(oes) nesta varredura (gateway Lastlink). Cinco reclamacoes com ID novo em 01/10 (260567113, 260574045, 260577145, 260603667, 260606589), todas acima do maior ID de 27/09 (260143667). A 260606589 mostra a escada inteira: Desafio R$ 37 + programa R$ 220 + Plano Trinca/TF 1.000 R$ 997. Biblioteca em 02/10, busca 'treino trinca': ~130 resultados, so Pedro Lotz, mais antigo carregado 17/08, criativos novos ate 26/09 (busca diferente da de 27/09, nao serve para delta).

Evidencia: https://www.reclameaqui.com.br/lastlink/lista-reclamacoes/ (ID 260606589)

## Rodada 2026-10-05

31 mencao(oes) nesta varredura (gateway Lastlink). 14 reclamacoes com ID novo entre 02 e 04/10 nomeando o produto (260647273 a 260781237, todas acima de 260606589). Aparece a variante 'Treino Trinca Pink' (260705171) e o upsell 'Comunidade Trinca Elite' de R$ 237,78 que 'abate' a primeira compra (260735427). Biblioteca: busca 'treino trinca' foi de ~130 (02/10) para ~230 resultados, criativos novos ate 30/09.

Evidencia: https://www.reclameaqui.com.br/lastlink/lista-reclamacoes/ (IDs 260781237, 260775619, 260765001, 260749927, 260735427, 260730863, 260715579, 260713755, 260713585, 260711997, 260705171, 260701265, 260654909, 260647273)

## Medicao 2026-10-05 (rodada diaria, Biblioteca de Anuncios)

Mesma busca de 02/10 ("treino trinca", ativos, BR): **~230 resultados contra ~130**. Das 29 primeiras carregadas, 28 sao de Pedro Lotz, com inicios entre 22/08 e 30/09. `criativos_ultima: 230` e `criativos_delta: 100` comparam com os ~130 da mesma busca em 02/10, e nao com os 91 gravados em 27/09, que vinham de outra busca. `dias_no_ar: 58` conta a partir de 08/08, o anuncio mais antigo medido em 27/09, e continua sendo limite inferior. `s_lucro` continua 8: esta na faixa de 45-90 dias, e a faixa 9-10 pede 90 dias ou mais.

## Rodada 2026-10-08

41 mencao(oes) nesta varredura (gateway Lastlink). 8 reclamacoes com ID novo em 06-07/10, todas acima de 260842051 (maior de 05/10): 261097585, 261092767 (desafio R$ 37), 261088161, 261087345, 261079447, 261048213 (link do treino volta para a avaliacao), 261017573 (desafio de 28 dias nao entregue) e 260965163. Duas mostram degraus novos: 261087345 descreve RENOVACAO AUTOMATICA da assinatura Trinca Elite em 06/10 (o degrau de R$ 237,78 e recorrente) e 260965163 nomeia um 'kit Trinca Force'. Biblioteca, mesma busca de 02 e 05/10: ~210 resultados (eram ~230), 29 de 29 carregados de Pedro Lotz, mais antigo carregado 22/08, criativos novos em 03 e 04/10.

Evidencia: https://www.reclameaqui.com.br/empresa/lastlink/lista-reclamacoes/ (IDs 261097585, 261092767, 261088161, 261087345, 261079447, 261048213, 261017573, 260965163)

## Biblioteca 2026-10-08

Mesma busca "treino trinca" de 02 e 05/10: ~210 resultados (eram ~230, delta -20). 29 de 29 carregados de Pedro Lotz, o mais antigo carregado de 22/08, criativos novos em 03 e 04/10. `dias_no_ar` mantido em 58 (limite inferior; o anuncio de 08/08 nao apareceu na leva carregada, mas so 29 de ~210 carregaram).
