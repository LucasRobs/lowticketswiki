// app.js — inicializacao, rotas (#/...), sessao e atualizacao ao vivo.
//
// Os dados vem de /api/dados (JSON gerados do vault por _meta/exportar_dados.py).
// A cada minuto o painel consulta /api/dados?f=versao; quando uma nova mineracao e
// publicada (push -> deploy na Vercel), o hash muda e a tela se atualiza sozinha.

import * as api from "./js/api.js";
import { html, qs, qsa, dataHora, relativo, numero, armazenamento, ICONE } from "./js/util.js";
import * as visao from "./js/paginas/visao.js";
import * as ofertas from "./js/paginas/ofertas.js";
import * as oferta from "./js/paginas/oferta.js";
import * as rodadas from "./js/paginas/rodadas.js";
import * as qualidade from "./js/paginas/qualidade.js";
import * as login from "./js/paginas/login.js";
import { esconderTooltip } from "./js/graficos.js";

const ESQUEMA = 1;
const INTERVALO_MS = 60 * 1000;

const estado = {
  painel: null,
  porSlug: new Map(),
  rodadas: null,
  deploy: null,
  sessao: { protegido: false, autenticado: true },
  ultimaChecagem: null,
  falhas: 0,
};

const PAGINAS = { visao, ofertas, oferta, rodadas, qualidade };

// ---------- rotas ----------
function lerRota() {
  const h = location.hash.replace(/^#\/?/, "");
  const [caminho, query = ""] = h.split("?");
  const partes = caminho.split("/").filter(Boolean).map(decodeURIComponent);
  const nome = partes[0] || "visao";
  return { nome: PAGINAS[nome] ? nome : "visao", resto: partes.slice(1), params: new URLSearchParams(query) };
}

export function navegar(hash) {
  if (location.hash === hash) rotear();
  else location.hash = hash;
}

let rotaAnterior = "";
function rotear({ manterScroll = false } = {}) {
  if (!estado.painel) return;
  esconderTooltip();
  document.body.classList.remove("deslogado");
  const rota = lerRota();
  const chave = rota.nome + "/" + rota.resto.join("/");
  for (const a of qsa(".abas a")) {
    const ativa = a.dataset.rota === rota.nome || (rota.nome === "oferta" && a.dataset.rota === "ofertas");
    if (ativa) a.setAttribute("aria-current", "page");
    else a.removeAttribute("aria-current");
  }
  const main = qs("#conteudo");
  const ctx = { estado, rota, navegar, api, recarregarRodadas };
  try {
    PAGINAS[rota.nome].render(main, ctx);
  } catch (e) {
    console.error(e);
    main.innerHTML = String(html`<div class="cartao"><h2 class="secao">Algo deu errado nesta tela</h2><p class="sub">${String(e && e.message || e)}</p></div>`);
  }
  if (!manterScroll && chave !== rotaAnterior) {
    window.scrollTo(0, 0);
    main.focus({ preventScroll: true });
  }
  rotaAnterior = chave;
  document.title = tituloPagina(rota);
}

function tituloPagina(rota) {
  const base = "Radar Low Ticket";
  if (rota.nome === "oferta") {
    const o = estado.porSlug.get(rota.resto[0]);
    return (o ? o.nome : "Oferta") + " · " + base;
  }
  return { visao: base, ofertas: "Ofertas · " + base, rodadas: "Rodadas · " + base, qualidade: "Qualidade · " + base }[rota.nome] || base;
}

// ---------- dados ----------
function indexar() {
  estado.porSlug = new Map(estado.painel.ofertas.map((o) => [o.slug, o]));
}

async function carregarPainel() {
  const p = await api.painel();
  if (p.esquema !== ESQUEMA) avisar("Os dados vieram num formato mais novo que esta tela. Recarregue a página.");
  estado.painel = p;
  estado.rodadas = null;
  indexar();
}

async function recarregarRodadas() {
  if (!estado.rodadas) estado.rodadas = await api.rodadas();
  return estado.rodadas;
}

async function checarVersao() {
  if (document.visibilityState === "hidden" || !estado.painel) return;
  try {
    const v = await api.versao();
    estado.ultimaChecagem = new Date();
    estado.deploy = v.deploy || null;
    estado.falhas = 0;
    const atual = estado.painel.versao && estado.painel.versao.hash;
    if (v.hash && atual && v.hash !== atual) {
      const antes = new Set(estado.painel.ofertas.map((o) => o.slug));
      document.body.classList.add("atualizando");
      await carregarPainel();
      document.body.classList.remove("atualizando");
      const novas = estado.painel.ofertas.filter((o) => !antes.has(o.slug)).length;
      avisar(novas ? `Dados atualizados — ${novas} oferta${novas > 1 ? "s" : ""} nova${novas > 1 ? "s" : ""} no radar` : "Dados atualizados pela última mineração");
      rotear({ manterScroll: true });
    }
  } catch (e) {
    estado.falhas++;
    if (e instanceof api.NaoAutorizado) return mostrarLogin();
  }
  pintarAoVivo();
  pintarRodape();
}

function pintarAoVivo() {
  const el = qs("#ao-vivo");
  const v = estado.painel && estado.painel.versao;
  if (!el || !v) return;
  el.hidden = false;
  const off = estado.falhas > 1;
  el.classList.toggle("parado", off);
  el.innerHTML = String(off
    ? html`<span>Sem conexão</span>`
    : html`<span><span class="texto-longo">Ao vivo · </span>dados ${relativo(v.atualizado_em)}</span>`);
  el.title = `Dados atualizados em ${dataHora(v.atualizado_em)}. O painel confere novas minerações a cada minuto.`;
}

function pintarRodape() {
  const el = qs("#rodape");
  const p = estado.painel;
  if (!el || !p) return;
  const v = p.versao || {};
  const d = estado.deploy;
  el.innerHTML = String(html`
    <span>${numero(p.totais.ofertas)} ofertas · ${numero(p.totais.angulos)} ângulos · ${numero(p.totais.observacoes)} snapshots</span>
    <span>Dados de ${dataHora(v.atualizado_em)}</span>
    ${d && d.commit ? html`<span>Deploy ${d.commit}</span>` : ""}
    <span>Fonte: vault <code>lowticket</code> (Obsidian) · <a href="#/qualidade">qualidade dos dados</a></span>
    ${estado.sessao.protegido ? html`<span><a href="#" id="sair">Sair</a></span>` : html`<span class="mudo" title="Defina DASHBOARD_SENHA nas variáveis de ambiente da Vercel para exigir senha">Acesso aberto</span>`}
  `);
  const sair = qs("#sair");
  if (sair) sair.addEventListener("click", async (ev) => {
    ev.preventDefault();
    await api.sair();
    location.reload();
  });
}

// ---------- avisos ----------
let timerToast;
export function avisar(texto) {
  const t = qs("#toast");
  if (!t) return;
  t.textContent = texto;
  t.hidden = false;
  clearTimeout(timerToast);
  timerToast = setTimeout(() => { t.hidden = true; }, 5200);
}

// ---------- tema ----------
function aplicarTema(t) {
  const raiz = document.documentElement;
  if (t === "light" || t === "dark") raiz.setAttribute("data-theme", t);
  else raiz.removeAttribute("data-theme");
}

function alternarTema() {
  const escuroSistema = window.matchMedia("(prefers-color-scheme: dark)").matches;
  const atual = document.documentElement.getAttribute("data-theme") || (escuroSistema ? "dark" : "light");
  const novo = atual === "dark" ? "light" : "dark";
  aplicarTema(novo);
  armazenamento("lt-tema", novo);
  rotear({ manterScroll: true }); // graficos leem as cores do tema
}

// ---------- login ----------
function mostrarLogin() {
  const main = qs("#conteudo");
  document.body.classList.add("deslogado");
  qs("#ao-vivo").hidden = true;
  login.render(main, {
    aoEntrar: async () => {
      api.limparCache();
      await iniciarDados();
    },
  });
}

async function iniciarDados() {
  const main = qs("#conteudo");
  try {
    await carregarPainel();
  } catch (e) {
    if (e instanceof api.NaoAutorizado) return mostrarLogin();
    main.innerHTML = String(html`<div class="cartao"><h2 class="secao">Não consegui carregar os dados</h2>
      <p class="sub">${String(e.message || e)}</p>
      <p class="sub">Se este é o primeiro deploy, confira se <code>dashboard/data/</code> foi publicado junto (rode <code>python3 _meta/publicar.py</code> no vault).</p></div>`);
    return;
  }
  estado.sessao = await api.sessao();
  rotear();
  pintarAoVivo();
  pintarRodape();
  checarVersao();
}

async function iniciar() {
  qs("#tema").addEventListener("click", alternarTema);
  window.addEventListener("hashchange", () => rotear());
  document.addEventListener("visibilitychange", () => { if (document.visibilityState === "visible") checarVersao(); });
  setInterval(checarVersao, INTERVALO_MS);
  setInterval(pintarAoVivo, 30 * 1000);
  window.addEventListener("scroll", () => { const t = qs("#tooltip"); if (t) t.hidden = true; }, { passive: true });

  estado.sessao = await api.sessao();
  if (estado.sessao.protegido && !estado.sessao.autenticado) return mostrarLogin();
  await iniciarDados();
}

void ICONE;
iniciar();
