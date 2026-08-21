---
tipo: radar
data: 2026-08-21
ofertas_vistas: 9
novas: 7
retornaram: 0
sumiram: 14
fontes: [reclame-aqui, busca-web]
duracao_min: 40
---

# Radar 2026-08-21 — rodada dos gateways

Terceira nota do dia. As duas anteriores cobriram os clusters religioso e de
comportamento infantil; esta é a varredura de **listas de reclamações de gateway como
fonte de descoberta** — Lowify, Wiapy, Kirvano, Cakto e Ticto.

**Biblioteca de Anúncios e unFunnelizer: fora de novo.** `list_connected_browsers`
devolveu vazio pela terceira rodada seguida. `dias_no_ar` e `criativos_ultima` seguem em 0
em todo o vault, e a tabela **Acelerando** do Painel continua vazia por falta de dado, não
por falta de movimento.

## Novas

Sete, todas descobertas na primeira página de reclamações de um gateway.

| Oferta | Gateway | Preço | Score | Por quê |
|---|---|---|---|---|
| [[app-do-paizao]] | kirvano | assinatura | **6,55** | primeiro ângulo de paternidade do vault, e com recorrência |
| [[unlovable]] | kirvano | R$ 57/mês | 5,55 | cinco meses de assinatura ativa confirmados num único caso |
| [[script-da-banca]] | lowify | R$ 9,99 → 29,99 | 5,30 | escada de valor inteira legível no corpo da reclamação |
| [[angulo-mounjaro-de-pobre]] | — | R$ 37 + bump | 5,30 | o padrão portátil da rodada; score preso pelo teto de saúde |
| [[kit-convites-casamento]] | lowify | R$ 24,90 | 5,25 | `s_replica: 9` — pacote de templates, funil de duas páginas |
| [[lowzap]] | kirvano | ~R$ 67 est. | 5,10 | marca em dois degraus (Lowzap → Low Scale) |
| [[mounjaro-de-pobre]] | cakto | R$ 37,90 | 4,75 | rastro de 11/2025 a 05/2026 — longevidade real |

## Movimento

- **[[instalador-robo-pronto-2]]** — reclamação nova na Cakto hoje, cinco dias depois da
  primeira. `ra_reclamacoes` 1 → 2, `rodadas_vista` 1 → 2, status `nova` → `ativa`. É a
  única oferta do vault com duas reclamações em rodadas diferentes: a série temporal do
  Reclame Aqui começou a existir.
- **[[wiapy-foto-com-pet]]** — sem reclamação nova. Ver a correção de método abaixo.
- **[[cinefy-tv]]** — a Lowify recebeu hoje mais uma reclamação de série com episódios
  incompletos. Não gravei snapshot novo porque o de hoje já existe e snapshot é
  append-only; fica registrado aqui.

## Retornaram

Nenhuma.

## Sumiram

Quatorze ofertas vistas apenas em 2026-08-16 completaram a segunda ausência e passaram
para `esfriando`: [[angulo-arquivos-stl]], [[angulo-artesanato-moldes-pdf]],
[[angulo-biblia-free-shipping]], [[angulo-eletricista-orcamento-app]],
[[angulo-material-pedagogico]], [[aula-desplugada]], [[hinario-em-movimento]],
[[lottoapp]], [[lowify-app-historias]], [[operax]], [[planos-aula-infantil-500]],
[[publion]], [[robo-hacker-book]], [[teacher-zap]].

Vale o mesmo aviso da rodada anterior: elas não sumiram do mercado, sumiram do alcance de
um radar que, sem biblioteca de anúncios, só reencontra uma oferta quando ela gera
reclamação nova. `esfriando` aqui mede a cobertura do instrumento, não a saúde da oferta.

## Correção de método — a data da reclamação não é o rótulo da listagem

A lista da Wiapy mostrava "Há 15 horas" na reclamação da [[wiapy-foto-com-pet]]. Abrindo o
corpo, a data é **04/08/2026** — a mesma reclamação já registrada em 2026-08-20. O rótulo
relativo da listagem marca a **última atividade do caso** (resposta, avaliação, réplica),
não a abertura.

Consequência direta: **contar reclamação pela listagem infla `ra_reclamacoes`.** Todo o
proxy de volume do `Pipeline.md` depende de datas corretas. A regra passa a ser: abrir o
corpo e ler a data antes de contar. Foi o que salvou esta rodada de registrar uma
aceleração inexistente na Wiapy — e o que confirmou uma real na Cakto.

## Leitura da rodada

**A lista de reclamações de gateway funciona melhor como descoberta do que como
validação.** Sete ofertas novas saíram da *primeira página* de cinco gateways. Nenhuma
delas foi encontrada por busca de nicho, por domínio netlify ou por biblioteca de
anúncios. O custo foi cinco requisições. Isso reordena o `Pipeline.md`: a Etapa 3 não é a
última, é a primeira quando o browser está fora.

**O corpo da reclamação é onde mora a anatomia do funil.** A rodada de 20/08 já tinha
descoberto isso com o PIX de R$ 10,90 da Wiapy; hoje o padrão se repetiu quatro vezes.
[[script-da-banca]] entregou a escada inteira (R$ 9,99 → R$ 29,99). [[lowzap]] entregou o
nome do upsell e o fato de ele ser cobrado após recusa. [[unlovable]] entregou cinco meses
de assinatura viva numa frase sobre data de compra. [[mounjaro-de-pobre]] entregou a
distância entre o criativo (saquinhos no vídeo) e o produto (PDF sem cardápio). **Nenhuma
dessas informações estaria no DOM da página de vendas**, nem sairia do Brute Mode do
unFunnelizer. Só quem pagou sabe.

**O achado que vale para amanhã é o [[app-do-paizao]].** As dezessete notas do cluster
infantil convergiram na conclusão de que o nicho vende alívio de culpa da mãe — e essa
conclusão vinha com um ponto cego que só apareceu agora: se o que converte é falar com o
comprador sobre ele mesmo, então existe um discurso de culpa paterna inexplorado. E a
única oferta que encontrei falando com o pai não vende ebook de R$ 27; vende **assinatura**.
O cluster inteiro roda sem backend nenhum. Esta roda com recorrência.

**Nada passou no corte de replicação, pela terceira rodada.** A melhor das sete novas é o
[[app-do-paizao]] com 6,55; o topo do vault inteiro segue sendo [[angulo-diagnostico-isca]]
e [[angulo-desintoxicacao-telas]], empatados em 7,35. O corte é 7,5 com `s_replica >= 7`. A causa continua sendo a mesma que o Diagnóstico do
Painel já nomeou: `s_lucro` pesa 35% e é estimado, não medido, porque a biblioteca de
anúncios nunca foi lida. **Três rodadas, zero candidatas, é resultado do instrumento.**
As duas correções pendentes — curva de sino em `s_lucro` e média geométrica no lugar da
soma — seguem sem ser aplicadas, e enquanto seguirem, a quarta rodada vai terminar igual.

## Pistas não convertidas em nota

Encontradas hoje, sem evidência suficiente para virar oferta:

- **Ameixa App** (Ticto, 15/10/2025) — emagrecimento com endosso falso de Dr. Drauzio
  Varella. Registrado dentro de [[angulo-mounjaro-de-pobre]] como o contraexemplo.
- **Luke ZAP** (Ticto, 15/10/2025) — cluster de ferramenta de WhatsApp, sem preço.
- **Atrio — captação de pacientes** (Kirvano, 2026-08-21) — venda de leads para clínicas.
  B2B de ticket alto, fora do recorte low ticket.
- **Serviço de desbanimento de número** (Cakto, R$ 100) — não entregue. Área cinzenta,
  registro apenas.
