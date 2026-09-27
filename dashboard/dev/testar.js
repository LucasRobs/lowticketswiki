// Teste rapido da API e dos dados (sem dependencias):  cd dashboard && node dev/testar.js
// Sobe o servidor local numa porta livre, com e sem senha, e confere o contrato.
"use strict";

const assert = require("assert");
const http = require("http");
const { criarServidor } = require("./servidor");

function pedir(porta, caminho, { metodo = "GET", corpo, cookie, headers = {} } = {}) {
  return new Promise((resolve, reject) => {
    const req = http.request({ host: "127.0.0.1", port: porta, path: caminho, method: metodo,
      headers: Object.assign({ Host: "localhost" }, cookie ? { Cookie: cookie } : {}, corpo ? { "Content-Type": "application/json" } : {}, headers) }, (res) => {
      let d = "";
      res.on("data", (c) => (d += c));
      res.on("end", () => resolve({ status: res.statusCode, headers: res.headers, texto: d, json: () => JSON.parse(d) }));
    });
    req.on("error", reject);
    if (corpo) req.write(JSON.stringify(corpo));
    req.end();
  });
}

async function comServidor(env, fn) {
  const antes = process.env.DASHBOARD_SENHA;
  if (env.DASHBOARD_SENHA === undefined) delete process.env.DASHBOARD_SENHA;
  else process.env.DASHBOARD_SENHA = env.DASHBOARD_SENHA;
  const srv = criarServidor();
  await new Promise((r) => srv.listen(0, "127.0.0.1", r));
  try {
    await fn(srv.address().port);
  } finally {
    srv.close();
    if (antes === undefined) delete process.env.DASHBOARD_SENHA;
    else process.env.DASHBOARD_SENHA = antes;
  }
}

(async () => {
  let n = 0;
  const ok = (msg) => { n++; console.log("  ok  " + msg); };

  await comServidor({}, async (porta) => {
    console.log("sem senha:");
    const s = (await pedir(porta, "/api/sessao")).json();
    assert.deepStrictEqual(s, { protegido: false, autenticado: true }); ok("sessao aberta");

    const v = await pedir(porta, "/api/dados?f=versao");
    assert.strictEqual(v.status, 200);
    const versao = v.json();
    assert.ok(/^[0-9a-f]{16}$/.test(versao.hash), "hash"); ok("versao.json tem hash " + versao.hash);

    const p = await pedir(porta, "/api/dados?f=painel");
    assert.strictEqual(p.status, 200);
    const painel = p.json();
    assert.strictEqual(painel.esquema, 1);
    assert.strictEqual(painel.versao.hash, versao.hash, "painel e versao do mesmo export"); ok("painel e versao batem");
    assert.ok(painel.ofertas.length > 0); ok(painel.ofertas.length + " notas no painel");
    const slugs = new Set();
    for (const o of painel.ofertas) {
      assert.ok(/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(o.slug), "slug " + o.slug);
      assert.ok(!slugs.has(o.slug), "slug duplicado " + o.slug);
      slugs.add(o.slug);
      assert.ok(["oferta", "angulo"].includes(o.classe), "classe " + o.slug);
      assert.strictEqual(typeof o.score, "number");
    }
    ok("slugs unicos, classe e score validos");
    assert.strictEqual(painel.qualidade.erros.length, 0, "erros de validacao: " + JSON.stringify(painel.qualidade.erros.slice(0, 3)));
    ok("validacao do vault sem erros");

    const um = painel.ofertas[0].slug;
    const d = await pedir(porta, "/api/dados?f=oferta&slug=" + um);
    assert.strictEqual(d.status, 200);
    assert.strictEqual(d.json().slug, um); ok("detalhe de " + um);

    assert.strictEqual((await pedir(porta, "/api/dados?f=oferta&slug=../versao")).status, 400); ok("slug malicioso barrado");
    assert.strictEqual((await pedir(porta, "/api/dados?f=../../etc/passwd")).status, 400); ok("arquivo fora da lista barrado");
    assert.strictEqual((await pedir(porta, "/api/dados?f=oferta&slug=nao-existe-xyz")).status, 404); ok("oferta inexistente = 404");
    const etag = p.headers.etag;
    assert.strictEqual((await pedir(porta, "/api/dados?f=painel", { headers: { "If-None-Match": etag } })).status, 304); ok("ETag -> 304");
    assert.strictEqual((await pedir(porta, "/data/painel.json")).status, 404); ok("dados fora de public/ (nao servidos como estatico)");
    assert.strictEqual((await pedir(porta, "/")).status, 200); ok("index.html servido");
  });

  await comServidor({ DASHBOARD_SENHA: "teste-123" }, async (porta) => {
    console.log("com senha:");
    assert.deepStrictEqual((await pedir(porta, "/api/sessao")).json(), { protegido: true, autenticado: false }); ok("sessao protegida");
    assert.strictEqual((await pedir(porta, "/api/dados?f=painel")).status, 401); ok("dados sem cookie = 401");
    assert.strictEqual((await pedir(porta, "/api/sessao", { metodo: "POST", corpo: { senha: "errada" } })).status, 401); ok("senha errada = 401");
    const r = await pedir(porta, "/api/sessao", { metodo: "POST", corpo: { senha: "teste-123" } });
    assert.strictEqual(r.status, 200);
    const cookie = String(r.headers["set-cookie"]).split(";")[0];
    assert.ok(cookie.startsWith("lt_sessao=")); ok("senha certa devolve cookie");
    assert.strictEqual((await pedir(porta, "/api/dados?f=painel", { cookie })).status, 200); ok("dados com cookie = 200");
    assert.strictEqual((await pedir(porta, "/api/dados?f=painel", { cookie: "lt_sessao=forjado" })).status, 401); ok("cookie forjado = 401");
    const sair = await pedir(porta, "/api/sessao", { metodo: "DELETE", cookie });
    assert.ok(String(sair.headers["set-cookie"]).includes("Max-Age=0")); ok("sair apaga o cookie");
  });

  console.log(`\n${n} verificacoes ok`);
})().catch((e) => {
  console.error("\nFALHOU:", e.message);
  process.exit(1);
});
