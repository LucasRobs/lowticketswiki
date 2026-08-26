---
name: radar-low-ticket
description: Garimpa ofertas low ticket nas reclamações de gateways (PerfectPay, Cakto, Kiwify, Hotmart) e gera planilha com links pra Biblioteca de Anúncios. Use ao garimpar ofertas ou minerar infoprodutos.
---
 
# Radar Low Ticket
 
## Quando isto se aplica
 
Além dos pedidos óbvios, entre em ação quando o usuário disser coisas como: garimpar ou minerar ofertas,
espionar concorrente, "o que está vendendo agora", "quero achar produto pra modelar", ver as reclamações
de um gateway (PerfectPay, Cakto, Kiwify, Hotmart, Monetizze, Braip, Payt, Ticto, Eduzz, Yampi), ou
procurar nomes pra colar na Biblioteca de Anúncios / Ad Library / biblioteca do Facebook. Ele raramente
vai dizer "low ticket" ou "ReclameAqui" com todas as letras — o pedido chega como "acha uns produtos
bons pra mim".
 
## A ideia central
 
Reclamação é rastro de venda. Ninguém reclama de uma oferta que não vendeu — cada reclamação no ReclameAqui contra um gateway de pagamento é a prova de que alguém pagou por um infoproduto naquela semana. Volume de reclamação de um mesmo produto é, na prática, um proxy grosseiro mas honesto de volume de tráfego pago rodando.
 
Então o trabalho aqui não é investigar fraude nem julgar empresa nenhuma. É ler o rastro para responder uma pergunta de mercado: **quais ofertas estão escalando agora, e com que ângulo?** O gateway é só o pedágio por onde tudo passa; os produtos são de terceiros.
 
O entregável é uma planilha, e ela é planilha por um motivo: o valor real aparece quando o usuário roda isso várias vezes e compara. Um nome que aparece hoje é curiosidade. Um nome que aparece hoje, semana passada e no mês passado é uma oferta que está sustentando verba — e essa é a que vale copiar a estrutura de funil. Por isso o script acumula histórico automaticamente.
 
## Antes de sair varrendo
 
Duas coisas mudam o resultado e valem trinta segundos de conversa, a não ser que o usuário já tenha dito ou que a sessão seja automática (agendada), caso em que assuma o padrão e siga:
 
- **Quais gateways.** Padrão: PerfectPay e Cakto. `references/gateways.md` tem os slugs de todos os outros e uma nota sobre o perfil de cada um — vale ler antes de escolher, porque o perfil de produto muda muito de um pra outro.
- **Qual profundidade.** Padrão: 25 páginas por gateway (~125 reclamações, cobre uns 3 dias). Pedido de "rapidinho" → 10 páginas. "Varredura completa" → 50+.
Se o usuário mencionar um nicho ("quero só coisa de IA", "só produto feminino"), não filtre a coleta — colete tudo e filtre na hora de montar a planilha. O que parece ruído num nicho costuma ser o ângulo que faltava em outro.
 
## Como coletar
 
A listagem pagina assim, 5 reclamações por página, mais recente primeiro:
 
```
https://www.reclameaqui.com.br/empresa/<slug>/lista-reclamacoes/?pagina=N
```
 
Use **WebFetch** para isso — nunca curl, wget ou requests. Além de ser a regra do ambiente, o WebFetch já devolve a página em texto limpo.
 
Dispare as páginas em **lotes paralelos de 12 a 16 chamadas na mesma mensagem**. Sequencial fica insuportavelmente lento e é o que faz essa tarefa parecer cara. Prompt enxuto por página, porque você vai fazer isso dezenas de vezes:
 
> Liste apenas os títulos das reclamações, literalmente, um por linha.
 
### O detalhe que decide se a varredura presta
 
**O nome do produto quase nunca está no título.** O ReclameAqui gera títulos resumidos e genéricos — "Solicitação de reembolso dentro do prazo", "Produto não entregue". Numas 20% das vezes a marca vaza pro título, e essas são de graça.
 
Para o resto, o nome está no corpo. Abrir todas as reclamações seria caro demais, então priorize: as que dizem **"propaganda enganosa"**, **"produto diferente do anunciado"**, **"produto não funciona"** ou **"cobrança adicional para liberar"** são as que quase sempre nomeiam a marca, porque o reclamante está tentando alertar outras pessoas. Pegue as URLs pedindo à listagem:
 
> Liste os títulos das reclamações E os links (URLs completas). Formato: título | url
 
E aí abra de 8 a 12 dessas em paralelo com:
 
> Extraia: nome do produto/curso/app comprado, nome do produtor/vendedor, valor pago, data. Se não houver nome de produto, diga "sem nome".
 
### Quando não há nome — e por que isso é bom
 
Boa parte dos compradores não lembra o nome do que comprou, mas descreve o produto: "app de novelas turcas", "curso de pedreiro", "apostila de crochê", "ganhar dinheiro avaliando produtos". Não descarte. Esses viram linhas de tipo **ângulo** na planilha, e frequentemente valem mais que as marcas: uma marca dá uma oferta pra estudar, um ângulo dá dezenas de uma vez quando buscado na Biblioteca de Anúncios. `references/nichos.md` tem a taxonomia e os termos de busca que funcionam pra cada ângulo.
 
### Sinais que valem anotar
 
Enquanto lê, registre no campo de descrição o que aparecer:
 
- **Grafias alternativas e clones.** "Stalkeia.ai", "Stalkea.ai", "Stalker AI" são a mesma família de oferta com criativos diferentes. Junte na mesma linha — é sinal de operação grande, não de três produtos.
- **O mesmo produto em vários gateways.** Se aparece na PerfectPay e na Mangofy, é operação que já se preparou pra derrubada. Sinal forte de escala.
- **Mecânica de monetização.** "Taxa pra liberar saldo", "cobrança de créditos", "pagamento adicional pra desbloquear" significam order bump e upsell pesados — é o que sustenta CPA alto no front. Anote, porque é o que o usuário vai querer copiar.
- **Faixa de preço**, quando o reclamante citar. Ancora se é entrada de R$ 9 ou de R$ 97.
## Montando o entregável
 
Junte tudo num JSON e passe para o script — ele cuida da planilha, do CSV, dos favoritos e do painel visual, então não escreva código de saída na mão:
 
```bash
python3 scripts/build_outputs.py achados.json --saida ./radar --historico ./radar/radar-low-ticket.xlsx
```
 
O `--historico` é o que faz a mágica: aponte para a planilha da rodada anterior e o script preenche `primeira_vez_visto` e `rodadas_visto` sozinho, marcando quem é novo e quem é persistente. Na primeira rodada, omita.
 
Formato do JSON (o script valida e reclama de campo faltando):
 
```json
{
  "data_varredura": "2026-08-16",
  "gateways": [
    {"nome": "PerfectPay", "slug": "perfectpay", "reclamacoes_ativas": 287224, "paginas_varridas": 28}
  ],
  "achados": [
    {
      "produto": "Stalkeia.ai",
      "tipo": "marca",
      "gateway": "PerfectPay",
      "nicho": "Espionagem e rastreamento",
      "temperatura": "quente",
      "mencoes": 7,
      "faixa_preco": "R$ 19-47",
      "termo_busca": "Stalkeia",
      "descricao": "App de espionar WhatsApp/Instagram. Grafias: Stalkea.ai, Stalkeia.com. Também vendido via Mangofy e Payt. Cobra créditos extras pra liberar resultado.",
      "evidencia_url": "https://www.reclameaqui.com.br/perfectpay/..."
    }
  ]
}
```
 
Campos que exigem critério:
 
- **`tipo`** — `marca` quando há nome próprio; `angulo` quando o produto foi só descrito. Os dois convivem na mesma planilha e o script separa na visualização.
- **`temperatura`** — `quente` para 4+ menções ou aparições em dias diferentes; `morna` para 2–3; `fria` para menção única. Isso é o que ordena a planilha, então vale calibrar em vez de chutar tudo como quente.
- **`termo_busca`** — o que de fato funciona na Biblioteca de Anúncios, que nem sempre é o nome completo. "Stalkeia" acha mais que "Stalkeia.ai" porque a busca é por palavras soltas; "Octuz" acha mais que "Octuz AI". Corte sufixos e domínios.
- **`descricao`** — uma ou duas frases sobre o que é e como monetiza. É o campo que o usuário lê pra decidir se abre ou não; frase genérica desperdiça a linha.
O script gera, na pasta de saída:
 
- `radar-low-ticket.xlsx` — planilha principal, com aba de achados (congelada, com filtro), aba de resumo por nicho e aba de histórico
- `radar-low-ticket-<data>.csv` — mesma coisa em texto, pra quem quiser jogar em outra ferramenta
- `favoritos-radar-<data>.html` — pasta de favoritos importável no Chrome, uma subpasta por nicho
- `radar-<data>.html` — painel visual, só se você passar `--painel`
Mande a planilha com SendUserFile sempre. Os favoritos, quando o usuário quiser clicar em vez de ler — vale oferecer, porque abrir uma subpasta inteira em abas de uma vez é o jeito mais rápido de varrer um nicho.
 
## Ao fechar
 
Resuma em texto curto o que o número não diz: qual cluster dominou, o que é novo em relação à rodada anterior (o script marca), e qual ângulo você abriria primeiro se fosse operar. Três parágrafos bastam — a planilha já tem os detalhes, e repetir a tabela em prosa é o erro mais fácil de cometer aqui.
 
Duas coisas para manter honestas no fechamento, porque elas protegem o usuário de decidir errado:
 
- Deixe claro que gateway não é vendedor. PerfectPay, Cakto e afins processam pagamento de produtos de terceiros; aparecer aqui não diz nada sobre a idoneidade delas, e o usuário pode acabar repetindo isso pra outra pessoa.
- Diga o tamanho da amostra. "25 páginas de cada, cobrindo ~3 dias" é diferente de "varri tudo". Sem isso o usuário superestima a confiança da leitura.
Se o usuário gostou do resultado, vale oferecer uma vez: isso funciona muito melhor rodando toda semana, e dá pra agendar com uma tarefa recorrente — o histórico da planilha é justamente o que transforma a rodada isolada em radar de verdade.
