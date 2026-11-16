---
tipo: painel
atualizado: 2026-11-16
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-11-16 (rodada diaria)

Passada: [[2026-11-16 -- 1600]] · nota do dia: [[2026-11-16]].

**492 notas · 391 ofertas · 101 ângulos · 0 novas hoje · 7 revistas (todas com ID novo) · 1 retorno · 3 mudanças de status · status (todas): 113 nova · 94 ativa · 1 aquecendo · 242 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Uma rodada de ~20 horas, de novo pela fresta.** A anterior foi a de 15/11 às 19h36 (maior ID: 264369015). A tarefa das 23h30 rodou às 16h00, e as passadas 6x/dia seguem paradas desde 18/10. **A API de busca do RA foi negada pela quinta rodada seguida** (executar JS na aba do RA), e a rodada não tentou contornar. Seguindo a autocrítica de ontem, a rodada **leu as listas antes de abrir corpos**: 12 gateways na lista de 5 linhas (Cakto só mostrou 3, e `/empresa/hubla/` deu 404), e só depois 9 corpos abertos. Desta vez **não houve 429 do Cloudflare**. Todos os 9 IDs ficam entre 264395635 e 264445105, publicados em 16/11 entre 09h05 e 15h04. As linhas cobrem só as últimas ~5 a 10 horas de cada gateway, de uma janela de ~20. A Biblioteca abriu sem aprovação para 2 buscas.

**Sinal novo real: pequeno, e o mais interessante veio da Biblioteca.**
- **[[angulo-oracao-perdida-nome-incerto]] ganhou nome e anúncio.** O 264396257 (Ticto, comprado em 11/11) confirma o produto como **"A Oração Perdida"**, que em 14/10 tinha entrado como ângulo por falta de nome confiável. A Biblioteca ("oração perdida", frase exata) devolve **~16 anúncios ativos de duas páginas novas**: "Fé em Jesus" (`jornalurgente.online`, 6 anúncios, mais antigo de 30/10) e "David Williams" (`brightlittlehearts.com`, ~10 anúncios de 12 a 15/11). O segundo é **VSL americana traduzida** ("Uma oração ARRUINOU a minha vida", Harvard, Rei Salomão, a casa no lago em Vermont deixada em testamento). Qual dos dois vende na Ticto não foi confirmado. O `nome` e o `checkout: ticto` foram gravados na nota; `classe` segue `angulo` até alguém ligar anunciante e checkout.
- [[gold-card-tv]] **2 → 3 e primeiro preço medido:** R$ 107,99, comprado em 03/11 e cancelado em 04/11, com a Braip prometendo estorno em 4 dias e não fazendo (264423903). A nota tinha `ticket_frente: 0` (sentinela) e passou a 107,99 (`s_ticket` 0 → 8, score 0,70 → 2,30, ainda provisório). **"Good card tv" dá zero anúncios na Biblioteca.**
- Gotejamento: [[shopminer]] **93**, de volta na Payt depois da estreia na Ticto. A Payt devolveu o Pix **quatro minutos depois da reclamação publicada**, e ela foi avaliada com nota 10. [[tokscale-ia]] **43** (ausente das linhas desde 05/11), comprado **parcelado pela Pagaleve**: a Payt confirmou o reembolso com o campo de valor em branco, e as parcelas do BNPL seguem abertas. [[atmoz]] **7** ("o Atmoz e o Atmoz Pro", no mesmo dia, no cartão). [[videoshop]] **4** (o app trava o celular).
- **Retorno:** [[fabrica-de-low-ticket]] (3 → 4, `esfriando` desde 23/10), agora **na Eduzz** pela plataforma Alumy, como "Aula Magnética com OBS" mais "compras extras além do curso". O cancelamento foi tentado 40 minutos depois da compra.

**Fila (1 ID, sem nota):** "três transações de Pix pelo stalker" (PerfectPay 264430841). Pode ser +1 em [[green-stalker]], mas o corpo não traz nome e não foi atribuído. **Só pelo título, sem ID:** curso Claude Code e Método Mais Cinco, com reembolso recusado dentro do prazo (Kirvano), Método ZN TikTok Shop e Rota do Dólar via Pix (Kiwify), Shark Map AI e "Black 2026" Docis/Felipe Russo (Hotmart), Memorivex e Sócios do Dólar (Payt), Norte Broker com saque travado e uma "ferramenta para WhatsApp" que virou curso (PerfectPay) e Victor Pareto/Time Híbrido com renovação automática (Lastlink). Da fila de 15/11, só o Green Stalker pode ter voltado.

**Mecânica de funil.** (1) **VSL estrangeira traduzida no nicho religioso** (Oração Perdida). O texto é o funil americano de "oração secreta" palavra por palavra, com a casa em Vermont e Harvard intactos, numa página criada há dias. É a mesma cópia que o vault já viu em manifestação e esotérico, agora com roupa cristã. (2) **BNPL no low ticket** (TokScale via Pagaleve). O parcelamento sem cartão sobrevive ao reembolso: o vendedor estorna, mas as parcelas da financeira continuam. É a mesma família da "frente de R$ 37 que vira 7x" do Trinca. (3) **"Compras extras" no checkout de curso de low ticket** (Fábrica), sem nome no corpo. É a escada de bumps de 06/11 (Profissão do Futuro), agora vendida a quem quer aprender a montar low ticket.

**Status.** **3 mudanças, todas pelo `sync`:** [[videoshop]] e [[angulo-oracao-perdida-nome-incerto]] saíram de `nova` para `ativa`, e [[fabrica-de-low-ticket]] voltou de `esfriando` para `ativa` (retorno). **Nenhum decaimento manual.** Os 12 gateways foram lidos só nas 5 linhas mais recentes, como em 31/10, 06/11 e 15/11, e aplicar a tabela de ausência contaria buraco de cobertura como esfriamento. O [[gold-card-tv]] estava `ativa` desde 12/10 sem ser vista. O `sync` não a decaiu, e isso já é a mesma regra.

**Cuidados.** (1) Só contaram IDs acima de 264369015. O 264344729 (ShopMiner na Ticto) ainda aparece na lista da Ticto e **não foi contado de novo**. (2) A Fábrica de Low Ticket foi atribuída **pelo nome**. A nota antiga era Ticto/Cakto, e esta é Eduzz/Alumy. Se for outro produtor com o mesmo nome, a contagem e o retorno estão inflados em 1. (3) O "~16" da Oração Perdida é contagem por frase exata. Os anúncios de "Fé em Jesus" nem citam a oração no texto visível ("Todo Cristão Precisa Ver Isso!"), então a frase deve estar no vídeo ou na legenda. Não é medição de `criativos_ultima` da oferta, e o campo não foi gravado. (4) Scores: Fábrica 4,75 e Atmoz 4,30, os dois `descartar`. ShopMiner 2,50, Gold Card TV 2,30, TokScale 1,75 e VideoShop 1,05, todos provisórios. Trinca 6,60 (observar, não revisto hoje). **Ninguém novo cruza o corte.**

**Autocrítica.** **No RA não houve sinal novo relevante:** 7 IDs em 7 notas já mapeadas, nenhuma estreia, numa fresta de ~5 a 10 horas por gateway. Ler as listas primeiro funcionou: 12 gateways lidos contra 9 ontem, sem 429. O instrumento continua o mesmo, e o gargalo também: **sem a API, a rodada diária só vê a manhã do dia em que roda.** O dado de mais valor foi a Biblioteca ligar um nome do RA (Oração Perdida) a uma coorte de anúncios de duas semanas. Falta o elo anunciante → checkout, e ele depende de abrir a LP. A rodada não abriu, e fica para a próxima. O Trinca, que ontem foi o único sinal forte, **não foi medido de novo hoje**: a série de criativos pede uma leitura a cada 5-10 dias, não diária. A pendência da Etapa 3b (`ra_primeira_reclamacao` do ShopMiner, Zap Radar e Paizão) segue aberta pela décima oitava vez, e continua dependendo da API.

---

## Leitura anterior — 2026-11-15 (rodada diaria)

Passada: [[2026-11-15 -- 1936]] · nota do dia: [[2026-11-15]].

**492 notas · 391 ofertas · 101 ângulos · 0 novas hoje · 3 revistas (todas com ID novo) · 0 retornos · 1 mudança de status (correção de `sync`) · status (todas): 115 nova · 91 ativa · 1 aquecendo · 243 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Nove dias sem rodada, lidos por uma fresta.** A anterior foi a de 06/11 às 16h06 (maior ID: 263599289). Não houve rodada de 07 a 14/11, e as passadas 6x/dia seguem paradas desde 18/10. **A API de busca do RA foi negada de novo**, pela quarta rodada seguida, e a rodada não tentou contornar. Sobrou a **lista de 5 linhas**, lida em 9 gateways: Kiwify, Hotmart, Ticto, Eduzz, Monetizze, Kirvano, Lastlink, Payt e PerfectPay. Depois de **8 corpos abertos o RA passou a devolver 429 com a verificação do Cloudflare**, e Cakto, Wiapy, Hubla e Braip ficaram sem leitura. Uma espera e uma nova tentativa não liberaram. As cinco linhas de cada gateway cobrem só **as últimas ~6 a 30 horas de 15/11**, todas com ID acima de 264340000: de uma janela de ~9 dias, a rodada viu talvez 5%. A Biblioteca abriu sem aprovação para 2 buscas.

**Sinal novo real: só na Biblioteca.**
- **[[treino-trinca]]: a verba acelerou.** "treino trinca" foi de ~120 (05/11) para **~200 resultados**, todos os carregados de Pedro Lotz. O mais antigo ativo segue de 22/08 (**`dias_no_ar` 75 → 85**). Há um **criativo novo** ("a metodologia de treino que praticamente todas as Famosas e Atrizes estão usando"), com lotes iniciados em 03, 06, 07 e 10/11. É a terceira leitura seguida com `criativos_delta` positivo (+16, +20, **+80**). No RA entrou +1 (131): o 264369015 diz que **a frente de R$ 37 virou 7x de R$ 42,53 (~R$ 298)** no cartão, perto do upsell de R$ 220 já registrado. Em cinco semanas, a série saiu de "a verba parou?" (27/10) para a maior medição de criativos do vault.
- A segunda busca ("app do paizão") voltou poluída, com ~210 resultados de outros anunciantes misturados, e **não serve como medição**. Ela só confirma que os anúncios de Carlão Silva (`avaliacaogratuitapaizao.com.br`) seguem ativos, com o mais antigo carregado de 05/10.

**RA: gotejamento das mesmas três, nenhuma estreia.**
- [[app-do-paizao]] **51 → 54 (+3)**, **três das cinco linhas da Kirvano**. O 264359355 repete a escada de 27/09, 06/10 e 06/11: "menos de R$ 50" e depois **duas cobranças de R$ 237 e R$ 39** no cartão. O 264345981 chama o produto de "app do personal de TikTok Carlão Silva", e o 264357515 diz que a assinatura cancelada em 20/10 continuou cobrando.
- [[shopminer]] **91 → 92 (+1)**, mas no **gateway novo: Ticto** (264344729, "Shopminer vitalício" mais um "curso da Hayane" no mesmo pedido). É a primeira reclamação do ShopMiner fora da Payt em 92. Ou o produtor abriu um segundo checkout, ou um afiliado/coprodutor revende com um curso acoplado. **A Payt não mostrou ShopMiner nas 5 linhas de hoje**, depois de três leituras seguidas com 2 em 5. Com 5 linhas, isso não diz nada.

**Fila (1 ID cada, sem nota):** produto de **Arthur Benatti** vendido em live (Kiwify 264362177), em que os "cursos adicionais" anunciados seriam liberados **só depois de 7 dias**, e não foram. Upsells em cascata, um deles sem nenhum entregável (Hotmart 264367233, produtor não nomeado). **Só pelo título, sem ID:** Green Stalker (PerfectPay, possível +1 em [[green-stalker]]), claudiaweb.com (Lastlink, possível [[claudia-app]]), Império de Apps e Mentoria Melfi (Payt), Pro Academy e MW Informática 4.0 (Hotmart, renovação automática), Comunidade FMI e Cicatrização da Alma (Eduzz), Presépio Novena (Kirvano, físico). Ninguém da fila de 06/11 (Sambox, jogos bíblicos, Profissão do Futuro, Hora Santa) voltou nas linhas lidas.

**Mecânica de funil.** (1) **Bônus liberado depois da garantia** (Benatti): a oferta promete cursos extras que só abrem no 8º dia. Quem espera para ver o pacote completo perde o prazo de arrependimento. É a versão de calendário do "vitalício que é teste de 21 dias" de 06/11. (2) **Frente de R$ 37 que vira parcelamento de ~R$ 298** (Trinca): o comprador não percebe o upsell como compra separada, só vê as 7 parcelas. É a mesma família do "preço só em vídeo" do Paizão. (3) **Produto de vídeo com segundo checkout e curso acoplado** (ShopMiner na Ticto): se for afiliado, a família "app que gera vídeo" já está na fase de revenda.

**Status.** **1 mudança, e é correção:** o `sync` gravou [[treino-trinca]] como `ativa` (vista hoje). Ela voltou à mão para **`aquecendo`** pela tabela do `Scoring.md` (`criativos_delta` > 0 por 2+ rodadas, agora 3). **Nenhum decaimento manual.** Os 9 gateways foram abertos só nas 5 linhas mais recentes, ~5% da janela, e quatro gateways nem isso. Como em 31/10 e 06/11, aplicar a tabela de ausência aqui contaria buraco de cobertura como esfriamento.

**Cuidados.** (1) Só contaram IDs acima de 263599289, e todos os 8 corpos abertos são de 15/11, entre 09h13 e 18h15. (2) O Trinca tem `ra_reclamacoes` 131 e "~200" anúncios, mas a busca é por palavra-chave: "todos de Pedro Lotz" vale para os carregados (~20), não foi conferido nos 200. (3) A atribuição do Paizão é por nome nos três corpos, sem ambiguidade desta vez. (4) Scores sem mudança: Trinca 6,60 (observar; `s_lucro` 8 mantido, o 9 só a partir de 90 dias, que ele cruza por volta de 20/11 se a verba continuar), Paizão 5,75 e ShopMiner 2,50 (provisório). **Ninguém novo cruza o corte.**

**Autocrítica.** **No RA não houve sinal novo relevante:** 5 IDs em três ofertas já mapeadas, nenhuma estreia, numa janela de nove dias vista por uma fresta de horas. O único dado novo que vale é a série do Trinca na Biblioteca, que dobrou de criativos em dez dias e é hoje a oferta medida com mais segurança no vault. Dois erros de processo: a rodada abriu corpos demais nos primeiros gateways e tomou o 429 antes de chegar a Cakto, Wiapy, Hubla e Braip. Na próxima, vale ler as 13 listas primeiro e só depois abrir corpos. E os nove dias sem rodada não foram culpa do instrumento: **a tarefa diária não rodou de 07 a 14/11**, e nada no vault registra por quê. A pendência da Etapa 3b (`ra_primeira_reclamacao` do ShopMiner, Zap Radar e Paizão) segue aberta pela décima sétima vez, e continua dependendo da API.

---

## Leitura anterior — 2026-11-06 (rodada diaria)

Passada: [[2026-11-06 -- 1606]] · nota do dia: [[2026-11-06]].

**492 notas · 391 ofertas · 101 ângulos · 0 novas hoje · 10 revistas (9 com ID novo, 1 só avistamento) · 0 retornos · 1 mudança de status · status (todas): 115 nova · 91 ativa · 1 aquecendo · 243 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Uma rodada de ~23 horas com o instrumento estreito.** A anterior foi o complemento de 05/11 às 17h12, e a última leitura completa foi a das 09h45 de 05/11 (maior ID: 263440907). A tarefa das 23h30 rodou às 16h06. A API de busca do RA respondeu a uma chamada de teste, mas **a varredura em lote pela API foi negada nesta sessão**, e a rodada não tentou contornar. Sobrou a **lista de 5 linhas por gateway**, lida nos 11 gateways de sempre (PerfectPay, Payt, Kirvano, Kiwify, Lastlink, Cakto, Ticto, Hotmart, Wiapy, Eduzz e Monetizze). Foram 18 corpos abertos, todos com **ID acima de 263440907** e publicados em 06/11. A Biblioteca não foi consultada.

**Sinal novo real: pequeno.** É gotejamento das mesmas ofertas, sem estreia.
- [[shopminer]] **89 → 91 (+2)**, na Payt: 263590861 e 263594469, dois compradores de cidades diferentes que compraram em 05/11 e usam o mesmo texto. **Pela terceira leitura seguida, duas das cinco linhas da Payt são ShopMiner.** Um terceiro título apareceu só em "reclamações parecidas" e não foi contado.
- [[app-do-paizao]] **49 → 51 (+2)**, na Kirvano. O 263586783 dá **três pedidos somando R$ 326,98** (R$ 38,99 + R$ 238,99 + R$ 49,00), e a compradora diz que os valores aparecem só **em vídeo, não por escrito**. É a mesma escada de 27/09 e 06/10, agora com o degrau de R$ 238,99. O 263565517 chama o produto de "aplicativo do Carlão" (R$ 47), o nome do anunciante da Biblioteca.
- [[treino-da-fera]] **10 → 12 (+2)**, na Payt. Um comprador levou "Treino da Fera" e "Treino da Fera **Vitalício**" juntos em 01/11, o que aponta para um bump de acesso vitalício. O outro diz que o e-mail de suporte informado na compra **devolve erro de entrega**.
- Com +1 ID cada: [[velix]] **8** ("Velix 2.0" em **12x de R$ 39,86**, ~R$ 478, com o estorno pedido em 28/10 e negado só em 06/11, depois dos 7 dias), [[stalkea-ai]] 11, [[app-direct-line]] 54 (plano PRO), [[postcloner]] 10 (de novo como "Posh Clone") e o ângulo [[angulo-treino-de-calistenia]] 12.
- [[spygram]] **3 → 4**, ausente desde 29/10. O pagamento foi pelo QR da PerfectPay, mas **a reclamação caiu na lista da Payt**. É o mesmo comportamento da reatribuição da Etapa 3b, só que entre gateways.
- [[fornece-up]]: avistamento sem contagem. O 263587717 é o mesmo comprador reabrindo uma reclamação encerrada (cancelamento em 06/10), e fica em 33.

**Fila (1 ID cada, sem nota):** Sambox (Kirvano 263550183, cancelamento dentro dos 7 dias sem resposta). Kits em PDF de "35 jogos bíblicos" e "kit educacional da palavra de Deus para os filhos", que viraram um curso que não carrega (Kirvano 263566577). "Mentoria Profissão do Futuro", com **quatro bumps no checkout** (Combo Master IA, Arsenal de Vendas Black, Máquina de Recorrência IA e Acesso Permanente) e nenhum entregue (Cakto 263599289). Biblioteca Hora Santa (Cakto 263588225). **Só pelo título, sem ID:** Auto Live Shop (Cakto, 3º avistamento depois dos 2 IDs da fila de 05/11), "aplicativo Criação" (Cakto), CRIE.AI vitalício (Cakto, possível [[crie-ai]]), Método Mini Expert (Payt, possível [[metodo-mini-experts-suelen-mello]]), Mago do Hot e Creator Automatização (PerfectPay), curso Fabio Miudinho (Kiwify), sala de operações da TSR e agentes de IA de Bruno Gabarra (Lastlink), Plano Enriquecer Digital e Workshop Super Públicos (Ticto), app Cozinha Perfeita cobrado de novo e pack de STL (Wiapy), RiseGuide, EmotionLift, AvantPro Ultra e crochê premium (Eduzz).

**Mecânica de funil.** (1) **"Vitalício" que é teste de 21 dias** (calistenia asiática, nome novo na coorte: Fernanda Yamamoto). O app vendido como acesso vitalício libera 21 dias e trava o "nível 2" atrás do plano Pro. É um upsell de assinatura escondido dentro da promessa de pagamento único. (2) **Escada de quatro bumps num checkout só** (Profissão do Futuro). É a versão em largura do que o Xicoria faz em altura: em vez de um bump caro, quatro bumps de nome genérico de IA. (3) **Preço só em vídeo** (Paizão). O degrau de R$ 238,99 não aparece por escrito, e a compradora não reconhece ter aceitado. É a mesma família do "bump não escolhido" do Xicoria.

**Status.** **1 mudança:** [[spygram]] saiu de `nova` para `ativa` pelo `sync`. Não é retorno, porque nunca esteve `esfriando`. **Nenhum decaimento manual.** Os 11 gateways foram abertos, mas só nas cinco linhas mais recentes, umas 3 a 6 horas de uma janela de ~23. As leituras anteriores só decaíram depois de duas leituras completas sem a oferta, e esta não é completa, como a de 31/10.

**Cuidados.** (1) Só contaram IDs acima de 263440907, e nenhum dos 10 IDs do complemento de 05/11 reapareceu. (2) Os dois IDs do ShopMiner têm texto idêntico, mas são de compradores e cidades diferentes, então contam os dois. (3) "Aplicativo do Carlão" foi atribuído ao Paizão pelo nome do anunciante (Carlão Silva) e pelo preço (R$ 47). Se for outro app do mesmo operador, a contagem do Paizão está inflada em 1. (4) Scores sem mudança: Trinca 6,60 (observar), Stalkeia 5,85, Paizão 5,75, Zap Radar 5,00, Velix e Spygram 3,05, Treino da Fera 2,65, ShopMiner 2,50, Fornece Up 2,15, PostCloner 1,90, Direct Line 1,75 e Stalkea 1,05, os de volume alto ainda provisórios. **Ninguém novo cruza o corte.**

**Autocrítica.** **Não houve sinal novo relevante.** São 12 IDs em 9 notas já mapeadas (mais 4 na fila), nenhuma estreia, e um instrumento que viu talvez 20% da janela. A rodada trouxe três mecânicas de funil (o "vitalício" de 21 dias, os quatro bumps e o preço só em vídeo) e o preço do Velix 2.0, e mais nada. A conclusão é a mesma de 29/10, 31/10 e do complemento de 05/11: **o gargalo é o acesso à API do RA, não a cadência.** Uma chamada isolada passou e a varredura foi barrada, então a próxima rodada deve perguntar antes se a leitura em lote está liberada, em vez de descobrir no meio. A pendência da Etapa 3b (`ra_primeira_reclamacao` do ShopMiner, Trinca, Zap Radar e Paizão) segue aberta pela décima sexta vez.

---

## Leitura anterior — 2026-11-05 (rodada diaria, complemento 17h12)

Passadas: [[2026-11-05 -- 0945]] e o complemento [[2026-11-05 -- 1712]] · nota do dia: [[2026-11-05]].

**492 notas · 391 ofertas · 101 ângulos · 0 novas no complemento (6 no dia) · 5 revistas no complemento · 1 retorno · 1 mudança de status · status (todas): 116 nova · 90 ativa · 1 aquecendo · 243 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Segunda rodada do dia, ~7,5 horas depois da primeira, com o instrumento estreito.** A das 09h45 leu a janela inteira pela API (maior ID: 263440907). Este complemento cobre só a tarde. **Executar JS na aba do RA foi negado de novo**, então a API de busca ficou fora e sobrou a **lista de 5 linhas por gateway**, como no complemento de 29/10. Foram lidos Payt, Kirvano, Kiwify e Lastlink, com corpos abertos, e Cakto e Hotmart só pela lista, porque **o acesso ao RA no navegador foi recusado no sétimo gateway**. PerfectPay, Ticto, Wiapy, Eduzz e Monetizze ficaram sem leitura. Ao todo, 10 corpos abertos, todos com **ID acima de 263440907**: 6 atribuídos a notas e 4 para a fila. A Biblioteca não foi consultada.

**Sinal novo real: pequeno.** É gotejamento das mesmas ofertas, sem estreia.
- [[shopminer]] **87 → 89 (+2)**, na Payt: 263490617 (R$ 297) e 263495429 (R$ 344 via Pix, comprado em 30/10). **Duas das cinco linhas da Payt da tarde são ShopMiner.** É o mesmo ritmo da manhã (~4 por dia), e ele não desacelerou depois da janela de 31/10.
- [[manual-do-hormonio-xicoria-team]] **4 → 5**, e o dado que importa é o preço. O 263475049 mede a escada pela primeira vez: **e-book de R$ 77 e mais R$ 298 de uma "consultoria que NÃO CONTRATEI"**, debitados no mesmo checkout, com reembolso negado dentro dos 7 dias. A nota trazia `ticket_frente: 300`, que era o preço da assinatura. Foi corrigida para `ticket_frente: 77`, `ticket_bump: 298`, `ticket_medio_est: 375` e `tem_recorrencia: true`. O `s_ticket` segue 10 e o score não muda (3,75, provisório).
- [[zap-radar]] **chega a 100** (263484877, R$ 137, "só recebi relatório falso"). [[app-do-paizao]] **49** (263472117, plano mensal comprado em 31/10, estorno recusado dentro dos 7 dias).
- **Retorno:** [[clipshort-ai]] (Kirvano, 5 → 6, ausente desde 20/10). O 263487929 traz uma mecânica nova: o comprador **pagou R$ 67,99 de novo porque o suporte avisou que a geração de vídeos tinha sido consertada**, e ela segue sem funcionar. É a recompra induzida pelo suporte, na mesma família "app que gera vídeo" do ShopMiner e do PostCloner.

**Fila (1 ID cada, sem nota):** NotificaShop (Kiwify 263475617, R$ 49,90, compra em 30/10). App "intestino blindado", com renovação anual de R$ 199 cobrada por link, que a dona do app não responde (Kiwify 263467939). Um "app para gerar vídeos" sem nome, divulgado por Instagram fechado (Lastlink 263473687), que pode ser a [[turbo-vendas]] e não foi atribuído. Uma plataforma de R$ 697 sem nome, que "quer obrigar a permanecer" (Kirvano 263469069). Ficaram sem abrir, só na lista: lupadocasal.online (Payt), "Aplicativo da criação" R$ 99 (Payt) e Clube da Agulha (Lastlink, "módulos vazios").

**Mecânica de funil.** (1) **O bump de assinatura do Xicoria agora tem número:** frente de R$ 77 e bump de R$ 298, quase 4x. É o primeiro caso do vault com bump medido maior que a frente, e os cinco corpos descrevem o bump como não escolhido, ou seja, pré-marcado ou embutido. (2) **Recompra induzida pelo suporte** (ClipShort): em vez de reembolsar, o suporte promete o conserto e o cliente paga de novo. Na prática é um downsell às avessas, e infla o RA por comprador.

**Status.** **1 mudança:** [[clipshort-ai]] saiu de `esfriando` para `ativa`, pelo `sync`, como retorno. O decaimento não foi reaplicado. Os gateways desta tarde já tinham sido lidos por inteiro às 09h45, o sync conta o dia como uma rodada só, e aplicar de novo contaria a mesma ausência duas vezes.

**Cuidados.** (1) Só contaram IDs acima de 263440907, e todos os 10 lidos são de 05/11 entre 12h17 e 16h02. (2) Este complemento leu ~5 linhas em 4 gateways, contra ~65 por gateway às 09h45. **Zero estreias aqui é instrumento estreito, não mercado parado.** (3) As quatro notas que já tinham `## Rodada 2026-11-05` receberam o complemento numa seção própria, anexada à mão. O snapshot do dia não foi tocado (append-only). (4) O `--leitura` do `publicar.py` sobrescreveu a leitura das 09h45 na nota do dia, e ela foi restaurada à mão ao lado da do complemento. (5) Scores sem mudança: Trinca 6,60 (observar), Stalkeia 5,85, Paizão 5,75, Zap Radar 5,00, Xicoria 3,75, ShopMiner 2,50 e ClipShort 2,30, os três últimos provisórios. **Ninguém novo cruza o corte.**

**Autocrítica.** **Não houve sinal novo relevante neste complemento.** O único dado novo de qualidade é o preço medido do Xicoria. O resto confirma o ritmo que a manhã já tinha mostrado. É a mesma conclusão do complemento de 29/10: com a primeira rodada do dia tendo lido tudo pela API, a segunda rende pouco, e rende menos ainda quando a API não está disponível. O gargalo continua sendo **acesso** (JS na aba do RA, aprovação de site), não cadência. A pendência da Etapa 3b (`ra_primeira_reclamacao` do ShopMiner, Trinca, Zap Radar e Paizão) segue aberta pela décima quinta vez, e não dá para fechá-la sem a API.

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
