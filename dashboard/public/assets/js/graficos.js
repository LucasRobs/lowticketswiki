// graficos.js — graficos sem biblioteca: colunas empilhadas (SVG), barras horizontais,
// medidores e a faixa de saude das passadas. Specs do skill de dataviz: marcas finas,
// topo arredondado de 4px e base reta, 2px de folga na cor da superficie entre segmentos,
// grade em linha fina, tooltip em hover/foco com alvo maior que a marca, e tabela equivalente.

import { html, esc, dataCurta, dataLonga, diaSemana, somarDias, numero } from "./util.js";

const NS = "http://www.w3.org/2000/svg";

// ---------- tooltip compartilhado ----------
const tip = () => document.getElementById("tooltip");

export function mostrarTooltip(ev, titulo, linhas) {
  const el = tip();
  if (!el) return;
  el.replaceChildren();
  const t = document.createElement("div");
  t.className = "tt-titulo";
  t.textContent = titulo;
  el.appendChild(t);
  for (const l of linhas) {
    const row = document.createElement("div");
    row.className = "tt-linha";
    const chave = document.createElement("span");
    chave.className = "tt-chave";
    if (l.cor) {
      const i = document.createElement("i");
      i.style.background = l.cor;
      chave.appendChild(i);
    }
    chave.appendChild(document.createTextNode(l.rotulo));
    const b = document.createElement("b");
    b.textContent = l.valor;
    row.append(b, chave);
    el.appendChild(row);
  }
  el.hidden = false;
  posicionar(ev);
}

function posicionar(ev) {
  const el = tip();
  if (!el || el.hidden) return;
  let x, y;
  if (ev && typeof ev.clientX === "number" && ev.type !== "focus" && ev.type !== "focusin") {
    x = ev.clientX; y = ev.clientY;
  } else if (ev && ev.target && ev.target.getBoundingClientRect) {
    const r = ev.target.getBoundingClientRect();
    x = r.left + r.width / 2; y = r.top;
  } else return;
  const w = el.offsetWidth, h = el.offsetHeight;
  let left = x + 14, top = y - h - 12;
  if (left + w > window.innerWidth - 8) left = x - w - 14;
  if (left < 8) left = 8;
  if (top < 8) top = y + 16;
  el.style.left = left + "px";
  el.style.top = top + "px";
}

export function esconderTooltip() {
  const el = tip();
  if (el) el.hidden = true;
}

function cor(varName) {
  return getComputedStyle(document.documentElement).getPropertyValue(varName).trim() || "#2a78d6";
}

function passoBonito(bruto) {
  const exp = Math.pow(10, Math.floor(Math.log10(Math.max(bruto, 1e-9))));
  const f = bruto / exp;
  return (f <= 1 ? 1 : f <= 2 ? 2 : f <= 5 ? 5 : 10) * exp;
}

function el(tag, attrs = {}, pai) {
  const n = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
  if (pai) pai.appendChild(n);
  return n;
}

function caminhoColuna(x, yTopo, largura, yBase, raio) {
  const h = yBase - yTopo;
  const r = Math.max(0, Math.min(raio, h, largura / 2));
  if (r === 0) return `M${x},${yBase}V${yTopo}H${x + largura}V${yBase}Z`;
  return `M${x},${yBase}V${yTopo + r}Q${x},${yTopo} ${x + r},${yTopo}H${x + largura - r}Q${x + largura},${yTopo} ${x + largura},${yTopo + r}V${yBase}Z`;
}

/**
 * Colunas empilhadas por dia (calendario continuo: dia sem rodada aparece como vazio).
 * @param {HTMLElement} alvo
 * @param {{series: {chave:string, rotulo:string, cor:string}[], porDia: Object<string, Object<string, number>>, altura?: number, aoClicar?: (dia:string)=>void}} cfg
 */
export function colunasEmpilhadas(alvo, cfg) {
  const dias = Object.keys(cfg.porDia).sort();
  alvo.replaceChildren();
  alvo.classList.add("grafico");
  if (!dias.length) {
    alvo.innerHTML = '<p class="vazio">Sem dados ainda.</p>';
    return;
  }
  const todos = [];
  for (let d = dias[0]; d <= dias[dias.length - 1]; d = somarDias(d, 1)) todos.push(d);

  // legenda (>= 2 series) acima do grafico
  if (cfg.series.length > 1) {
    const leg = document.createElement("div");
    leg.className = "legenda";
    for (const s of cfg.series) {
      const span = document.createElement("span");
      const i = document.createElement("i");
      i.style.background = cor(s.cor);
      span.append(i, document.createTextNode(s.rotulo));
      leg.appendChild(span);
    }
    alvo.appendChild(leg);
  }

  const caixa = document.createElement("div");
  alvo.appendChild(caixa);

  const desenhar = () => {
    caixa.replaceChildren();
    const W = Math.max(280, caixa.clientWidth || alvo.clientWidth || 600);
    const alturaPlot = cfg.altura || 180;
    const m = { e: 30, d: 6, t: 8, b: 24 };
    const H = alturaPlot + m.t + m.b;
    const pw = W - m.e - m.d;
    const totais = todos.map((d) => cfg.series.reduce((a, s) => a + ((cfg.porDia[d] || {})[s.chave] || 0), 0));
    const maxBruto = Math.max(1, ...totais);
    const passo = passoBonito(maxBruto / 3);
    const yMax = Math.ceil(maxBruto / passo) * passo;
    const y = (v) => m.t + alturaPlot - (v / yMax) * alturaPlot;

    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: W, height: H, role: "img",
      "aria-label": `Colunas por dia, de ${dataLonga(todos[0])} a ${dataLonga(todos[todos.length - 1])}. Tabela equivalente abaixo.` });
    const eixo = el("g", { class: "eixo" }, svg);
    for (let v = 0; v <= yMax + 1e-9; v += passo) {
      const yy = Math.round(y(v)) + 0.5;
      el("line", { class: v === 0 ? "linha-base" : "grade-l", x1: m.e, x2: W - m.d, y1: yy, y2: yy }, svg);
      const t = el("text", { x: m.e - 8, y: yy + 3.5, "text-anchor": "end" }, eixo);
      t.textContent = numero(v);
    }
    const slot = pw / todos.length;
    const larg = Math.max(2, Math.min(24, slot * 0.62));
    const cada = Math.max(1, Math.ceil(44 / slot));
    const cores = cfg.series.map((s) => cor(s.cor));
    const superficie = cor("--superficie");

    const marcas = el("g", {}, svg);
    todos.forEach((d, i) => {
      const x = m.e + i * slot + (slot - larg) / 2;
      const valores = cfg.porDia[d] || {};
      const g = el("g", { class: "coluna" }, marcas);
      let acumulado = 0;
      const visiveis = cfg.series.map((s) => valores[s.chave] || 0);
      const ultimo = visiveis.reduce((u, v, k) => (v > 0 ? k : u), -1);
      cfg.series.forEach((s, k) => {
        const v = visiveis[k];
        if (!v) return;
        const yBase = y(acumulado) - (acumulado > 0 ? 2 : 0); // 2px de folga entre segmentos
        acumulado += v;
        const yTopo = y(acumulado);
        if (yBase - yTopo <= 0) return;
        el("path", { d: caminhoColuna(x, yTopo, larg, yBase, k === ultimo ? 4 : 0), fill: cores[k] }, g);
      });
      if ((todos.length - 1 - i) % cada === 0) {
        const t = el("text", { x: m.e + i * slot + slot / 2, y: H - 6, "text-anchor": "middle" }, eixo);
        t.textContent = dataCurta(d);
      }
      // alvo de hover/foco: a faixa inteira do dia, mais larga que a coluna
      const hit = el("rect", { class: "alvo", x: m.e + i * slot, y: m.t, width: slot, height: alturaPlot, tabindex: "0",
        "aria-label": `${dataLonga(d)}: ` + cfg.series.map((s, k) => `${s.rotulo} ${visiveis[k]}`).join(", ") }, svg);
      const abrir = (ev) => {
        g.classList.add("ativa");
        const linhas = cfg.series.map((s, k) => ({ rotulo: s.rotulo, valor: numero(visiveis[k]), cor: cores[k] }));
        if (cfg.series.length > 1) linhas.push({ rotulo: "Total", valor: numero(totais[i]) });
        mostrarTooltip(ev, `${diaSemana(d)}, ${dataLonga(d)}`, linhas);
      };
      const fechar = () => { g.classList.remove("ativa"); esconderTooltip(); };
      hit.addEventListener("pointerenter", abrir);
      hit.addEventListener("pointermove", (ev) => posicionar(ev));
      hit.addEventListener("pointerleave", fechar);
      hit.addEventListener("focus", abrir);
      hit.addEventListener("blur", fechar);
      if (cfg.aoClicar && totais[i] > 0) {
        hit.style.cursor = "pointer";
        hit.addEventListener("click", () => cfg.aoClicar(d));
        hit.addEventListener("keydown", (ev) => { if (ev.key === "Enter") cfg.aoClicar(d); });
      }
    });
    void superficie;
    caixa.appendChild(svg);
  };
  desenhar();

  // tabela equivalente (acessibilidade: o valor nunca depende do hover)
  const botao = document.createElement("button");
  botao.type = "button";
  botao.className = "alternar-tabela";
  botao.textContent = "Ver tabela";
  const tabela = document.createElement("div");
  tabela.className = "tabela-grafico";
  tabela.hidden = true;
  botao.addEventListener("click", () => {
    tabela.hidden = !tabela.hidden;
    botao.textContent = tabela.hidden ? "Ver tabela" : "Esconder tabela";
    if (!tabela.hidden && !tabela.firstChild) {
      const linhas = dias.slice().reverse().map((d) => {
        const v = cfg.porDia[d] || {};
        const tot = cfg.series.reduce((a, s) => a + (v[s.chave] || 0), 0);
        return `<tr><td>${esc(dataLonga(d))}</td>${cfg.series.map((s) => `<td class="num">${esc(numero(v[s.chave] || 0))}</td>`).join("")}${cfg.series.length > 1 ? `<td class="num"><b>${esc(numero(tot))}</b></td>` : ""}</tr>`;
      }).join("");
      tabela.innerHTML = `<table class="tabela-simples"><thead><tr><th>Dia</th>${cfg.series.map((s) => `<th class="num">${esc(s.rotulo)}</th>`).join("")}${cfg.series.length > 1 ? '<th class="num">Total</th>' : ""}</tr></thead><tbody>${linhas}</tbody></table>`;
    }
  });
  alvo.append(botao, tabela);

  if (window.ResizeObserver) {
    let largura = caixa.clientWidth;
    const ro = new ResizeObserver(() => {
      if (Math.abs(caixa.clientWidth - largura) > 4) { largura = caixa.clientWidth; desenhar(); }
    });
    ro.observe(caixa);
  }
}

/**
 * Barras horizontais de uma serie (uma cor so). Cada linha pode ser um link.
 * @param {{rotulo:string, valor:number, href?:string, titulo?:string}[]} itens
 */
export function barrasHorizontais(itens, { total } = {}) {
  if (!itens.length) return html`<p class="vazio">Sem dados.</p>`;
  const max = Math.max(...itens.map((i) => i.valor), 1);
  const soma = total || itens.reduce((a, i) => a + i.valor, 0);
  return html`<div class="barras">${itens.map((i) => {
    const pct = soma ? Math.round((i.valor / soma) * 100) : 0;
    const corpo = html`<span class="rot" title="${i.titulo || i.rotulo}">${i.rotulo}</span><span class="trilho"><span class="fill" style="width:${((i.valor / max) * 78).toFixed(1)}%"></span><span class="val">${numero(i.valor)} <span class="mudo">· ${pct}%</span></span></span>`;
    return i.href ? html`<a class="barra" href="${i.href}">${corpo}</a>` : html`<div class="barra">${corpo}</div>`;
  })}</div>`;
}

export function medidor(rotulo, valor, total, dica) {
  const pct = total ? Math.round((valor / total) * 100) : 0;
  return html`<div class="medidor" title="${dica || ""}">
    <div class="topo-m"><span>${rotulo}</span><span>${numero(valor)} de ${numero(total)} · ${pct}%</span></div>
    <div class="trilha" role="meter" aria-valuemin="0" aria-valuemax="${total}" aria-valuenow="${valor}" aria-label="${rotulo}"><div style="width:${pct}%"></div></div>
  </div>`;
}

/**
 * Faixa de saude: um quadrado por passada, dia a dia (cor = status de coleta; o rotulo
 * vem no tooltip e na legenda com icone — cor nunca e o unico canal).
 */
export function faixaSaude(alvo, passadas, dias = 14, hoje) {
  const porDia = {};
  for (const p of passadas) (porDia[p.data] = porDia[p.data] || []).push(p);
  const fim = hoje;
  alvo.replaceChildren();
  const cont = document.createElement("div");
  cont.className = "saude";
  for (let k = dias - 1; k >= 0; k--) {
    const d = somarDias(fim, -k);
    const lista = (porDia[d] || []).slice().sort((a, b) => (a.hora || "").localeCompare(b.hora || ""));
    const col = document.createElement("div");
    col.className = "saude-dia";
    const qs = document.createElement("div");
    qs.className = "quadros";
    if (!lista.length) {
      const q = document.createElement("span");
      q.className = "quadro";
      q.tabIndex = 0;
      q.setAttribute("aria-label", `${dataLonga(d)}: nenhuma passada registrada`);
      q.addEventListener("pointerenter", (ev) => mostrarTooltip(ev, `${diaSemana(d)}, ${dataLonga(d)}`, [{ rotulo: "passadas registradas", valor: "0" }]));
      q.addEventListener("focus", (ev) => mostrarTooltip(ev, `${diaSemana(d)}, ${dataLonga(d)}`, [{ rotulo: "passadas registradas", valor: "0" }]));
      q.addEventListener("pointerleave", esconderTooltip);
      q.addEventListener("blur", esconderTooltip);
      qs.appendChild(q);
    }
    for (const p of lista) {
      const q = document.createElement("a");
      q.className = "quadro " + (p.coleta || "");
      q.href = `#/rodadas/${p.data}`;
      const rot = p.coleta === "ok" ? "coleta ok" : p.coleta === "sem-coleta" ? "sem coleta" : "coleta parcial";
      q.setAttribute("aria-label", `${dataLonga(p.data)} ${p.hora}: ${rot}`);
      const linhas = [
        { rotulo: rot, valor: p.hora || "—" },
        { rotulo: "gateways", valor: (p.gateways || []).length ? p.gateways.join(", ") : "—" },
        { rotulo: "ofertas citadas", valor: String((p.ofertas || []).length) },
      ];
      q.addEventListener("pointerenter", (ev) => mostrarTooltip(ev, `${diaSemana(p.data)}, ${dataLonga(p.data)}`, linhas));
      q.addEventListener("focus", (ev) => mostrarTooltip(ev, `${diaSemana(p.data)}, ${dataLonga(p.data)}`, linhas));
      q.addEventListener("pointerleave", esconderTooltip);
      q.addEventListener("blur", esconderTooltip);
      qs.appendChild(q);
    }
    const rotulo = document.createElement("span");
    rotulo.className = "d";
    rotulo.textContent = dataCurta(d);
    col.append(qs, rotulo);
    cont.appendChild(col);
  }
  alvo.appendChild(cont);
  const leg = document.createElement("div");
  leg.className = "legenda-saude";
  leg.innerHTML = `<span><i style="background:var(--bom)"></i>✓ coleta ok</span><span><i style="background:var(--atencao)"></i>! parcial</span><span><i style="background:var(--critico)"></i>✕ sem coleta</span><span><i style="background:var(--grade)"></i>nenhuma passada</span>`;
  alvo.appendChild(leg);
}
