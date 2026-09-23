import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_gateway(gateway_slug, gateway_name, max_pages=5):
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        for page_num in range(1, max_pages + 1):
            url = f'https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}'
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=30000)
                await page.wait_for_selector('[data-testid="complaint-listagem-v2-title-link"]', timeout=10000)
                await page.wait_for_timeout(2000)
                
                data = await page.evaluate('''
                    () => {
                        const links = document.querySelectorAll('[data-testid="complaint-listagem-v2-title-link"]');
                        const results = [];
                        links.forEach(link => {
                            const title = link.getAttribute('title') || link.innerText.trim();
                            const url = link.href;
                            if (title && url) {
                                results.push({ title, url });
                            }
                        });
                        return results;
                    }
                ''')
                results.extend(data)
                print(f'{gateway_name} Page {page_num}: {len(data)} complaints')
                if len(data) < 5:
                    break
            except Exception as e:
                print(f'{gateway_name} Page {page_num} error: {e}')
        await browser.close()
    return results

async def main():
    print('=== Scraping PerfectPay ===')
    perfectpay = await scrape_gateway('perfectpay', 'PerfectPay', 5)
    print(f'Total PerfectPay: {len(perfectpay)}')
    
    print('=== Scraping Cakto ===')
    cakto = await scrape_gateway('cakto-pay', 'Cakto', 5)
    print(f'Total Cakto: {len(cakto)}')
    
    with open('perfectpay_complaints.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    with open('cakto_complaints.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)

asyncio.run(main())