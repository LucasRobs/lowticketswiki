// GET /api/dados?f=versao|painel|rodadas
// GET /api/dados?f=oferta&slug=<slug>
//
// Serve os JSON de dashboard/data/ (gerados por _meta/exportar_dados.py a partir do
// vault). Os dados nao ficam em public/: so saem daqui, depois da checagem de sessao.
"use strict";

const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const s = require("../lib/sessao");

const RE_SLUG = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
const ARQUIVOS = new Set(["versao", "painel", "rodadas"]);
const cache = new Map();

function pastaDados() {
  const candidatos = [
    path.join(__dirname, "..", "data"),
    path.join(process.cwd(), "data"),
    path.join(process.cwd(), "dashboard", "data"),
  ];
  for (const c of candidatos) {
    if (fs.existsSync(path.join(c, "versao.json"))) return c;
  }
  return candidatos[0];
}

function ler(arquivo) {
  // Os dados so mudam a cada deploy: cache por instancia, invalidado pelo mtime.
  const st = fs.statSync(arquivo);
  const hit = cache.get(arquivo);
  if (hit && hit.mtime === st.mtimeMs) return hit;
  const texto = fs.readFileSync(arquivo, "utf8");
  const etag = '"' + crypto.createHash("sha1").update(texto).digest("hex").slice(0, 20) + '"';
  const item = { texto, etag, mtime: st.mtimeMs };
  cache.set(arquivo, item);
  return item;
}

module.exports = (req, res) => {
  if ((req.method || "GET").toUpperCase() !== "GET") {
    res.setHeader("Allow", "GET");
    return s.json(res, 405, { erro: "metodo_nao_permitido" });
  }
  if (!s.autenticado(req)) return s.json(res, 401, { erro: "nao_autorizado" });

  const url = new URL(req.url || "/", "http://local");
  const f = url.searchParams.get("f") || "painel";
  const pasta = pastaDados();
  let arquivo;
  if (f === "oferta") {
    const slug = url.searchParams.get("slug") || "";
    if (!RE_SLUG.test(slug)) return s.json(res, 400, { erro: "slug_invalido" });
    arquivo = path.join(pasta, "ofertas", slug + ".json");
  } else if (ARQUIVOS.has(f)) {
    arquivo = path.join(pasta, f + ".json");
  } else {
    return s.json(res, 400, { erro: "arquivo_invalido" });
  }
  if (!fs.existsSync(arquivo)) {
    return s.json(res, 404, {
      erro: "nao_encontrado",
      dica: f === "oferta" ? "oferta nao existe no vault" : "rode python3 _meta/exportar_dados.py e publique",
    });
  }

  let item = ler(arquivo);
  let texto = item.texto;
  if (f === "versao") {
    // anexa de qual commit/deploy estes dados vieram (variaveis de sistema da Vercel)
    const v = JSON.parse(texto);
    v.deploy = {
      commit: (process.env.VERCEL_GIT_COMMIT_SHA || "").slice(0, 7) || null,
      ambiente: process.env.VERCEL_ENV || "local",
      protegido: s.protegido(),
    };
    texto = JSON.stringify(v);
    item = { texto, etag: '"' + crypto.createHash("sha1").update(texto).digest("hex").slice(0, 20) + '"' };
  }

  res.setHeader("ETag", item.etag);
  res.setHeader("Cache-Control", "private, no-cache");
  res.setHeader("Vary", "Cookie");
  if (req.headers["if-none-match"] === item.etag) {
    res.statusCode = 304;
    return res.end();
  }
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json; charset=utf-8");
  res.end(texto);
};
