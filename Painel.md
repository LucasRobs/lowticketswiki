---
tipo: painel
atualizado: 2026-10-02
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-10-02 (rodada diaria)

Passada: [[2026-10-02 -- 0102]] · nota do dia: [[2026-10-02]].

**199 notas · 174 ofertas · 25 ângulos · 6 novas hoje · 12 vistas hoje · status: 79 nova · 44 ativa · 31 esfriando · 45 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Cinco dias sem nada gravado.** A rodada anterior foi a de 27/09. Entre 27/09 e 02/10 as passadas 6x/dia não deixaram nenhuma nota em `Radar/rodadas/`, nem passada vazia. Ou não rodaram, ou gravaram só na fila do Projeto Claude. O buraco aparece no dashboard como ausência, não como "sem-coleta". Antes de culpar o mercado por qualquer silêncio nesse intervalo, alguém precisa olhar a fila.

**O instrumento melhorou de novo.** Em 27/09 o `?pagina=2` voltava vazio. Hoje, clicar no número da página dentro do navegador interno troca a lista, e o corpo de cada reclamação abre por `fetch` na mesma origem, com ID e carimbo. Foram 26 páginas em 10 gateways (Kiwify, Hotmart, Ticto, Eduzz, Monetizze, Lastlink, Wiapy, Payt, Kirvano, Lowify), cerca de 150 corpos lidos, quase todos de 30/09 e 01/10. A Biblioteca de Anúncios abriu sem aprovação para 5 consultas. Ressalva: o Meta anunciou pausa de anúncios políticos no Brasil de 2 a 5/10. Não afeta infoproduto, mas pode deixar a Biblioteca mais ruidosa nesses dias.

**Sinal novo real: sim, concentrado em três notas que já existiam.** Todas tinham `status: ativa`, então não contam como "retorno".
- [[treino-trinca]] ganhou **5 reclamações com ID novo** num dia (260567113 a 260606589, todas acima de 260143667), de 12 para **17**. Uma delas mostra a escada inteira: Desafio **R$ 37 → programa R$ 220 → Plano Trinca/TF 1.000 R$ 997**. O degrau de R$ 997 não aparecia em nenhuma leitura anterior. `ticket_upsell` passou de 37 para 220, e o `ticket_medio_est` ficou como estava porque a taxa de aceitação não é conhecida. A busca "treino trinca" na Biblioteca dá ~130 anúncios, só de Pedro Lotz, com criativos novos até 26/09. A busca de 27/09 foi outra, então não há `criativos_delta` honesto. Score continua **6,60**.
- [[chatgpt-privado]] saiu de 1 para **5**: quatro reclamações em 01/10 nomeiam o produto ou o vendedor (Infinity Apps), e há mais duas prováveis que não foram contadas. A mecânica se repete: o "anual" vira Pix automático mensal. A Biblioteca mostra o que está por trás: **~120 anúncios de "ChatGPT anual", todos iniciados entre 27 e 30/09, vários anunciantes a R$ 21,90.** É uma coorte que nasceu na semana do buraco. Com medição, `s_saturacao` foi para 2 e `s_replica` para 2 (revenda de acesso de terceiro), e o score ficou em **3,00**. Mostra onde há verba, não o que copiar.
- [[app-do-paizao]] subiu de 3 para **5**. A reclamação 260569507 descreve uma mecânica nova: o comprador apertou o botão "reembolse aqui" e caiu uma cobrança de **R$ 284,90**. Se o relato estiver certo, é upsell de um clique disfarçado de reembolso. Ainda é um relato só.

**Estreias: 6, e uma com longevidade medida.** O **Achados da Ellen** (Kiwify) é um perfil de achadinhos ("comenta eu quero") com anúncio ativo desde **01/08 (62 dias)**. O perfil vende um treinamento de R$ 67 e um grupo por assinatura em Pix automático de R$ 49,90. Foi medido com `s_lucro: 6`, não 7, porque o anúncio vende o achadinho e não a oferta. Score **3,70**, provisório (`s_replica` e `s_saturacao` seguem na sentinela). O **Date Nights Cristão** (Payt, R$ 42, 2 reclamações) encosta no cluster religioso/casal e não tem anúncio ativo com o nome exato. Também estrearam **Coramaflix** (Lowify), que cobra taxa por episódio depois da mensalidade e era o "coramafix" que ficou como sinal fraco em 27/09; **+100 Projetos de Parquinho** (Wiapy, R$ 25,90), PLR de marcenaria com um irmão na Lowify; **SerBene** (Hotmart), R$ 9,90 que vira R$ 59,90 no terceiro mês; e **Seu Curso Viral em 1 Dia** (Kiwify, R$ 47 + 27).

**Mecânica de funil: o preço que muda depois da compra.** SerBene (9,90 → 59,90), ChatGPT "anual" que vira mensal, o Pix automático do grupo da Ellen, a taxa por episódio da Coramaflix e o botão de reembolso do Paizão são a mesma família. O ticket de frente é isca e o valor real está numa cobrança recorrente ou escondida, que a LP não mostra. É o mesmo campo que 27/09 chamou de "venda depois da venda", agora no lado da recorrência. Na Wiapy apareceu outra variante: um checkout com **quatro produtos extras** oferecidos na compra (260571759), ou seja, bump múltiplo em ticket de R$ 20-30.

**Status (decaimento à mão, só nos 10 gateways varridos hoje e só em notas vindas do RA).** **11 estreias de 27/09** que não reapareceram passaram de `nova` para `ativa` (uma rodada de ausência é cobertura). **6 estreias de 24/09** (carteira do estudante, comunidade renda em dólar, divas milionárias, mentoria VPJ, método gringa turbo, protocolo leite sem fim) estão na segunda rodada sem aparecer e foram para `esfriando`. Gerachat e White Driver foram **avistadas**: a mesma reclamação relida na primeira página da Ticto. Atualizaram `visto_ultimo` sem mover a contagem. As notas de dança, parentalidade e infantil desses gateways **não** foram tocadas, porque vieram da Biblioteca e a lista do RA não as mede. As `esfriando` de agosto também ficaram como estavam: a conta de rodadas por gateway desde então dá 5 ou 6, e não dá para afirmar 7.

**Cuidados.** Ler cinco dias de buraco numa noite só infla o "sinal do dia". As 5 reclamações do Treino Trinca e as 4 do ChatGPT Privado são de 01/10, mas foram vistas pela primeira vez hoje porque ninguém olhou antes. Isso mede acumulado, não aceleração. A estreia "Date Nights" usa o nome que o comprador escreveu, e o nome comercial pode ser outro. **73 notas continuam `nova` depois da estreia** (o aviso do `--verificar`), e 13 notas violam o teto de `s_lucro` sem insumo de longevidade. As duas dívidas são as mesmas de 27/09.

**Autocrítica.** O resumo da passada saiu primeiro com "7 novas, 3 retornos". Eram 6 novas e zero retornos, porque as três notas com ID novo já estavam `ativa`. Foi corrigido antes do commit do Painel. É o mesmo vício de 31/08: narrar antes de computar.

---

## Leitura anterior — 2026-09-27 (rodada diaria)

Passada: [[2026-09-27 -- 0113]] · nota do dia: [[2026-09-27]].

**193 notas · 168 ofertas · 25 ângulos · 14 novas hoje · 16 vistas hoje · status: 87 nova · 36 ativa · 25 esfriando · 45 morta · 1 no corte ([[little-genius]], 7,60)**

**O instrumento mudou nesta rodada.** O WebFetch leva 403 no Reclame Aqui, mas o navegador interno abre a lista e os corpos sem pedir aprovação, e a Biblioteca de Anúncios também abriu sem aprovação. Com isso a rodada cobriu os dez gateways que as passadas 6x/dia não varrem (Kiwify, Hotmart, Ticto, Eduzz, Monetizze, Lastlink, Wiapy, Payt, Kirvano, Lowify), cerca de 50 corpos lidos com ID. Ainda é só a primeira página (5 por gateway, carimbos de 23 a 27/09): o `?pagina=2` volta vazio porque a lista é montada no cliente. Hubla não tem página no RA com os slugs tentados. Os slugs que funcionam são `kirvano-pagamentos` e `lowify-tecnologia`.

**Sinal novo real: dois retornos, os dois com longevidade medida.** [[treino-trinca]] ganhou duas reclamações com ID novo na Lastlink (260142269 e 260143667, contra o maior anterior de 256520497), e uma delas mostra a escada cobrada: **R$ 110 + 67 + 37**. Na Biblioteca são **~91 anúncios ativos** de Pedro Lotz, o mais antigo carregado de 08/08, e criativos novos todo dia entre 17 e 23/09. É a primeira vez que o vault mede escala nessa nota. [[app-do-paizao]] teve uma reclamação nova (260146503) que descreve a mecânica: frente de R$ 47 e, depois da compra, um vídeo vendendo 12x R$ 19 com a promessa de "devolver os 47". Os anúncios de Carlão Silva estão no ar desde 04/08.

**A correção honesta vem junto.** O `s_lucro: 9` do Treino Trinca era palpite e caiu para **8** agora que foi medido (50 dias é limite inferior, e 9-10 pede 90+). O score foi de 6,95 para **6,60**. A nota que o Painel de 29/08 chamou de "teto das ofertas reais" continua abaixo do corte, agora por medição e não por chute. O Paizão subiu de `s_lucro` 5 para 7, mas o `s_replica: 3` o mantém em 5,75.

**Estreias: 14, e só uma com longevidade.** O **Ateliê das Velas** (Kiwify, R$ 47, curso de velas artesanais) tem anúncios desde **17/06, 102 dias**, e vende subprodutos dentro da área de membros. Encosta no cluster de artesanato de [[angulo-artesanato-moldes-pdf]]. Aparece como "descartar" (5,50) só porque `s_saturacao` segue em 0, a sentinela. É a primeira candidata a uma busca pelo ângulo "velas artesanais" na Biblioteca. As outras 13 são uma menção cada, sem medição. A Wiapy confirma que é o gateway do ticket de R$ 10-20: +100.000 Manuais Técnicos a R$ 17, Doramas Hot Vitalício (mesmo cluster de [[angulo-streaming-doramas-turcas]]), Manual do Shihtzu e Descobrindo o Porquê da Fé. Em IA/automação há ChatGPT Privado (Kirvano, que exige e-mail novo todo mês), Gerachat e Luke ZAP (Ticto): é a saída travada de PerfectPay/Cakto em outro gateway.

**Mecânica de funil que se repetiu fora de PerfectPay/Cakto: a venda depois da venda.** Paizão (vídeo pós-compra com 12x R$ 19), Beautifycursos (vídeo pós-pagamento diz que "só esse curso não dá resultado" e vende o segundo), Protocolo Natural da Diabetes (R$ 18,50 + "desconto de 50%" + mais cursos na mesma compra) e Treino Trinca (três cobranças). Nenhuma dessas escadas aparece na LP. Continuam sendo o campo `ticket_upsell` que só a Etapa 2 captura.

**Status.** Seis estreias de 24/09 vindas do RA de Monetizze, Kiwify, Eduzz e Ticto passaram de `nova` para `ativa` (uma rodada de ausência na primeira página é cobertura, não esfriamento). As notas de dança, parentalidade e infantil desses mesmos gateways **não** foram decaídas: vieram da Biblioteca, e a primeira página do RA não é instrumento para elas. **73 notas continuam `nova` depois da estreia.** É dívida do contrato, e não se paga sem uma passada de manutenção pela Biblioteca.

**Cuidados.** `dias_no_ar` de Treino Trinca e Paizão é limite inferior: só a primeira leva de anúncios carregou (30 de ~91; 8 numa busca larga por "paizão"). Os `criativos_ultima` também são contagens parciais e não servem de base para `criativos_delta` sem repetir a mesma busca. Nenhuma das 14 estreias teve LP aberta.

---

## Leitura anterior — 2026-09-26 (rodadas agendadas de 22 a 26/09)

Lista completa, separada pelo que fazer: [[2026-09-27 -- novidades-22-a-26-09]].

**172 notas · 147 ofertas · 25 ângulos · 41 notas novas entre 24 e 26/09 · status: 72 nova · 25 ativa · 27 esfriando · 48 morta**

As passadas agendadas de 24, 25 e 26/09 gravaram só no Projeto Claude. Em 27/09 foram trazidas para cá pelo `sync_vault.py` (nota do dia em `Radar/`, snapshots em `Observacoes/`, notas em `Ofertas/`) e cada passada ficou arquivada em `Radar/rodadas/`. Dos 41 achados novos, 15 vieram de gateways que a automação nunca tinha varrido (Kiwify, Hotmart, Ticto, Eduzz, Monetizze) — e nenhum se sobrepõe ao portfólio de PerfectPay/Cakto.

**O que a semana disse.** Em PerfectPay/Cakto o que se repetiu não foi um produto, foi uma mecânica: saída travada. [[angulo-assinatura-com-cancelamento-bloqueado]], [[luna-ia]] (cobra para excluir a conta), [[trendy-ia]], [[livego-pro]] e [[lumi-ai]] são a mesma engrenagem com nomes diferentes; [[angulo-cobranca-extra-para-liberar-acesso]] e as três cobranças por função da [[stalkeia-ai]] são a versão de entrada. Em Kiwify/Hotmart domina assinatura, com trava anti-reembolso desenhada ([[hap-2-0]]). Quase tudo isso é golpe ou suporte fantasma: mostra onde há verba, não o que copiar.

**O que vale replicar continua no mesmo cluster.** As únicas estreias com entregável em arquivo foram [[900-mapas-mentais]] e [[caderno-de-professor]], e o crochê voltou em [[angulo-artesanato-moldes-pdf]] — todos encostados no material pedagógico/imprimível, o cluster com escala medida ([[2026-09-26 -- ofertas-escaladas]]).

**Cuidados com os números.** A listagem "ativas" do Reclame Aqui não é cronológica: a passada de 25/09 17h leu reclamações de julho e agosto, e várias ofertas "persistentes" são a mesma reclamação relida ([[lumi-ai]] não teve reclamação nova desde 20/08). Nenhuma das 41 notas novas tem `dias_no_ar` ou criativos medidos, então `s_lucro` ficou no piso conservador e `s_replica`/`s_saturacao` em 0 (sentinela). 15 notas estão com `checkout: desconhecido` porque a passada de Kiwify/Hotmart não separou os dois. A passada de 26/09 22h15 não coletou nada.

---

## Leitura anterior — 2026-09-11 · parentalidade, TEA e TDAH (rodada dirigida)

**Rodada dirigida: 7 novas ofertas, 3 revisitadas e 10 snapshots.** Relatório: [[2026-09-11]].

Prioridades por aderência: [[31-segredos-pais-tdah]] para TDAH e escola; [[tdah-tod-paula-frati]] para conflitos familiares; [[autismo-para-pais-lacerda]] para organização parental; [[meu-filho-e-unico-horleana]] e [[parentalidade-atipica-sarah-hayden]] para TEA + TDAH.

[[tea-sem-crise]] tem quatro anúncios ativos observados, pelo menos três vídeos distintos e anúncio desde 12/08; frente capturada em R$71. Os dois kits Só Escola responderam nesta consulta, por R$47 (TDAH) e R$37 (autismo). Não são manuais de parentalidade.

A Biblioteca de Anúncios funcionou nesta rodada. Ainda faltam métricas de tráfego para a maioria das ofertas; lucro não foi medido. **Scores e decisões automáticas nas Bases abaixo continuam provisórios quando faltam dados.** As outras ofertas não foram reclassificadas por falta de cobertura.

---

## Ranking — ofertas reais

Só `classe: oferta`. Ângulo tem tabela própria mais abaixo: ele não tem produtor, gateway
nem ticket, então não pode disputar o corte de replicação com uma oferta concreta.

```base
filters:
  and:
    - note.tipo == "oferta"
    - note.classe == "oferta"
formulas:
  score: (note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100
  decisao: if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 7.5 && note.s_replica >= 7, "REPLICAR", if((note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100 >= 6, "observar", "descartar"))
properties:
  file.name:
    displayName: Oferta
  formula.score:
    displayName: Score
  formula.decisao:
    displayName: Decisao
views:
  - type: table
    name: Ranking
    order:
      - file.name
      - formula.score
      - formula.decisao
      - nicho
      - checkout
      - ra_reclamacoes
      - dias_no_ar
      - status
    sort:
      - property: formula.score
        direction: DESC

```

## Padrões (ângulos)

Nota de ângulo é **padrão sem dono**. A métrica útil aqui não é o score composto — é quantas
ofertas nomeadas já foram ligadas ao padrão. Zero operador = hipótese. Dois ou mais = padrão
confirmado, e aí a próxima rodada procura produtor *no nicho* dele (Etapa 3b, porta de fora).

```base
filters:
  and:
    - note.tipo == "oferta"
    - note.classe == "angulo"
formulas:
  score: (note.s_lucro * 35 + note.s_replica * 30 + note.s_ticket * 20 + note.s_saturacao * 15) / 100
properties:
  file.name:
    displayName: Ângulo
  formula.score:
    displayName: Score
views:
  - type: table
    name: Padroes
    order:
      - file.name
      - formula.score
      - nicho
      - sub_nicho
      - s_replica
      - s_saturacao
      - status
    sort:
      - property: formula.score
        direction: DESC
```

## Acelerando

Quem ganhou criativos desde a rodada anterior. **Esta é a tabela que vale dinheiro** —
o topo do ranking diz o que é bom, esta diz o que está esquentando *agora*.

```base
filters:
  and:
    - 'note.tipo == "oferta"'
    - 'note.classe == "oferta"'
    - 'note.criativos_delta > 0'
views:
  - type: table
    name: Acelerando
    order:
      - file.name
      - note.criativos_delta
      - note.criativos_ultima
      - note.dias_no_ar
      - note.nicho
    sort:
      - property: note.criativos_delta
        direction: DESC
```

## Fila de captura

Ofertas com sinal mas sem o unFunnelizer rodado. Enquanto estiverem aqui, os tickets
delas são estimativa.

```base
filters:
  and:
    - 'note.tipo == "oferta"'
    - 'note.classe == "oferta"'
    - 'note.unfunnelizer_capturado != true'
views:
  - type: table
    name: Fila
    order:
      - file.name
      - note.url_pagina
      - note.checkout
      - note.ra_reclamacoes
      - note.dias_no_ar
    sort:
      - property: note.ra_reclamacoes
        direction: DESC
```

## Rodadas

```base
filters:
  and:
    - 'note.tipo == "radar"'
views:
  - type: table
    name: Rodadas
    order:
      - file.name
      - note.ofertas_vistas
      - note.novas
      - note.retornaram
      - note.sumiram
    sort:
      - property: note.data
        direction: DESC
    limit: 30
```

---

## Diagnóstico do instrumento

Rodado em 2026-08-16 sobre as 6 primeiras ofertas. **O score composto está compactando
o sinal em vez de separá-lo.**

| Eixo | Amplitude |
|---|---|
| s_ticket | 6,00 |
| s_saturacao | 5,00 |
| s_replica | 4,00 |
| s_lucro | 3,00 |
| **score final** | **0,80** |

Seis ofertas muito diferentes em cada dimensão colapsam entre 6,00 e 6,80. Causa: os
eixos são anticorrelados na prática — ticket alto vem com nicho lotado, replicabilidade
fácil vem com ticket baixo — e a soma ponderada faz eles se anularem.

Correlação de cada eixo com o score final:

| Eixo | Peso | r com o score |
|---|---|---|
| s_replica | 30 | **+0,73** |
| s_saturacao | 15 | +0,33 |
| s_lucro | **35** | **−0,19** |
| s_ticket | 20 | −0,20 |

`s_lucro` tem o maior peso e influência praticamente nula. **Peso só funciona se a
variável variar** — e `s_lucro` ficou espremido entre 5 e 8 porque, sem biblioteca de
anúncios, as seis foram pontuadas pelo mesmo proxy magro.

**Correção proposta:** média geométrica ponderada no lugar da soma. A soma deixa um eixo
forte compensar um eixo quase zerado; a geométrica pune o elo fraco. Nos dados atuais
separa 1,4× melhor e joga `lowify-app-historias` de 3º para último — correto, porque
R$19 em campo lotado não é a terceira melhor oportunidade por mais fácil que seja.

Enquanto a fila de captura não esvaziar, **trate o ranking como ordem de investigação,
não como ordem de decisão.**

## Mesa de Garimpo — links de todas as ofertas (2026-08-21)

Página com as 57 ofertas do vault, cada uma com **página de vendas** e **busca pronta na
Biblioteca de Anúncios**. Filtros por nicho, veredito, "só com página" e "2+ rodadas".

https://claude.ai/code/artifact/a9f45cac-2553-48ec-8e9b-f86fdb7ec13f

Fonte dos dados: `_arquivo/exports-antigos/ofertas-export-2026-08-21.json` — foto de 21/08,
congelada. **Substituída pelo dashboard** (`dashboard/`, publicado na Vercel), que lê todas as
notas e se atualiza sozinho a cada mineração publicada: ver [[dashboard/README|Dashboard]].
