---
tipo: painel
atualizado: 2026-10-19
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-10-19 (rodada diaria)

Passada: [[2026-10-19 -- 1434]] · nota do dia: [[2026-10-19]].

**473 notas · 375 ofertas · 98 ângulos · 3 novas hoje · 26 vistas hoje · status (todas): 114 nova · 119 ativa · 197 esfriando · 43 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Cinco dias sem rodada completa, e o que chegou nesse meio foi a passada leve.** A última leitura com a lista inteira do RA foi a de 14/10 às 17h38. Entre ela e hoje rodaram **24 passadas 6x/dia** (15 a 18/10), num clone separado que só entrou no `main` com o merge de 18/10 (`80677a4`). Com o merge entraram 69 notas, 36 delas estreadas entre 15 e 18/10. É isso que explica o salto de 401 para 473. Mas essas passadas usam busca por título e página do RA, e as próprias notas delas registram **paginação travada e primeira página congelada desde 04/10**: a de 18/10 às 07h17 releu as mesmas reclamações de 17/10. Desde 07h17 de 18/10 não houve passada. Esta rodada rodou às 14h34 de 19/10, não às 23h30. Usou **a API de busca do RA** de dentro da aba do navegador interno, nos **11 gateways** de sempre, em 94 páginas: **869 reclamações únicas**, todas criadas entre 14/10 17h38 e 19/10 14h25, sem buraco. A Biblioteca abriu sem aprovação para 3 buscas.

**Antes de somar: o merge de 18/10 regrediu cinco contagens.** Na reconciliação das duas linhas de histórico, `ra_reclamacoes` voltou ao valor anterior a 14/10 em [[zap-radar]] (45 → 26), [[stalkeia-ai]] (36 → 28), [[fornece-up]] (16 → 8), [[app-direct-line]] (11 → 5) e [[comunidade-mvz]] (3 → 1). Os outros campos ficaram certos. As quatro primeiras foram corrigidas pelo próprio `max()` do `sync`, porque o JSON desta rodada leva o total acumulado. A [[comunidade-mvz]] não teve ID novo e foi corrigida à mão. Conferi as 470 notas contra o `main` de antes do merge (`3a84b1d`), e só essas cinco tinham caído.

**Sinal novo real: sim, e é o mesmo grupo de sempre, maior.** São sete notas com 5 IDs novos ou mais:
- [[treino-trinca]] teve **17 IDs novos e foi de 69 para 86**. Dez deles são de **18/10**, o maior volume em um dia já medido em uma nota. A média de ~3,4 por dia é menor que os ~6 por dia de 11-14/10. O pico é de sábado. Os corpos repetem a escada: R$ 37 que não entrega o "plano personalizado", questionário de avaliação que não fecha (261944925) e o **Trinca Force de R$ 997**, vendido com desconto de sorteio (261963675). Na Biblioteca, com a mesma busca, foram **~150 resultados (eram ~210 em 14/10)**. Os 28 carregados são todos de Pedro Lotz, e o mais novo começou em **09/10**. A queda bate com o adendo de 31/08: ninguém mantém verba por 58 dias numa oferta que não paga, mas ela está **reduzindo a verba enquanto as reclamações sobem**. `criativos_ultima` foi de 210 para 150. Atenção: a Biblioteca agora abre ordenada por impressões, então "mais novo carregado" deixa de ser comparável com as leituras anteriores.
- [[zap-radar]] teve **21 IDs novos e foi de 45 para 66**: 18 na Payt e 3 na PerfectPay. Uma reclamação (261923227) diz o que o produto é: "dizia ter acesso às mensagens, mas na verdade é um curso". Os preços citados são R$ 67, R$ 97 e R$ 137. Ficaram fora da conta 2 do "Manual da Verdade" e cerca de 5 de "relatório" de R$ 137 sem nome.
- [[shopminer]] teve **10 IDs novos e foi de 21 para 31**. [[stalkeia-ai]] teve 9 e foi de 36 para **45**. [[app-direct-line]] teve 9 e foi de 11 para **20**, quase tudo cancelamento de assinatura sem resposta. Uma delas confirma "Direct Line + IA Larissa para WhatsApp". [[tokscale-ia]] teve 7 e foi de 8 para **15**, cinco delas em 15/10.
- [[app-do-paizao]] teve **5 IDs novos e foi de 20 para 25**. Na Biblioteca há **criativos novos de 16/10**, depois de 11 e 14/10 sem rotação. São ~12 anúncios de Carlão Silva nos 5 cartões carregados.
- Mornas: [[fornece-up]] 16 → 21, [[irryss]] 8 → 11, [[pilates-na-parede-lastlink]] 8 → 10, [[malu-sua-assistente]] 8 → 10, [[renda-fortuna]] 5 → 8, [[receitas-sem-pensar]] 5 → 7, [[spinmaster]] 3 → 6, [[escola-de-personagens]] 4 → 6, [[cao360]] 3 → 6 (a segunda reclamação da Payt cita o "Cão Blindado", o degrau seguinte), [[movimento-prosperas-luana-bittencourt]] 3 → 5, [[anunciaie]] 2 → 4 e [[trendly]] 1 → 3.

**Estreias: 3, e só uma tem corpo.** Somei as menções desta rodada às da fila de 14/10, como em 14/10:
- [[crie-ai]] (Cakto, 6 menções). É um gerador de sites com IA vendido como "criação ilimitada", num **plano vitalício de R$ 297,99** com garantia de 15 dias. Na prática, limita o número de sites e cobra créditos de IA à parte. Uma reclamação (261809083) chama isso de "venda casada de créditos". As compras vão de 03 a 13/10. Na Biblioteca, "crie.ai" só devolve ruído. Não é a [[criaai]] (Ticto, 1 menção vaga).
- [[ht-secar-sem-dieta]] (Hotmart, 3). Programa de emagrecimento em 9x com **renovação anual automática** que a compradora não percebe. Uma delas comprou em outubro de 2025 e diz que soube pelos "relatos anteriores". O corpo já dá a idade: a operação tem pelo menos um ano. `ra_primeira_reclamacao` não foi preenchido, porque a reclamação de 2025 não foi lida.
- [[treino-da-fera]] (Payt, 3). Treino de R$ 67 no Pix, com uma "Fera de Elite" de R$ 100. É a mesma escada do Trinca em escala menor.

Ficaram na fila, com 2 menções cada: Curso VOE da Isa Elias (Kiwify), Shape 3D do Breno Aceti (Kiwify), Dark Planner (Cakto, assinatura que continua cobrando), Ferramentas Guru (Cakto, R$ 67), Nova Renda em Dólar (Cakto, R$ 497), Ecossistema do Low Ticket (Payt), Payt Academy (Payt), CTRL IA (Payt), Viver de Produtos Digitais (Hotmart, 10x no Pix), a dieta hormonal da Marina Cardoso (Hotmart) e a Biblioteca Digital (Cakto).

**Retornos: 2, ambos fracos.** [[o-truque-da-loto-pro]] (Payt) voltou de `esfriando` com 2 IDs, e [[luna-ia]] (PerfectPay) com 1.

**Mecânica de funil.** Dois padrões se repetiram, e um apareceu. (1) **O preço real depois da frente**: Trinca Force (R$ 997), Cão Blindado, Fera de Elite e os créditos de IA do Crie AI. (2) **Assinatura que o comprador não sabe que é assinatura**: Direct Line, Dark Planner, Ferramentas Guru e Secar Sem Dieta, em três gateways. Isso fora as dezenas de "renovação automática sem aviso" sem nome de produto na Hotmart e na Lastlink. É o mesmo vício de [[angulo-renovacao-automatica-indevida-de-assinatura-curso]], agora com nome de produto. (3) Novo: **"gerador ilimitado" com limite**. O Crie AI vende vitalício e cobra o uso, o que é a versão SaaS do "taxa para liberar".

**Status (decaimento à mão, só nos 11 gateways varridos, mesmas exclusões de 14/10).** São **37 mudanças**. **22 notas** sem aparição desde 13/10 ou antes ficaram de fora das duas leituras completas (14/10 e hoje) e foram para `esfriando`: 16 eram `ativa` e 6 ainda eram `nova`. Entre elas estão Thermafit App, Viva de Martelinho de Ouro, Auks Bot, Arsenal Lucrativo, Muscleflix, Livego Pro e Sora. **15 notas** vistas pelas passadas de 14 a 17/10 passaram de `nova` para `ativa`, porque `nova` só vale na estreia. Ficaram de fora, de propósito, as duplicatas `escola-de-personagem`, `stalkea-ai`, `stalker-ai` e `loopzy`, e também [[chatgpt-privado]], que tem anúncio medido. Nenhuma nota foi para `morta`.

**Cuidados.** (1) As contagens das passadas de 15 a 18/10 **não entram na soma**. Elas leem a página 1 congelada e não registram ID, então não há como saber se reclamação contada lá é nova. As notas que só elas tocaram têm `ra_reclamacoes` de passada leve. (2) O salto de 401 para 473 notas é **o merge das passadas**, não mercado. (3) Score não mudou em nenhuma nota quente. ShopMiner (0,70), Direct Line (1,75), TokScale (1,75) e Fornece Up (2,15) continuam em "descartar" com 15 a 31 reclamações em uma semana e meia. O Crie AI estreia em "descartar" (3,75) com o maior ticket do grupo. A rubrica não pontua volume sem longevidade. (4) O commit da passada levou junto uma mudança local em `.obsidian/graph.json`, que já estava no checkout antes da rodada.

**Autocrítica.** O instrumento funcionou e a leitura é comparável à de 14/10. Mas a rodada ficou, de novo, **só na Etapa 3**. A pendência das últimas quatro leituras continua aberta: **a API nas páginas de produtor (Etapa 3b)**, para medir `ra_primeira_reclamacao` do Trinca, do Zap Radar e do Paizão. O Secar Sem Dieta mostrou que o corpo da reclamação às vezes já traz a idade. Também ficou sem resposta por que **as passadas 6x/dia continuam rodando contra uma página congelada há duas semanas**: são 24 passadas em quatro dias que quase não acrescentam sinal, e a correção é trocar o instrumento delas pela API, não aumentar a cadência.

---

## Leitura anterior — 2026-10-14 (rodada diaria, complemento das 17h38)

Passadas: [[2026-10-14 -- 0154]] e [[2026-10-14 -- 1738]] · nota do dia: [[2026-10-14]].

**401 notas · 329 ofertas · 72 ângulos · 0 novas nesta passada (3 no dia) · 23 vistas no dia · status: 98 nova · 79 ativa · 181 esfriando · 43 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Uma segunda passada no mesmo dia, e ela quase não achou nada.** A tarefa das 23h30 de 13/10 rodou às 01h54 de hoje, e a de hoje rodou às 17h38. O intervalo entre as duas foi de **~16 horas**, contra ~2 a 3 dias nas rodadas anteriores. A rotina foi a mesma: API de busca do RA de dentro da aba do navegador interno, **11 gateways, 22 páginas, 166 reclamações** com ID acima de 261557535 (o maior lido às 01h54). Só 2 IDs da lista já estavam no vault. A Biblioteca abriu sem aprovação para 2 buscas.

**Sinal novo real: pouco, e quase todo numa nota só.**
- [[treino-trinca]] teve **7 IDs novos e foi de 62 para 69** em um dia, o mesmo ritmo das duas rodadas anteriores (~6 por dia). Uma reclamação (261617433) acrescenta **o degrau mais caro já visto no funil do Lotz**: R$ 37 no Pix, mais R$ 67 de "cardápio personalizado" e, no mesmo dia, **um kit de suplementos de R$ 1.162,70 em 7x no cartão**. A 261616413 confirma os R$ 67 do cardápio, que chegou genérico. O "desafio de 28 dias" (261615547) foi contado porque é o nome do Trinca nos anúncios. Na Biblioteca foram **~210 resultados (eram ~200 às 01h54)**, os 29 carregados são de Pedro Lotz e **o mais novo continua sendo de 05/10**. São nove dias sem criativo novo enquanto a contagem sobe.
- [[zap-radar]] de 43 para **45**, [[stalkeia-ai]] de 34 para **36**. Há mais dois casos da mesma mecânica de espionagem sem o nome do produto (R$ 137 para "passar as conversas do marido"; "paguei o rastreamento de celular"), e eles ficaram fora da conta.
- [[irryss]] de 6 para **8**, e agora **em dois gateways**. Na Lastlink (261615499) o produto aparece como **"treino de inglês irryss", com acesso de um ano**. É a primeira pista do que o app vende. Até hoje a nota estava em `nao-classificado`.
- [[renda-fortuna]] de 4 para **5**. A 261544235 mostra a escada: **R$ 186,99 e, logo depois do Pix, um "produto americano"**. Outra reclamação (261521183: "apresentação no Facebook", programas de R$ 186,99 e R$ 497) quase certamente é a mesma operação, mas não cita o nome e não entrou na conta.
- Gotejamento de 1 ID: [[shopminer]] 21, [[fornece-up]] 16, [[app-do-paizao]] 20, [[app-direct-line]] 11, [[comunidade-mvz]] 3.

**Estreias: nenhuma.** Nenhum nome novo teve 3 menções. Ficaram na fila, com 1 menção cada e sem nota: App Zap Million (PerfectPay, R$ 97,99), Flux AI Anual (Cakto, R$ 197,99), Ctrl AI (Payt), Aivarolab (PerfectPay, vendido no TikTok), Rotina Lucrativa (PerfectPay, anunciado como "comissão por avaliar app" e entregue como curso de influenciador), Sistema Tik Tok Remunerado (Payt), SouDrop (Kiwify) e um gerador de notificações falsas (Cakto). Na Biblioteca, "zap million" só devolveu um anúncio institucional de um "MillionZap" de atendimento. Não é a mesma coisa.

**Retornos: 3, e nenhum é venda nova.** [[bike-in-casa]] (Ticto) voltou com a **quarta parcela de uma anual cancelada em agosto**: é cobrança residual. [[linflora]] (Payt, 2 IDs) é **loja de produto físico**, sem relação com low ticket digital. [[curso-massagem-tantrica]] (Wiapy) teve 1 ID, o primeiro desde 27/08. Os três mudaram de `esfriando` para `ativa` pela regra, e são esses os **3 movimentos de status** do dia.

**Mecânica de funil.** O padrão "o preço real vem depois da frente" ganhou o caso mais extremo até agora: o Trinca já tem **R$ 37 → R$ 67 → assinatura do app → Trinca Elite recorrente → kit de suplementos de R$ 1.162,70**. A frente low ticket é a porta de entrada para um ticket médio que o `ticket_medio_est` da nota não captura.

**Decaimento: nenhum, de propósito.** Os 11 gateways foram varridos de novo, mas o `sync_vault.py` conta rodada por **dia**, e o decaimento de 14/10 já foi aplicado às 01h54 (121 mudanças). Aplicar de novo contaria o mesmo dia duas vezes.

**Instrumento: o `--leitura` apagava a lista de passadas.** No `sync_vault.py`, a regex da `## Leitura da rodada` ia até o fim do arquivo (`(.*)` com DOTALL). Numa segunda passada no mesmo dia, ela substituía a leitura anterior e **apagava a `## Passadas do dia`**, que o `publicar.py` recriava só com a passada nova. A nota do dia foi restaurada à mão, com as duas leituras e as duas passadas, e a regex agora para na seção seguinte. Conferi o histórico: desde 27/09, quando a lista de passadas passou a existir, só **27/09** tem passadas fora da lista (5 listadas de 7 em `Radar/rodadas/`). Não investiguei se foi este bug, e a nota daquele dia não foi mexida.

**Cuidados.** (1) As 10 notas já tocadas às 01h54 tiveram `ra_reclamacoes` atualizado, mas **o corpo delas não ganhou os IDs desta passada**, porque o `sync` só escreve uma seção `## Rodada` por dia. Os IDs estão na nota da passada e no JSON em `Radar/dados/`. (2) O ritmo do Trinca (~6 por dia) é a única série com três pontos comparáveis. As outras têm volume pequeno demais para medir velocidade. (3) Score não mudou em nenhuma nota. O vício registrado às 01h54 continua: ShopMiner (0,70), Fornece Up (2,15) e Irryss (1,75) estão em "descartar" enquanto acumulam reclamações.

**Autocrítica.** Esta passada foi uma **checagem de cadência, não uma descoberta**. Com 16 horas de intervalo, o RA devolve sobretudo gotejamento, e o adendo de 11/10 tinha razão em pedir janelas maiores para essa fonte. A pendência das duas últimas leituras continua aberta: a **Etapa 3b com a API** (páginas de produtor, `ra_primeira_reclamacao` do Trinca, do Zap Radar e do Paizão) é o que tiraria o `s_lucro` dessas notas do palpite. Ela caberia no tempo que esta passada não usou, e não foi feita.

---

## Leitura anterior — 2026-10-14 (rodada diaria, 01h54)

Passada: [[2026-10-14 -- 0154]] · nota do dia: [[2026-10-14]].

**401 notas · 329 ofertas · 72 ângulos · 3 novas hoje · 20 vistas hoje · status: 98 nova · 76 ativa · 184 esfriando · 43 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**O vault quase dobrou, e não foi por esta rodada.** Entre a leitura de 11/10 (228 notas) e hoje entraram no `main` dois merges (`c95e356` e `a5e3b1c`) com **as passadas 6x/dia de 07 a 10/10**, que rodaram num clone separado e só chegaram agora. Isso corrige três leituras seguidas deste Painel: os "buracos" de 02-05/10, 05-08/10 e 08-11/10 **não eram passadas paradas**, eram passadas que não tinham chegado ao `main`. Elas trouxeram ~170 notas, a maioria com uma menção e `status: nova`. Esta rodada rodou às 01h47 de 14/10 (a tarefa das 23h30 de 13/10 atrasou de novo). Usou **a mesma API de busca do RA** de 11/10 em **11 gateways** (Kiwify, Hotmart, Ticto, Lastlink, Kirvano, PerfectPay, Cakto, Wiapy, Payt, Eduzz, Monetizze). Foram **453 reclamações**, todas com ID acima de 261385839 e criadas depois de 11/10 23h05, sem buraco de leitura. A Biblioteca abriu sem aprovação para 4 buscas.

**Instrumento: o ID de empresa do adendo de 11/10 estava errado.** `kirvano-pagamentos` e `cakto-pay` são os slugs da URL, não o `company=` da API, que devolve lista vazia com eles. O valor certo é o `identifier` do JSON-LD da página da empresa, um hash (Kirvano `JVD9Q_FXbkZdW_e6`, PerfectPay `2rdaK76G_uK2tYoE`, Payt `0DjGISB4pDHUfbQK`; Hotmart, Eduzz e Monetizze usam número). O slug da PerfectPay no RA é `perfectpay`, sem hífen. Lowify e Hubla continuam sem página.

**Sinal novo real: sim, e pela primeira vez comparável com a rodada anterior.** É a segunda rodada seguida com lista completa, e o intervalo é parecido (~2,1 dias contra ~3). As mesmas seis notas concentram o volume:
- [[treino-trinca]] teve **12 IDs novos e foi de 50 para 62**, o maior volume nominal do vault. Uma reclamação (261475005) muda a escada: os **R$ 37 não dão acesso ao treino sem a assinatura do app**, que o checkout não mostra. O Trinca Elite é a assinatura que a leitura de 08/10 achou. Três reclamações de outros produtos do Lotz ficaram fora da conta: compra em live, "DF 1000" em live e Magra Sem Fome. Na Biblioteca, com a mesma busca, foram **~200 resultados (eram ~160)**, depois de três quedas seguidas. Os 29 carregados são todos de Pedro Lotz, e **o mais novo continua sendo de 05/10**. Mais resultado sem criativo novo é verba nos criativos que já existem, não teste. Score **6,60**.
- [[zap-radar]] teve **17 IDs novos e foi de 26 para 43**: 16 na Payt e 1 na PerfectPay. É a nota que mais cresce. A segunda cobrança agora tem preço: **R$ 137 e depois R$ 147** (261432177), ou mais R$ 137 + R$ 67 (261531979). Há uma família inteira em volta que não foi contada: "Manual da Verdade" (R$ 137), "Protocolo da Verdade" (R$ 67), "relatório de áudios" (R$ 137), "clonar o zap" e "WhatsSpy Up1". Uma das reclamações chama o produto de "ZAP radar - manual da verdade", então é provável que pelo menos o Manual seja a mesma operação. Score **5,00**.
- [[shopminer]] teve **9 IDs novos e foi de 11 para 20**. O nome comercial completo é "acesso vitalício ao ShopMiner (Shop Flix)", vendido **em live**. Na Biblioteca, "shopminer" devolve **zero anúncios**, o que confirma o canal. O cluster de vídeo de produto para marketplace cresceu: [[tokscale-ia]] de 6 para 8, VideoShop (Kirvano, 1) e TT Shop IA (Kiwify, R$ 286,90, 1).
- [[fornece-up]] teve **7 IDs novos e foi de 8 para 15**. São **todos de cancelamento ou estorno travado** (R$ 175 a R$ 315,54). Na Biblioteca, "forneceup" não devolve anúncio da operação.
- [[stalkeia-ai]] de 28 para **34** (6 nomeados). Outras três com a mesma mecânica de vários Pix ficaram fora porque não citam o nome.
- [[app-do-paizao]] de 15 para **19** (4 nomeados). Uma quinta, não contada, descreve a escada inteira: **mês de R$ 50, depois "promoção" de 1 ano a R$ 20/mês**, cobrados juntos. Na Biblioteca continua com **~11 anúncios**, todos de 05 a 09/10. É a primeira vez em três buscas que ele **não** rotaciona os criativos.
- Mornas: [[app-direct-line]] de 5 para **10**. Uma reclamação ("Larissa no WhatsApp / Direct Line") dá a primeira pista do que o app faz: uma atendente no WhatsApp. [[malu-sua-assistente]] 6 → 8, [[irryss]] 4 → 6, [[receitas-sem-pensar]] 3 → 5, [[renda-fortuna]] 3 → 4 (cobrança de outro produto depois do Pix).

**Estreias: 3, pequenas.** Agora que existem duas leituras completas, dá para somar menções entre rodadas. **Escola de Personagens** (Kiwify, 4 em duas rodadas) é entregue "em uma semana, via live", por um grupo de WhatsApp cujo link chega quebrado. **SpinMaster** (Kirvano, 3 em duas rodadas) é um "programa de roleta" que, depois do pagamento, manda o comprador depositar numa casa de apostas: **o infoproduto serve de porta para afiliação de bet**. **Movimento Prósperas** de Luana Bittencourt (Kiwify, 3) é uma mentoria feminina de prosperidade, com reembolso negociado no WhatsApp da produtora. Nenhuma das três tem preço no corpo. Ficaram de fora, com 2 menções: Treino da Fera (Payt, R$ 100 com "Fera de Elite"), 7 Améns da Madrugada (Payt, nicho religioso), CrieAI (Cakto), Low Ticket Academy + Nickse Hub (Kirvano), Low Ticket Automatizado (Cakto, R$ 216,68) e o protocolo de treino da Aline Pamplona (Kiwify).

**Retorno: 1, fraco.** [[comunidade-mvz]] (Cakto, R$ 149,73) voltou de `esfriando` com 1 ID. [[loopyz]], [[pack-produtos-validados-sistema-billion]], [[clipshort-ai]] e [[beto-ia]] tiveram 1 ID cada, mas já estavam `ativa`.

**Mecânica de funil.** Dois padrões de 11/10 se repetiram, com mais casos. (1) **O preço real depois da frente**: a assinatura do app no Trinca, os R$ 147 do Zap Radar, o anual do Paizão, o "plano Pro" do Beto IA e do Direct Line, e a frente do ClipShort que virou três produtos (Corte Virais + Clipshort Gringo + Clipshort). (2) **A live como canal sem rastro na Biblioteca**: ShopMiner, Escola de Personagens, o DF 1000 e o kit do Lotz, a Trendly (PerfectPay, plano vitalício de 12x R$ 30,02 "após live") e o Fornece Up. **Quatro das seis notas mais quentes não têm anúncio encontrável pelo nome.** Para essas, o RA é o único instrumento, e a Etapa 1 não vai destravar o `s_lucro` delas.

**Status (decaimento à mão, só nos 11 gateways varridos, só em notas vindas do RA, sem ângulos, dança, infantil, material pedagógico, multi-gateway ou nota com anúncio medido).** **121 mudanças**, quase todas atrasadas. **118 notas** vistas pela última vez até 10/10 não apareceram nem em 11/10 nem hoje, nas duas leituras completas, e foram para `esfriando`: **60 eram `ativa`** e **58 ainda eram `nova`**. A maior parte veio no merge das passadas de 07-10/10 e nunca tinha passado por um decaimento. Entre elas estão Hi Spy 4.0, TCS Spy, Gerachat, White Driver, Bike in Casa, Dieta das 3 Fases, Painel Elite, Luna IA, Método Atlas e os Biscoitos Natalinos. **3 estreias de 11/10** passaram de `nova` para `ativa` (Cão360, Thermafit App, Viva de Martelinho de Ouro). Ficaram de fora de propósito **cinco duplicatas de notas vistas hoje** (`direct-line-app`, `stalkea-ai`, `stalker-ai`, `loopzy`, `a-renda-da-fortuna`), para não esfriar o nome repetido de uma oferta quente, e também [[google-captcha-tw]] (página de produtor) e [[atelie-das-velas]], [[kit-80-casinhas-de-natal-para-imprimir]] e [[chatgpt-privado]] (anúncio medido). Nenhuma nota foi para `morta`: a contagem de 7 rodadas não é confiável com passadas que chegam fora de ordem.

**Cuidados.** (1) O salto de 228 para 401 notas é **merge, não mercado**. O número de notas não deve ser lido como série. (2) As 98 `nova` restantes estão em gateways não varridos ou nos nichos excluídos. O `--verificar` acusa 95. (3) As duplicatas acima (Stalkeia ×3, Direct Line ×2, Loopyz ×2, Renda Fortuna ×2, Thermafit ×2, Congresso Humanamente ×2, GTD Academy ×3, Rendafini ×3) **dividem a contagem de reclamações** entre notas. Precisam de merge manual, que esta rodada não fez. (4) Score não mudou em nenhuma nota com ID novo. ShopMiner (0,70), Fornece Up (2,15) e Direct Line (1,75) estão em "descartar" com `s_ticket: 0` ou `s_lucro` de palpite, enquanto acumulam 10 a 20 reclamações em uma semana. É o mesmo vício de 29/08 ao contrário: **a rubrica não tem como pontuar volume de reclamação sem longevidade.** (5) A primeira passada de hoje foi commitada com o autor `jpmonmelo`, e não "Radar Low Ticket", porque a identidade não foi exportada naquele comando. Só o autor ficou diferente.

**Autocrítica.** A rodada foi barata e limpa: uma rotina de JS na aba do RA, 453 linhas, 11 corpos abertos. Mas não pagou a pendência de 11/10: **a API não foi usada nas páginas de produtor (Etapa 3b)**, que era o próximo passo para medir `ra_primeira_reclamacao` do Trinca, do Zap Radar e do Paizão e tirar o `s_lucro` deles do palpite. O decaimento de 121 notas é correto pela regra, mas é limpeza de backlog: o retrato honesto é que **237 das 401 notas têm `rodadas_vista: 1`**: foram vistas uma vez e não voltaram. A correção do `company=` foi registrada no adendo de 11/10 do `Pipeline.md`.

---

## Leitura anterior — 2026-10-11 (rodada diaria)

Passada: [[2026-10-11 -- 2305]] · nota do dia: [[2026-10-11]].

**228 notas · 203 ofertas · 25 ângulos · 10 novas hoje · 21 vistas hoje · status: 67 nova · 40 ativa · 77 esfriando · 44 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Três dias de novo sem passada, mas desta vez nada se perdeu.** É o quarto buraco seguido das passadas 6x/dia: nada em `Radar/rodadas/` entre 08/10 e hoje. A tarefa das 23h30 rodou às 23h05. O que mudou foi o instrumento. A paginação por clique do RA parou de responder hoje (o site migrou para outra pilha e `?pagina=2` continua vazio). No lugar dela, **a API de busca que o próprio site usa** (`iosearch.reclameaqui.com.br/.../companyComplains/10/<offset>?company=<id>`) respondeu do navegador interno com a lista completa: ID, data, título, empresa e o começo do corpo, em blocos de 10, até a data que se quiser. Foram **~650 reclamações de 11 gateways** (Kiwify, Hotmart, Ticto, Lastlink, Kirvano, PerfectPay, Cakto, Wiapy, Payt, Eduzz, Monetizze), cobrindo **tudo desde 08/10 03h**, sem o limite de 5 linhas e sem o buraco de leitura que 08/10 admitiu. Lowify e Hubla ficaram de fora porque o slug da empresa não foi achado. A Biblioteca abriu sem aprovação para três buscas.

**Sinal novo real: sim, e o maior desde que o vault existe.** Pela primeira vez a contagem não é limitada pela janela de leitura, então os números abaixo medem volume e não sorte.
- [[zap-radar]] teve **16 IDs novos e foi de 10 para 26**. São 12 na Payt e 4 na PerfectPay. O volume **mudou de gateway**: em 08/10 o sinal estava na PerfectPay. Os corpos repetem a mecânica (R$ 97 a R$ 137, depois outra cobrança para abrir as mensagens). Uma reclamação da PerfectPay nomeia "Zap Radar / WhatsSpy", e há mais duas de "Whats Spy" não contadas. Na Biblioteca, "zap radar" não devolve nenhum anúncio da operação. Score **5,00**.
- [[stalkeia-ai]] teve **13 IDs novos e foi de 15 para 28**, todos na PerfectPay. É a nota com mais reclamações de oferta de frente barata no vault. O `s_lucro: 8` continua sem insumo de longevidade e segue na lista de violações. Score **5,85**.
- [[treino-trinca]] teve **9 IDs novos e foi de 41 para 50**. Uma das reclamações descreve "venda casada": vários upgrades dentro do checkout de R$ 37. Outra é um **kit de R$ 997 sorteado numa live do Lotz** e não entregue. Na Biblioteca, com a mesma busca, foram **~160 resultados (eram ~210 em 08/10 e ~230 em 05/10)**, e nenhum criativo carregado começou depois de 05/10. É a **terceira queda seguida**, enquanto as reclamações continuam subindo. Score **6,60**, sem mudança.
- [[app-do-paizao]] teve **5 IDs novos e foi de 10 para 15**. A escada ficou clara: frente de ~R$ 50, depois **plano anual de R$ 289,99 em 12x** no cartão. Na Biblioteca foram **~11 anúncios (eram ~19)**, todos começados entre 05 e 09/10. É a segunda rotação completa de criativos em uma semana. Score **5,75**.
- Mornas: [[pilates-na-parede-lastlink]] de 3 para **8** (LP de quiz `desafiopilates.com/q/simple`, campanha com "PreEscala" no nome, R$ 27); [[chatgpt-privado]] de 6 para 8; [[malu-sua-assistente]] de 2 para **6**, agora em **três gateways** (Wiapy, Cakto e PerfectPay).

**Estreias: 10, todas com 3 menções ou mais.** É a resposta à autocrítica de 05/10 ("doze estreias de uma menção é volume, não descoberta"). Com a lista completa, o corte de 3 menções vira possível. Cerca de 15 candidatas com duas menções ficaram de fora (Escola de Personagens, Biblioteca Digital TM, Spygram, BicarbonaApp, Ritual do Número Mestre, Sambox, SpinMaster, Fusion Ads, Anunciaê...).
- **ShopMiner** (Payt, **11**): app que "minera" produtos e gera imagem e vídeo deles, vendido **em live** com plano vitalício de R$ 297 (5x R$ 65,76). Não aparece na Biblioteca pelo nome, porque o canal é a live.
- **Fornece Up** (PerfectPay, **8**): lista de fornecedores por assinatura em 12x. Quase todas as reclamações têm o mesmo texto ("não consigo cancelar"). O volume vem do cancelamento travado.
- **TokScale IA** (Payt, 6): vídeos com IA para TikTok Shop, assinatura. Forma um cluster com o ShopMiner: **ferramenta de vídeo de produto para quem vende em marketplace**, 17 reclamações somadas em três dias, todas na Payt.
- **App Direct Line** (Cakto, 5) e **Irryss** (Payt, 4): apps por assinatura em que o botão de reembolso existe mas não estorna. Nenhum dos corpos diz o que os apps fazem, e por isso o nicho ficou `nao-classificado`.
- Com 3 cada: **Receitas Sem Pensar** (Payt, app de nutricionista que cobra à parte as marmitas que motivaram a compra), **Renda Fortuna** (Payt, 12x), **Thermafit App** (Payt, R$ 47), **Cão360** (Payt e Cakto, R$ 97, "frequência canina") e **Viva de Martelinho de Ouro** (Hotmart, curso de ofício).

**Retornos: 3, fracos.** [[loopyz]] (Cakto, de `morta`, 2 IDs), [[auks-bot]] e [[cashnopix]] (PerfectPay, de `esfriando`, 1 ID cada). [[love-pix]] teve +1, mas já estava `ativa`. Nenhum desses retornos indica um dono que voltou a escalar.

**Mecânica de funil.** Três padrões se repetiram em várias notas sem relação entre si. (1) **O preço real está depois da frente**: o anual parcelado do Paizão, as marmitas pagas à parte do Receitas Sem Pensar, os upgrades no checkout do Trinca, a API cobrada da Malu, a segunda cobrança do Zap Radar. (2) **A garantia anunciada que não funciona** é o que gera a reclamação: Fornece Up, Direct Line, Irryss, TokScale. O comprador não reclama do produto, reclama de não conseguir sair. (3) **A Payt virou o gateway com mais sinal**: 123 reclamações em três dias, seis das dez estreias e o deslocamento do Zap Radar. Até 05/10 ela era varrida como gateway secundário.

**Status (decaimento à mão, só nos 11 gateways varridos, só em notas vindas do RA, sem ângulos, dança, infantil, material pedagógico, multi-gateway ou nota com anúncio medido).** **13 `ativa`** vistas pela última vez em 02 ou 05/10 completaram a segunda rodada sem aparecer e foram para `esfriando`, entre elas App Mão Verde, Atleta Híbrido, Bíblia 3D, ClipShort, Date Nights Cristão, Fórmula YouTube Viral, Livros de Enoque e UltraCut. **3 `nova`** passaram para `ativa` (Biscoitos Natalinos, Beto IA, Dieta das 3 Fases). O sync tirou Pilates e Malu de `nova`, e houve 3 retornos. No total foram **21 mudanças de status**. O [[atelie-das-velas]] e o Kit +80 Casinhas ficaram de fora, mesmo ausentes do RA, porque o insumo deles é anúncio e não reclamação.

**Cuidados.** (1) A API devolve o corpo cortado em ~120 caracteres. Preço e mecânica saíram de **10 corpos abertos por fetch**, não de todos. As contagens dependem de o nome do produto aparecer no título ou no começo do corpo, então são **limite inferior**. (2) O volume de uma rodada com lista completa **não é comparável** com as de 5 linhas. Parte do salto do Zap Radar e da Stalkeia é instrumento, não mercado. A comparação honesta começa na próxima rodada que usar a mesma API. (3) O kit de R$ 997 do Lotz entrou na conta do Trinca porque é o mesmo operador, mas é outro produto. (4) Score não mudou em nenhuma nota com ID novo, porque `s_lucro` pede longevidade e o RA só deu volume. Zap Radar e Stalkeia passam de 20 reclamações, o que pela tabela da Etapa 3 vale +2, mas a Stalkeia já está acima do teto sem insumo. Nenhuma nota foi rescorada. O ShopMiner tem `s_ticket: 10` por causa dos R$ 297, e isso é o sync lendo o preço, não uma avaliação.

**Autocrítica.** A rodada rendeu mais que as quatro anteriores somadas, e quase todo o ganho veio de **um instrumento achado por acaso** depois que o clique de paginação falhou, não de método. Ela também gastou o tempo que deveria ir para a Biblioteca: só três buscas, e nenhuma para as estreias com volume (TokScale, Fornece Up, Pilates). O próximo passo óbvio é usar a mesma API nas **páginas de produtor** (Etapa 3b), onde ela deve entregar `ra_primeira_reclamacao` e destravar o `s_lucro` que o vault nunca conseguiu medir. Também falta registrar o procedimento num adendo do `Pipeline.md` antes que ele se perca como se perdeu o clique de 02/10.

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
