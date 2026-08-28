---
name: radar-low-ticket
description: Garimpa ofertas low ticket nas reclamações de gateways (PerfectPay, Cakto, Kiwify, Hotmart, Monetizze, Braip, Payt, Ticto, Eduzz, Yampi) usando agentes IA, extrai ângulos de venda, valida escala via Ad Library, enriquece dados de produtor e gera planilha historizada com scores quantitativos. Use ao garimpar ofertas ou minerar infoprodutos.
---

# Radar Low Ticket — Versão Aprimorada (Agente IA)

## Quando isto se aplica

Além dos pedidos óbvios, entre em ação quando o usuário disser coisas como:
garimpar ou minerar ofertas, espionar concorrente, "o que está vendendo agora", "quero achar produto pra modelar", ver as reclamações de um gateway (PerfectPay, Cakto, Kiwify, Hotmart, Monetizze, Braip, Payt, Ticto, Eduzz, Yampi), ou procurar nomes pra colar na Biblioteca de Anúncios / Ad Library / biblioteca do Facebook. Ele raramente vai dizer "low ticket" ou "ReclameAqui" com todas as letras — o pedido chega como "acha uns produtos bons pra mim".

A ideia central

Reclamação é rastro de venda. Ninguém reclama de uma oferta que não vendeu — cada reclamação no ReclameAqui contra um gateway de pagamento é a prova de que alguém pagou por um infoproduto naquela semana. Volume de reclamação de um mesmo produto é, na prática, um proxy grosseiro mas honesto de volume de tráfego pago rodando.

Então o trabalho aqui não é investigar fraude nem julgar empresa nenhuma. É ler o rastro para responder uma pergunta de mercado: **quais ofertas estão escalando agora, e com que ângulo?** O gateway é só o pedágio por onde tudo passa; os produtos são de terceiros.

Valor diferenciador: Nosso agente IA não coleta apenas nomes — ele **pontua, valida escala real e extrai ângulos de copy**. A planilha é o entregável porque o valor real aparece quando o usuário roda isso várias vezes e compara. Um nome que aparece hoje é curiosidade. Um nome que aparece hoje, semana passada e no mês passado é uma oferta que está sustentando verba — e essa é a que vale copiar a estrutura de funil. O score quantitativo do agente indica prioridade.

## Antes de sair varrendo

Duas coisas mudam o resultado e valem trinta segundos de conversa, a não ser que o usuário já tenha dito ou que a sessão seja automática (agendada), caso em que assuma o padrão e siga:

- **Quais gateways.** Padrão: PerfectPay e Cakto. `references/gateways.md` tem os slugs de todos os outros e uma nota sobre o perfil de cada um — vale ler antes de escolher, porque o perfil de produto muda muito de um pra outro.
- **Qual profundidade.** Padrão: 25 páginas por gateway (~125 reclamações, cobre uns 3 dias). Pedido de "rapidinho" → 10 páginas. "Varredura completa" → 50+.

Se o usuário mencionar um nicho ("quero só coisa de IA", "só produto feminino"), não filtre a coleta — colete tudo e filtre na hora de montar a planilha. O que parece ruído num nicho costuma ser o ângulo que faltava em outro.

## Etapas do Pipeline do Agente IA

O processo segue esta ordem para transformar reclamações brutas em insights acionáveis:

```
1. Coleta (WebFetch, paralelo 12-16 páginas) → 2. Normalizar/Fuzzy dedup → 3. Extrair via LLM (produto + ângulo + mecânica) → 4. Calcular score 0-100 → 5. Validar escala (Ad Library) → 6. Enriquecer produtor → 7. Gerar alertas → 8. Persistir histórico
```

### Etapas detalhadas:

#### 1. Coleta
- Dispare páginas em lotes paralelos de 12 a 16 chamadas na mesma mensagem
- Use WebFetch (nunca curl/wget/requests)
- Extrair: títulos das reclamações E URLs completas (formato: título | url)
- Abra de 8 a 12 reclamações em paralelo para extrair o corpo

#### 2. Normalizar & Fuzzy Dedup
- Agrupar grafias alternativas: "Stalkeia.ai" ≃ "Stalkea.ai" ≃ "Stalker AI"
- Detectar mesmo produto em vários gateways → sinal de operação de escala
- Deduplicar por `reclamante_hash` (nome + trecho do corpo)

#### 3. Extrair via LLM (Prompt Structured)
```
Extraia do texto da reclamação (JSON estrito):
{
  "produto": "nome ou 'sem nome'",
  "produtor": "nome do vendedor",
  "valor_pago": "número ou 'desconhecido'",
  "angulos": ["curiosidade", "medo", "ganância", "autoridade", "prova_social", "novidade", "facilidade"],
  "mecanica_monetizacao": "front simples | order bump | upsell | recorrência | créditos",
  "sinais_cloaker": ["página_diferente", "redirecionamento", "link_expirado"],
  "faixa_preco": "quando citar (ex: 'R$ 19-47')"
}
```
- Se não houver nome de produto, o campo `angulos` vale mais que a marca
- Termos de busca otimizados: remover sufixos (.ai, .com, AI, Pro, Max), manter raiz da marca

#### 4. Calcular Score 0-100 (Agente)
```
score_final = (menções × 0.4) + (dias_diferentes × 0.3) + (multi_gateway × 0.2) + (preço_alto × 0.1)
```
- **≥ 80**: Oferta quente, validada, testar imediatamente
- **65-79**: Watch list, monitorar 2-3 dias
- **50-64**: Archive, backtest monthly
- **< 50**: Descartar

#### 5. Validar Escala (Ad Library em Paralelo)
Para cada achado "quente" (score ≥ 65), em paralelo:
- Buscar na Meta Ad Library usando `termo_busca` (remover sufixos, manter raiz)
- Extrair: `ad_count`, `dias_ativo_max`, `criativos_unicos`, `paises`, `fontes_trafego`
- Atualizar `score_final` com esses dados
- Flag `cloaker_suspeito: true` se `sinais_cloaker` presentes OU ad count muito alto mas criativos poucos

#### 6. Enriquecer Produtor
- Extrair CNPJ/CPF do produtor mencionado
- Buscar outras ofertas no mesmo gateway + Ad Library
- Gerar portfólio: `outras_ofertas`, `gateways_historico`
- Detectar "operadora profissional" se mesmo produto em 3+ gateways

#### 7. Gerar Alertas Automáticos
- Novo produto vs. persistente (comparar com histórico)
- Cluster dominante esta rodada
- Ângulo recomendado pra testar primeiro
- Se score > 80 + validação Ad Library: alerta "TESTAR IMEDIATO"

#### 8. Persistir Histórico
- Script `build_outputs.py` já faz isso: `primeira_vez_visto`, `rodadas_visto`
- Na primeira rodada, omitir comparação histórica
- Acumular em `radar-low-ticket.xlsx` com abas: achados, resumo por nicho, histórico

## Novos Campos no JSON de Saída (Validação do Script)

```json
{
  "data_varredura": "2026-08-16",
  "gateways": [
    {"nome": "PerfectPay", "slug": "perfectpay", "reclamacoes_ativas": 287224, "paginas_varridas": 28}
  ],
  "achados": [
    {
      "produto": "Stalkeia.ai",
      "tipo": "marca",      // ou "angulo" quando descrito apenas
      "gateway": "PerfectPay",
      "nicho": "Espionagem e rastreamento",
      "score_final": 87,    // 0-100, substituí temperatura subjetiva
      "temperatura": "quente", // mantido apenas para compatibilidade visual
      "mencoes": 7,
      "faixa_preco": "R$ 19-47",
      "termo_busca": "Stalkeia",  // otimizado para Ad Library (sem sufixos)
      "descricao": "App de espionar WhatsApp/Instagram. Grafias: Stalkea.ai, Stalkeia.com. Também vendido via Mangofy e Payt. Cobra créditos extras pra liberar resultado.",
      "evidencia_url": "https://www.reclameaqui.com.br/perfectpay/...",
      "validacao_ad_library": {
        "ad_count": 47,
        "dias_rodando_max": 31,
        "criativos_unicos": 12,
        "paises": ["BR", "PT"],
        "fontes_trafego": ["facebook_feed", "instagram_stories"],
        "score_ajustado": 92
      },
      "angulos_detectados": ["curiosidade_voyeurismo", "medo_traiçao", "facilidade_tecnologica"],
      "cloaker_suspeito": true,
      "produtor": {
        "nome": "Stalker Tech LTDA",
        "cnpj": "XX.XXX.XXX/0001-XX",
        "outras_ofertas": ["Stalkea.ai", "Stalker Pro", "MonitoraZap"],
        "gateways_historico": ["PerfectPay", "Mangofy", "Payt"],
        "portfolio_size_est": "3-5 ofertas ativas"
      },
      "funil_estimado": {
        "front": "R$ 27",
        "order_bump": "R$ 17 (créditos extras)",
        "upsell_1": "R$ 97 (acesso vitalício)",
        "upsell_2": "R$ 197 (painel agência)",
        "recorrencia": "R$ 29/mês (créditos)"
      },
      "acao_recomendada": "TESTAR_IMEDIATO" // TESTAR | MONITORAR | DESCARTAR
    }
  ]
}
```

## Campos que Exigem Critério (Prompt do Agente)

- **`tipo`** — `marca` quando há nome próprio; `angulo` quando o produto foi só descrito. Os dois convivem na mesma planilha e o script separa na visualização.
- **`score_final`** — 0-100 calculado pelo agente (não chutar temperatura). Isso ordena a planilha, então vale calibrar os pesos dos fatores.
- **`termo_busca`** — o que de fato funciona na Biblioteca de Anúncios. Corte sufixos e domínios. "Stalkeia" acha mais que "Stalkeia.ai" porque a busca é por palavras soltas; "Octuz" acha mais que "Octuz AI".
- **`descricao`** — uma ou duas frases sobre o que é e como monetiza. É o campo que o usuário lê pra decidir se abre ou não; frase genérica desperdiça a linha.
- **`acao_recomendada`** — calculada pelo agente: `TESTAR_IMEDIATO` (score≥80 + validação), `MONITORAR` (65-79), `DESCARTAR` (<50 ou cloaker suspeito + saturado).

## O Script Gera (pós-processamento)

- `radar-low-ticket.xlsx` — planilha principal, com aba de achados (congelada, com filtro), aba de resumo por nicho e aba de histórico
- `radar-low-ticket-<data>.csv` — mesma coisa em texto, pra quem quiser jogar em outra ferramenta
- `favoritos-radar-<data>.html` — pasta de favoritos importável no Chrome, uma subpasta por nicho
- `radar-<data>.html` — painel visual, só se você passar `--painel`
- `radar-angles-<data>.md` — **NOVO**: Relatório só de ângulos: "Top 10 ângulos desta semana + exemplos de copy + sugestão de criativo para cada um"
- `radar-producers-<data>.json` — **NOVO**: Mapa de produtores → portfólio completo (para o usuário "espionar o player, não só o produto")
- `radar-funnel-templates-<data>.html` — **NOVO**: Funis clonados (VSL + LP + checkout) dos top 3, prontos para modelar

Mande a planilha com SendUserFile sempre. Os favoritos, quando o usuário quiser clicar em vez de ler — vale oferecer, porque abrir uma subpasta inteira em abas de uma vez é o jeito mais rápido de varrer um nicho.

## Ao Fecher

Resuma em texto curto o que o número não diz: qual cluster dominou, o que é novo em relação à rodada anterior (o script marca), e qual ângulo você abriria primeiro se fosse operar. Três parágrafos bastam — a planilha já tem os detalhes, e repetir a tabela em prosa é o erro mais fácil de cometer aqui.

Duas coisas para manter honestas no fechamento, porque elas protegem o usuário de decidir errado:

- **Deixe claro que gateway não é vendedor.** PerfectPay, Cakto e afins processam pagamento de produtos de terceiros; aparecer aqui não diz nada sobre a idoneidade delas, e o usuário pode acabar repetindo isso pra outra pessoa.
- **Diga o tamanho da amostra.** "25 páginas de cada, cobrindo ~3 dias" é diferente de "varri tudo". Sem isso o usuário superestima a confiança da leitura.

Se o usuário gostou do resultado, vale oferecer uma vez: isso funciona muito melhor rodando toda semana, e dá pra agendar com uma tarefa recorrente — o histórico da planilha é justamente o que transforma a rodada isolada em radar de verdade.

## Riscos Automaticamente Monitorados Pelo Agente

Ao final de cada execução, o agente deve registrar estas métricas de qualidade no log interno:

```json
{
  "metricas_qualidade": {
    "paginas_varridas_total": 84,
    "reclamacoes_lidas": 420,
    "com_nome_produto": 156,      // % de sucesso na extração
    "com_valor_pago": 89,         // % com preço explícito
    "angulos_detectados": 203,    // % com ângulo identificado
    "multi_gateway": 12,
    "cloaker_flags": 7,
    "score_medio": 54,
    "quentes": 8,                 // score >= 65 após validação Ad Library
    "novos_vs_historico": {"novos": 23, "persistentes": 15, "sumiram": 4},
    "tempo_total_seg": 187,
    "custo_estimado_llm_usd": 0.42,
    "paginas_erro": 3,            // falhas de WebFetch - indicar se precisa ajustar
    "reclamacoes_sem_produto": 12 // quantas foram "sem nome" - podem ser ângulos valiosos
  }
}
```

## Fluxo de Integração com o Script `build_outputs.py`

O script agora espera JSON com os campos novos. Exemplo de chamada:

```bash
python3 scripts/build_outputs.py achados.json \
  --saida ./radar \
  --historico ./radar/radar-low-ticket.xlsx \
  --painel                              # opcional: gera painel visual
```

O script cuida de:
1. Validar campos obrigatórios (produto, gateway, score_final, termo_busca)
2. Separar `tipo: marca` vs `tipo: angulo` nas abas
3. Calcular `primeira_vez_visto` e `rodadas_visto` usando histórico
4. Gerar aba resumo ordenada por `score_final`
5. Criar `favoritos-radar-<data>.html` com subpastas por nicho e por `acao_recomendada`
6. Produzir `radar-angles-<data>.md` automaticamente dos ângulos detectados

## Próximos Passos de Implementação (Roadmap)

| Sprint | Entregável | Impacto |
|--------|------------|---------|
| 1 | Adicionar **score 0-100** + cálculo automático no agente | ⭐⭐⭐ Maior prioridade — substitui "temperatura" subjetiva |
| 2 | Integrar **validação Ad Library** em paralelo p/ achados quentes | ⭐⭐⭐ Sem isso, score é teoria, não prática |
| 3 | **Extrair ângulos via LLM** do corpo da reclamação | ⭐⭐⭐⭐ Transformação: de "lista de nomes" para "playbook de copy" |
| 4 | **Enriquecer produtor** + detecção multi-gateway | ⭐⭐⭐ Permite rastrear operações, não ofertas isoladas |
| 5 | Gerar **`radar-angles-<data>.md`** e **`radar-producers-<data>.json`** | ⭐⭐ Valor agregado para o usuário final |
| 6 | Dashboard temporal interativo (substituir `--painel` estático) | ⭐⭐ Visualização avançada para power users |

---

**Nota de versão**: Esta atualização substitui a versão anterior por completo. O agente agora possui pipeline estruturado, scoring quantitativo, validação externa e extração de ângulos — transformando-o de um simples coletor de rastros em um radar de oportunidades validadas com playbook de execução.