---
tipo: meta
---

# Pipeline de mineração

Ordem fixa. Cada etapa alimenta um campo específico do `Schema.md` — se você pular uma
etapa, o score sai enviesado e a Base mente.

## Etapa 1 — Biblioteca de anúncios (descoberta)

Ferramenta: **claude-in-chrome** (`mcp__claude-in-chrome__*`).

1. `tabs_context_mcp` → ver o que já está aberto. Nunca reaproveitar tab de sessão antiga.
2. `tabs_create_mcp` + `navigate` → biblioteca de anúncios da plataforma alvo.
3. `get_page_text` / `read_page` → extrair anunciante, tempo no ar, contagem de criativos.
4. Filtrar por: **mínimo 7 dias no ar** e **2+ criativos ativos**. Abaixo disso é teste,
   não é oferta validada — não gasta rodada com isso.

Campos que saem daqui: `dias_no_ar`, `criativos_ultima`, `url_ads`, `plataforma_ads`.

> A extensão unFunnelizer tem um **FB Ads Spy** próprio com filtro de mín-criativos e
> badge de dias-ativo, e exporta CSV/JSON. Quando o volume for grande, use ele em vez de
> raspar a página: é mais rápido e já sai estruturado.

## Etapa 2 — unFunnelizer (dissecar o funil)

Ferramenta: **controle de desktop** (`mcp__remote-devices__computer_*`), não o
claude-in-chrome. Motivo: o unFunnelizer vive no *side panel* da extensão, fora do DOM da
página — os tools de browser não alcançam. É preciso clicar de verdade.

Antes da primeira vez: `computer_resolve_access` com "Google Chrome" → passar o resultado
**literal** para `computer_request_access` → Lucas aprova.

Na página de vendas da oferta:

| Recurso do unFunnelizer | O que extrair | Vai para |
|---|---|---|
| **Smart Mode** | botões de compra atrasados, depoimentos, ofertas ocultas | corpo da nota: Funil |
| **Brute Mode** | tudo que estava escondido — order bump, downsell, upsell oculto | `ticket_bump`, `ticket_upsell` |
| **Find Links** | URL do gateway de pagamento (varre DOM + scripts) | `checkout`, `gateways_detectados` |
| **Assets Capture → Download All** | imagens e vídeos do funil | `Ativos/<slug>/` |
| **FB Ads Spy → export** | CSV/JSON dos criativos | `Ativos/<slug>/ads.csv` |

Downloads caem na pasta padrão do Chrome. **Mover para `Ativos/<slug>/`** antes de
commitar — o schema espera esse caminho em `ativos_pasta`.

O **Brute Mode é a etapa que mais muda o score**: order bump e upsell escondidos
mudam `ticket_medio_est`, que muda `s_ticket`. Oferta que parece de R$27 vira de R$90.

## Etapa 3 — Reclame Aqui (validação de volume real)

Contra-intuitivo mas é o sinal mais honesto do pipeline: **reclamação é prova de venda.**
Ninguém reclama de produto que ninguém comprou. Volume de reclamações recentes numa
plataforma de checkout é proxy direto de faturamento.

Buscar o nome do produto e o nome do anunciante nestas plataformas:

- Perfect Pay
- Cakto
- Kirvano
- LastLink
- Wiapy
- Lowify
- Kiwify, Hotmart, Ticto, Monetizze, Eduzz (as tradicionais, manter)

O que registrar: `ra_reclamacoes`, `ra_plataformas`, `ra_primeira_reclamacao`.

Leitura dos números:

| Reclamações (30d) | Leitura |
|---|---|
| 0 | ou é nova, ou não vende — cruze com `dias_no_ar` antes de concluir |
| 1-5 | vendendo, volume baixo/médio |
| 6-20 | volume relevante, `s_lucro` +1 |
| 20+ | escala real, `s_lucro` +2 (teto 10) |

Cuidado com o falso negativo: oferta de 90 dias no ar com **zero** reclamação
geralmente significa que o nome comercial na RA é outro. Procure pelo CNPJ ou pelo nome
do gateway antes de dar `s_lucro` baixo.

## Etapa 4 — Gravar

Na ordem: snapshot em `Observacoes/` → atualizar/criar `Ofertas/` → nota da rodada em
`Radar/` → `./_meta/radar-commit.sh`.

## Etapa 5 — Ler o movimento

`./_meta/radar-diff.sh` mostra o diff entre as duas últimas rodadas. É onde a tendência
aparece: não em quem está no topo do ranking hoje, mas em quem subiu desde ontem.

---

## Exceção de nicho — quando a Etapa 3 não vale (registrado 2026-08-21)

**Comportamento infantil e parentalidade não deixam rastro no Reclame Aqui.** Varredura
completa de 5 gateways (PerfectPay, Cakto, Kiwify, Hotmart, Ticto), 40 páginas cada,
~1.000 reclamações e ~180 corpos abertos devolveu **4 batidas no nicho** — e duas delas
eram tangenciais.

Por quê: ticket de R$ 7 a R$ 47, entrega imediata por e-mail, garantia de 7 dias honrada,
e vergonha. Reclamar publicamente é admitir que comprou um manual para lidar com o
próprio filho. O comprador some, não briga.

**Como aplicar:** neste nicho — e provavelmente em qualquer um com ticket baixo + carga
de estigma (saúde mental, sexualidade, dificuldade financeira pessoal) — inverta a ordem
do pipeline. A Biblioteca de Anúncios vira Etapa 1 *e* fonte de volume; o Reclame Aqui
vira etapa opcional de confirmação. E **não leia `ra_reclamacoes: 0` como sinal de baixo
volume**: aqui zero é o esperado.

Nichos onde a Etapa 3 continua valendo: espionagem, cashback/Pix, apostas, trading, IA,
streaming — todos com mecânica de "taxa pra liberar", que é o que faz o comprador brigar.

---

## Adendo — o que fazer quando so a Etapa 3 esta disponivel (2026-08-23)

Quinta rodada consecutiva sem Biblioteca de Anuncios e sem unFunnelizer. O pipeline
escrito acima pressupoe as tres etapas; sem as duas primeiras ele nao degrada com
elegancia, entao aqui esta a versao curta do que funciona.

**1. Ler o corpo, nao so o titulo.** O titulo da reclamacao e um resumo gerado; o corpo
tem data de compra, valor pago e a escada de ofertas. Em 22/08 o [[app-do-paizao]] foi
pontuado pelo titulo e a nota inteira estava errada — o corpo estava a uma requisicao de
distancia. **Data de compra no corpo e o melhor proxy de `dias_no_ar` disponivel sem
browser**, e mede a oferta em vez do anuncio.

**2. A lista de reclamacoes so entrega as 5 mais recentes por requisicao.** Paginacao nao
esta acessivel. Consequencia pratica: cada gateway rende no maximo 5 sinais por rodada, e
**ampliar o numero de gateways rende mais que aprofundar em um**. Cobertura atual: Lowify,
Wiapy, Lastlink, Kirvano, PerfectPay, Ticto, Kiwify, Hubla, Cakto.

**3. `hubla` entrou na varredura** — pendencia aberta pelo `Schema.md` em 22/08, fechada.

**4. Cuidado com URL filtrada.** Em 23/08 a lista da Cakto veio com `?problema=...` grudado
e devolveu so "Atraso na entrega" — 5 reclamacoes de 9 a 18 dias atras, nenhuma recente.
Parecia Cakto parada; era a URL. **Sempre conferir se o cabecalho diz "Todas as reclamacoes
para X" e nao "Todas as reclamacoes sobre <problema> para X".**

**5. Oferta sem nome ainda vale nota.** A mecanica pode ser o achado mesmo quando o produto
nao se identifica — ver [[desafio-anamnese-plano-alimentar]]. `slug` congela, `nome` carrega
"(nome nao capturado)" ate alguem capturar.

**6. `s_ticket: 0` e sentinela, nao avaliacao.** Quando o valor nao aparece no corpo, zero
e mais honesto que estimativa — mas derruba o score composto e afunda a nota no Ranking.
Notas com `s_ticket: 0` nao devem ser comparadas com as outras ate a captura.


---

## Adendo — a lista nao gira em 24h (2026-08-24)

O adendo de 23/08 registrou que cada gateway rende no maximo 5 sinais por rodada. Faltava a
metade pior do problema: **essas 5 linhas nao sao 5 linhas novas.**

Medido em 24/08, com os corpos abertos e datados:

- A reclamacao da [[desafio-anamnese-plano-alimentar]] listada hoje e a de **22/08 as 17h33,
  ID 257133061** — a mesma que originou a nota em 23/08.
- A linha da [[stalkeia-ai]] aponta para `bsQiiX5mms5RNOcb`, **a mesma URL citada como evidencia
  na nota de 22/08**. Tres rodadas na primeira pagina, contada como sinal novo em duas.
- Das 5 linhas da PerfectPay, 5 sao identicas as de ontem. No total, ~40 das 45 vagas repetem.

**Os rotulos relativos mentem.** A anamnese aparece como "Ha 21 horas" com carimbo proprio de
43 horas. O rotulo parece refletir atividade na reclamacao, nao criacao. **Nunca datar uma
observacao pelo rotulo relativo — sempre abrir o corpo e ler o carimbo.**

**Regra (substitui a contagem ingenua):** `ra_reclamacoes` so incrementa quando a data do corpo
e **posterior a rodada anterior**. Aparecer na lista conta como avistamento — atualiza
`visto_ultimo`, `rodadas_vista` e `status`, grava snapshot — mas nao move a contagem. Quando
nao for viavel abrir o corpo, nao incrementar: falso negativo e barato, contagem inflada
contamina `s_lucro`, que tem o maior peso do score.

**Consequencia de cadencia.** Rodar diariamente contra uma fonte que se move a cada 2-3 dias
nao produz serie temporal; produz a mesma fotografia com datas diferentes. Enquanto a Etapa 1
estiver fora, **a cadencia certa e de 2 a 3 dias.**

---

## Adendo — o carimbo do corpo tambem se move; so o ID e estavel (2026-08-27)

O adendo de 24/08 mandava abrir o corpo e confiar no carimbo. Insuficiente.

A reclamacao **ID 257133061** ([[desafio-anamnese-plano-alimentar]], Lastlink) foi lida com
carimbo de 22/08 as 17h33 na rodada de 24/08 e com carimbo de **25/08 as 16h24** na rodada de
27/08 — mesmo ID, mesmo texto, mesmo comprador. O carimbo se move quando a reclamacao e
editada ou respondida pela empresa.

**O ID e o unico identificador estavel, e e monotonico.** Na rodada de 27/08:
257133061 (anamnese) < 257150511 ([[agentor]], 23/08) < 257168105 ([[capcut-pro-revenda]], 23/08)
< 257339487 e 257345233 (Kiwify, 25/08) < 257581811 e 257584931 (PerfectPay, 27/08). A anamnese
tem o menor ID e o segundo carimbo mais recente: e a mais antiga da lista, e o carimbo mente.

**Regra (substitui "leia o carimbo"):** deduplicar e ordenar por **ID**. `ra_reclamacoes` so
incrementa quando o ID nunca foi visto antes **e** e maior que o maior ID registrado na rodada
anterior. Data serve para narrativa, nao para contagem. Registrar o ID no corpo da nota da
oferta e no snapshot, sempre.

## Adendo — cadencia por gateway (2026-08-27)

A cadencia de 2-3 dias do adendo de 24/08 se confirmou: primeira rodada com intervalo de tres
dias devolveu quatro ofertas ineditas, duas carimbadas no proprio dia — zero rodadas diarias
anteriores tinham conseguido isso.

Mas a cadencia certa nao e a mesma para todos. O volume de reclamacoes ativas determina quanto
tempo a primeira pagina leva para girar:

| Gateway | Reclamacoes ativas | Giro da 1a pagina | Cadencia util |
|---|---|---|---|
| PerfectPay | ~287.000 | horas | diaria |
| Kiwify | ~49.000 | ~1 dia | diaria |
| Kirvano | ~37.000 | 2-3 dias | 3 dias |
| Cakto | ~17.000 | 2-3 dias | 3 dias |
| Lastlink | ~7.000 | dias | 3+ dias |
| Hubla | ~8.600 | dias | 3+ dias |
| Ticto | ~10.500 | dias | 3+ dias |
| Lowify | ~1.800 | **~7 dias** | semanal |
| Wiapy | ~1.200 | ~7 dias | semanal |

Lowify e Wiapy continuam valendo como **fonte de descoberta** — sao os gateways de ticket mais
baixo — mas visita-los diariamente e desperdicio: em 27/08 a primeira pagina da Lowify ainda
mostrava a reclamacao de 20/08 do [[kit-convites-casamento]] no topo, com rotulo de "Ha 2 dias".

---

## Adendo — Etapa 3b: a pagina do produtor (2026-08-28)

A Etapa 3 escrita acima manda buscar o nome do produto e do anunciante **nas paginas dos
gateways**. Isso e uma fonte larga e rasa: a lista de um gateway mistura centenas de ofertas
e devolve 5 linhas por requisicao, entao cada oferta rende no maximo uma mencao e
`ra_reclamacoes` fica travado em 1 para sempre.

Em 28/08 apareceu a fonte estreita e funda. A reclamacao **ID 257574289** estava listada na
PerfectPay, mas o bloco de empresa dentro dela era `TW EMPREENDIMENTOS DIGITAIS`, com pagina
propria no RA (`/empresa/joyce-roberts/`). **O gateway reatribui a reclamacao ao produtor e
ela continua listada nos dois lugares** — outra reclamacao na mesma pagina se chama, ao pe da
letra, *"PERFECT PAY MOVENDO RECLAMACAO PRA OUTRA EMPRESA"*.

A pagina do produtor tinha 39 reclamacoes ativas, **todas da mesma oferta**, com a mais antiga
carimbada em 29/06 — 60 dias de idade medida, sem Biblioteca de Anuncios.

**Procedimento.** Ao abrir o corpo de qualquer reclamacao numa lista de gateway, olhar o bloco
de empresa:

1. Se disser o nome do gateway → segue como hoje, sinal de 1 mencao.
2. Se disser **outro nome** → e o produtor. Ir para
   `https://www.reclameaqui.com.br/empresa/<slug-do-produtor>/lista-reclamacoes/` e minerar.

Dali saem tres campos que a lista de gateway nunca deu:

| Campo | De onde | Por que importa |
|---|---|---|
| `ra_reclamacoes` | "Exibindo 5 de **N** reclamacoes" no cabecalho | volume real da oferta, nao 1 |
| `ra_primeira_reclamacao` | carimbo da mais antiga (paginar ate o fim) | idade da **oferta** |
| `dias_no_ar` | hoje menos a primeira | **destrava `s_lucro`, peso 35** |

**Isto e o substituto parcial da Etapa 1.** Nao mede anuncio, mede venda — o que e melhor
proxy, nao pior. A limitacao e a cobertura: so ofertas cujo produtor tem pagina propria no RA
aparecem, e um produtor so ganha pagina quando acumula reclamacao suficiente. Ou seja, **a
fonte enviesa para oferta com volume**, que e exatamente o vies desejado.

**Aplicar retroativamente.** As notas ja mapeadas nunca foram checadas por produtor. A varredura
de mais valor agora nao e a primeira pagina dos gateways, e procurar pagina de produtor para as
notas do topo do Ranking — sao elas que estao travadas em `s_lucro` de palpite.

### Etapa 3b tem duas portas — a de fora e melhor (2026-08-29)

O procedimento acima chega a pagina do produtor **por dentro**: abre uma reclamacao da lista do
gateway e ve que o bloco de empresa e outro. Isso limita a descoberta ao que ja caiu nas cinco
linhas do gateway.

Da para chegar **por fora**, e rende muito mais: buscar
`reclameaqui.com.br "lista-reclamacoes" <termo do nicho>` devolve paginas de produtor
diretamente. Uma busca por material pedagogico devolveu Alfabetinho, Apostilas Brasil, Portal de
Apostilas, Cursos e Apostilas Aprovacao e Groove Caligrafia de uma vez; foi assim que a
[[alfabetinho]] (177 reclamacoes ativas) entrou no vault.

O vies e o desejado: **produtor so ganha pagina propria quando acumula reclamacao suficiente**,
entao a busca por fora so devolve quem tem volume — o inverso da lista do gateway, que devolve
as cinco mais recentes seja qual for o tamanho.

**Angulo nao tem produtor.** A Etapa 3b se aplica a oferta nomeada. Quando o alvo e uma nota de
angulo, a busca certa nao e pelo produtor *do* angulo (nao existe) e sim por produtores *no
nicho* do angulo. Foi o que ligou o [[angulo-material-pedagogico]] a [[alfabetinho]] treze dias
depois de o padrao ter sido catalogado sem dono.

### Limite: `dias_no_ar` nao sai da Etapa 3b sem browser (2026-08-29)

O adendo de 28/08 prometia tres campos da pagina do produtor. Dois deles exigem paginar ate a
reclamacao mais antiga, e **URL com `?pagina=N` nao passa no filtro de proveniencia do fetch** —
so e possivel buscar URLs vindas de resultado de busca ou de fetch anterior, e paginacao nunca
aparece. A [[alfabetinho]] tem 36 paginas e a primeira reclamacao ficou inacessivel.

O `dias_no_ar: 60` da [[google-captcha-tw]] saiu porque aquela lista tinha 8 paginas e a mais
antiga apareceu por acaso. **Nao e procedimento reproduzivel.** Sem browser, a Etapa 3b entrega
`ra_reclamacoes`, nao idade.

### Substituto: o contador de velocidade `M - N` (2026-08-29)

Uma requisicao, sem paginar. A pagina do produtor traz dois numeros em lugares diferentes:

- **N** = "Esta empresa recebeu **N** reclamacoes" (cartao de desempenho, janela de 6 meses)
- **M** = "Exibindo 5 de **M** reclamacoes ativas" (cabecalho da lista)

`M - N` e aproximadamente o que chegou depois do fim da janela.

| Produtor | N | M | Leitura |
|---|---|---|---|
| `joyce-roberts` ([[google-captcha-tw]]) | 22 | 39 | ~17 em agosto contra 3,7/mes antes: **acelerou ~4,6x** |
| `alfabetinho` | 24 | 177 | N baixo contra M alto: operacao antiga **desacelerando** |

Para produtor novo, `M - N` mede aceleracao. Para produtor antigo, `N` baixo com `M` alto ja
denuncia a desaceleracao. Nos dois casos e sinal de `s_lucro` sem depender de carimbo.

### Correcao: a tabela de cadencia por gateway e palpite (2026-08-29)

A tabela de 27/08 da a PerfectPay "giro de horas" por ter ~287.000 reclamacoes ativas. Em 29/08 a
PerfectPay tinha 287.431 e **a primeira pagina nao girou em 24h**: os tres IDs identificaveis
(257574289, 257584931, 257581811) eram todos de rodadas anteriores.

**Volume de reclamacoes da empresa nao prediz giro da primeira pagina** — a ordenacao nao e
puramente por recencia. Ler aquela tabela como estimativa, nunca como medicao, e nao voltar a um
gateway so porque ele e grande.

### Ausencia de pagina de produtor nao e evidencia de ausencia de vendas (2026-08-29)

A `Bebe Dorminhoco`, unico produtor nomeavel do sub-nicho de [[angulo-sono-bebe]], tem 12
reclamacoes ativas, a mais recente de ha 4 anos e **zero na janela de seis meses** — apesar de
anunciar 70.000 familias. A tentacao e derrubar o `s_lucro` do angulo. Nao derrube.

Motivo: as ofertas de sono citadas naquela nota rodam **na Hotmart**, e reclamacao de produto
vendido em gateway cai na pagina do gateway. A reatribuicao ao produtor que a PerfectPay faz
**nao e comportamento universal**. A pagina vazia mede aquele produtor, nao o sub-nicho. Trocar um
proxy magro por um proxy errado e pior que ficar sem proxy.

### Marcador barato de carimbo movido

O adendo de 27/08 estabeleceu que so o ID e estavel. Falta um atalho: **titulo com
`[Editado pelo Reclame Aqui]` sinaliza carimbo empurrado para frente.** O ID 257574289 exibia
28/08 12h13 sendo mais antigo que o 257586513, carimbado 27/08 21h05 — e a diferenca visivel
era a edicao do RA. Serve para desconfiar sem precisar de leitura anterior daquele ID.
