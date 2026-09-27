// util.js — HTML seguro, formatacao pt-BR e rotulos do vocabulario do vault.

// ---------- HTML seguro ----------
// html`...` escapa toda interpolacao; so o que vem de raw() ou de outro html`` entra cru.
const ESC = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
export const esc = (v) => String(v ?? "").replace(/[&<>"']/g, (c) => ESC[c]);

class Cru {
  constructor(s) { this.s = s; }
  toString() { return this.s; }
}
export const raw = (s) => new Cru(String(s ?? ""));

function render(v) {
  if (v === null || v === undefined || v === false) return "";
  if (v instanceof Cru) return v.s;
  if (Array.isArray(v)) return v.map(render).join("");
  return esc(v);
}

export function html(partes, ...valores) {
  let out = partes[0];
  for (let i = 0; i < valores.length; i++) out += render(valores[i]) + partes[i + 1];
  return new Cru(out);
}

export const qs = (sel, raiz = document) => raiz.querySelector(sel);
export const qsa = (sel, raiz = document) => Array.from(raiz.querySelectorAll(sel));

// ---------- datas (sempre no fuso de Fortaleza, como o vault) ----------
const TZ = "America/Fortaleza";
const fmtISO = new Intl.DateTimeFormat("en-CA", { timeZone: TZ, year: "numeric", month: "2-digit", day: "2-digit" });

export function hojeISO(agora = new Date()) {
  return fmtISO.format(agora); // AAAA-MM-DD
}

export function somarDias(iso, n) {
  const d = new Date(iso + "T12:00:00Z");
  d.setUTCDate(d.getUTCDate() + n);
  return d.toISOString().slice(0, 10);
}

export function diasEntre(a, b) {
  if (!a || !b) return null;
  return Math.round((new Date(b + "T12:00:00Z") - new Date(a + "T12:00:00Z")) / 86400000);
}

export function dataCurta(iso) {
  if (!iso || !/^\d{4}-\d{2}-\d{2}/.test(iso)) return iso || "—";
  return iso.slice(8, 10) + "/" + iso.slice(5, 7);
}

export function dataLonga(iso) {
  if (!iso || !/^\d{4}-\d{2}-\d{2}/.test(iso)) return iso || "—";
  return iso.slice(8, 10) + "/" + iso.slice(5, 7) + "/" + iso.slice(0, 4);
}

const SEMANA = ["dom", "seg", "ter", "qua", "qui", "sex", "sáb"];
export function diaSemana(iso) {
  return SEMANA[new Date(iso + "T12:00:00Z").getUTCDay()];
}

export function dataHora(isoCompleto) {
  if (!isoCompleto) return "—";
  const d = new Date(isoCompleto);
  if (isNaN(d)) return isoCompleto;
  return new Intl.DateTimeFormat("pt-BR", { timeZone: TZ, day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit" }).format(d);
}

export function relativo(alvo, agora = new Date()) {
  // alvo: ISO completo (com hora) ou AAAA-MM-DD
  if (!alvo) return "";
  let d;
  if (/^\d{4}-\d{2}-\d{2}$/.test(alvo)) {
    const dias = diasEntre(alvo, hojeISO(agora));
    if (dias === 0) return "hoje";
    if (dias === 1) return "ontem";
    if (dias > 1) return `há ${dias} dias`;
    return dataCurta(alvo);
  }
  d = new Date(alvo);
  if (isNaN(d)) return "";
  const s = Math.round((agora - d) / 1000);
  if (s < 60) return "agora";
  const m = Math.round(s / 60);
  if (m < 60) return `há ${m} min`;
  const h = Math.round(m / 60);
  if (h < 36) return `há ${h} h`;
  return `há ${Math.round(h / 24)} dias`;
}

// data + hora de uma passada ("2026-09-26", "22:15") -> Date
export function momentoPassada(data, hora) {
  if (!data) return null;
  const h = /^\d{2}:\d{2}$/.test(hora || "") ? hora : "12:00";
  return new Date(`${data}T${h}:00-03:00`);
}

// ---------- numeros ----------
const nf = new Intl.NumberFormat("pt-BR");
export const numero = (n) => (n === null || n === undefined || n === "" ? "—" : nf.format(n));

export function dinheiro(v, moeda = "BRL") {
  if (v === null || v === undefined || v === "" || Number(v) <= 0) return "—";
  const n = Number(v);
  try {
    return new Intl.NumberFormat("pt-BR", { style: "currency", currency: moeda || "BRL", maximumFractionDigits: Number.isInteger(n) ? 0 : 2, minimumFractionDigits: Number.isInteger(n) ? 0 : 2 }).format(n);
  } catch (_) {
    return nf.format(n);
  }
}

export const score = (s) => (s === null || s === undefined ? "—" : Number(s).toFixed(2).replace(".", ","));

export function compacto(n) {
  return new Intl.NumberFormat("pt-BR", { notation: "compact", maximumFractionDigits: 1 }).format(n);
}

// ---------- rotulos ----------
const GATEWAYS = {
  perfectpay: "PerfectPay", cakto: "Cakto", kirvano: "Kirvano", lastlink: "Lastlink", wiapy: "Wiapy",
  lowify: "Lowify", kiwify: "Kiwify", hotmart: "Hotmart", ticto: "Ticto", monetizze: "Monetizze",
  eduzz: "Eduzz", hubla: "Hubla", ggcheckout: "GGCheckout", payt: "Payt", onprofit: "OnProfit",
  stripe: "Stripe", clickbank: "ClickBank", whatsapp: "WhatsApp", proprio: "Checkout próprio",
  desconhecido: "Desconhecido", braip: "Braip", yampi: "Yampi",
};
export const gateway = (g) => GATEWAYS[g] || humano(g);

const PALAVRAS = {
  ia: "IA", tdah: "TDAH", tea: "TEA", mei: "MEI", pdf: "PDF", vsl: "VSL", tsl: "TSL", stl: "STL", nfc: "NFC",
  danca: "dança", educacao: "educação", saude: "saúde", estetica: "estética", pedagogico: "pedagógico",
  mecanica: "mecânica", servicos: "serviços", esoterico: "esotérico", certificacao: "certificação", oficio: "ofício",
  bemestar: "bem-estar", musica: "música", producao: "produção", imprimiveis: "imprimíveis", nao: "não",
  alfabetizacao: "alfabetização", crista: "cristã", cristas: "cristãs", oracao: "oração", video: "vídeo",
  videos: "vídeos", familia: "família", emocoes: "emoções", gestao: "gestão", negocios: "negócios",
  credito: "crédito", financas: "finanças", inteligencia: "inteligência", relacoes: "relações", ansiedade: "ansiedade",
  graficos: "gráficos", audio: "áudio", biblia: "bíblia", catolico: "católico", catolica: "católica",
  evangelico: "evangélico", pratica: "prática", praticas: "práticas", tecnico: "técnico", eletrica: "elétrica",
  eletricista: "eletricista", joias: "joias", espiritual: "espiritual", espiritualidade: "espiritualidade",
  bebe: "bebê", bebes: "bebês", criancas: "crianças", crianca: "criança", adolescencia: "adolescência",
  maes: "mães", mae: "mãe", pais: "pais", concursos: "concursos", idiomas: "idiomas", ingles: "inglês",
  espanhol: "espanhol", caligrafia: "caligrafia", musculacao: "musculação", nutricao: "nutrição",
  receitas: "receitas", confeitaria: "confeitaria", artesanato: "artesanato", croche: "crochê", trico: "tricô",
  conteudo: "conteúdo", automacao: "automação", licoes: "lições", licao: "lição", sessao: "sessão",
};
export function humano(slug) {
  if (!slug) return "—";
  const t = String(slug).split("-").map((p) => PALAVRAS[p] || p).join(" ");
  return t.charAt(0).toUpperCase() + t.slice(1);
}

export const STATUS = {
  nova: "Nova", aquecendo: "Aquecendo", ativa: "Ativa", esfriando: "Esfriando", morta: "Morta",
};
export const DECISAO = {
  replicar: "Replicar", observar: "Observar", descartar: "Descartar", padrao: "Padrão (ângulo)",
};
export const VEREDITO = {
  replicar: "Replicar", observar: "Observar", descartar: "Descartar", replicando: "Replicando", replicada: "Replicada",
};
export const COLETA = { ok: "Coleta ok", parcial: "Coleta parcial", "sem-coleta": "Sem coleta" };

export const FLAGS = {
  "lucro-sem-medicao": {
    curto: "Lucro sem medição",
    texto: "s_lucro ≥ 7 sem tempo no ar medido. Sem dias_no_ar ou primeira reclamação, o teto é 6 (Scoring.md, 31/08).",
  },
  "score-provisorio": {
    curto: "Score provisório",
    texto: "Algum eixo está em 0 — sentinela de \"não avaliado\". Não compare com notas completas até a captura.",
  },
  "sem-longevidade": {
    curto: "Tempo no ar não medido",
    texto: "Falta dias_no_ar e primeira reclamação. Biblioteca de Anúncios (Etapa 1) ou página do produtor no RA (Etapa 3b) resolvem.",
  },
  "checkout-desconhecido": {
    curto: "Gateway desconhecido",
    texto: "Checkout não identificado. Abrir o botão de compra da LP costuma resolver (Pipeline.md, 06/09).",
  },
  "sem-lp": { curto: "Sem página de vendas", texto: "url_pagina vazia — sem LP registrada para estudar o funil." },
  "status-vencido": {
    curto: "Status \"nova\" vencido",
    texto: "\"nova\" só vale na rodada de estreia (Scoring.md, 23/08). A automação ainda não recalcula esse campo.",
  },
};

// ---------- icones (svg inline, cor = currentColor) ----------
export const ICONE = {
  check: raw('<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" d="M3 8.5l3.2 3L13 4.5"/></svg>'),
  alerta: raw('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path fill="currentColor" d="M8 1.5 15 14H1L8 1.5Zm0 4a.9.9 0 0 0-.9.95l.2 3.6a.7.7 0 0 0 1.4 0l.2-3.6A.9.9 0 0 0 8 5.5Zm0 6.1a.85.85 0 1 0 0 1.7.85.85 0 0 0 0-1.7Z"/></svg>'),
  x: raw('<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" d="M4 4l8 8M12 4l-8 8"/></svg>'),
  externo: raw('<svg width="12" height="12" viewBox="0 0 16 16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M9 3h4v4M13 3 7.5 8.5M12 9.5V13H3V4h3.5"/></svg>'),
  busca: raw('<svg width="15" height="15" viewBox="0 0 16 16" aria-hidden="true"><circle cx="7" cy="7" r="4.8" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="m10.6 10.6 3.4 3.4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>'),
  seta: raw('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" d="M10 3 5 8l5 5"/></svg>'),
  baixar: raw('<svg width="14" height="14" viewBox="0 0 16 16" aria-hidden="true"><path fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" d="M8 2.5v8m-3.5-3.5L8 10.5 11.5 7M3 13.5h10"/></svg>'),
};

// ---------- selos ----------
export function seloStatus(s) {
  if (!s) return "";
  return html`<span class="selo st-${s}"><span class="ponto"></span>${STATUS[s] || s}</span>`;
}

export function seloDecisao(d, flags = []) {
  if (!d) return "";
  const prov = flags.includes("score-provisorio") && d !== "padrao";
  if (prov && d === "descartar") {
    return html`<span class="selo dec-avaliar" title="Score provisório: algum eixo ainda está em 0 (não avaliado). A fórmula daria “descartar”, mas faltam dados para decidir.">A avaliar</span>`;
  }
  const icone = d === "replicar" ? ICONE.check : "";
  return html`<span class="selo dec-${d}" title="${prov ? "Score provisório: há eixo sem avaliação" : "Decisão pela fórmula do Scoring.md"}">${icone}${DECISAO[d] || d}${prov ? html`<span class="mudo">·prov.</span>` : ""}</span>`;
}

export function seloColeta(c) {
  if (!c) return "";
  const icone = c === "ok" ? ICONE.check : c === "sem-coleta" ? ICONE.x : ICONE.alerta;
  return html`<span class="selo col-${c}">${icone}${COLETA[c] || c}</span>`;
}

export function seloVeredito(v, prioridade) {
  if (!v) return "";
  return html`<span class="selo" title="Veredito (decisão sua, no frontmatter)">${VEREDITO[v] || v}${prioridade ? html` <span class="mudo">· P${prioridade}</span>` : ""}</span>`;
}

// ---------- links externos ----------
export function linkSeguro(url) {
  try {
    const u = new URL(url);
    return u.protocol === "https:" || u.protocol === "http:" ? u.href : null;
  } catch (_) {
    return null;
  }
}

export function obsidianLink(arquivo, vault = "Obsidian Vault", prefixo = "lowticket/") {
  const file = (prefixo + arquivo).replace(/\.md$/, "");
  return `obsidian://open?vault=${encodeURIComponent(vault)}&file=${encodeURIComponent(file)}`;
}

export function normalizar(t) {
  return String(t || "").normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
}

export function debounce(fn, ms) {
  let t;
  return (...a) => { clearTimeout(t); t = setTimeout(() => fn(...a), ms); };
}

export function armazenamento(chave, valor) {
  try {
    if (valor === undefined) return localStorage.getItem(chave);
    if (valor === null) localStorage.removeItem(chave);
    else localStorage.setItem(chave, valor);
  } catch (_) { /* navegacao privada: segue sem lembrar */ }
  return null;
}
