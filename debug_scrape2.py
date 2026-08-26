import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_perfectpay_pages():
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
        
        # Just fetch page 1 and wait for complaints to load
        url = "https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        
        # Wait for complaint cards to appear - try multiple selectors
        for selector in [
            '[data-testid="complaint-card"]',
            '.complaint-card',
            '[class*="complaint"]',
            'article',
            '[class*="card"]',
        ]:
            try:
                await page.wait_for_selector(selector, timeout=10000)
                print(f"Found selector: {selector}")
                break
            except:
                continue
        
        await page.wait_for_timeout(5000)
        
        # Now try to extract complaints
        data = await page.evaluate("""
            () => {
                // Find all links that go to complaint pages
                const allLinks = Array.from(document.querySelectorAll('a[href*="/reclamacao/"]'));
                const results = [];
                allLinks.forEach(link => {
                    // Find the title - could be in the link itself or in a parent
                    let title = link.innerText.trim();
                    if (!title || title === 'Ler reclamação completa') {
                        // Try to find a better title in parent elements
                        const parent = link.closest('article, [class*="card"], [class*="complaint"]');
                        if (parent) {
                            const titleEl = parent.querySelector('h3, h4, [class*="title"]');
                            if (titleEl) {
                                title = titleEl.innerText.trim();
                            }
                        }
                    }
                    if (title && title !== 'Ler reclamação completa') {
                        results.push({
                            title: title,
                            url: link.href
                        });
                    }
                });
                return results;
            }
        """)
        print(f"Found {len(data)} complaints")
        for d in data:
            print(f"  {d['title'][:80]} -> {d['url']}")
        
        await browser.close()

asyncio.run(scrape_perfectpay_pages())