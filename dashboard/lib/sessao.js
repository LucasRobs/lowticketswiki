// Sessao do dashboard — senha opcional via variavel de ambiente DASHBOARD_SENHA.
//
// Sem DASHBOARD_SENHA configurada o painel fica aberto (bom para o primeiro deploy).
// Com ela, os dados so saem da API para quem tem o cookie assinado. O cookie e um
// HMAC da propria senha: trocar a senha na Vercel derruba todas as sessoes.
"use strict";

const crypto = require("crypto");

const COOKIE = "lt_sessao";
const TRINTA_DIAS = 60 * 60 * 24 * 30;

function senha() {
  return String(process.env.DASHBOARD_SENHA || "");
}

function protegido() {
  return senha().length > 0;
}

function token() {
  return crypto.createHmac("sha256", senha()).update("lowticket-dashboard-v1").digest("base64url");
}

function lerCookies(req) {
  const out = {};
  const bruto = (req.headers && req.headers.cookie) || "";
  for (const parte of bruto.split(";")) {
    const i = parte.indexOf("=");
    if (i < 0) continue;
    const k = parte.slice(0, i).trim();
    if (k) out[k] = decodeURIComponent(parte.slice(i + 1).trim());
  }
  return out;
}

function iguais(a, b) {
  const ha = crypto.createHash("sha256").update(String(a)).digest();
  const hb = crypto.createHash("sha256").update(String(b)).digest();
  return crypto.timingSafeEqual(ha, hb);
}

function autenticado(req) {
  if (!protegido()) return true;
  const c = lerCookies(req)[COOKIE];
  return Boolean(c) && iguais(c, token());
}

function senhaConfere(tentativa) {
  return protegido() && iguais(String(tentativa || ""), senha());
}

function local(req) {
  const host = String((req.headers && req.headers.host) || "");
  return /^(localhost|127\.0\.0\.1|\[::1\])(:\d+)?$/.test(host);
}

function cookieEntrar(req) {
  return `${COOKIE}=${token()}; Path=/; HttpOnly; SameSite=Lax; Max-Age=${TRINTA_DIAS}${local(req) ? "" : "; Secure"}`;
}

function cookieSair(req) {
  return `${COOKIE}=; Path=/; HttpOnly; SameSite=Lax; Max-Age=0${local(req) ? "" : "; Secure"}`;
}

function json(res, status, corpo, extras) {
  res.statusCode = status;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  for (const [k, v] of Object.entries(extras || {})) res.setHeader(k, v);
  res.end(JSON.stringify(corpo));
}

async function lerCorpo(req) {
  // Na Vercel o runtime Node ja entrega req.body parseado; no servidor local lemos o stream.
  const parse = (t) => {
    if (!t) return {};
    try { return JSON.parse(t); } catch (_) {
      return Object.fromEntries(new URLSearchParams(String(t)));
    }
  };
  if (req.body !== undefined && req.body !== null) {
    if (Buffer.isBuffer(req.body)) return parse(req.body.toString("utf8"));
    if (typeof req.body === "string") return parse(req.body);
    return req.body;
  }
  return new Promise((resolve) => {
    let dados = "";
    req.on("data", (c) => { dados += c; if (dados.length > 1e5) req.destroy(); });
    req.on("end", () => resolve(parse(dados)));
    req.on("error", () => resolve({}));
  });
}

module.exports = { protegido, autenticado, senhaConfere, cookieEntrar, cookieSair, json, lerCorpo };
