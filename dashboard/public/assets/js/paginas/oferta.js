// Detalhe de uma oferta: a nota inteira do vault, os scores, o historico de snapshots
// e onde ela foi citada (rodadas, passadas, analises).
import {
  html, raw, qs, dataCurta, dataLonga, relativo, numero, dinheiro, score, humano, gateway,
  seloDecisao, seloStatus, seloVeredito, linkSeguro, obsidianLink, FLAGS, ICONE,
} from "../util.js";
import { medidor } from "../graficos.js";
import { markdown } from "../markdown.js";

const EIXOS = [
  ["s_lucro", "Sinal de lucro", 35, "Tempo no ar e aceleração de criativos (proxy de que alguém paga para manter no ar)."],
  ["s_replica", "Facilidade de replicar", 30, "Entrega digital simples, funil curto, criativo fácil de refazer."],
  ["s_ticket", "Ticket e margem", 20, "Ticket médio estimado (frente + bump + upsell)."],
  ["s_saturacao", "Campo livre", 15, "Invertido: 10 = poucos players no ângulo."],
];

const lista = (v) => (Array.isArray(v) && v.length ? v.join(", ") : "—");
const sim = (b) => (b ? "sim" : "não");

function fatos(pares) {
  return html`<dl class="fatos">${pares.filter(Boolean).map(([k, v]) => html`<dt>${k}</dt><dd>${v === "" || v === null || v === undefined ? "—" : v}</dd>`)}</dl>`;
}

function renderDetalhe(alvo, o, det, estado) {
  const fm = det.fm || {};
  const url = linkSeguro(o.url_pagina);
  const ads = linkSeguro(o.url_ads);
  const flags = (det.calc && det.calc.flags) || o.flags || [];
  const obs = det.observacoes || [];
  const cit = det.citacoes || [];
  const corpo = markdown(det.corpo || "", { ofertas: estado.porSlug, pularH1: true });

  alvo.innerHTML = String(html`
    <a class="voltar" href="#/ofertas">${ICONE.seta} Ofertas</a>
    <div class="detalhe-topo">
      <div>
        <h1>${o.nome}</h1>
        <div class="selos">
          <span class="selo forte">${o.classe === "angulo" ? "Ângulo" : "Oferta"}</span>
          ${seloStatus(o.status)} ${seloDecisao(o.decisao, flags)} ${seloVeredito(o.veredito, o.prioridade)}
          <span class="selo">${humano(o.nicho)}${o.sub_nicho ? html` <span class="mudo">· ${humano(o.sub_nicho)}</span>` : ""}</span>
        </div>
      </div>
      <div class="acoes">
        ${url ? html`<a class="botao" href="${url}" target="_blank" rel="noopener noreferrer">Página de vendas ${ICONE.externo}</a>` : ""}
        ${ads ? html`<a class="botao" href="${ads}" target="_blank" rel="noopener noreferrer">Biblioteca de Anúncios ${ICONE.externo}</a>` : ""}
        <a class="botao" href="${obsidianLink(det.arquivo || "Ofertas/" + o.slug + ".md")}" title="Abre a nota no Obsidian deste computador">Abrir no Obsidian</a>
      </div>
    </div>

    <div class="grade-detalhe">
      <div class="pilha">
        <section class="cartao">
          <div class="md">${raw(corpo)}</div>
        </section>
        <section class="cartao">
          <h2 class="secao">Snapshots <span class="sub">${numero(obs.length)} registro${obs.length === 1 ? "" : "s"} em Observacoes/ (append-only)</span></h2>
          ${obs.length ? html`<ol class="linha-tempo">${obs.slice().reverse().map((s) => html`<li>
            <span class="quando">${dataLonga(s.data)}</span>
            <div class="o-que">${s.texto ? html`<div class="md">${raw(markdown(s.texto, { ofertas: estado.porSlug, nivelTitulo: 3 }))}</div>` : html`<span class="mudo">sem texto</span>`}
              <div class="nums">
                <span>fonte: ${s.fonte || "—"}</span>
                ${s.ra_reclamacoes !== "" ? html`<span>reclamações: ${s.ra_reclamacoes}</span>` : ""}
                ${s.criativos_ativos ? html`<span>criativos: ${s.criativos_ativos}${s.criativos_novos ? ` (+${s.criativos_novos})` : ""}</span>` : ""}
                ${s.dias_no_ar ? html`<span>dias no ar: ${s.dias_no_ar}</span>` : ""}
                ${s.ticket_frente ? html`<span>frente: ${dinheiro(s.ticket_frente, o.moeda)}</span>` : ""}
                ${s.preco_mudou ? html`<span><b>preço mudou</b></span>` : ""}
                ${s.angulo_novo ? html`<span><b>ângulo novo</b></span>` : ""}
              </div></div></li>`)}</ol>` : html`<p class="vazio">Nenhum snapshot ainda.</p>`}
        </section>
        ${cit.length ? html`<section class="cartao">
          <h2 class="secao">Citada em <span class="sub">${numero(cit.length)} nota${cit.length === 1 ? "" : "s"}</span></h2>
          <ul class="lista">${cit.map((c) => html`<li><a class="linha" href="${c.tipo === "analise" ? "#/ofertas" : `#/rodadas/${c.data}`}" ${c.tipo === "analise" ? html`title="Análise no vault: ${c.arquivo}"` : ""}>
            <span class="nome">${c.titulo}</span><span class="direita">${dataCurta(c.data)}</span>
            <span class="meta">${c.tipo === "radar" ? "nota do dia" : c.tipo === "passada" ? "passada da tarefa agendada" : "análise"} · ${c.arquivo}</span></a></li>`)}</ul>
        </section>` : ""}
      </div>

      <aside class="pilha lateral">
        <section class="cartao">
          <div class="score-grande"><span class="n">${score(o.score)}</span><span class="sub">score composto${flags.includes("score-provisorio") ? " · provisório" : ""}</span></div>
          <div class="eixos">${EIXOS.map(([k, rot, peso, dica]) => medidor(`${rot} · peso ${peso}`, Number(fm[k] || o[k] || 0), 10, dica))}</div>
          ${flags.length ? html`<div class="bloco-titulo" style="margin-top:18px">Cuidados com os números</div>
            <div class="alertas">${flags.map((fl) => html`<div class="alerta">${ICONE.alerta}<div><b>${(FLAGS[fl] || { curto: fl }).curto}</b><span>${(FLAGS[fl] || { texto: "" }).texto}</span></div></div>`)}</div>` : ""}
        </section>
        <section class="cartao">
          <div class="bloco-titulo">Economia</div>
          ${fatos([
            ["Ticket de frente", dinheiro(fm.ticket_frente, fm.moeda)],
            ["Order bump", dinheiro(fm.ticket_bump, fm.moeda)],
            ["Upsell", dinheiro(fm.ticket_upsell, fm.moeda)],
            ["Ticket médio estimado", dinheiro(fm.ticket_medio_est, fm.moeda)],
            ["Margem estimada", fm.margem_est ? Math.round(Number(fm.margem_est) * 100) + "%" : "—"],
            ["Recorrência", sim(fm.tem_recorrencia)],
            ["Bump / upsell oculto", `${sim(fm.bump_oculto)} / ${sim(fm.upsell_oculto)}`],
          ])}
          <div class="bloco-titulo">Funil e canais</div>
          ${fatos([
            ["Checkout", o.checkout ? gateway(o.checkout) : "—"],
            ["Gateways detectados", lista((fm.gateways_detectados || []).map(gateway))],
            ["Reclame Aqui em", lista((fm.ra_plataformas || []).map(gateway))],
            ["Modelo", lista(fm.modelo)],
            ["Entrega", lista(fm.formato_entrega)],
            ["Anúncios em", lista(fm.plataforma_ads)],
          ])}
          <div class="bloco-titulo">Ciclo de vida</div>
          ${fatos([
            ["Visto pela 1ª vez", `${dataLonga(fm.visto_primeiro)} (${relativo(fm.visto_primeiro)})`],
            ["Visto por último", `${dataLonga(fm.visto_ultimo)} (${relativo(fm.visto_ultimo)})`],
            ["Rodadas em que apareceu", numero(fm.rodadas_vista)],
            ["Dias no ar", fm.dias_no_ar ? numero(fm.dias_no_ar) : "não medido"],
            ["Criativos (última / delta)", `${numero(fm.criativos_ultima || 0)} / ${fm.criativos_delta > 0 ? "+" : ""}${numero(fm.criativos_delta || 0)}`],
            ["Reclamações (RA)", numero(fm.ra_reclamacoes || 0)],
            ["1ª reclamação", fm.ra_primeira_reclamacao ? dataLonga(fm.ra_primeira_reclamacao) : "—"],
            ["RA checado em", fm.ra_checado ? dataLonga(fm.ra_checado) : "—"],
            ["Idioma / país", `${fm.idioma || "—"} / ${fm.pais || "—"}`],
          ])}
          <div class="bloco-titulo">Arquivo</div>
          <p class="sub" style="margin:0;overflow-wrap:anywhere"><code>${det.arquivo}</code> · slug <code>${o.slug}</code></p>
        </section>
      </aside>
    </div>
  `);
}

export function render(main, { estado, rota, api }) {
  const slug = rota.resto[0];
  const o = estado.porSlug.get(slug);
  if (!o) {
    main.innerHTML = String(html`<a class="voltar" href="#/ofertas">${ICONE.seta} Ofertas</a>
      <div class="cartao"><h2 class="secao">Oferta não encontrada</h2><p class="sub">Não há nota <code>${slug}</code> no vault publicado.</p></div>`);
    return;
  }
  main.innerHTML = String(html`<a class="voltar" href="#/ofertas">${ICONE.seta} Ofertas</a><div class="cartao"><p class="carregando" style="padding:24px 0">Carregando ${o.nome}…</p></div>`);
  api.oferta(slug).then((det) => {
    if (!location.hash.startsWith("#/oferta/" + encodeURIComponent(slug)) && !location.hash.startsWith("#/oferta/" + slug)) return;
    renderDetalhe(main, o, det, estado);
  }).catch((e) => {
    main.innerHTML = String(html`<a class="voltar" href="#/ofertas">${ICONE.seta} Ofertas</a>
      <div class="cartao"><h2 class="secao">Não consegui abrir esta oferta</h2><p class="sub">${String(e.message || e)}</p></div>`);
  });
  void qs;
}
