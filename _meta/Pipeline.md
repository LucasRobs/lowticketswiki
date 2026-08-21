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
