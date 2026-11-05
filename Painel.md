---
tipo: painel
atualizado: 2026-11-05
---

# Painel — Radar Low Ticket

A leitura consolidada. As tabelas abaixo são vivas: mudam sozinhas quando a rodada
diária grava. O texto entre elas é o que a rodada **concluiu** — é a única parte que
precisa ser reescrita, e a tarefa agendada reescreve.

---

## Leitura atual — 2026-11-05 (rodada diaria, complemento 17h12)

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

## Leitura anterior — 2026-11-05 (rodada diaria, 09h45)

Passada: [[2026-11-05 -- 0945]] · nota do dia: [[2026-11-05]].

**492 notas · 391 ofertas · 101 ângulos · 6 novas hoje · 29 revistas · 4 retornos · 12 mudanças de status · status (todas): 116 nova · 89 ativa · 1 aquecendo · 244 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**O instrumento voltou inteiro.** A anterior foi a de 31/10 às 20h43 (maior ID: 263094707). Não houve rodada de 1º a 4/11, e as passadas 6x/dia seguem paradas desde 18/10. Executar JS na aba do RA **voltou a ser permitido**, e a API de busca (`iosearch`) respondeu sem desafio do Cloudflare. Foram **78 chamadas de 10, nos 11 gateways de sempre (a Braip ficou fora: não tem `identifier` registrado no adendo de 11/10)**, cada um paginado até passar de 31/10 20h40. Isso deu **700 reclamações únicas**, cerca de 4,5 dias de janela **completa**, e uns 40 corpos abertos para confirmar nome e preço. É a primeira leitura completa desde 29/10 às 13h55. A Biblioteca abriu sem aprovação para 3 buscas.

**Sinal novo real: sim, e concentrado em ferramenta de vídeo/venda.**
- **[[shopminer]] +19 (68 → 87), todos na Payt.** É o maior volume da janela: 19 das 142 reclamações da Payt, que passou a ser o gateway mais reclamado depois da Hotmart. As compras vão de 14/10 a 04/11, e o padrão é cancelar no dia seguinte porque o app não gera os vídeos. **A Biblioteca devolve zero anúncios para "shopminer" e para "shop miner" (frase exata).** Com esse volume de compradores, a aquisição não é Meta. Pelo resto da janela, o suspeito é live no TikTok, mas isso não foi medido.
- **Família "app que gera vídeo para vender" cresceu em quatro nomes de uma vez:** [[tokscale-ia]] +7 (42), [[postcloner]] +6 (3 → 9, triplicou), [[velix]] +4 (7, vendido "em live no TikTok pelo Luan" como ferramenta de afiliado do Mercado Livre, R$ 132,72 de assinatura) e as estreias [[videoshop]] (Kirvano, 3) e [[turbo-vendas]] (Lastlink, 3, R$ 49/mês, vídeo automático a partir de link de produto do TikTok/Shopee). Nenhum desses aparece com verba relevante na Meta.
- Assinatura que não cancela: [[app-do-paizao]] +8 (48) e [[app-direct-line]] +7 (53). Os dois seguem no mesmo ritmo das rodadas de 26-29/10.
- [[treino-trinca]]: a Biblioteca foi de ~100 para **~120 anúncios**, mais antigo de 22/08 (**`dias_no_ar` 70 → 75**), e o status virou **`aquecendo`** (`criativos_delta` +16 e +20, duas rodadas seguidas). No RA entraram só +2, e um deles é o **Pix de R$ 997 do "pacote TF1000"** não devolvido (263163939), o upsell alto da escada.

**Estreias (6).** [[manual-do-hormonio-xicoria-team]] (Kirvano, 4 IDs) é a mais interessante. O e-book "Manual do Hormônio" de Tim Chicoria leva o comprador, no checkout, a contratar a assessoria "Xicoria Team" por **~R$ 300/mês**. Os quatro pedem estorno **da assinatura, não do e-book**. A busca "manual do hormônio" na Biblioteca devolveu outra marca (Manual, telemedicina, ~170 anúncios) e não serve como medição. As outras: [[videoshop]] e [[turbo-vendas]] (acima), [[claudia-app]] (Lastlink, app de inglês, pagamento pela Adyen, 3), [[metodo-produto-viral-fernanda-cardoso]] (Hotmart, 3, "produtos virais prontos" que são prompts de ChatGPT) e o ângulo [[angulo-taxa-de-acesso-a-vagas-home-office]] (PerfectPay, 5 IDs, "taxa única" de R$ 37,90-39,90 e depois novo Pix para sacar).

**Retornos (4):** [[instalador-robo-pronto-2]] (+1), [[ecossistema-low-ticket-nathan-kurnick]] (+2), [[natflix-fitness]] (+2, renovação automática que não cancela) e o ângulo [[angulo-streaming-doramas-turcas]] (+4), agora na Wiapy com três nomes: Cinerama, Cinekadrama e Cinedramatv.

**Gotejamento:** [[zap-radar]] +6 (99, um comprador somou R$ 509), [[green-stalker]] +5 (9, "pagamento único de R$ 67" e depois Pix para "adicionar crédito"), [[treino-da-fera]] e [[metodo-mini-experts-suelen-mello]] +4, [[stalkeia-ai]], [[atmoz]] (agora também na Cakto, R$ 297), [[fornece-up]], [[o-truque-da-loto-pro]] (o preço subiu de R$ 97 para **R$ 149**), [[crie-ai]], [[loopyz]] e o ângulo de calistenia (nome novo: "Calistenia Shaolin") +3. [[desafio-hiit-dance]], [[spinmaster]], [[bicarbonapp]], [[anunciaie]] e [[stalkea-ai]] +2. [[chatgpt-privado]] e [[operax]] +1.

**Fila, para somar por ID (2 IDs cada, sem nota):** FlashShortz (Cakto 263099779, 263352369), Auto Live Shop / Livespace (Cakto), "Tik Tok Lucrativo" de Carol Cardoso (Payt), Betaprost (Payt, físico), "O Segredo da Insulina" / Clube do Segredo (Lastlink e Payt), Renda Play (Kiwify, 2º ID depois do 262951069), Fiado Prático / Estoque Fácil (Kiwify), Movva Broker com saldo retido (PerfectPay), Tube Recompensas / Perfect Tube (PerfectPay) e Dominando a Fome (Hotmart). Ninguém da fila de 31/10 (ARES B3, Cupom de Prêmios) voltou.

**Mecânica de funil.** (1) **Assinatura cara induzida no checkout de um e-book barato** (Xicoria). É um order bump recorrente de ~R$ 300/mês acoplado a um low ticket, e é o primeiro caso no vault em que o bump vale mais que a frente. (2) **Ferramenta de vídeo vendida em live, fora da Meta** (ShopMiner, Velix, Turbo Vendas). O RA vê o volume, mas a Biblioteca não vê a aquisição, e o par de instrumentos fica cego justo na família que mais cresce. (3) **"Pagamento único" seguido de recarga** (Green Stalker, vagas home office, Stalkeia). É a escada de taxa de sempre, agora também fora de espionagem.

**Status.** São **12 mudanças**. Os 4 retornos voltaram para `ativa` pelo `sync`, e [[green-stalker]] e [[desafio-hiit-dance]] saíram de `nova`. O [[treino-trinca]] foi para `aquecendo` à mão, pela tabela do `Scoring.md`. **5 notas** `ativa` vistas pela última vez em 27/10 ficaram fora das duas leituras completas seguintes (29/10 às 13h55 e hoje) e foram para `esfriando`: [[beto-ia]], [[bike-in-casa]], [[lift-gold]], [[luke-zap]] e [[mentoria-nova-profissao-gustavo-castro]]. O decaimento só valeu para os 11 gateways lidos por inteiro e manteve as exclusões das leituras anteriores. Nenhuma de comportamento infantil foi decaída por ausência no RA. Nenhuma nota foi para `morta`: a regra crua de 7+ rodadas pegaria ~210 notas `esfriando`, mas a maioria dessas rodadas foi de lista de 5 linhas e não de leitura completa.

**Cuidados.** (1) Só contaram IDs acima de 263094707. O 262778703 do Zap Radar, recarimbado em 03/11, já estava contado em 29/10 e ficou fora. Os IDs baixos recarimbados (263074187, 262758757, 263059951) também ficaram fora. (2) O 263287601 ("stalke ai", 37 + 37 + 67 + 97) e o 263397659 (genérico) não foram atribuídos a nenhum Stalke*. (3) A VideoShop estreia com o 262940693, da fila de 29/10, que foi lido e nunca contado. Não há contagem dupla. (4) Scores: Trinca 6,60 (observar), Stalkeia 5,85, Paizão 5,75, Zap Radar 5,00, Trendly 4,70 e Atmoz 4,30. ShopMiner fica em 2,50, TokScale e Direct Line em 1,75 e PostCloner em 1,90, todos provisórios: volume alto e score baixo porque `s_ticket`/`s_replica` seguem sentinela. As estreias ficam entre 1,05 e 3,75, provisórias. **Ninguém novo cruza o corte.**

**Autocrítica.** **Desta vez houve sinal novo real, e a diferença foi o instrumento, não a cadência.** A lista de 5 linhas de 31/10 teria visto no máximo 55 das 700 (cinco por gateway), ~8% da janela. O achado que importa é estrutural: **a família que mais cresce no RA (ShopMiner, TokScale, PostCloner, Velix) é invisível na Biblioteca**, então `dias_no_ar` e `criativos` nunca vão sair para ela pela Etapa 1, e o score delas fica travado em provisório por construção. A rodada não resolveu isso: o próximo passo é a Etapa 3b com a API (`ra_primeira_reclamacao` do ShopMiner pela paginação até o fim), que mede idade sem anúncio. Essa pendência, junto com a do Trinca, Zap Radar e Paizão, segue aberta pela décima quarta vez. A rodada também gastou 3 buscas na Biblioteca e só uma (Trinca) mediu algo.

---

## Leitura anterior — 2026-10-31 (rodada diaria)

Passada: [[2026-10-31 -- 2043]] · nota do dia: [[2026-10-31]].

**486 notas · 386 ofertas · 100 ângulos · 0 novas hoje · 7 revistas · 1 retorno · 2 mudanças de status · status (todas): 112 nova · 89 ativa · 243 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Uma rodada de ~47 horas com o instrumento mais estreito desde 11/10.** Não houve rodada em 30/10. A anterior foi o complemento de 29/10 às 21h26 (maior ID lido: 262959519). As passadas 6x/dia seguem paradas desde 18/10. **Executar JS na aba do RA foi negado de novo**, então a API de busca ficou fora. Sobrou a lista de 5 linhas, e a paginação por clique continua sem trocar a lista (`?pagina=2` devolve as mesmas cinco). Foram **12 gateways, 1 página cada**, as 11 de sempre mais a Braip. Depois de **8 corpos abertos, o RA passou a exibir a verificação anti-bot do Cloudflare** ("Just a moment…"). A página não liberou depois de duas esperas, e a rodada não tentou contorná-la. As cinco linhas de cada gateway cobrem só de ~30/10 22h até agora, umas 19 das ~47 horas. A Biblioteca abriu sem aprovação para 2 buscas.

**Sinal novo real: só na Biblioteca, e responde à pergunta que estava aberta.**
- **[[treino-trinca]]: a verba não parou.** "treino trinca" foi de ~84 (26/10) para **~100 resultados**, todos os carregados de Pedro Lotz. O mais antigo carregado é de 22/08 (**`dias_no_ar` 60 → 70**), e há **5 criativos iniciados de 26 a 28/10**, nenhum de 29 a 31/10. A pergunta de 27/10 (coorte esgotada ou reembolso funcionando) ganha meia resposta: **o silêncio do RA desde 27/10 não é a oferta saindo do ar.** Ou o reembolso passou a funcionar, ou os compradores novos ainda estão dentro dos 7 dias. A série do RA segue em 2 IDs em 46 horas e 0 nas cinco linhas da Lastlink hoje. O frontmatter ainda guardava o 140 de 21-23/10, e foi corrigido para `criativos_ultima: 100`, `criativos_delta: +16` contra a leitura de 26/10.
- **[[atmoz]]: segunda leitura, e a verba segue subindo.** De ~110 para **~120 anúncios**, ainda de um anunciante só (John Atmoz Rodrigues, `inteligenciajohn.com/atmoz`). Há **5 iniciados em 29/10 e 1 em 30/10**, e o mais antigo segue sendo de 18/10 (`dias_no_ar` 13). Nas cinco linhas da Kirvano não houve ID novo, o que com 5 linhas não diz nada. O status saiu de `nova` para `ativa`. Ainda não é `aquecendo`, que pede `criativos_delta` > 0 por 2+ rodadas, e esta é a primeira com delta.

**RA: 4 IDs novos, nenhum nome novo com ritmo.**
- [[chatgpt-privado]] 8 → **9** (Kirvano 263094041), o primeiro desde 11/10. "CHAT GPT PRIVADO [G]" por R$ 67 no Pix. **Prometia credencial privada e entregou um tutorial no Telegram para pegar uma promoção gratuita.** O produtor recusou o reembolso dentro dos 7 dias alegando "produto digital resgatado". É provável que seja o mesmo "ChatGPT GO sem credencial" da fila de 29/10 (262947323). Não foi somado, porque o nome não bate.
- Com +1 ID: [[fornece-up]] **30** (comprado em 11/10, "cadastrei diversos produtos e nenhuma venda", 263068407) e [[app-direct-line]] **46** (comprado em 30/10, cancelamento pedido no mesmo dia sem resposta, 263090227).
- **Retorno: [[arsenal-lucrativo]]** (Cakto, 3 → 4, `esfriando` → `ativa`). É o nível "Flow Ultra", com renovação automática cobrada em 18/10. O corpo (263094707) diz que **restrições do Google no início de outubro** impediram o uso, e que o suporte prometeu cancelar a renovação de todos e migrar para um serviço novo. É a primeira menção a uma ferramenta derrubada por mudança de plataforma, e não por fraude.
- [[trendly]]: avistamento sem contagem. O 263072749 repete o texto do 262754769, contado em 29/10 (R$ 239,76 em março): é o mesmo comprador reabrindo, agora com a PerfectPay negando pelo prazo de 7 dias.

**Fila, para a próxima rodada somar por ID (1 ID cada):** "ARES B3 - B3" (Kirvano 263090387, comprado em 31/10, suporte "só em dias úteis" antes do feriado de segunda). Pelo nome, é trading/B3. "Cupom de Prêmios", app de jogo com "saldo bloqueado" (PerfectPay 263060223), da família "taxa para liberar". Sem corpo aberto, só pelo título: Descomplicart R$ 97 e Fábrica de Comissões (Kiwify), Vitrine Lucrativa (Eduzz), Slim Detox Caps (Monetizze), "jogos virtuais" (Payt), Hi Spy (Ticto, possível [[hi-spy-4-0]]), dicas de Pilates (Lastlink), Teacher Zap vitalício (Lastlink, possível [[teacher-zap]]), Perfect Lizz e Lift Gold (Monetizze, possíveis [[perfect-liss]] e [[lift-gold]]), Gold Card TV (Braip, possível [[gold-card-tv]]), ShopMiner (Payt) e "plantas de casa" (Wiapy, 2º título depois do 262947487 de 29/10). **Esses 11 ficaram sem ID porque o Cloudflare cortou a leitura antes, e não entram na conta.**

**Mecânica de funil.** (1) **"Credencial privada" que é tutorial de promoção gratuita** (ChatGPT Privado). É a mesma família do "ChatGPT GO sem credencial": vende-se o acesso, entrega-se o caminho para o acesso grátis. (2) **Suporte só em dia útil na véspera de feriado** (ARES B3), para gastar o prazo de 7 dias. É a versão de calendário do "suporte não responde". (3) **Assinatura que sobrevive ao fim do produto** (Flow Ultra): a ferramenta parou por restrição do Google, e a renovação automática seguiu cobrando.

**Gargalos do instrumento.** (1) **O RA fechou as duas portas na mesma sessão:** a API (JS negado) e, depois de 8 corpos, a própria página (Cloudflare). Se isso se repetir, **a rodada passa a ler títulos, não IDs**, e a regra de 27/08 (só o ID conta) deixa quase tudo na fila. (2) As 5 linhas cobrem ~19 de ~47 horas. **As contagens desta rodada não são comparáveis nem com as do complemento de 29/10**, que abriu ~45 corpos. (3) A Biblioteca foi a única fonte que respondeu inteira. Com 2 buscas por rodada sem aprovação, as melhores perguntas são as de série (Trinca, Atmoz), não as de descoberta.

**Status.** São **2 mudanças**: [[arsenal-lucrativo]] voltou para `ativa` pelo `sync` (retorno de `esfriando`) e [[atmoz]] saiu de `nova` para `ativa`. **Nenhum decaimento manual.** Os 12 gateways foram abertos, mas só nas cinco linhas mais recentes, ~40% da janela. As leituras anteriores só decaíram depois de "duas leituras completas" sem a oferta, e esta não é completa. Aplicar a tabela aqui contaria buraco de cobertura como esfriamento, que é exatamente o que o `sync` evita de propósito.

**Cuidados.** (1) As 7 "revistas" incluem 2 que vieram só da Biblioteca (Trinca e Atmoz), com `mencoes` igual à contagem anterior: o snapshot registra o avistamento, não um ID novo. (2) O Trendly ficou em 4 pela regra do comprador reabrindo. (3) Scores sem mudança: Trinca 6,60 (observar, `s_lucro` 8 na faixa de 45-90 dias), Stalkeia 5,85, Paizão 5,75, Zap Radar 5,00, Trendly 4,70, Atmoz 4,30 (provisório), ChatGPT Privado 3,00 e Arsenal Lucrativo 0,70 (provisório). Ninguém novo cruza o corte.

**Autocrítica.** **No RA não houve sinal novo relevante:** 4 IDs em ofertas já mapeadas e nenhuma estreia, com um instrumento que viu 40% da janela. O que a rodada acrescenta de verdade são duas leituras de série na Biblioteca. O Trinca continua comprando anúncio enquanto o RA silencia, e isso muda a leitura dos últimos quatro Painéis. A Atmoz tem agora duas medições com verba subindo. A cadência diária não é o gargalo: **o gargalo é o acesso ao RA.** Sem a API, uma rodada de 47 horas rende menos que o complemento de 7,5 horas de 29/10. A pendência da Etapa 3b (`ra_primeira_reclamacao` do Trinca, do Zap Radar e do Paizão) segue aberta pela décima terceira vez, e agora também depende de o RA voltar a responder.

---

## Leitura anterior — 2026-10-29 (rodada diaria, complemento 21h26)

Passadas: [[2026-10-29 -- 1355]] e o complemento [[2026-10-29 -- 2126]] · nota do dia: [[2026-10-29]].

**486 notas · 386 ofertas · 100 ângulos · 0 novas no complemento (4 no dia) · 9 revistas no complemento · 0 mudanças de status · status (todas): 113 nova · 87 ativa · 244 esfriando · 42 morta · 1 no corte ([[little-genius]], 7,60, sem mudança)**

**Segunda rodada do dia, ~7,5 horas depois da primeira.** A tarefa das 23h30 rodou às 21h26, e a das 13h55 já tinha lido ~46 horas pela API. Este complemento cobre só o intervalo entre as duas. **O instrumento piorou:** a API de busca do RA (`iosearch.reclameaqui.com.br`) devolveu um desafio do Cloudflare ("Attention Required"), e executar JS dentro da aba foi negado nesta sessão. Sobrou a **lista de 5 linhas por gateway**, a mesma do adendo de 23/08, aberta pelo navegador interno, com os corpos lidos um a um. Foram **11 gateways, 1 página cada e ~45 corpos abertos**. Desses, **25 IDs estão acima do maior citado às 13h55 (262916077)**. Ticto, Lastlink, Eduzz e Monetizze não tiveram nenhum: as cinco linhas de cada um eram de 27 e 28/10, já lidas. A Biblioteca não foi consultada.

**Sinal novo real: pequeno.** É gotejamento das mesmas ofertas, sem estreia e sem nome com ritmo novo.
- [[app-do-paizao]] **38 → 40 (+2)**, na Kirvano. Um dos corpos traz a mecânica: o plano **mensal de R$ 47,01 virou cobrança única de R$ 229,99** no checkout (262927087). É o mesmo degrau "mensal → anual" que a leitura das 13h55 descreveu como empurrado por vídeo dentro do app, só que aqui aparece já na compra. O outro corpo traz **compra em 05/08** (262959519), a data mais antiga já lida num corpo do Paizão.
- Com +1 ID cada: [[zap-radar]] 93 (R$ 137 na PerfectPay), [[fornece-up]] 29 ("centenas de influenciadores no TikTok fazendo lives"), [[operax]] 5 (R$ 97, Payt), [[tokscale-ia]] 35 (pedido de **29/07**, ou seja, vende há pelo menos três meses), [[o-truque-da-loto-pro]] 13 (R$ 97), [[crie-ai]] 10 e [[app-direct-line]] 45 (comprado por **anúncio no Instagram**, Cakto).
- [[shopminer]]: avistamento sem contagem. O 262945537 é o mesmo comprador reabrindo o 261303597, já contado em 11/10 (R$ 267 vitalício, reembolso parcial de R$ 36,56).

**Fila, para a próxima rodada somar por ID (1 ID cada, nenhum chegou a 3):** VideoShop, um APK que trava o celular (Kirvano 262940693). ChatGPT GO sem credencial entregue (Kirvano 262947323), que pode ser o mesmo vendedor da nota [[chatgpt-privado]], onde o Go já aparecia como "provável, não contada". Renda Play R$ 49,90 + Pro R$ 29,90 via Pix (Kiwify 262951069). Manual do Afiliado 2.0 + grupo VIP de Anderson Gavineski (Kiwify 262928885). "+1.300 Animações de Exercícios", vendido por anúncio no Instagram (Wiapy 262944409). Fábrica de Renda com Vídeos + Código das IAs, dois cursos do mesmo comprador (Hotmart 262955095). "Ferramenta BOT I.A do Caio Martins" (Cakto 262945673). Pode ser o [[instalador-robo-pronto-2]] ou a [[mentoria-caio-martins]], então não foi atribuída. Também: "plantas de casa" (Wiapy 262947487) e "material Kids" com adicionais (Wiapy 262929703).

**Mecânica de funil.** (1) **Troca de plano no checkout.** No Paizão, quem escolheu o mensal levou a cobrança única (262927087). Se isso se repetir, é um ticket médio inflado pelo checkout, não pelo upsell. (2) **TikTok live como canal**, de novo: Fornece Up e uma plataforma sem nome na Payt (262957579, "compra de uma plataforma em uma live no TikTok"). É o mesmo canal da [[velix]], e o instrumento não o vê.

**Gargalos do instrumento.** (1) **A API do RA caiu atrás do Cloudflare.** É a primeira vez desde 11/10. Se persistir, a regra de 24/08 ("5 sinais por gateway por rodada") volta a valer, e **as contagens deste complemento não são comparáveis com as das 13h55**. (2) **O carimbo movido, ao vivo:** dois IDs da Fornece Up de 26 e 27/10 (262641247, 262722243) aparecem com carimbo de 29/10 12h43 e 13h03. A lista ordena por atividade, e só o ID separou o novo do relido, como manda o adendo de 27/08. (3) Os corpos das "reclamações parecidas" trazem o carimbo de outras quatro reclamações do mesmo gateway. Isso ajudou a achar o 20h45 da PerfectPay ("estorno do meu curso e da IA"), que não estava na lista. Ficou sem abrir.

**Status.** **Nenhuma mudança.** As 9 ofertas revistas já tinham sido vistas às 13h55. O sync conta o dia como uma rodada só, e o decaimento dos 11 gateways já foi aplicado de manhã. Aplicar de novo contaria a mesma ausência duas vezes.

**Cuidados.** (1) Este complemento leu ~5 linhas por gateway, contra as ~30 por gateway das 13h55. **Zero estreias aqui não quer dizer mercado parado, quer dizer instrumento estreito.** (2) Como as notas já tinham a seção `## Rodada 2026-10-29`, os IDs do complemento foram anexados à mão no fim de cada nota. O snapshot do dia não foi tocado (append-only). (3) Scores sem mudança: Trinca 6,60 (observar), Stalkeia 5,85, Paizão 5,75, Zap Radar 5,00 e Atmoz 4,30 (provisório). Ninguém cruza o corte.

**Autocrítica.** **Não houve sinal novo relevante neste complemento.** Ele confirma que as ofertas com ritmo seguem pingando, com o Paizão de novo à frente, e acrescenta dois dados de idade por data de compra (Paizão em 05/08, TokScale em 29/07). Ainda assim, não entram como `dias_no_ar`, porque são uma compra só cada. A cadência diária com duas rodadas no mesmo dia rende pouco quando a primeira já leu tudo. O que segura a próxima rodada é o acesso à API, não a hora em que ela roda. A pendência da Etapa 3b (`ra_primeira_reclamacao` do Trinca, do Zap Radar e do Paizão) segue aberta pela décima segunda vez.

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
