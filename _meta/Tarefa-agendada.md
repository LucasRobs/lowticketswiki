---
tipo: meta
---

# Tarefa agendada — prompt da mineração 6x/dia

A tarefa **"Radar Low Ticket - Mineração diária de ofertas"** roda às 06h, 10h, 13h, 17h, 20h e
22h (Fortaleza). Até 27/09 ela gravava só no Projeto Claude e alguém tinha que importar para o
vault. O prompt abaixo faz cada passada gravar **direto no vault** com `_meta/publicar.py` — é de
lá que o dashboard lê — e guarda na fila do Projeto quando o Mac estiver desligado.

**Como aplicar:** no app Claude (desktop) → tarefas agendadas → *Radar Low Ticket - Mineração
diária de ofertas* → editar → trocar o prompt pelo bloco abaixo. (Mudança de prompt de tarefa
presa a este Mac só vale com aprovação feita nele.)

```text
Passada agendada do Radar Low Ticket (Projeto "lowticket"). Fuso: America/Fortaleza (UTC-3). Nao faca perguntas: decida com bom senso e termine a passada. Roda 6x/dia, entao seja objetivo.

O destino dos dados e o VAULT no Mac (pasta lowticket): o dashboard na Vercel le de la. O Projeto so guarda fila quando o Mac estiver desligado.

0) DATA/HORA E MAC
- No device_bash rode: date -u -d '-3 hours' '+%F %H:%M' ; ls "$HOME/mnt/lowticket/_meta/publicar.py"
- Se o device_bash responder e o arquivo existir: MAC=ligado. Se a ferramenta nao existir ou falhar: MAC=desligado (calcule voce a data/hora em UTC-3).

1) FILA PENDENTE (so com MAC=ligado)
- project_info. Para cada doc cujo caminho comeca com "claude/fila/" (ordem alfabetica):
  a) project_read no doc (e um JSON de achados);
  b) grave o conteudo exato em "$HOME/mnt/lowticket/Radar/dados/<nome do arquivo do doc>" com device_bash e heredoc: cat > "<caminho>" <<'JSON' ... JSON
  c) cd "$HOME/mnt/lowticket" && python3 _meta/publicar.py --achados "Radar/dados/<nome do arquivo do doc>"
  d) se a saida mostrar "passada:" e nao mostrar "achados invalidos" nem "falhou", faca project_delete no doc da fila.

2) MINERAR
- Execute a skill radar-low-ticket: PerfectPay e Cakto, ~10-12 paginas cada (outros gateways so se sobrar tempo).
- Com MAC=ligado, veja o que as passadas de hoje ja registraram: ls "$HOME/mnt/lowticket/Radar/rodadas/" e leia as de hoje com cat. Nao repita no relatorio o que ja esta la.
- NAO gere planilha, CSV, favoritos nem HTML, e nao use SendUserFile: o dashboard substitui isso.

3) MONTAR O JSON DA PASSADA (formato da skill + bloco "passada")
{"data_varredura": "AAAA-MM-DD",
 "gateways": [{"nome": "PerfectPay", "slug": "perfectpay", "paginas_varridas": 12}, {"nome": "Cakto", "slug": "cakto-pay", "paginas_varridas": 12}],
 "achados": [{"produto": "Nome", "tipo": "marca", "gateway": "PerfectPay", "nicho": "ferramentas-ia", "temperatura": "morna", "mencoes": 1, "faixa_preco": "R$ 27", "termo_busca": "Nome", "descricao": "1-2 frases: o que e e como monetiza", "evidencia_url": "url da reclamacao"}],
 "passada": {"hora": "HH:MM", "gateways": ["perfectpay", "cakto"], "paginas": 24, "coleta": "ok",
             "relatorio": "## Quentes\n- [[slug]] ou Nome — gateway · por que\n\n## Mornas\n- ...\n\nLeitura: 1-2 linhas", "resumo": "uma linha"}}
- tipo: "marca" (tem nome proprio) ou "angulo" (produto so descrito). coleta: "ok", "parcial" ou "sem-coleta".
- Se o Reclame Aqui nao respondeu: "coleta": "sem-coleta" e "achados": []. Nunca invente achado.
- Oferta que ja apareceu hoje pode entrar de novo (o vault conta uma vez por dia).

4A) GRAVAR (MAC=ligado)
- Grave o JSON em "$HOME/mnt/lowticket/Radar/dados/achados-AAAA-MM-DD-HHMM.json" (device_bash, heredoc com <<'JSON').
- Rode: cd "$HOME/mnt/lowticket" && python3 _meta/publicar.py --achados "Radar/dados/achados-AAAA-MM-DD-HHMM.json"
- Confira na saida "passada: ..." e "git: commit ...". Se aparecer "achados invalidos", corrija o JSON e rode de novo. Se der erro de git, NAO rode git pull/merge/reset/checkout nem apague nada: so registre o erro na linha final.

4B) FILA (MAC=desligado)
- project_write com path "claude/fila/achados-AAAA-MM-DD-HHMM.json" e o JSON do passo 3 como conteudo, exatamente.

5) FECHAR
- Nao crie outros docs no Projeto.
- Termine com UMA linha: "Passada HH:MM — N novas (nomes), M revistas, coleta X — gravado no vault" ou "— guardado na fila do Projeto (Mac desligado)".
```

## Por que cada regra existe

- **Um comando só (`publicar.py`)**: grava `Ofertas/`, `Observacoes/`, `Radar/` e `Radar/rodadas/`,
  regenera `dashboard/data/` e commita. Menos passos para o modelo pequeno errar.
- **Nada de git pull/merge/reset pelo agente**: o VM do Cowork não consegue apagar arquivo; essas
  operações deixariam o repositório pela metade. Quem sincroniza com o GitHub é o Mac.
- **Fila no Projeto**: com o Mac dormindo a passada não se perde; entra no vault na próxima
  passada com o Mac ligado.
- **Sem planilha/HTML**: o dashboard já mostra tudo, sempre atualizado.
