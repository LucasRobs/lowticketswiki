---
tipo: painel
atualizado: 2026-09-27
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-09-27 (rodada diaria)

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

## Leitura anterior — 2026-08-31 (segunda passada)

**110 notas · 91 ofertas · 19 angulos · 0 novas nesta passada · 1 no corte de replicacao**

Duas passadas hoje. A da manha varreu o nicho infantil pela Biblioteca de Anuncios e trouxe quinze
notas; esta executou a fila que ela deixou. **A Etapa 1 nao estava disponivel aqui** — o navegador
interno recusou `facebook.com` duas vezes e o claude-in-chrome segue vazio. O adendo da manha
descreve um procedimento que custa 2-3 aprovacoes por termo, e **aprovacao pressupoe o Lucas na
frente da tela**: a Etapa 1 pelo navegador interno e ferramenta de rodada assistida, nao de rodada
agendada. A cadencia diaria que a manha declarou restaurada vale so para as passadas acompanhadas.

**A correcao que importa: as duas rodadas anteriores relataram o corte sem calcular o corte.** A
manha abriu anunciando o primeiro cruzamento de sempre — [[little-genius]], 7,60. Mas [[soulmate-sketcher]]
(7,85) e [[retrato-da-alma-gemea]] (7,65) ja cruzavam, e as duas nasceram em **30/08** — rodada que
fechou o texto dizendo "decimo dia de zero no corte". O corte e uma formula sobre o frontmatter e
ninguem a estava rodando; a narrativa vinha da memoria do que tinha acabado de ser escrito. Regra
nova de processo: **computar o ranking antes de narrar**, toda rodada.

**Auditadas, as duas caem — e pelo mesmo vicio, nos dois eixos de maior peso.** A soulmate marcava
`s_lucro: 9` com `dias_no_ar: 0`, `criativos_ultima: 0` e `ra_reclamacoes: 0`, e o corpo da nota
escrevendo *"so a Biblioteca de Anuncios mede"* — declarou nao ter instrumento e cravou o maximo do
eixo de peso 35. O retrato marcava `s_saturacao: 8` com a prosa da propria nota dizendo *"ha dezenas
de clones"*; ali nem faltava dado, faltava ler. Corrigidas para 6,10 e 6,40. **Isso inverte o
diagnostico de 29/08:** campo faltando nao empurra o score para baixo, empurra para onde quem
preencheu quis — e quem preenche acabou de gastar meia hora se convencendo de que a oferta e boa.
Hoje **22 ofertas** tem `s_lucro >= 5` sem nenhum insumo de longevidade e **14** tem `s_lucro >= 7`
nas mesmas condicoes, entre elas [[treino-trinca]], a nota que o Painel de 29/08 citou como "o teto
das ofertas reais". O teto era ele proprio um palpite. Regra nova no `Scoring.md`: **`s_lucro >= 7`
exige `dias_no_ar > 0` ou `ra_primeira_reclamacao`; sem isso o teto e 6** — aplicada so onde muda
veredito, para nao trocar um palpite por outro em lote.

**De medicao de campo, o angulo de alma gemea:** tres paginas de produtor no Reclame Aqui,
`retrato-da-alma-gemea` (M=206, N=21, mais recente ha 16 dias), `alma-gemea` (M=19, N=2, ha 3 meses)
e `desenho-da-alma-gemea` (M=16, N=0, ha 1 ano), mais Marcia Sensitiva, Mestre Zion, Aurara Vidal e
Alma Gemea Chay soltos nos corpos. **Seis operadores nomeaveis, um vivo** — e as 206 reclamacoes do
sobrevivente sao de nao-entrega. Mesma forma do achado da manha sobre bonecas de papel: o ativo
circula pronto, os clones sao muitos, e **o que separa vivo de morto nao e a copy, e a entrega.**
Proxima passada precisa ser **assistida**, para os tres itens de browser que ficaram na fila.
Distribuicao final: **52 morta · 29 esfriando · 20 nova · 9 ativa**.
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
