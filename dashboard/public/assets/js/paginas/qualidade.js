// Qualidade dos dados: o que falta medir para o score deixar de ser palpite,
// e o que o validador do pipeline (_meta/exportar_dados.py) encontrou.
import { html, numero, score, humano, dataCurta, FLAGS, ICONE } from "../util.js";
import { medidor } from "../graficos.js";

const CODIGOS = {
  "regra-s_lucro": "s_lucro ≥ 7 sem tempo no ar medido (teto 6)",
  vocabulario: "Valor fora do vocabulário controlado",
  data: "Data fora do formato AAAA-MM-DD",
  tipo: "Valor não numérico",
  escala: "Fora da escala 0–10",
  "nome-arquivo": "Nome de arquivo fora do padrão",
  slug: "Slug fora do padrão",
  classe: "Classe ausente",
  tipo_nota: "Tipo de nota inesperado",
};

function faltas(o) {
  const f = o.flags || [];
  const out = [];
  if (f.includes("sem-longevidade")) out.push("tempo no ar");
  if (!o.criativos_ultima) out.push("criativos");
  if (f.includes("sem-lp")) out.push("página de vendas");
  if (f.includes("checkout-desconhecido")) out.push("gateway");
  if (!o.ticket_medio_est) out.push("ticket");
  return out;
}

export function render(main, { estado }) {
  const p = estado.painel;
  const q = p.qualidade || {};
  const porSlug = estado.porSlug;
  const fila = (q.fila_enriquecimento || []).map((s) => porSlug.get(s)).filter(Boolean);
  const grupos = new Map();
  for (const a of q.avisos || []) {
    if (!grupos.has(a.codigo)) grupos.set(a.codigo, []);
    grupos.get(a.codigo).push(a);
  }
  const vencidas = q.status_vencido || [];
  const estilos = q.estilos_frontmatter || {};

  main.innerHTML = String(html`
    <div class="cabecalho-pagina">
      <div>
        <h1>Qualidade dos dados</h1>
        <p>O que falta medir para o score deixar de ser palpite — e o que o validador do pipeline encontrou no vault.</p>
      </div>
    </div>

    <div class="grade grade-2 topo-alinhado">
      <section class="cartao">
        <h2 class="secao">Cobertura <span class="sub">${numero(p.totais.ofertas)} ofertas concretas (ângulos fora)</span></h2>
        <div class="medidores">${(q.cobertura || []).map((c) => medidor(c.rotulo, c.preenchidas, c.total))}</div>
        <p class="sub" style="margin:14px 0 0">Tempo no ar é o insumo de <b>s_lucro</b>, o eixo de maior peso (35). Sem ele o score fica no teto conservador — ver <code>_meta/Scoring.md</code>.</p>
      </section>
      <section class="cartao">
        <h2 class="secao">Fila de enriquecimento <span class="sub">maior score sem tempo no ar medido</span></h2>
        ${fila.length ? html`<ul class="lista">${fila.map((o) => html`<li><a class="linha" href="#/oferta/${o.slug}">
          <span class="nome">${o.nome}</span><span class="direita"><b>${score(o.score)}</b></span>
          <span class="meta">${humano(o.nicho)} · falta: ${faltas(o).join(", ") || "—"}${(o.flags || []).includes("lucro-sem-medicao") ? html` · <span class="aviso-mini">s_lucro acima do teto</span>` : ""}</span>
        </a></li>`)}</ul>` : html`<p class="vazio">Nada na fila.</p>`}
        <p class="sub" style="margin:12px 0 0">Medir estas primeiro rende mais: Biblioteca de Anúncios (Etapa 1) dá <code>dias_no_ar</code> e criativos; a página do produtor no Reclame Aqui (Etapa 3b) dá volume e idade.</p>
      </section>
    </div>

    <section class="cartao" style="margin-top:16px">
      <h2 class="secao">Validação do vault <span class="sub">${numero((q.erros || []).length)} erro(s) · ${numero((q.avisos || []).length + (vencidas.length ? 1 : 0))} aviso(s)</span></h2>
      ${(q.erros || []).length ? html`<div class="alertas" style="margin-bottom:14px">${q.erros.map((e) => html`<div class="alerta" style="background:color-mix(in srgb, var(--critico) 10%, var(--superficie));border-color:color-mix(in srgb, var(--critico) 40%, transparent)">${ICONE.x}<div><b>${e.arquivo} · ${e.campo}</b><span>${e.msg}</span></div></div>`)}</div>`
        : html`<p class="sub" style="margin:0 0 12px">${ICONE.check} Nenhum erro: toda nota tem frontmatter legível, slug igual ao nome do arquivo e snapshot apontando para oferta que existe.</p>`}
      ${[...grupos.entries()].map(([cod, itens]) => html`<details style="margin-top:8px">
        <summary><b>${CODIGOS[cod] || cod}</b> <span class="sub">· ${numero(itens.length)}</span></summary>
        <table class="tabela-simples" style="margin-top:8px"><thead><tr><th>Nota</th><th>Campo</th><th>Detalhe</th></tr></thead>
        <tbody>${itens.map((a) => {
          const slug = (a.arquivo.match(/^Ofertas\/(.+)\.md$/) || [])[1];
          return html`<tr><td>${slug && porSlug.has(slug) ? html`<a href="#/oferta/${slug}">${porSlug.get(slug).nome}</a>` : a.arquivo}</td><td><code>${a.campo}</code></td><td>${a.msg}</td></tr>`;
        })}</tbody></table>
      </details>`)}
      ${vencidas.length ? html`<details style="margin-top:8px">
        <summary><b>Status “nova” depois da estreia</b> <span class="sub">· ${numero(vencidas.length)} notas</span></summary>
        <p class="sub">Pelo <code>Scoring.md</code> (adendo 23/08), “nova” só vale na rodada de estreia. O <code>sync_vault.py</code> não decai status de propósito (a automação não cobre todos os gateways), então esse campo precisa de uma passada de manutenção.</p>
        <p class="sub">${vencidas.map((s, i) => html`${i ? " · " : ""}<a href="#/oferta/${s}">${porSlug.has(s) ? porSlug.get(s).nome : s}</a>`)}</p>
      </details>` : ""}
    </section>

    <section class="cartao" style="margin-top:16px">
      <h2 class="secao">Formato das notas</h2>
      <p class="sub" style="margin:0">Frontmatter canônico: ${numero(estilos.canonico || 0)} · outro estilo: ${numero(estilos.pyyaml || 0)}${estilos["sem-fm"] ? html` · sem frontmatter: ${numero(estilos["sem-fm"])}` : ""}.
      ${estilos.pyyaml ? html` Rode <code>python3 _meta/vault.py normalizar --aplicar</code> para padronizar.` : " Tudo padronizado."}
      Última rodada no vault: ${dataCurta(p.totais.ultima_rodada)}.</p>
    </section>
  `);
}
