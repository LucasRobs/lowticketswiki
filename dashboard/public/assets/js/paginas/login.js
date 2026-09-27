// Tela de senha (so aparece se DASHBOARD_SENHA estiver definida na Vercel).
import { html, qs } from "../util.js";
import { entrar } from "../api.js";

export function render(main, { aoEntrar }) {
  main.innerHTML = String(html`
    <div class="cartao login">
      <h1>Radar Low Ticket</h1>
      <p class="sub">Painel privado. Entre com a senha definida em <code>DASHBOARD_SENHA</code>.</p>
      <form id="form-login" autocomplete="on">
        <label class="sub" for="senha">Senha</label>
        <input class="entrada" id="senha" name="senha" type="password" autocomplete="current-password" required autofocus>
        <button class="botao primario" type="submit">Entrar</button>
        <div class="erro" id="erro-login" role="alert"></div>
      </form>
    </div>`);
  const form = qs("#form-login");
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const botao = form.querySelector("button");
    botao.disabled = true;
    qs("#erro-login").textContent = "";
    const ok = await entrar(qs("#senha").value).catch(() => false);
    botao.disabled = false;
    if (ok) aoEntrar();
    else {
      qs("#erro-login").textContent = "Senha incorreta.";
      qs("#senha").select();
    }
  });
  qs("#senha").focus();
}
