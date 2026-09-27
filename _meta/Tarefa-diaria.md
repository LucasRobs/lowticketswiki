---
tipo: meta
---

# Tarefa agendada — rodada diária de consolidação

Duas automações alimentam o vault:

| Tarefa | Onde roda | Quando | O que faz |
|---|---|---|---|
| *Radar Low Ticket - Mineração diária de ofertas* ([[Tarefa-agendada]]) | Projeto Claude / Cowork, grava no Mac | 06h, 10h, 13h, 17h, 20h, 22h | passadas curtas de PerfectPay/Cakto no Reclame Aqui |
| *Radar Low Ticket — rodada diária* (esta) | app Claude neste computador (Linux), clone do GitHub | 23h30 | puxa as passadas do dia, minera o que elas não cobrem, grava via `publicar.py`, reescreve a *Leitura atual* do [[Painel]] e envia |

Até 27/09 o prompt desta rodada mandava gravar à mão (snapshot, oferta, `Radar/AAAA-MM-DD.md`) e
commitar com `radar-commit.sh`, numa pasta `lowticketswiki` montada em `$HOME/mnt`. O prompt abaixo
segue o adendo de 27/09 do [[Pipeline]]: quem grava é `_meta/publicar.py`; a nota do dia e a da
passada (`Radar/rodadas/`) saem dele.

**Como aplicar:** a tarefa fica em *tarefas agendadas* do app Claude (id `radar-low-ticket-rodada-diaria`).
Para mudar o prompt, edite lá e copie a versão nova para cá.

```text
Rodada diaria de consolidacao do Radar Low Ticket. Tarefa agendada, diaria as 23h30 (America/Fortaleza, UTC-3 — mesmo fuso deste computador). Voce nao tem memoria das execucoes anteriores: oriente-se pelo proprio vault. Nao faca perguntas: decida com bom senso e termine a rodada. A cadencia diaria e pedido explicito do usuario, mesmo que adendos do Pipeline.md/Painel.md recomendem 2-3 dias: trate como aviso, rode, e deixe registrado quando nao houver sinal novo real.

ONDE ESTA O VAULT
- E o repositorio git /home/user/Repositories/lowticketswiki, neste computador. Use a ferramenta Bash direto (nao existe device_bash aqui). Rode tudo com: cd /home/user/Repositories/lowticketswiki && ...
- Os documentos do vault chamam a mesma pasta de "lowticket" ou "$HOME/mnt/lowticket" (vista do Mac e do VM do Cowork). E o mesmo repositorio; o GitHub (origin/main) liga os dois.
- Identidade do git: este computador nao tem user.name/user.email. Exporte, so nos comandos que commitam: GIT_AUTHOR_NAME="Radar Low Ticket" GIT_AUTHOR_EMAIL="radar@local" GIT_COMMITTER_NAME="Radar Low Ticket" GIT_COMMITTER_EMAIL="radar@local" (a mesma de todo o historico). Nao altere o git config.
- Quem grava no vault e SEMPRE python3 _meta/publicar.py. NAO crie a mao Radar/AAAA-MM-DD.md, nada em Radar/rodadas/, snapshots em Observacoes/ nem dashboard/data/ (gerado). NAO use mais _meta/radar-commit.sh.

0) SINCRONIZAR E DATA
- date '+%F %H:%M' -> HOJE (AAAA-MM-DD) e HORA (HH:MM).
- git status -sb ; git pull --ff-only origin main  (traz as passadas 6x/dia que o Mac enviou).
- Se o pull nao for fast-forward, der conflito ou pedir credencial: NAO rode merge, rebase, reset, checkout, stash nem apague nada. Va para o passo 6 (bloqueio).

1) ORIENTAR — leia com cat, nesta ordem
- README.md; _meta/Pipeline.md inteiro (os Adendos no fim valem sobre as etapas originais; o de 27/09 "Etapa 4 agora e um comando so" substitui a gravacao manual); _meta/Schema.md (adendos de 27/09: tipo rodada, bloco "passada", formato canonico); _meta/Scoring.md; Painel.md.
- A nota de dia mais recente: ls Radar/*.md | sort | tail -2 (se Radar/HOJE.md ja existir, leia ela e a anterior).
- Todas as passadas de hoje: ls Radar/rodadas/ | grep HOJE, e cat em cada uma. E o que ja foi coberto hoje; nao repita.

2) MINERAR — complementar as passadas do dia
- As passadas 6x/dia ja varrem PerfectPay e Cakto no Reclame Aqui. Use esta rodada para o que elas nao cobrem: outros gateways do vocabulario do Schema.md (kiwify, hotmart, ticto, eduzz, monetizze, kirvano, hubla, lastlink...), termos novos, e revisitar ofertas da "Fila de captura" do Painel.
- Etapa 1 (Biblioteca de Anuncios): tente pelo navegador (browser interno ou Claude in Chrome) se estiver acessivel sem aprovacao. Se pedir aprovacao que nao chega, ou recusar facebook.com, pule sem esperar.
- Etapa 2 (unFunnelizer): so com controle de desktop disponivel; senao pule.
- Etapa 3 (Reclame Aqui) na versao degradada dos Adendos (WebSearch/WebFetch), com as regras deles: so incrementar ra_reclamacoes quando a data do CORPO da reclamacao for posterior a rodada anterior; nunca datar pelo rotulo relativo ("ha 2 dias"); o ID da reclamacao e o unico identificador estavel; conferir que a URL nao veio filtrada por ?problema=; reclamacao relida nao e sinal novo.
- Nunca invente achado. Se nenhuma fonte respondeu: coleta "sem-coleta" e achados [].

3) GRAVAR (Etapa 4 = um comando)
- Monte o JSON (formato da skill radar-low-ticket + bloco "passada"):
{"data_varredura": "HOJE",
 "gateways": [{"nome": "Kiwify", "slug": "kiwify", "paginas_varridas": 5}],
 "achados": [{"produto": "Nome", "tipo": "marca", "gateway": "Kiwify", "nicho": "slug-do-nicho", "temperatura": "morna", "mencoes": 1, "faixa_preco": "R$ 27", "termo_busca": "Nome", "descricao": "1-2 frases: o que e e como monetiza", "evidencia_url": "url da reclamacao ou do anuncio"}],
 "passada": {"hora": "HORA", "gateways": ["kiwify"], "paginas": 5, "coleta": "ok",
             "relatorio": "## Quentes\n- [[slug]] ou Nome — gateway · por que\n\n## Mornas\n- ...\n\nLeitura: 1-2 linhas", "resumo": "rodada diaria — uma linha"}}
  tipo: "marca" (nome proprio) ou "angulo" (so descrito). Gateway e checkout no vocabulario do Schema.md. Nicho: reuse um slug ja existente (grep -h '^nicho:' Ofertas/*.md | sort | uniq -c). coleta: ok | parcial | sem-coleta.
- Grave em Radar/dados/achados-HOJE-HHMM.json (heredoc com <<'JSON') e rode:
  python3 _meta/publicar.py --achados Radar/dados/achados-HOJE-HHMM.json --sem-push --leitura "2-4 frases: o que esta rodada concluiu"
  Ele grava o snapshot novo em Observacoes/ (append-only), cria/atualiza Ofertas/ no contrato do Templates/T-Oferta.md, grava a nota da passada em Radar/rodadas/, cria/atualiza Radar/HOJE.md (contagens, novas, retornaram, lista de passadas, Leitura da rodada), regenera dashboard/data/ e commita.
- Confira "passada: ..." e "git: commit ..." na saida. Se aparecer "achados invalidos", corrija o JSON e rode de novo. Se o git falhar, nao conserte na forca: passo 6.
- Insumos medidos: se voce mediu dias_no_ar, criativos, preco, checkout, LP etc., edite Ofertas/<slug>.md seguindo Schema.md e recalcule os eixos pelo Scoring.md (frontmatter canonico: listas inline, datas sem aspas). Nunca edite snapshots antigos em Observacoes/.
- Decaimento de status: o sync_vault.py NAO decai por ausencia, de proposito (ausencia fora do escopo varrido e falta de cobertura, nao mercado esfriando). Aplique a tabela de rodadas do Scoring.md a mao SO nas ofertas cujo gateway foi de fato varrido hoje (por esta rodada ou pelas passadas do dia) e que nao apareceram. Anote cada mudanca de status para a leitura.

4) CONSOLIDAR NO PAINEL
- Compute antes de narrar (regra de 31/08 do Painel): python3 _meta/publicar.py --verificar, e leia os numeros de dashboard/data/painel.json (totais, status por oferta, score/decisao, novas de hoje, quem cruza o corte de replicacao).
- Reescreva o texto do Painel.md, nao as tabelas/Bases: o bloco "## Leitura atual — ..." vira "## Leitura anterior — ..." e acima dele entra "## Leitura atual — HOJE (rodada diaria)". Mantenha as 3 leituras anteriores mais recentes e apague as mais velhas (o historico fica no git). Siga o tom e o formato das leituras ja presentes: linha de numeros em negrito, o que mudou desde a rodada anterior, o que e sinal genuino vs. a mesma foto relida, achados de mecanica de funil, gargalos do instrumento, cuidados com os numeros, autocritica honesta. Se nao houve sinal novo real, diga isso com todas as letras.
- Atualize atualizado: HOJE no frontmatter do Painel.md, e em Inicio.md o link "(ultima: [[AAAA-MM-DD]])" e o atualizado.
- Commite (sem push direto): python3 _meta/publicar.py --sem-push --mensagem "painel: leitura da rodada HOJE"
- Abra um PR e faca o merge (SEMPRE, em toda rodada — pedido do usuario). O push HTTPS comum pede senha; use a credencial do gh so no comando:
  git branch -f radar/HOJE HEAD
  git -c credential.helper= -c credential.helper='!gh auth git-credential' push -u origin radar/HOJE
  gh pr create --base main --head radar/HOJE --title "radar: rodada diaria HOJE" --body "<resumo da rodada: gateways, novas, retornos, mudancas de status> + linha final '🤖 Generated with [Claude Code](https://claude.com/claude-code)'"
  gh pr merge radar/HOJE --merge --delete-branch
  git -c credential.helper= -c credential.helper='!gh auth git-credential' fetch origin && git merge --ff-only origin/main && git branch -D radar/HOJE
  Se o gh responder "No commits between main and radar/HOJE", o commit ja esta no main: apague o branch remoto e siga. Se o PR ou o merge falharem (credencial, rede, conflito), o commit fica local: registre na linha final e nao insista.

5) NAO FAZER
- Nao gere planilha, CSV, favoritos nem HTML; nao use SendUserFile. O dashboard substitui isso.
- Nao rode git pull/merge/rebase/reset/checkout fora do passo 0, exceto o "git merge --ff-only origin/main" depois do merge do PR no passo 4.

6) BLOQUEIO
- Se a rodada nao puder ser executada (vault inacessivel, pull em conflito, sem rede, todas as fontes fora do ar), nao invente dados nem escreva Leitura atual ficticia. Se o vault estiver acessivel e o git limpo, registre a passada vazia (JSON com "coleta": "sem-coleta", "achados": [] e o motivo no "resumo") via publicar.py, e acrescente em _meta/Pipeline.md um adendo curto "## Adendo — bloqueio da rodada diaria (HOJE)" se o motivo for novo. Depois pare.

7) FECHAR
- Termine com UMA linha: "Rodada HOJE — N novas (nomes), M revistas, K mudancas de status, coleta X, sinal novo: sim/nao — commit <hash>, PR #<n> merged|pendente".
```

## Por que cada regra existe

- **`git pull --ff-only` no começo e `--push` no fim**: este clone não é o vault do Mac. Sem o
  pull, a leitura não vê as passadas do dia; sem o push, o dashboard e o Mac não veem a rodada.
  Aqui (Linux) o git apaga arquivo normalmente, diferente do VM do Cowork, mas mesmo assim nada de
  merge/rebase pelo agente: divergência é para gente resolver.
- **`--sem-push` no primeiro `publicar.py`**: um push só, no fim, com a leitura do Painel junto.
- **Decaimento manual e só no escopo varrido**: é o que o `sync_vault.py` documenta em
  `aplicar_decaimento` e o [[Scoring]] corrige em vários adendos.
