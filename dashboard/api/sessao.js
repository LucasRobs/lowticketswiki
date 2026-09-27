// GET    /api/sessao  -> { protegido, autenticado }
// POST   /api/sessao  -> { senha }  entra (cookie de 30 dias)
// DELETE /api/sessao  -> sai
"use strict";

const s = require("../lib/sessao");

module.exports = async (req, res) => {
  const metodo = (req.method || "GET").toUpperCase();

  if (metodo === "GET") {
    return s.json(res, 200, { protegido: s.protegido(), autenticado: s.autenticado(req) });
  }

  if (metodo === "POST") {
    if (!s.protegido()) return s.json(res, 200, { ok: true, protegido: false });
    const corpo = await s.lerCorpo(req);
    if (s.senhaConfere(corpo && corpo.senha)) {
      return s.json(res, 200, { ok: true }, { "Set-Cookie": s.cookieEntrar(req) });
    }
    await new Promise((r) => setTimeout(r, 600)); // freia tentativa em serie
    return s.json(res, 401, { ok: false, erro: "senha_incorreta" });
  }

  if (metodo === "DELETE") {
    return s.json(res, 200, { ok: true }, { "Set-Cookie": s.cookieSair(req) });
  }

  res.setHeader("Allow", "GET, POST, DELETE");
  return s.json(res, 405, { erro: "metodo_nao_permitido" });
};
