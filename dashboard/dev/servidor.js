// Servidor local para ver o dashboard antes de publicar — imita a Vercel:
// public/ servido como estatico e /api/<nome> chamando o mesmo handler de api/<nome>.js.
//
//   cd dashboard && node dev/servidor.js          -> http://localhost:3000
//   DASHBOARD_SENHA=teste node dev/servidor.js     -> testa a tela de senha
//
// Sem dependencias. Nao rode `npm install` dentro do vault: nao ha o que instalar.
"use strict";

const http = require("http");
const fs = require("fs");
const path = require("path");

const RAIZ = path.join(__dirname, "..");
const PUBLICO = path.join(RAIZ, "public");
const PORTA = Number(process.env.PORT || 3000);
const TIPOS = {
  ".html": "text/html; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".txt": "text/plain; charset=utf-8",
  ".ico": "image/x-icon",
  ".png": "image/png",
};

function estatico(req, res) {
  const url = new URL(req.url, "http://local");
  let rel = decodeURIComponent(url.pathname);
  if (rel.endsWith("/")) rel += "index.html";
  const arquivo = path.normalize(path.join(PUBLICO, rel));
  if (!arquivo.startsWith(PUBLICO)) {
    res.statusCode = 403;
    return res.end("proibido");
  }
  fs.readFile(arquivo, (err, buf) => {
    if (err) {
      res.statusCode = 404;
      res.setHeader("Content-Type", "text/plain; charset=utf-8");
      return res.end("404");
    }
    res.statusCode = 200;
    res.setHeader("Content-Type", TIPOS[path.extname(arquivo)] || "application/octet-stream");
    res.setHeader("Cache-Control", "no-cache");
    res.end(buf);
  });
}

function criarServidor() {
  return http.createServer((req, res) => {
    const m = /^\/api\/([a-z0-9_-]+)\/?(?:\?.*)?$/.exec(req.url || "");
    if (m) {
      const handler = path.join(RAIZ, "api", m[1] + ".js");
      if (!fs.existsSync(handler)) {
        res.statusCode = 404;
        return res.end("{}");
      }
      delete require.cache[require.resolve(handler)];
      return Promise.resolve(require(handler)(req, res)).catch((e) => {
        console.error(e);
        res.statusCode = 500;
        res.end(JSON.stringify({ erro: String(e) }));
      });
    }
    return estatico(req, res);
  });
}

if (require.main === module) {
  criarServidor().listen(PORTA, () => {
    const senha = process.env.DASHBOARD_SENHA ? "com senha" : "aberto (sem DASHBOARD_SENHA)";
    console.log(`dashboard em http://localhost:${PORTA}  —  ${senha}`);
  });
}

module.exports = { criarServidor };
