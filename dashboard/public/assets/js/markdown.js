// markdown.js — renderizador pequeno e seguro para as notas do vault.
// Cobre o que as notas usam: titulos, paragrafos, listas (aninhadas), citacoes, tabelas,
// codigo, regua, negrito/italico/riscado, links, autolinks e [[wikilinks]].
// Todo texto e escapado antes de qualquer marcacao; link so vira <a> se for http(s).

import { esc } from "./util.js";

const TOKEN = "\u0000";

function linkSeguro(url) {
  try {
    const u = new URL(url);
    return u.protocol === "https:" || u.protocol === "http:" || u.protocol === "mailto:" ? u.href : null;
  } catch (_) {
    return null;
  }
}

function inline(texto, ctx) {
  const guardados = [];
  const guardar = (h) => { guardados.push(h); return TOKEN + (guardados.length - 1) + TOKEN; };
  let t = String(texto);

  // codigo inline (antes de tudo: dentro de `...` nada e interpretado)
  t = t.replace(/`([^`\n]+)`/g, (_, c) => guardar(`<code>${esc(c)}</code>`));
  // wikilinks [[alvo|apelido]] / [[alvo#secao]] / [[alvo\|apelido]] (forma usada em tabela)
  t = t.replace(/\[\[([^\]|#\n\\]+)(?:#[^\]|\n\\]*)?(?:\\?\|([^\]\n]+))?\]\]/g, (_, alvo, apelido) => guardar(ctx.wikilink(alvo.trim(), apelido && apelido.trim())));
  // escapes do markdown: \$ \| \* \_ \[ ...
  t = t.replace(/\\([\\`*_{}\[\]()#+\-.!|$~>])/g, (_, c) => guardar(esc(c)));
  // imagens: nao carregamos midia externa; mostramos o texto alternativo
  t = t.replace(/!\[([^\]]*)\]\(([^)\s]+)[^)]*\)/g, (_, alt) => guardar(`<span class="mudo">[imagem${alt ? ": " + esc(alt) : ""}]</span>`));
  // links [texto](url)
  t = t.replace(/\[([^\]\n]+)\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g, (m, rot, url) => {
    const href = linkSeguro(url);
    const rotulo = inlineSimples(rot);
    return guardar(href ? `<a href="${esc(href)}" target="_blank" rel="noopener noreferrer">${rotulo}</a>` : rotulo);
  });
  // autolinks
  t = t.replace(/(^|[\s(])(https?:\/\/[^\s<>()]+[^\s<>().,;:!?'"])/g, (m, antes, url) => {
    const href = linkSeguro(url);
    return antes + guardar(href ? `<a href="${esc(href)}" target="_blank" rel="noopener noreferrer">${esc(url)}</a>` : esc(url));
  });

  t = enfase(esc(t));
  return t.replace(new RegExp(TOKEN + "(\\d+)" + TOKEN, "g"), (_, i) => guardados[Number(i)]);
}

function inlineSimples(t) {
  return enfase(esc(t));
}

function enfase(t) {
  return t
    .replace(/\*\*(?=\S)([\s\S]*?\S)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^\w])__(?=\S)([\s\S]*?\S)__(?!\w)/g, "$1<strong>$2</strong>")
    .replace(/(^|[^\w*])\*(?=[^\s*])([^*\n]*?[^\s*])\*(?!\*)/g, "$1<em>$2</em>")
    .replace(/(^|[^\w])_(?=[^\s_])([^_\n]*?[^\s_])_(?!\w)/g, "$1<em>$2</em>")
    .replace(/~~(?=\S)([\s\S]*?\S)~~/g, "<del>$1</del>");
}

function celulas(linha) {
  let l = linha.trim();
  if (l.startsWith("|")) l = l.slice(1);
  if (l.endsWith("|") && !l.endsWith("\\|")) l = l.slice(0, -1);
  const out = [];
  let atual = "";
  for (let i = 0; i < l.length; i++) {
    if (l[i] === "\\" && l[i + 1] === "|") { atual += "\\|"; i++; continue; }
    if (l[i] === "|") { out.push(atual.trim()); atual = ""; continue; }
    atual += l[i];
  }
  out.push(atual.trim());
  return out;
}

const RE_LISTA = /^(\s*)([-*+]|\d+[.)])\s+(.*)$/;
const RE_SEP_TABELA = /^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$/;

function blocos(linhas, ctx, nivelTitulo) {
  const out = [];
  let i = 0;
  while (i < linhas.length) {
    const linha = linhas[i];

    if (!linha.trim()) { i++; continue; }

    // cerca de codigo
    const cerca = /^\s*(```|~~~)(.*)$/.exec(linha);
    if (cerca) {
      const fim = cerca[1];
      const corpo = [];
      i++;
      while (i < linhas.length && !linhas[i].trim().startsWith(fim)) corpo.push(linhas[i++]);
      i++;
      out.push(`<pre><code>${esc(corpo.join("\n"))}</code></pre>`);
      continue;
    }

    // titulos
    const tit = /^(#{1,6})\s+(.*?)\s*#*\s*$/.exec(linha);
    if (tit) {
      const n = Math.min(6, tit[1].length + nivelTitulo);
      out.push(`<h${n}>${inline(tit[2], ctx)}</h${n}>`);
      i++;
      continue;
    }

    // regua
    if (/^\s*([-*_])(\s*\1){2,}\s*$/.test(linha)) {
      out.push("<hr>");
      i++;
      continue;
    }

    // tabela
    if (linha.includes("|") && i + 1 < linhas.length && RE_SEP_TABELA.test(linhas[i + 1])) {
      const cab = celulas(linha);
      const alin = celulas(linhas[i + 1]).map((c) => (/^:-+:$/.test(c) ? "center" : /-+:$/.test(c) ? "right" : ""));
      i += 2;
      const corpo = [];
      while (i < linhas.length && linhas[i].includes("|") && linhas[i].trim()) corpo.push(celulas(linhas[i++]));
      const th = cab.map((c, k) => `<th${alin[k] ? ` style="text-align:${alin[k]}"` : ""}>${inline(c, ctx)}</th>`).join("");
      const trs = corpo.map((r) => "<tr>" + cab.map((_, k) => `<td${alin[k] ? ` style="text-align:${alin[k]}"` : ""}>${inline(r[k] || "", ctx)}</td>`).join("") + "</tr>").join("");
      out.push(`<table><thead><tr>${th}</tr></thead><tbody>${trs}</tbody></table>`);
      continue;
    }

    // citacao
    if (/^\s*>/.test(linha)) {
      const dentro = [];
      while (i < linhas.length && /^\s*>/.test(linhas[i])) dentro.push(linhas[i++].replace(/^\s*>\s?/, ""));
      out.push(`<blockquote>${blocos(dentro, ctx, nivelTitulo)}</blockquote>`);
      continue;
    }

    // lista
    if (RE_LISTA.test(linha)) {
      const itens = [];
      while (i < linhas.length && (RE_LISTA.test(linhas[i]) || (/^\s{2,}\S/.test(linhas[i]) && itens.length))) {
        itens.push(linhas[i++]);
      }
      out.push(lista(itens, ctx));
      continue;
    }

    // paragrafo
    const par = [];
    while (i < linhas.length && linhas[i].trim() && !/^(#{1,6})\s/.test(linhas[i]) && !/^\s*(```|~~~)/.test(linhas[i])
      && !/^\s*>/.test(linhas[i]) && !RE_LISTA.test(linhas[i]) && !/^\s*([-*_])(\s*\1){2,}\s*$/.test(linhas[i])
      && !(linhas[i].includes("|") && i + 1 < linhas.length && RE_SEP_TABELA.test(linhas[i + 1]))) {
      par.push(linhas[i++].trim());
    }
    out.push(`<p>${inline(par.join(" "), ctx)}</p>`);
  }
  return out.join("\n");
}

function lista(linhas, ctx) {
  // arvore por indentacao (2+ espacos = nivel abaixo)
  const raiz = { filhos: [], ordenada: false };
  const pilha = [{ indent: -1, no: raiz }];
  let ultimo = null;
  for (const l of linhas) {
    const m = RE_LISTA.exec(l);
    if (!m) {
      if (ultimo) ultimo.texto += " " + l.trim();
      continue;
    }
    const indent = m[1].replace(/\t/g, "  ").length;
    while (pilha.length > 1 && indent <= pilha[pilha.length - 1].indent) pilha.pop();
    const pai = pilha[pilha.length - 1].no;
    const item = { texto: m[3], filhos: [], ordenada: /\d/.test(m[2]) };
    if (!pai.filhos.length) pai.ordenada = item.ordenada;
    pai.filhos.push(item);
    pilha.push({ indent, no: item });
    ultimo = item;
  }
  const emitir = (no) => {
    const tag = no.ordenada ? "ol" : "ul";
    return `<${tag}>` + no.filhos.map((f) => {
      const tarefa = /^\[( |x|X)\]\s+/.exec(f.texto);
      const txt = tarefa ? (tarefa[1] === " " ? "☐ " : "☑ ") + f.texto.slice(tarefa[0].length) : f.texto;
      return `<li>${inline(txt, ctx)}${f.filhos.length ? emitir(f) : ""}</li>`;
    }).join("") + `</${tag}>`;
  };
  return emitir(raiz);
}

/**
 * @param {string} md
 * @param {{ofertas?: Map<string,{nome:string}>, pularH1?: boolean, nivelTitulo?: number}} opcoes
 */
export function markdown(md, opcoes = {}) {
  const ofertas = opcoes.ofertas || new Map();
  const ctx = {
    wikilink(alvo, apelido) {
      const o = ofertas.get(alvo);
      if (o) return `<a class="wl" href="#/oferta/${encodeURIComponent(alvo)}">${esc(apelido || o.nome || alvo)}</a>`;
      const dia = /^(\d{4}-\d{2}-\d{2})(?:\s+--\s+(\d{4}))?$/.exec(alvo);
      if (dia) return `<a class="wl" href="#/rodadas/${dia[1]}">${esc(apelido || alvo)}</a>`;
      return `<span class="wikilink" title="Nota do vault: ${esc(alvo)}">${esc(apelido || alvo)}</span>`;
    },
  };
  let linhas = String(md || "").replace(/\r\n?/g, "\n").split("\n");
  if (opcoes.pularH1) {
    const k = linhas.findIndex((l) => l.trim());
    if (k >= 0 && /^#\s+/.test(linhas[k])) linhas = linhas.slice(k + 1);
  }
  return blocos(linhas, ctx, opcoes.nivelTitulo ?? 1);
}
