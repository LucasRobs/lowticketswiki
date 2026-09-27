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
ticket_upsell: 37
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
visto_ultimo: 2026-09-27
rodadas_vista: 4
dias_no_ar: 50
criativos_ultima: 91
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/treino-trinca"
gateways_detectados: [lastlink]
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 12
ra_plataformas: [lastlink]
ra_primeira_reclamacao: 
ra_checado: 2026-09-27
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
