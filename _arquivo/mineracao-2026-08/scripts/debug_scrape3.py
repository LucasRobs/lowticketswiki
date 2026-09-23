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
        
        url = "https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1"
        await page.goto(url, wait_until="domcontentloaded", timeout=60000)
        
        # Wait for complaint cards
        await page.wait_for_selector('[class*="complaint"]', timeout=10000)
        await page.wait_for_timeout(5000)
        
        # Debug: get all elements with class containing "complaint"
        elements = await page.evaluate("""
            () => {
                const elements = document.querySelectorAll('[class*="complaint"]');
                const results = [];
                elements.forEach((el, i) => {
                    if (i < 20) {  // Limit to first 20
                        results.push({
                            tag: el.tagName,
                            class: el.className,
                            text: el.innerText.trim().substring(0, 200),
                            html: el.outerHTML.substring(0, 500)
                        });
                    }
                });
                return results;
            }
        """)
        
        for i, el in enumerate(elements):
            print(f"\n--- Element {i} ---")
            print(f"Tag: {el['tag']}")
            print(f"Class: {el['class']}")
            print(f"Text: {el['text']}")
            print(f"HTML: {el['html']}")
        
        # Also find all links with reclamacao
        links = await page.evaluate("""
            () => {
                const links = document.querySelectorAll('a[href*="/reclamacao/"]');
                const results = [];
                links.forEach((link, i) => {
                    if (i < 20) {
                        results.push({
                            href: link.href,
                            text: link.innerText.trim(),
                            parent_class: link.parentElement?.className,
                            parent_tag: link.parentElement?.tagName
                        });
                    }
                });
                return results;
            }
        """)
        
        print("\n=== Links ===")
        for link in links:
            print(f"  {link['text'][:80]} -> {link['href']}")
            print(f"    Parent: {link['parent_tag']}.{link['parent_class']}")
        
        await browser.close()

asyncio.run(scrape_perfectpay_pages())