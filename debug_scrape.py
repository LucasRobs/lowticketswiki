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
        
        # Just fetch page 1 and save HTML for debugging
        url = "https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        await page.wait_for_timeout(5000)
        
        html = await page.content()
        with open('/Users/robson/Documents/Obsidian Vault/lowticket/debug_page1.html', 'w') as f:
            f.write(html)
        
        print("Page title:", await page.title())
        print("HTML length:", len(html))
        
        # Try to find any links
        links = await page.evaluate("""
            () => {
                const allLinks = Array.from(document.querySelectorAll('a[href]'));
                return allLinks.map(a => ({href: a.href, text: a.innerText.trim()})).filter(l => l.href.includes('reclamacao'));
            }
        """)
        print("Complaint links found:", len(links))
        for link in links[:10]:
            print(f"  {link['text'][:80]} -> {link['href']}")
        
        await browser.close()

asyncio.run(scrape_perfectpay_pages())