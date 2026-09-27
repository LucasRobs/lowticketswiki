// api.js — acesso aos dados (/api/dados) com cache por ETag, e sessao (/api/sessao).

const cache = new Map(); // url -> { etag, dados }

export class NaoAutorizado extends Error {}

async function pegar(url) {
  const hit = cache.get(url);
  const headers = hit ? { "If-None-Match": hit.etag } : {};
  const r = await fetch(url, { headers, credentials: "same-origin" });
  if (r.status === 304 && hit) return hit.dados;
  if (r.status === 401) throw new NaoAutorizado("nao autorizado");
  if (!r.ok) {
    let det = "";
    try { det = (await r.json()).dica || ""; } catch (_) { /* sem corpo */ }
    throw new Error(`HTTP ${r.status}${det ? " — " + det : ""}`);
  }
  const dados = await r.json();
  const etag = r.headers.get("ETag");
  if (etag) cache.set(url, { etag, dados });
  return dados;
}

export const versao = () => pegar("/api/dados?f=versao");
export const painel = () => pegar("/api/dados?f=painel");
export const rodadas = () => pegar("/api/dados?f=rodadas");
export const oferta = (slug) => pegar("/api/dados?f=oferta&slug=" + encodeURIComponent(slug));

export async function sessao() {
  try {
    const r = await fetch("/api/sessao", { credentials: "same-origin" });
    if (!r.ok) return { protegido: false, autenticado: true };
    return await r.json();
  } catch (_) {
    return { protegido: false, autenticado: true };
  }
}

export async function entrar(senha) {
  const r = await fetch("/api/sessao", {
    method: "POST",
    credentials: "same-origin",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ senha }),
  });
  return r.ok;
}

export async function sair() {
  await fetch("/api/sessao", { method: "DELETE", credentials: "same-origin" });
  cache.clear();
}

export function limparCache() {
  cache.clear();
}
