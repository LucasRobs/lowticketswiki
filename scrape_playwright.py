import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_gateway(gateway_slug, gateway_name, max_pages=25):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
        )
        await context.add_init_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
        page = await context.new_page()
        
        all_complaints = []
        
        for page_num in range(1, max_pages + 1):
            url = f'https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}'
            print(f'Scraping {gateway_name} page {page_num}...')
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
                await page.wait_for_timeout(5000)
                
                # Try multiple selectors
                complaints = await page.evaluate("""() => {
                    const results = [];
                    // Try different selectors for complaint links
                    const selectors = [
                        'a[href*="/reclamacao/"]',
                        'a[data-testid="complaint-title"]',
                        '.complaint-card a',
                        '[class*="complaint"] a',
                        'article a'
                    ];
                    
                    let links = [];
                    for (const sel of selectors) {
                        links = document.querySelectorAll(sel);
                        if (links.length > 0) break;
                    }
                    
                    for (const link of links) {
                        const title = link.innerText.trim();
                        const href = link.href;
                        if (title && href && !href.includes('/empresa/') && title !== 'Ler reclamação completa' && title.length > 5) {
                            results.push({title, url: href});
                        }
                    }
                    return results;
                }""")
                
                if complaints:
                    all_complaints.extend(complaints)
                    print(f'  Found {len(complaints)} complaints')
                else:
                    # Print page content for debugging
                    content = await page.content()
                    print(f'  No complaints found. Page length: {len(content)}')
                    # Check if there's a "Nenhuma reclamação" message
                    if 'nenhuma reclama' in content.lower() or 'sem reclama' in content.lower():
                        print('  Page indicates no complaints')
                    break
                    
            except Exception as e:
                print(f'  Error on page {page_num}: {e}')
                continue
        
        await browser.close()
        return all_complaints

async def main():
    perfectpay = await scrape_gateway('perfectpay', 'PerfectPay', 25)
    with open('perfectpay_complaints_full.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    print(f'PerfectPay total: {len(perfectpay)} complaints')
    
    cakto = await scrape_gateway('cakto-pay', 'Cakto', 25)
    with open('cakto_complaints_full.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)
    print(f'Cakto total: {len(cakto)} complaints')

asyncio.run(main())