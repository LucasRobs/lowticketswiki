import asyncio
from playwright.async_api import async_playwright
import json

perfectpay_urls = [
    "https://www.reclameaqui.com.br/perfectpay/propaganda-inganosa_WXGZ3QLZ1OhfoBjb/",
    "https://www.reclameaqui.com.br/perfectpay/propaganda-enganosa-do-aplicativo-stalkeia-app-e-solicitacao-de-reembolso_zrIGWUSWcSp7p5Xp/",
    "https://www.reclameaqui.com.br/perfectpay/usuario-pagou-por-app-de-monitoramento-falso-e-nao-recebeu-acesso-a-nada-solicita-reembolso_h9AXG_wRQFTAEB9J/",
    "https://www.reclameaqui.com.br/perfectpay/compra-e-nao-recebi_IgLy-Z3TgKa5WfbK/",
    "https://www.reclameaqui.com.br/perfectpay/compra-de-aplicativo-editado-pelo-reclame-aqui-com-promessas-nao-cumpridas-e-solicitacao-de-pagamentos-adicionais_QBT9INmhnCqkBp0I/",
]

cakto_urls = [
    "https://www.reclameaqui.com.br/cakto-pay/reembolso_Ou6F1k9zy_0W3ATN/",
    "https://www.reclameaqui.com.br/cakto-pay/reembolso-negado-e-produtor-indisponivel-para-consultoria-contratada_1JR4bg_J5EeujSt_/",
    "https://www.reclameaqui.com.br/cakto-pay/cliente-solicita-cancelamento-e-estorno-de-compra-de-acesso-anual-ao-chat-gpt-plus-devido-a-instabilidade-e-perda-de-dados_EoZfnW91AeWZK4TZ/",
    "https://www.reclameaqui.com.br/cakto-pay/cakto-nao-realiza-reembolso-solicitado-dentro-do-prazo-legal_HGxCCLOtHQ-WS7BF/",
    "https://www.reclameaqui.com.br/cakto-pay/solicitacao-de-cancelamento-e-reembolso-de-compra-de-seguidores-por-propaganda-enganosa_hiaN6FFls08qzwFb/",
]

async def fetch_complaint(url, gateway):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled', '--disable-dev-shm-usage', '--no-sandbox'])
        context = await browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36', viewport={'width': 1920, 'height': 1080}, locale='pt-BR', timezone_id='America/Sao_Paulo')
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(5000)
            title = await page.title()
            if "Just a moment" in title or "404" in title:
                await page.wait_for_timeout(15000)
                title = await page.title()
                if "Just a moment" in title or "404" in title:
                    return {"url": url, "gateway": gateway, "error": "Cloudflare challenge"}
            
            data = await page.evaluate("""() => {
                const getText = (sel) => {
                    const el = document.querySelector(sel);
                    return el ? el.innerText.trim() : '';
                };
                let raw_text = '';
                const selectors = [
                    '[data-testid="complaint-detail-description"]',
                    '.complaint-detail__description',
                    '[class*="complaint"][class*="description"]',
                    'main section:first-of-type'
                ];
                for (const sel of selectors) {
                    const text = getText(sel);
                    if (text && text.length > 50) {
                        raw_text = text;
                        break;
                    }
                }
                if (!raw_text) {
                    raw_text = document.body.innerText.substring(0, 3000);
                }
                const list_title = getText('[data-testid="complaint-detail-title"]') || getText('h1') || document.title;
                const full_text = document.body.innerText;
                return {
                    url: window.location.href,
                    list_title: list_title,
                    raw_text: raw_text,
                    full_text_preview: full_text.substring(0, 500)
                };
            }""")
            await browser.close()
            return {"gateway": gateway, **data}
        except Exception as e:
            await browser.close()
            return {"url": url, "gateway": gateway, "error": str(e)}

async def fetch_all(urls, gateway, output_file):
    results = []
    for url in urls:
        print(f"Fetching: {url}")
        result = await fetch_complaint(url, gateway)
        results.append(result)
        print(f"  -> {'OK' if 'error' not in result else 'ERROR: ' + result.get('error', '')}")
    
    with open(output_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file}")

async def main():
    await fetch_all(perfectpay_urls, "PerfectPay", "/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_new_details.json")
    await fetch_all(cakto_urls, "Cakto", "/Users/robson/Documents/Obsidian Vault/lowticket/cakto_new_details.json")

asyncio.run(main())