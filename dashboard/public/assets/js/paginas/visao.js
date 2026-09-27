// Visao geral: estado da mineracao, numeros do vault, descobertas por dia e o que mexeu.
import {
  html, qs, hojeISO, diasEntre, dataCurta, dataHora, relativo, numero, dinheiro, score, humano, gateway,
  seloColeta, seloDecisao, seloStatus, momentoPassada, STATUS, ICONE,
} from "../util.js";
import { colunasEmpilhadas, barrasHorizontais } from "../graficos.js";

function linhaOferta(o, direita) {
  const meta = [humano(o.nicho), o.checkout && o.checkout !== "desconhecido" ? gateway(o.checkout) : null,
    o.ticket_medio_est > 0 ? dinheiro(o.ticket_medio_est, o.moeda) : null].filter(Boolean);
  return html`<li><a class="linha" href="#/oferta/${o.slug}">
    <span class="nome">${o.nome}</span>
    <span class="direita">${direita}</span>
    <span class="meta">${meta.join(" · ")}${o.classe === "angulo" ? html` · <span class="mudo">ângulo</span>` : ""}</span>
    ${o.resumo ? html`<span class="resumo">${o.resumo}</span>` : ""}
  </a></li>`;
}

function contar(lista, chave) {
  const c = new Map();
  for (const o of lista) {
    const v = o[chave] || "—";
    c.set(v, (c.get(v) || 0) + 1);
  }
  return [...c.entries()].sort((a, b) => b[1] - a[1] || String(a[0]).localeCompare(String(b[0])));
}

export function render(main, { estado, navegar }) {
  const p = estado.painel;
  const hoje = hojeISO();
  const todas = p.ofertas;
  const reais = todas.filter((o) => o.classe === "oferta");
  const ult = p.totais.ultima_rodada;

  const idade = (o) => diasEntre(o.visto_primeiro, hoje);
  const novas7 = todas.filter((o) => o.visto_primeiro && idade(o) >= 0 && idade(o) <= 6);
  const novasAnt = todas.filter((o) => o.visto_primeiro && idade(o) >= 7 && idade(o) <= 13);
  const delta = novas7.length - novasAnt.length;
  const vistasUlt = todas.filter((o) => o.visto_ultimo === ult);
  const novasUlt = todas.filter((o) => o.visto_primeiro === ult);
  const noCorte = reais.filter((o) => o.decisao === "replicar");
  const comVeredito = todas.filter((o) => ["replicar", "replicando", "replicada"].includes(o.veredito));
  const nichos = new Set(todas.map((o) => o.nicho)).size;

  // passadas: ultima, ultima com coleta e o placar de hoje
  const passadas = p.passadas || [];
  const ultima = passadas[0];
  const ultimaOk = passadas.find((x) => x.coleta === "ok" || x.coleta === "parcial");
  const deHoje = passadas.filter((x) => x.data === hoje);

  const novidades = todas.slice().sort((a, b) =>
    (b.visto_primeiro || "").localeCompare(a.visto_primeiro || "") || b.score - a.score).slice(0, 12);
  const revistas = todas.filter((o) => o.rodadas_vista >= 2 && o.visto_ultimo && o.visto_primeiro < o.visto_ultimo
    && diasEntre(o.visto_ultimo, ult) <= 2)
    .sort((a, b) => (b.visto_ultimo || "").localeCompare(a.visto_ultimo || "") || b.rodadas_vista - a.rodadas_vista || b.ra_reclamacoes - a.ra_reclamacoes)
    .slice(0, 8);
  const melhores = reais.slice().sort((a, b) => b.score - a.score || b.prioridade - a.prioridade).slice(0, 8);

  const porNicho = contar(todas, "nicho");
  const topNichos = porNicho.slice(0, 10);
  const outros = porNicho.slice(10).reduce((a, [, n]) => a + n, 0);
  const porGateway = contar(reais, "checkout").slice(0, 10);
  const porStatus = contar(todas, "status").sort((a, b) => Object.keys(STATUS).indexOf(a[0]) - Object.keys(STATUS).indexOf(b[0]));

  main.innerHTML = String(html`
    <div class="cabecalho-pagina">
      <div>
        <h1>Visão geral</h1>
        <p>Tudo o que o radar já minerou, direto do vault. Atualiza sozinho a cada nova mineração publicada.</p>
      </div>
    </div>

    <section class="faixa-status" aria-label="Estado da mineração">
      ${ultima ? html`<span class="item">Última passada <strong>${dataCurta(ultima.data)} ${ultima.hora}</strong>
        <span class="mudo">(${relativo(momentoPassada(ultima.data, ultima.hora).toISOString())})</span> ${seloColeta(ultima.coleta)}</span>` : html`<span class="item">Nenhuma passada registrada ainda</span>`}
      ${ultima && ultima.coleta === "sem-coleta" && ultimaOk ? html`<span class="item">Última com coleta <strong>${dataCurta(ultimaOk.data)} ${ultimaOk.hora}</strong></span>` : ""}
      <span class="item">Hoje <strong>${deHoje.length}</strong> passada${deHoje.length === 1 ? "" : "s"}${deHoje.length ? html` <span class="mudo">(${deHoje.filter((x) => x.coleta !== "sem-coleta").length} com coleta)</span>` : ""}</span>
      <span class="item">Dados de <strong>${dataHora(p.versao && p.versao.atualizado_em)}</strong></span>
      <a class="item" href="#/rodadas">Ver rodadas →</a>
    </section>

    <section class="kpis" aria-label="Números do vault">
      <div class="cartao kpi">
        <div class="rotulo">Ofertas mapeadas</div>
        <a class="valor" href="#/ofertas?classe=oferta">${numero(reais.length)}</a>
        <div class="detalhe">+ ${numero(p.totais.angulos)} ângulos · ${numero(nichos)} nichos</div>
      </div>
      <div class="cartao kpi">
        <div class="rotulo">Novas nos últimos 7 dias</div>
        <a class="valor" href="#/ofertas?desde=7&campo=primeiro">${numero(novas7.length)}</a>
        <div class="detalhe"><span class="${delta > 0 ? "delta-sobe" : "delta-desce"}">${delta > 0 ? "+" : delta < 0 ? "−" : "±"}${numero(Math.abs(delta))}</span> vs. 7 dias anteriores</div>
      </div>
      <div class="cartao kpi">
        <div class="rotulo">Vistas na última rodada${ult ? html` (${dataCurta(ult)})` : ""}</div>
        <a class="valor" href="#/ofertas?visto=${ult}">${numero(vistasUlt.length)}</a>
        <div class="detalhe">${numero(novasUlt.length)} estreia${novasUlt.length === 1 ? "" : "s"} no dia</div>
      </div>
      <div class="cartao kpi">
        <div class="rotulo">No corte de replicação</div>
        <a class="valor" href="#/ofertas?decisao=replicar">${numero(noCorte.length)}</a>
        <div class="detalhe">${numero(comVeredito.length)} com veredito “replicar” seu</div>
      </div>
      <div class="cartao kpi">
        <div class="rotulo">Snapshots registrados</div>
        <div class="valor">${numero(p.totais.observacoes)}</div>
        <div class="detalhe">${numero(p.totais.dias_radar)} dias de radar · ${numero(p.totais.passadas)} passadas</div>
      </div>
    </section>

    <div class="grade grade-principal">
      <div class="pilha">
        <section class="cartao">
          <h2 class="secao">Descobertas por dia <span class="sub">primeira vez que cada nota foi vista · clique num dia para filtrar</span></h2>
          <div id="grafico-descobertas"></div>
        </section>
        <section class="cartao">
          <h2 class="secao">Novidades <a class="sub" href="#/ofertas?ordem=primeiro">ver todas →</a></h2>
          <ul class="lista">${novidades.map((o) => linhaOferta(o, html`${dataCurta(o.visto_primeiro)} ${seloDecisao(o.decisao, o.flags)}`))}</ul>
        </section>
      </div>
      <div class="pilha">
        <section class="cartao">
          <h2 class="secao">Revistas nas últimas rodadas <span class="sub">apareceram de novo</span></h2>
          ${revistas.length ? html`<ul class="lista">${revistas.map((o) => linhaOferta(o, html`${o.rodadas_vista}× · ${dataCurta(o.visto_ultimo)}`))}</ul>`
            : html`<p class="vazio">Nenhuma oferta reapareceu nas últimas rodadas.</p>`}
        </section>
        <section class="cartao">
          <h2 class="secao">Maiores scores <a class="sub" href="#/ofertas?classe=oferta&ordem=score">ranking →</a></h2>
          <ul class="lista">${melhores.map((o) => linhaOferta(o, html`<b>${score(o.score)}</b> ${seloDecisao(o.decisao, o.flags)}`))}</ul>
          <p class="sub" style="margin:10px 0 0">Score = (lucro×35 + réplica×30 + ticket×20 + saturação×15)/100. “prov.” = há eixo não avaliado.</p>
        </section>
      </div>
    </div>

    <div class="grade grade-3" style="margin-top:16px">
      <section class="cartao">
        <h2 class="secao">Por nicho <span class="sub">${numero(nichos)} nichos</span></h2>
        ${barrasHorizontais(topNichos.map(([n, v]) => ({ rotulo: humano(n), valor: v, href: `#/ofertas?nicho=${encodeURIComponent(n)}` })), { total: todas.length })}
        ${outros ? html`<p class="nota-rodape">+ ${numero(outros)} notas em ${numero(porNicho.length - topNichos.length)} outros nichos — <a href="#/ofertas">ver todas</a></p>` : ""}
      </section>
      <section class="cartao">
        <h2 class="secao">Por gateway <span class="sub">checkout das ofertas</span></h2>
        ${barrasHorizontais(porGateway.map(([g, v]) => ({ rotulo: gateway(g), valor: v, href: `#/ofertas?gateway=${encodeURIComponent(g)}` })), { total: reais.length })}
      </section>
      <section class="cartao">
        <h2 class="secao">Por status <span class="sub">ciclo de vida no vault</span></h2>
        ${barrasHorizontais(porStatus.map(([s, v]) => ({ rotulo: STATUS[s] || s, valor: v, href: `#/ofertas?status=${encodeURIComponent(s)}` })), { total: todas.length })}
        <p class="nota-rodape">${ICONE.alerta} ${numero((p.qualidade.status_vencido || []).length)} notas seguem “nova” depois da estreia — ver <a href="#/qualidade">qualidade</a>.</p>
      </section>
    </div>
  `);

  const porDia = {};
  for (const [dia, v] of Object.entries(p.serie.descobertas || {})) porDia[dia] = { oferta: v.oferta || 0, angulo: v.angulo || 0 };
  colunasEmpilhadas(qs("#grafico-descobertas"), {
    series: [
      { chave: "oferta", rotulo: "Ofertas", cor: "--serie-1" },
      { chave: "angulo", rotulo: "Ângulos", cor: "--serie-2" },
    ],
    porDia,
    altura: 170,
    aoClicar: (dia) => navegar(`#/ofertas?primeiro=${dia}`),
  });
}
