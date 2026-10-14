---
tipo: painel
atualizado: 2026-10-14
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-10-14 (rodada diaria)

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

## Leitura anterior — 2026-10-08 (rodada diaria)

Passada: [[2026-10-08 -- 0309]] · nota do dia: [[2026-10-08]].

**218 notas · 193 ofertas · 25 ângulos · 5 novas hoje · 18 vistas hoje · status: 62 nova · 45 ativa · 66 esfriando · 45 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Três dias de novo sem passada.** Entre 05/10 e 08/10 as passadas 6x/dia não gravaram nada em `Radar/rodadas/`. É o terceiro buraco seguido. A tarefa das 23h30 rodou às 03h09. Esta rodada cobriu numa passada só os oito gateways que em 05/10 tinham ficado divididos entre duas: Kiwify, Hotmart, Ticto, Lastlink, Kirvano, **PerfectPay, Cakto** e Wiapy. Foram 33 páginas e cerca de 175 corpos com ID e carimbo, quase todos de 06 e 07/10. As 3 a 5 páginas por gateway voltam só cerca de um dia e meio. **O intervalo entre a tarde de 05/10 e a manhã de 06/10 não foi lido**, e o que entrou nele pode ter ficado de fora. Payt, Lowify, Eduzz e Monetizze não foram varridos. A Biblioteca abriu sem aprovação. Desta vez ela foi usada só para **repetir as quatro buscas** que a autocrítica de 05/10 pediu.

**Sinal novo real: sim, de novo concentrado nas mesmas três notas.**
- [[treino-trinca]] ganhou **8 IDs novos** (261097585 a 260965163, todos acima de 260842051) e foi de 33 para **41**. Uma reclamação muda a leitura do funil. A 261087345 descreve a **renovação automática da assinatura Trinca Elite** em 06/10. O degrau de R$ 237,78 que 05/10 viu como upsell é **recorrente**. Outra reclamação nomeia um "kit Trinca Force" (260965163), mais um produto na escada. Na Biblioteca, com a mesma busca, o número foi de **~230 para ~210 (−20)**. Os 29 anúncios carregados continuam todos de Pedro Lotz, com criativos novos em 03 e 04/10. As reclamações estão acelerando enquanto o número de anúncios encolhe um pouco. É o primeiro delta negativo medido nessa nota. Score: **6,60**, sem mudança.
- [[app-do-paizao]] teve **4 IDs novos** e foi de 6 para **10**. A 261028367 mostra a escada cobrada: **R$ 49 + R$ 283 + 6x R$ 86**. É a segunda vez em uma semana que aparece um valor alto perto de R$ 284 depois da frente, o que torna menos provável que o relato de 02/10 tenha sido um caso isolado. Na Biblioteca, com o mesmo domínio: **~19 anúncios (+3), todos iniciados em 05 e 07/10**. O lote de 03-04/10 e o anúncio de 18/08 saíram do ar. É **rotação completa de criativos em três dias**, uma mecânica de mídia que o vault ainda não tinha medido. Score: **5,75** (o `s_replica: 3` segura).
- [[stalkeia-ai]] teve **4 IDs novos** e foi de 11 para **15**. Apareceu o nome "Acesso Completo 2.0", e os preços de entrada vão de R$ 39,90 a R$ 47,90. [[zap-radar]] foi de 8 para 10, também na PerfectPay e também com cobrança extra para liberar o acesso.

**Retornos: 4, todos fracos.** [[mdr-despertar-2-0]], [[mentoria-caio-martins]], [[pack-produtos-validados-sistema-billion]] (Cakto) e [[love-pix]] (PerfectPay) voltaram de `esfriando` com **uma reclamação nova cada**. A mais informativa é a do Billion: numa única compra de 13/09 aparece a escada inteira, Pack R$ 97,28 + Sistema R$ 247,71 + Sistema GLOBAL R$ 597,99 = **R$ 942,98**. A do Love Pix é a primeira menção desde 24/08 e mostra a mesma "taxa de R$ 20" de agosto. São retornos pela regra, mas não indicam um dono que voltou a escalar. Gerachat e White Driver foram relidas pelos mesmos IDs (avistamento, contagem parada).

**Estreias: 5, e duas com mais de uma menção.** **Pilates na Parede** (Lastlink) tem **3 reclamações num dia**. É um plano de 21 dias vendido no Instagram, entregue num app que só lista o nome dos exercícios. Mesmo gateway e mesma família de desafio fitness do Trinca. **Malu, Sua Assistente** (Wiapy, R$ 37,90) é uma assistente de postagem para lojistas da Shopee que, depois da compra, cobra **mais R$ 24 "da API"**, outra taxa para liberar, fora do nicho de espionagem. As outras três têm uma menção cada: **+100 Modelos de Biscoitos Natalinos** (Wiapy), **Desafio Hiit Dance** (Lastlink, R$ 37, nicho de dança) e **Horinha da Leitura** (Kirvano, vídeos de alfabetização).

**Mecânica de funil.** O cluster de **Natal na Wiapy** ganhou corpo. Em três dias apareceram o Kit +80 Casinhas, os Biscoitos Natalinos e um presépio de papelão comprado pelo Facebook (260984353, sem nota). O ticket é de R$ 20 a R$ 40, o imprimível é de entrega imediata e a validade acaba em dezembro. Também se repetiu a **frente barata que vira assinatura**: Trinca Elite (renovação), Bike in Casa (+2, "teste grátis" sem canal de cancelamento, de 1 para 3), Comunidade Subido na Hotmart e mais duas renovações na Kiwify e na Lastlink. Ficaram sem nota por ter só uma menção e nenhuma medição: Pack Achadinhos Virais (Kiwify, R$ 29), FVV (Kiwify), Dólar Hub (Cakto, R$ 88,98), Octuz AI e Nexus Focuz (Cakto), Kit Orça Pintor (Wiapy, R$ 37,90, que encosta no [[angulo-eletricista-orcamento-app]]) e uma "licença para trabalhar no Facebook dando notas" a R$ 48 na PerfectPay (renda por tarefas com taxa).

**Status (decaimento à mão, só nos 8 gateways varridos, só em notas vindas do RA, sem ângulos, dança, infantil ou multi-gateway).** **11 estreias de 05/10** passaram de `nova` para `ativa` (uma rodada de ausência é cobertura). **3 `ativa`** de 02/10 que não apareceram em 05/10 nem hoje foram para `esfriando`: Achados da Ellen, SerBene e Seu Curso Viral. **10 `ativa`** de PerfectPay/Cakto vistas pela última vez até 26/09 completaram a segunda rodada sem aparecer e foram para `esfriando`: Caderno de Professor, Comunidade MVZ, E-Workflow, Knights Club, Lumi AI, Luna IA, MS Green Premium, Painel Elite, RB Operações e Trendy IA. Somando os 4 retornos e o Bike in Casa (`nova` → `ativa` pelo sync), são **29 mudanças de status**. Beto IA e Dieta das 3 Fases (Payt) ficaram em `nova` porque a Payt não foi varrida. Isso explica parte das **57 notas** que o `--verificar` ainda acusa.

**Cuidados.** Os três deltas da Biblioteca (Trinca −20, Paizão +3, Ateliê das Velas ~33 → **~21, −12**) agora são comparáveis, porque vêm da mesma busca. Mas contam anúncios que casam com o termo, não criativos distintos, e só carregam os primeiros ~30. O Ateliê perdeu o anúncio de 27/05, e o mais antigo carregado é de 12/06. O `dias_no_ar` das três notas **foi mantido** como idade da operação, embora o criativo ativo mais antigo agora seja mais novo (no Paizão, de dois dias). Se o contrato quer "idade do anúncio mais antigo ativo", o Paizão iria para 3 dias e perderia o insumo de longevidade. Isso não foi feito sem decisão explícita. As 8 reclamações do Trinca medem cerca de dois dias, não um.

**Autocrítica.** A pendência de 05/10 foi paga: as quatro buscas foram repetidas com o mesmo termo, e pela primeira vez o vault tem uma série de três pontos (Trinca 130 → 230 → 210). O resultado é menos animador do que a narrativa das últimas leituras sugeria. Duas das três ofertas mais fortes estão com **anúncios estáveis ou em queda** enquanto as reclamações sobem, o que é compatível com uma operação madura colhendo a base, e não com uma operação escalando. As cinco estreias foram escolhidas com mais rigor (cerca de dez candidatas de uma menção ficaram de fora), mas ainda são cinco notas sem nenhuma medição.

---

## Leitura anterior — 2026-10-05 (rodada diaria, complemento das 16h33)

Passada: [[2026-10-05 -- 1633]] · nota do dia: [[2026-10-05]].

**213 notas · 188 ofertas · 25 ângulos · 14 novas hoje (12 às 03h17 + 2 agora) · 22 vistas hoje · status: 69 nova · 42 ativa · 57 esfriando · 45 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Segunda leitura no mesmo dia.** A tarefa das 23h30 rodou às 16h27, treze horas depois da rodada das 03h17. Esta passada não refez o que aquela cobriu. Ela fez três coisas que a das 03h17 deixou de fora: a primeira página de **PerfectPay e Cakto**, que ninguém varria desde 26/09 porque as passadas 6x/dia continuam sem gravar; uma nova leitura de Lastlink, Kiwify e Hotmart para pegar o que entrou durante o dia; e **7 consultas na Biblioteca**, três delas repetindo termos antigos, como a autocrítica de hoje cedo pedia. A coleta foi marcada como `parcial`, porque foram 5 páginas e não 35.

**Sinal novo real: sim, pequeno, e quase todo de hoje.**
- [[treino-trinca]] ganhou **2 IDs novos** (260842051 e 260840917, ambos acima de 260781237) e foi de 31 para **33**. A segunda reclamação explica a mecânica: o app fica bloqueado e "queriam que eu comprasse mais curso". O acesso ao que foi pago depende do próximo degrau. O score continua **6,60**.
- [[stalkeia-ai]] recebeu **3 reclamações nomeadas com ID novo**, todas de hoje (260834783, 260836685, 260841477), as primeiras com ID desde 256618461, e foi de 8 para **11**. Duas descrevem **três Pix por compra** (R$ 155,70 e R$ 232,64). Uma quarta ("Stalker app", 260833211) provavelmente é a mesma operação e não foi contada. A taxa escalonada continua viva na PerfectPay cinquenta dias depois da estreia no vault. O `s_lucro: 8` dela continua sem insumo de longevidade e segue na lista de violações.

**Biblioteca: as buscas repetidas mostram o que a lista do RA não mostra.**
- [[atelie-das-velas]]: a busca pelo anunciante "Carol a artesã" devolve **~33 anúncios**, o mais antigo carregado de **27/05 (131 dias)** e criativos novos em 17 e 26/09. Na busca larga "velas artesanais" aparece um anúncio dela iniciado em **16/07/2024**. Pode ser agrupamento de criativo, então não foi usado. O `s_saturacao` saiu da sentinela para **6**: os ~1.100 resultados são quase todos fornecedores de insumo, o infoproduto em pt-BR visível é Carol e Haromalita, e "curso de velas" é dominado por operadores em espanhol. O score foi de 5,50 para **6,40** (observar). A nota tinha ido para `esfriando` hoje cedo por ausência no RA e **voltou**. É o retorno do dia, e é exatamente o caso que a leitura das 03h17 apontou: o decaimento media a lista de reclamações, não o anúncio.
- [[app-do-paizao]]: a busca pelo domínio dá **~16 anúncios** de Carlão Silva, **8 deles iniciados em 03 e 04/10**. O anúncio de 04/08 saiu do ar e o mais antigo ativo é de 18/08. É verba entrando, mas não é `criativos_delta`, porque a busca de 27/09 foi outra. Fica como linha de base.
- "chatgpt plus anual": **~120, igual a 02/10**. A coorte parou de crescer em volume, mas a AgenciaDesign segue subindo criativos a R$ 21,90 (04/10) e entrou a Assina Prime a R$ 97. É o primeiro delta zero medido com o mesmo termo, e também é informação.

**Estreias: 2, uma menção cada.** **Frequência de Cura Dívida** (Instituto Cristão Online, PerfectPay, R$ 48, entregue pela Perfect Academy) encosta no cluster religioso. Na Biblioteca o produtor não aparece, mas "frequência de cura" devolve uma coorte de frequências a R$ 19,90-20 (Frequências Proibidas desde 24/08, O Segredo do Som desde 11/07), um sub-ângulo esotérico/religioso que o vault ainda não tem como nota de ângulo. **Fórmula YouTube Viral** (Kiwify, R$ 37,90 + bump "Pack Edição Suprema 2.0" R$ 15,90) é bump de frente barato, sem anúncio encontrado pelo nome.

**Status (decaimento à mão, só PerfectPay/Cakto, só notas vindas do RA, ângulos fora).** A conta foi feita por rodada de PerfectPay/Cakto: 22, 23, 24, 25 e 26/09 e hoje. **6 estreias de 26/09** saíram de `nova` para `ativa` (Caderno de Professor, Comunidade MVZ, Knights Club, Luna IA, Método Atlas, Painel Elite). **12 estreias de 22 e 25/09** estão na segunda rodada ou mais sem reaparecer e foram para `esfriando` (900 Mapas Mentais, AppLuna, Boss IA Trade, Comunidade Fornecedores NFC, Glow Mode, IA FX Promocional, InstaUnlocked, MDR Despertar, Modão Raiz, Pack Produtos Validados, RPR, Um Puxa o Outro). **5 `ativa`** vistas pela última vez até 25/09 também foram para `esfriando` (Auks Bot, Cash no Pix, Mentoria Caio Martins, Mentoria Nova Profissão, Jantar Chef Luana). Ficaram de fora [[google-captcha-tw]], que vem da página do produtor, e as notas com vários gateways. As notas presas em `nova` caíram de **73 para 55**. Foram **24 mudanças de status** no total, contando o retorno do Ateliê.

**Gargalo do instrumento: o `publicar.py` apagou a passada das 03h17 da nota do dia.** Na segunda passada do mesmo dia, o `sync_vault.py` reescreveu `Radar/2026-10-05.md`. A linha `[[2026-10-05 -- 0317]]` sumiu de "Passadas do dia" e o `--leitura` substituiu a leitura anterior em vez de acrescentar. As duas foram restauradas à mão. A nota da passada em `Radar/rodadas/` não foi afetada. **Toda segunda passada no mesmo dia vai repetir isso** até alguém corrigir o `sync_vault.py`.

**Cuidados.** As 23 mudanças de status por ausência se apoiam em **uma página de 5 linhas** por gateway, contra várias páginas nas passadas de setembro. O tamanho da amostra caiu e a regra não sabe disso. Se a varredura completa de PerfectPay/Cakto voltar, algumas dessas notas devem reaparecer. A slug `cakto` no RA não existe, e a lista que responde é `/empresa/cakto-pay/`. Os 131 dias do Ateliê e os 16 anúncios do Paizão vêm de busca por anunciante ou domínio, mais precisa que a busca larga, mas sem série anterior com o mesmo termo.

**Autocrítica.** Rodar de tarde, com a rodada da madrugada já feita, deu uma foto melhor do dia, mas a "rodada diária" virou duas leituras parciais em vez de uma completa. O que mais rendeu foi de novo a Biblioteca com busca por anunciante, e não o RA. O Ateliê das Velas só saiu do `esfriando` porque alguém foi olhar o anúncio. A pendência da manhã continua de pé: repetir **as mesmas** buscas ("Carol a artesã", "avaliacaogratuitapaizao", "treino trinca", "chatgpt plus anual") na próxima rodada, para que o próximo número seja um delta e não outra linha de base.

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
