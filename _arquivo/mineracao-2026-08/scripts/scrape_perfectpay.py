import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_perfectpay_pages():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
            ]
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        for page_num in range(1, 26):  # 25 pages
            url = f"https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina={page_num}"
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                await page.wait_for_timeout(3000)
                
                # Try to find complaint cards with multiple selectors
                data = await page.evaluate("""
                    () => {
                        // Try multiple selectors for complaint cards
                        let items = document.querySelectorAll('[data-testid="complaint-card"]');
                        if (items.length === 0) {
                            items = document.querySelectorAll('.complaint-card');
                        }
                        if (items.length === 0) {
                            items = document.querySelectorAll('[class*="complaint"]');
                        }
                        if (items.length === 0) {
                            items = document.querySelectorAll('article, .card, [class*="card"]');
                        }
                        
                        const results = [];
                        items.forEach(item => {
                            // Try multiple selectors for title
                            let titleEl = item.querySelector('h3, h4, [class*="title"]');
                            if (!titleEl) {
                                titleEl = item.querySelector('a[href*="/reclamacao/"]');
                            }
                            
                            // Try multiple selectors for link
                            let linkEl = item.querySelector('a[href*="/reclamacao/"]');
                            if (!linkEl) {
                                linkEl = item.querySelector('a[href]');
                            }
                            
                            if (titleEl && linkEl && linkEl.href.includes('/reclamacao/')) {
                                results.push({
                                    title: titleEl.innerText.trim(),
                                    url: linkEl.href
                                });
                            }
                        });
                        return results;
                    }
                """)
                results.extend(data)
                print(f"PerfectPay Page {page_num}: {len(data)} complaints")
            except Exception as e:
                print(f"PerfectPay Page {page_num} error: {e}")
        
        await browser.close()
    return results

results = asyncio.run(scrape_perfectpay_pages())
with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_complaints.json', 'w') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print(json.dumps(results, ensure_ascii=False, indent=2))