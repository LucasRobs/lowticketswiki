// Rodadas: a saude da mineracao (cada passada da tarefa agendada) e o registro de cada dia.
import { html, raw, qs, qsa, hojeISO, dataCurta, dataLonga, diaSemana, numero, seloColeta, gateway, ICONE } from "../util.js";
import { faixaSaude } from "../graficos.js";
import { markdown } from "../markdown.js";

function agrupar(p) {
  const porData = new Map();
  const pegar = (d) => {
    if (!porData.has(d)) porData.set(d, { data: d, notas: [], passadas: [] });
    return porData.get(d);
  };
  for (const n of p.dias || []) pegar(n.data).notas.push(n);
  for (const x of p.passadas || []) pegar(x.data).passadas.push(x);
  return [...porData.values()].sort((a, b) => b.data.localeCompare(a.data));
}

function resumoDia(g) {
  const n = g.notas[0];
  const ok = g.passadas.filter((x) => x.coleta === "ok").length;
  const sem = g.passadas.filter((x) => x.coleta === "sem-coleta").length;
  const parcial = g.passadas.length - ok - sem;
  return html`<summary>
    <span class="d-titulo">${diaSemana(g.data)}, ${dataLonga(g.data)}${n && n.titulo && !/^Radar \d{4}-\d{2}-\d{2}$/.test(n.titulo) ? html` <span class="sub">· ${n.titulo}</span>` : ""}</span>
    <span class="d-nums">
      ${n ? html`<span class="selo">${numero(n.ofertas_vistas)} vistas</span><span class="selo forte">${numero(n.novas)} novas</span>${n.retornaram ? html`<span class="selo">${numero(n.retornaram)} retornaram</span>` : ""}` : html`<span class="selo">sem nota do dia</span>`}
      ${g.passadas.length ? html`<span class="selo" title="Passadas da tarefa agendada">${numero(g.passadas.length)} passada${g.passadas.length > 1 ? "s" : ""}${ok ? html` · <span class="col-ok">✓${ok}</span>` : ""}${parcial ? html` · !${parcial}` : ""}${sem ? html` · <span class="col-sem-coleta">✕${sem}</span>` : ""}</span>` : ""}
    </span>
    ${n && n.leitura ? html`<span class="d-leitura">${n.leitura}</span>` : g.passadas[0] && g.passadas[0].resumo ? html`<span class="d-leitura">${g.passadas[0].resumo}</span>` : ""}
  </summary><div class="d-corpo"><p class="carregando" style="padding:8px 0">Carregando…</p></div>`;
}

async function preencher(det, g, estado, recarregarRodadas) {
  const corpo = det.querySelector(".d-corpo");
  if (corpo.dataset.ok) return;
  try {
    const r = await recarregarRodadas();
    const notas = r.dias.filter((d) => d.data === g.data);
    const passadas = r.passadas.filter((x) => x.data === g.data).sort((a, b) => (a.hora || "").localeCompare(b.hora || ""));
    corpo.innerHTML = String(html`
      ${notas.map((n) => html`<div>
        <div class="bloco-titulo">Nota do dia · <code>${n.arquivo}</code>${n.fontes && n.fontes.length ? html` · fontes: ${n.fontes.map(gateway).join(", ")}` : ""}</div>
        <div class="md">${raw(markdown(n.corpo, { ofertas: estado.porSlug, pularH1: true }))}</div></div>`)}
      ${passadas.length ? html`<div>
        <div class="bloco-titulo">Passadas da tarefa agendada</div>
        <div class="pilha">${passadas.map((x) => html`<article class="passada">
          <div class="passada-topo"><strong>${x.hora || "—"}</strong> ${seloColeta(x.coleta)}
            <span class="sub">${x.gateways && x.gateways.length ? x.gateways.map(gateway).join(", ") : "sem gateway"} · ${numero(x.paginas)} páginas</span>
            <span class="sub mudo">${x.arquivo}</span></div>
          <div class="md">${raw(markdown(x.corpo, { ofertas: estado.porSlug, pularH1: true, nivelTitulo: 2 }))}</div>
        </article>`)}</div></div>` : ""}
    `);
    corpo.dataset.ok = "1";
  } catch (e) {
    corpo.innerHTML = String(html`<p class="sub">Não consegui carregar: ${String(e.message || e)}</p>`);
  }
}

export function render(main, { estado, rota, recarregarRodadas }) {
  const p = estado.painel;
  const hoje = hojeISO();
  const grupos = agrupar(p);
  const alvo = rota.resto[0];
  const passadas = p.passadas || [];
  const semana = passadas.filter((x) => x.data > dataMenos(hoje, 7));
  const okSemana = semana.filter((x) => x.coleta !== "sem-coleta").length;
  const ultimaOk = passadas.find((x) => x.coleta !== "sem-coleta");

  main.innerHTML = String(html`
    <div class="cabecalho-pagina">
      <div>
        <h1>Rodadas</h1>
        <p>Cada passada da tarefa agendada vira uma nota em <code>Radar/rodadas/</code>; cada dia, uma nota em <code>Radar/</code>.</p>
      </div>
    </div>
    <section class="cartao" style="margin-bottom:16px">
      <h2 class="secao">Saúde da coleta · últimos 14 dias
        <span class="sub">${numero(okSemana)} de ${numero(semana.length)} passadas com coleta nos últimos 7 dias${ultimaOk ? html` · última com coleta: ${dataCurta(ultimaOk.data)} ${ultimaOk.hora}` : ""}</span></h2>
      <div id="saude"></div>
    </section>
    <div class="pilha" id="dias">
      ${grupos.map((g) => html`<details class="cartao dia" id="dia-${g.data}" data-data="${g.data}" ${g.data === alvo ? "open" : ""}>${resumoDia(g)}</details>`)}
    </div>
  `);

  faixaSaude(qs("#saude"), passadas, 14, hoje);
  for (const det of qsa("details.dia")) {
    const g = grupos.find((x) => x.data === det.dataset.data);
    det.addEventListener("toggle", () => { if (det.open) preencher(det, g, estado, recarregarRodadas); });
    if (det.open) preencher(det, g, estado, recarregarRodadas);
  }
  if (alvo) {
    const el = document.getElementById("dia-" + alvo);
    if (el) setTimeout(() => el.scrollIntoView({ block: "start" }), 30);
  }
  void ICONE;
}

function dataMenos(iso, n) {
  const d = new Date(iso + "T12:00:00Z");
  d.setUTCDate(d.getUTCDate() - n);
  return d.toISOString().slice(0, 10);
}
