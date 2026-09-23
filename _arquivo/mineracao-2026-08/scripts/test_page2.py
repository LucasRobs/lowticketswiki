import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled', '--no-sandbox'])
        context = await browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36', viewport={'width': 1920, 'height': 1080}, locale='pt-BR', timezone_id='America/Sao_Paulo')
        await context.add_init_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
        page = await context.new_page()
        
        # Test page 2
        url = 'https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=2'
        await page.goto(url, wait_until='domcontentloaded', timeout=60000)
        await page.wait_for_timeout(5000)
        
        links = await page.evaluate('''() => {
            const allLinks = Array.from(document.querySelectorAll('a[href]'));
            return allLinks.map(l => ({href: l.href, text: l.innerText.trim().substring(0,100)})).filter(l => l.href.includes('/perfectpay/') && l.text);
        }''')
        print(f'Total links page 2: {len(links)}')
        for l in links:
            print(f'  {l["text"][:80]} -> {l["href"]}')
        
        await browser.close()

asyncio.run(test())