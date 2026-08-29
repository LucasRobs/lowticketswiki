---
tipo: oferta
classe: oferta
slug: certificado-curso-online
nome: "Certificado Curso Online — curso gratis, certificado R$ 139,90"
nicho: certificacao
sub_nicho: taxa-para-liberar-certificado
idioma: pt-BR
pais: BR
plataforma_ads: [google]
checkout: desconhecido
url_pagina: "http://certificadocursosonline.com"
url_ads: "https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=certificado%20curso%20online&search_type=keyword_unordered&media_type=all"
moeda: BRL
ticket_frente: 139.9
ticket_bump: 0
ticket_upsell: 0
ticket_medio_est: 139.9
margem_est: 0.95
modelo: [direct]
formato_entrega: [curso]
tem_recorrencia: false
s_ticket: 9
s_lucro: 4
s_replica: 5
s_saturacao: 4
status: nova
visto_primeiro: 2026-08-29
visto_ultimo: 2026-08-29
rodadas_vista: 1
dias_no_ar: 0
criativos_ultima: 0
criativos_delta: 0
unfunnelizer_capturado: false
ativos_pasta: "Ativos/certificado-curso-online"
gateways_detectados: []
bump_oculto: false
upsell_oculto: false
ra_reclamacoes: 58
ra_plataformas: []
ra_primeira_reclamacao:
ra_checado: 2026-08-29
veredito: observar
prioridade: 1
tags: [oferta, lowticket, certificacao]
---

# Certificado Curso Online — curso gratis, certificado R$ 139,90

Segundo maior volume do vault depois da [[alfabetinho]]: **58 reclamacoes ativas**. E a unica nota do dia com **ticket capturado**, porque um corpo diz o valor ao pe da letra: *"informando que e gratuito, mas na hora tem que pagar certificado. Paguei R$ 139,90"*.

## A mecanica, escrita pelos proprios reclamantes

O titulo da reclamacao mais util e literal: **"Cobranca indevida de certificado em curso anunciado como gratuito"**. O funil e:

1. Anuncio de curso **gratuito com certificado**
2. Aluno faz o curso inteiro (custo afundado, semanas de esforco)
3. Na emissao, o certificado e pago — R$ 139,90

O ponto de cobranca fica **depois** do investimento de tempo, nao antes do de dinheiro. E a versao educacional da "taxa pra liberar" que o `Pipeline.md` ja lista como a mecanica que faz o comprador brigar — e por isso deixa rastro no RA. Ver [[angulo-taxa-do-certificado]].

Distribuicao de problemas nas 58: **propaganda enganosa (20)**, outro problema (11), boletos (3). Categoria dominante: Cursos Livres (32). Nomes de curso citados nos corpos indicam catalogo largo e generico — "Historia da Velhice no Brasil" (com professora nomeada), "operador de empilhadeira".

## Volume alto, operacao fria

| Numero | Valor |
|---|---|
| **M** — ativas | 58 |
| **N** — recebidas em 01/02-31/07 | 3 |
| Mais recente | ha 2 meses |
| Respondeu | 0% |

`M − N` aqui nao mede aceleracao: mede **acumulo de anos**. Tres reclamacoes em seis meses contra 58 ativas e o padrao de desaceleracao que a [[alfabetinho]] tambem mostra, so que mais extremo. `s_lucro: 4`.

**Contraste util com a [[certifica-brasil]].** Mesmo nicho, mesma mecanica, sinais opostos: esta tem 4,5x mais volume historico e esta parada; a outra tem volume pequeno e esta acelerando ~3,8x. **Se o vault tivesse que apostar em uma, e na que esta esquentando** — o que e exatamente o que `s_lucro` (peso 35) deveria estar dizendo e nao diz, porque esta nota compensa com `s_ticket: 9`.

Vale registrar o efeito: esta nota marca **5,30** e a [[certifica-brasil]] marca **4,90**, ou seja o ranking coloca a operacao morta na frente da viva por causa de um ticket capturado por acaso. E o mesmo defeito que o Diagnostico do `Painel.md` chamou de anticorrelacao entre eixos, agora com um par limpo para ilustrar.

## O que copiar

O ponto de cobranca. Nao o produto — o **momento**. Cobrar depois do esforco investido, e nao antes, converte melhor que cobrar na entrada; o custo e que gera reclamacao, porque o comprador se sente enganado. Para uma replica limpa: **anunciar o preco do certificado desde o inicio** e manter o curso gratuito de verdade. Perde-se parte da conversao por surpresa e ganha-se a operacao que nao vive de churn.

## Estado dos dados

- **Confirmado:** volume (58), ticket (R$ 139,90), mecanica, mix de problemas, site (`certificadocursosonline.com`).
- **Faltando:** gateway, `dias_no_ar`, se ha bump/upsell (a carteirinha citada na [[certifica-brasil]] sugere que o padrao tem upsell).

Pagina do produtor: https://www.reclameaqui.com.br/empresa/certificado-curso-online/lista-reclamacoes/

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
