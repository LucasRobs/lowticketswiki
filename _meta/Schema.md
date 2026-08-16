---
tipo: meta
---

# Contrato de dados

A skill `radar-low-ticket` **deve** gravar exatamente estas propriedades. Nomes em
snake_case sem acento — Bases e Dataview lidam mal com acento em chave de frontmatter.

## 1. Nota de oferta — `Ofertas/<slug>.md`

Entidade persistente. Uma por oferta, atualizada a cada rodada.

```yaml
tipo: oferta
slug: metodo-x-jejum          # kebab-case, é o id. Nunca muda.
nome: "Método X — Jejum 16h"
nicho: emagrecimento
sub_nicho: jejum-intermitente
idioma: pt-BR                 # pt-BR | en-US | es | ...
pais: BR

# --- onde vive ---
plataforma_ads: [meta]        # meta | google | tiktok | youtube | native
checkout: kiwify              # kiwify | hotmart | ticto | stripe | clickbank | ...
url_pagina: "https://..."
url_ads: "https://..."        # link direto pra biblioteca de anúncios

# --- economia da oferta ---
moeda: BRL
ticket_frente: 27
ticket_bump: 19               # 0 se não tem
ticket_upsell: 97             # 0 se não tem
ticket_medio_est: 47          # estimativa de valor por comprador
margem_est: 0.85              # 0-1, líquido de custo de produto/plataforma

# --- anatomia ---
modelo: [vsl]                 # vsl | quiz | advertorial | tsl | webinar | direct
formato_entrega: [ebook]      # ebook | curso | comunidade | planilha | fisico | app
tem_recorrencia: false

# --- scores 0-10 (ver Scoring.md) ---
s_ticket: 7
s_lucro: 8
s_replica: 9
s_saturacao: 5                # INVERTIDO: 10 = campo livre, 0 = lotado

# --- ciclo de vida (a skill mantém) ---
status: ativa                 # nova | aquecendo | ativa | esfriando | morta
visto_primeiro: 2026-08-16
visto_ultimo: 2026-08-16
rodadas_vista: 1
dias_no_ar: 34                # idade do anúncio mais antigo
criativos_ultima: 12          # criativos ativos na última rodada
criativos_delta: 0            # variação vs rodada anterior — é o sinal de aceleração

# --- decisão sua ---
veredito: observar            # replicar | observar | descartar | replicando | replicada
prioridade: 0                 # 0-3, você define

tags: [oferta, lowticket]
```

## 2. Snapshot — `Observacoes/YYYY-MM-DD -- <slug>.md`

**Append-only.** Nunca reescreva um snapshot: ele é o que torna a série temporal
confiável. Um arquivo por oferta por rodada.

```yaml
tipo: observacao
data: 2026-08-16
slug: metodo-x-jejum
oferta: "[[metodo-x-jejum]]"
criativos_ativos: 12
dias_no_ar: 34
ticket_frente: 27
preco_mudou: false
angulo_novo: false            # true se apareceu ângulo/criativo estruturalmente novo
fonte: ads-library
```

No corpo: o que mudou, em uma linha. Se nada mudou, escreva `sem alteração`.

## 3. Rodada — `Radar/YYYY-MM-DD.md`

```yaml
tipo: radar
data: 2026-08-16
ofertas_vistas: 0
novas: 0
retornaram: 0                 # estavam esfriando/mortas e voltaram
sumiram: 0                    # não apareceram nesta rodada
fontes: []
duracao_min: 0
```

No corpo, três seções obrigatórias: **Novas**, **Movimento**, **Sumiram** — cada
oferta como wikilink `[[slug]]`.

## Regras que a skill não pode quebrar

1. `slug` é imutável. Se a oferta mudar de nome, muda `nome`, nunca `slug`.
2. Snapshot nunca é editado nem deletado.
3. `criativos_delta` = `criativos_ultima` de hoje menos o da rodada anterior. Se não
   houve rodada anterior, `0`.
4. Datas sempre `YYYY-MM-DD`, sem hora.
5. Valores monetários como número puro, sem `R$` e sem separador de milhar.

---

## Adendo — campos de mineração (ver `Pipeline.md`)

Acrescentar à nota de oferta:

```yaml
# --- unFunnelizer ---
unfunnelizer_capturado: false
ativos_pasta: "Ativos/metodo-x-jejum"
gateways_detectados: [cakto]      # saida do Find Links
bump_oculto: false                # so visivel em Brute Mode
upsell_oculto: false

# --- Reclame Aqui (proxy de volume de vendas) ---
ra_reclamacoes: 0                 # nos ultimos 30 dias
ra_plataformas: []                # perfectpay | cakto | kirvano | lastlink | wiapy | lowify | kiwify | hotmart | ticto | monetizze | eduzz
ra_primeira_reclamacao: 
ra_checado: 
```

E ao snapshot em `Observacoes/`:

```yaml
ra_reclamacoes: 0
criativos_novos: 0                # quantos criativos apareceram desde a rodada anterior
```

`checkout` e `ra_plataformas` usam o mesmo vocabulário controlado. Não invente valor
novo sem adicionar aqui primeiro — filtro de Base quebra silenciosamente com typo.
