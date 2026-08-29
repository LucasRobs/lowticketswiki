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

`checkout`, `gateways_detectados` e `ra_plataformas` usam o mesmo vocabulário controlado.
Não invente valor novo sem adicionar aqui primeiro — filtro de Base quebra silenciosamente
com typo.

### Vocabulário de gateway (atualizado 2026-08-22)

Auditoria da rodada de 22/08 encontrou seis valores já em uso nas notas e ausentes desta
lista. Registrados agora para fechar o buraco:

| Valor | Onde apareceu | Nota |
|---|---|---|
| `hubla` | `gateways_detectados` de [[lowzap]] | cobra o upsell de um funil cuja frente roda na Kirvano. **Não está na varredura do `Pipeline.md`** — adicionar à Etapa 3. |
| `ggcheckout` | `checkout` de [[aula-desplugada]] | gateway real, faltava na lista |
| `payt` | `checkout` de [[zap-radar]] | gateway real, faltava na lista |
| `whatsapp` | `checkout` de [[planos-aula-infantil-500]] | não é gateway: é venda por conversa, sem checkout. Valor legítimo, semântica diferente. |
| `desconhecido` | `checkout` dos dois [[desafio-21-dias-com-deus-traco]] | sentinela explícita para "não capturado ainda". Preferível a deixar vazio, que a Base lê como igual a qualquer coisa. |

Lista completa válida para os três campos:

`perfectpay` · `cakto` · `kirvano` · `lastlink` · `wiapy` · `lowify` · `kiwify` ·
`hotmart` · `ticto` · `monetizze` · `eduzz` · `hubla` · `ggcheckout` · `payt` ·
`stripe` · `clickbank` · `whatsapp` · `desconhecido`

---

## Adendo — `classe`: separar oferta de angulo (2026-08-29, segunda passada)

O `tipo` das notas de `Ofertas/` sempre foi `oferta`, inclusive nas 14 notas que descrevem
**padrao estrutural sem dono** — os angulos. Consequencia: as duas coisas competiam na mesma
Base, com a mesma rubrica, e o Ranking premiava a abstracao (ver `Painel.md`, leitura de 29/08).

**Campo novo, obrigatorio em toda nota de `Ofertas/`:**

```yaml
classe: oferta     # oferta | angulo
```

| Valor | Significado | Tem produtor, ticket e gateway? |
|---|---|---|
| `oferta` | operacao concreta, ainda que o nome nao tenha sido capturado | sim, ou sentinela `desconhecido` |
| `angulo` | padrao replicavel observado em varias ofertas, sem dono unico | nao, por construcao |

**`tipo` continua `oferta` nas duas.** Mudar `tipo` quebraria em silencio todas as Bases,
o Dataview e o `radar-diff.sh`, que filtram por ele. `classe` e aditivo: quem nao filtrar
por ele continua vendo o vault inteiro.

### Criterio de classificacao — e por que nao e o slug

O criterio e a **tag `angulo`**, nao o prefixo do slug. Os dois discordam em um caso e a tag
esta certa: [[angulo-taxa-escalonada-decrescente]] tem prefixo de angulo mas tem gateway
(`perfectpay`), ticket de frente, bump, upsell e ID de reclamacao — e uma oferta real cujo
nome comercial nao foi capturado. Ficou como `classe: oferta`.

Ao criar nota nova: se ela tem — ou pode vir a ter — um produtor identificavel, e `oferta`,
mesmo sem nome. Se ela so existe como generalizacao de outras notas, e `angulo` e leva a tag.

### O que a separacao mediu

Aplicada as 85 notas (71 `oferta`, 14 `angulo`):

| | Score medio | `s_replica` medio | Melhor do grupo |
|---|---|---|---|
| `angulo` | 6,55 | 7,86 | 7,35 |
| `oferta` | 5,43 | 6,28 | 6,95 |

O vies existia e tem tamanho: **1,1 ponto de score e 1,6 de `s_replica`**, na direcao prevista.
Angulo pontua alto em replicabilidade porque nao tem produto concreto para atrapalhar.
