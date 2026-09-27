// Ofertas: a tabela de tudo que ja foi minerado, com busca, filtros e ordenacao.
// Os filtros vivem na URL (#/ofertas?nicho=...&status=...) — da para salvar e compartilhar.
import {
  html, qs, qsa, esc, hojeISO, diasEntre, dataCurta, dataLonga, relativo, numero, dinheiro, score, humano, gateway,
  seloDecisao, seloStatus, normalizar, debounce, STATUS, DECISAO, VEREDITO, FLAGS, ICONE,
} from "../util.js";

const CAMPOS_FILTRO = ["q", "classe", "status", "nicho", "gateway", "veredito", "decisao", "desde", "campo", "primeiro", "visto", "flag", "ordem", "dir"];

const ORDENS = {
  recentes: { rotulo: "Visto por último", chave: (o) => (o.visto_ultimo || "") + (o.visto_primeiro || ""), dir: "desc" },
  primeiro: { rotulo: "Primeira vez vista", chave: (o) => o.visto_primeiro || "", dir: "desc" },
  score: { rotulo: "Score", chave: (o) => o.score, dir: "desc" },
  nome: { rotulo: "Nome", chave: (o) => normalizar(o.nome), dir: "asc" },
  ra: { rotulo: "Reclamações", chave: (o) => o.ra_reclamacoes, dir: "desc" },
  dias: { rotulo: "Dias no ar", chave: (o) => o.dias_no_ar, dir: "desc" },
  ticket: { rotulo: "Ticket médio", chave: (o) => o.ticket_medio_est, dir: "desc" },
  rodadas: { rotulo: "Rodadas vista", chave: (o) => o.rodadas_vista, dir: "desc" },
  status: { rotulo: "Status", chave: (o) => Object.keys(STATUS).indexOf(o.status), dir: "asc" },
};

function lerFiltros(params) {
  const f = {};
  for (const c of CAMPOS_FILTRO) f[c] = params.get(c) || "";
  if (!ORDENS[f.ordem]) f.ordem = "recentes";
  if (f.dir !== "asc" && f.dir !== "desc") f.dir = ORDENS[f.ordem].dir;
  return f;
}

function escreverFiltros(f) {
  const p = new URLSearchParams();
  for (const c of CAMPOS_FILTRO) {
    if (!f[c]) continue;
    if (c === "ordem" && f[c] === "recentes") continue;
    if (c === "dir" && f[c] === ORDENS[f.ordem].dir) continue;
    p.set(c, f[c]);
  }
  const q = p.toString();
  history.replaceState(null, "", "#/ofertas" + (q ? "?" + q : ""));
}

export function filtrar(ofertas, f, hoje = hojeISO()) {
  const termo = normalizar(f.q).trim();
  return ofertas.filter((o) => {
    if (f.classe && o.classe !== f.classe) return false;
    if (f.status && o.status !== f.status) return false;
    if (f.nicho && o.nicho !== f.nicho) return false;
    if (f.gateway && o.checkout !== f.gateway && !(o.gateways || []).includes(f.gateway)) return false;
    if (f.veredito && o.veredito !== f.veredito) return false;
    if (f.decisao && o.decisao !== f.decisao) return false;
    if (f.flag && !(o.flags || []).includes(f.flag)) return false;
    if (f.primeiro && o.visto_primeiro !== f.primeiro) return false;
    if (f.visto && o.visto_ultimo !== f.visto) return false;
    if (f.desde) {
      const campo = f.campo === "primeiro" ? o.visto_primeiro : o.visto_ultimo;
      const d = diasEntre(campo, hoje);
      if (d === null || d < 0 || d > Number(f.desde) - 1) return false;
    }
    if (termo) {
      const alvo = normalizar([o.nome, o.slug, o.nicho, o.sub_nicho, o.resumo, o.checkout, (o.gateways || []).join(" ")].join(" "));
      for (const palavra of termo.split(/\s+/)) if (!alvo.includes(palavra)) return false;
    }
    return true;
  });
}

function ordenar(lista, f) {
  const o = ORDENS[f.ordem];
  const fator = f.dir === "asc" ? 1 : -1;
  return lista.slice().sort((a, b) => {
    const va = o.chave(a), vb = o.chave(b);
    if (va < vb) return -1 * fator;
    if (va > vb) return 1 * fator;
    return b.score - a.score || a.slug.localeCompare(b.slug);
  });
}

function opcoes(valores, atual, rotulo, todos) {
  return html`<option value="">${todos}</option>${valores.map(([v, n]) =>
    html`<option value="${v}" ${v === atual ? "selected" : ""}>${rotulo(v)}${n !== undefined ? ` (${n})` : ""}</option>`)}`;
}

function contagem(lista, fn) {
  const c = new Map();
  for (const o of lista) for (const v of [].concat(fn(o))) if (v) c.set(v, (c.get(v) || 0) + 1);
  return c;
}

function linha(o) {
  const prov = (o.flags || []).includes("score-provisorio") && o.classe !== "angulo";
  const alerta = (o.flags || []).includes("lucro-sem-medicao");
  return html`<tr data-slug="${o.slug}">
    <td class="t-nome"><a href="#/oferta/${o.slug}">${o.nome}</a>
      ${alerta ? html` <span class="aviso-mini" title="${FLAGS["lucro-sem-medicao"].texto}">${ICONE.alerta}</span>` : ""}
      <span class="sub">${humano(o.nicho)}${o.classe === "angulo" ? " · ângulo" : ""}</span></td>
    <td class="num"><span class="pontuacao ${prov ? "provisorio" : ""}" title="${prov ? "Score provisório: há eixo em 0 (não avaliado)" : ""}">
      <span class="mini"><div style="width:${Math.min(100, o.score * 10)}%"></div></span>${score(o.score)}</span></td>
    <td class="col-celular-oculta">${seloDecisao(o.decisao, o.flags)}</td>
    <td>${seloStatus(o.status)}</td>
    <td class="col-opcional nowrap">${o.checkout ? gateway(o.checkout) : "—"}</td>
    <td class="num col-media">${dinheiro(o.ticket_medio_est, o.moeda)}</td>
    <td class="num col-opcional">${o.ra_reclamacoes || "—"}</td>
    <td class="num col-opcional">${o.dias_no_ar || "—"}</td>
    <td class="nowrap"><span title="Visto pela primeira vez em ${dataLonga(o.visto_primeiro)}">${dataCurta(o.visto_ultimo)}</span>
      <span class="sub">${o.rodadas_vista}× · desde ${dataCurta(o.visto_primeiro)}</span></td>
    <td class="col-opcional nowrap">${o.veredito ? VEREDITO[o.veredito] || o.veredito : "—"}${o.prioridade ? html` <span class="mudo">P${o.prioridade}</span>` : ""}</td>
  </tr>`;
}

function csv(lista) {
  const cols = ["slug", "nome", "classe", "nicho", "sub_nicho", "status", "decisao", "score", "s_lucro", "s_replica", "s_ticket",
    "s_saturacao", "veredito", "prioridade", "checkout", "gateways", "ticket_frente", "ticket_medio_est", "ra_reclamacoes",
    "dias_no_ar", "criativos_ultima", "visto_primeiro", "visto_ultimo", "rodadas_vista", "url_pagina", "url_ads", "flags", "resumo"];
  const cel = (v) => {
    if (Array.isArray(v)) v = v.join(", ");
    if (typeof v === "number") v = String(v).replace(".", ",");
    v = String(v ?? "");
    return /[;"\n\r]/.test(v) ? '"' + v.replace(/"/g, '""') + '"' : v;
  };
  const linhas = [cols.join(";")].concat(lista.map((o) => cols.map((c) => cel(o[c])).join(";")));
  const blob = new Blob(["﻿" + linhas.join("\r\n")], { type: "text/csv;charset=utf-8" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `radar-ofertas-${hojeISO()}.csv`;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 500);
}

export function render(main, { estado, navegar }) {
  const todas = estado.painel.ofertas;
  const f = lerFiltros(new URLSearchParams(location.hash.split("?")[1] || ""));
  const nichos = [...contagem(todas, (o) => o.nicho).entries()].sort((a, b) => humano(a[0]).localeCompare(humano(b[0]), "pt-BR"));
  const gws = [...contagem(todas, (o) => [o.checkout, ...(o.gateways || [])].filter((g, i, arr) => arr.indexOf(g) === i)).entries()]
    .sort((a, b) => b[1] - a[1]);
  const status = Object.keys(STATUS).map((s) => [s, todas.filter((o) => o.status === s).length]);
  const vereditos = Object.keys(VEREDITO).map((v) => [v, todas.filter((o) => o.veredito === v).length]).filter(([, n]) => n);
  const decisoes = Object.keys(DECISAO).map((d) => [d, todas.filter((o) => o.decisao === d).length]).filter(([, n]) => n);

  const cabecalho = (chave, rotulo, classe = "") => {
    const ativo = f.ordem === chave;
    return html`<th class="${classe}" scope="col" ${ativo ? html`aria-sort="${f.dir === "asc" ? "ascending" : "descending"}"` : ""}><button type="button" data-ordem="${chave}">${rotulo}</button></th>`;
  };

  main.innerHTML = String(html`
    <div class="cabecalho-pagina">
      <div>
        <h1>Ofertas</h1>
        <p>${numero(todas.length)} notas no vault — ofertas concretas e ângulos (padrões sem dono). Clique numa linha para abrir a nota.</p>
      </div>
    </div>
    <div class="filtros" role="search">
      <div class="campo-busca">${ICONE.busca}<input id="f-q" type="search" placeholder="Buscar por nome, nicho, gateway, ângulo…" value="${f.q}" aria-label="Buscar ofertas"></div>
      <div class="segmentado" role="group" aria-label="Classe">
        <button type="button" data-classe="" aria-pressed="${!f.classe}">Todas</button>
        <button type="button" data-classe="oferta" aria-pressed="${f.classe === "oferta"}">Ofertas</button>
        <button type="button" data-classe="angulo" aria-pressed="${f.classe === "angulo"}">Ângulos</button>
      </div>
      <select id="f-status" aria-label="Status">${opcoes(status, f.status, (s) => STATUS[s], "Status: todos")}</select>
      <select id="f-nicho" aria-label="Nicho">${opcoes(nichos, f.nicho, humano, "Nicho: todos")}</select>
      <select id="f-gateway" aria-label="Gateway">${opcoes(gws, f.gateway, gateway, "Gateway: todos")}</select>
      <select id="f-decisao" aria-label="Decisão pelo score">${opcoes(decisoes, f.decisao, (d) => DECISAO[d], "Decisão: todas")}</select>
      <select id="f-veredito" aria-label="Seu veredito">${opcoes(vereditos, f.veredito, (v) => VEREDITO[v], "Veredito: todos")}</select>
      <select id="f-desde" aria-label="Período">
        ${opcoes([["1"], ["3"], ["7"], ["14"], ["30"]], f.desde, (d) => (d === "1" ? "Vistas hoje" : `Vistas nos últimos ${d} dias`), "Período: todo")}
      </select>
      <button type="button" class="botao fantasma" id="limpar">Limpar</button>
    </div>
    <div id="filtros-extra" class="selos" style="margin:-2px 0 10px"></div>
    <div class="contagem"><span id="contagem"></span>
      <span class="selos">
        <label class="sub" for="f-ordem">Ordenar</label>
        <select id="f-ordem" class="entrada" style="height:30px">${Object.entries(ORDENS).map(([k, v]) => html`<option value="${k}" ${k === f.ordem ? "selected" : ""}>${v.rotulo}</option>`)}</select>
        <button type="button" class="botao" id="csv" title="Baixar as linhas filtradas em CSV (abre no Excel)">${ICONE.baixar} CSV</button>
      </span>
    </div>
    <div class="tabela-caixa">
      <table class="tabela">
        <thead><tr>
          ${cabecalho("nome", "Oferta")}
          ${cabecalho("score", "Score", "num")}
          <th scope="col" class="col-celular-oculta">Decisão</th>
          ${cabecalho("status", "Status")}
          <th scope="col" class="col-opcional">Gateway</th>
          ${cabecalho("ticket", "Ticket médio", "num col-media")}
          ${cabecalho("ra", "Reclam.", "num col-opcional")}
          ${cabecalho("dias", "Dias no ar", "num col-opcional")}
          ${cabecalho("recentes", "Visto")}
          <th scope="col" class="col-opcional">Veredito</th>
        </tr></thead>
        <tbody id="corpo-tabela"></tbody>
      </table>
    </div>
  `);

  const pintar = () => {
    const lista = ordenar(filtrar(todas, f), f);
    qs("#corpo-tabela").innerHTML = lista.length ? String(html`${lista.map(linha)}`)
      : String(html`<tr><td colspan="10" class="vazio" style="text-align:center;padding:28px">Nenhuma oferta com esses filtros.</td></tr>`);
    qs("#contagem").textContent = lista.length === todas.length ? `${numero(todas.length)} notas` : `${numero(lista.length)} de ${numero(todas.length)} notas`;
    for (const sel of ["status", "nicho", "gateway", "decisao", "veredito", "desde"]) qs("#f-" + sel).classList.toggle("ativo", Boolean(f[sel]));
    qs("#f-q").classList.toggle("ativo", Boolean(f.q));
    for (const b of qsa(".segmentado button")) b.setAttribute("aria-pressed", String((b.dataset.classe || "") === f.classe));
    for (const th of qsa(".tabela thead th")) {
      const b = th.querySelector("button");
      if (!b) continue;
      if (b.dataset.ordem === f.ordem) th.setAttribute("aria-sort", f.dir === "asc" ? "ascending" : "descending");
      else th.removeAttribute("aria-sort");
    }
    // filtros que nao tem controle proprio viram selos removiveis
    const extras = [];
    if (f.primeiro) extras.push(["primeiro", `Primeira vez vista em ${dataLonga(f.primeiro)}`]);
    if (f.visto) extras.push(["visto", `Vistas em ${dataLonga(f.visto)}`]);
    if (f.flag) extras.push(["flag", (FLAGS[f.flag] || { curto: f.flag }).curto]);
    if (f.desde && f.campo === "primeiro") extras.push(["campo", "Contando pela primeira vez vista"]);
    qs("#filtros-extra").innerHTML = String(html`${extras.map(([k, t]) => html`<button type="button" class="selo" data-remover="${k}" title="Remover filtro">${t} ${ICONE.x}</button>`)}`);
    for (const b of qsa("#filtros-extra [data-remover]")) b.addEventListener("click", () => { f[b.dataset.remover] = ""; escreverFiltros(f); pintar(); });
    escreverFiltros(f);
    return lista;
  };

  let atual = pintar();
  const mudar = (campo, valor) => { f[campo] = valor; atual = pintar(); };

  qs("#f-q").addEventListener("input", debounce((ev) => mudar("q", ev.target.value), 120));
  for (const sel of ["status", "nicho", "gateway", "decisao", "veredito", "desde"]) {
    qs("#f-" + sel).addEventListener("change", (ev) => mudar(sel, ev.target.value));
  }
  qs("#f-ordem").addEventListener("change", (ev) => { f.ordem = ev.target.value; f.dir = ORDENS[f.ordem].dir; atual = pintar(); });
  for (const b of qsa(".segmentado button")) b.addEventListener("click", () => mudar("classe", b.dataset.classe || ""));
  for (const b of qsa(".tabela thead th button")) {
    b.addEventListener("click", () => {
      const k = b.dataset.ordem;
      if (f.ordem === k) f.dir = f.dir === "asc" ? "desc" : "asc";
      else { f.ordem = k; f.dir = ORDENS[k].dir; }
      qs("#f-ordem").value = f.ordem;
      atual = pintar();
    });
  }
  qs("#limpar").addEventListener("click", () => navegar("#/ofertas"));
  qs("#csv").addEventListener("click", () => csv(atual));
  qs("#corpo-tabela").addEventListener("click", (ev) => {
    if (ev.target.closest("a")) return;
    const tr = ev.target.closest("tr[data-slug]");
    if (tr) navegar("#/oferta/" + tr.dataset.slug);
  });
  void esc; void relativo;
}
