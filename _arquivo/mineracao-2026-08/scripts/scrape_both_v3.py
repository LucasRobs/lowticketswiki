import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_gateway(gateway_slug, gateway_name, max_pages=25):
    """Scrape complaints from a gateway's ReclameAqui page."""
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
            ]
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080},
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
        )
        
        # Add stealth scripts
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        page = await context.new_page()
        
        for page_num in range(1, max_pages + 1):
            url = f"https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}"
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                
                # Wait for Cloudflare challenge to pass
                await page.wait_for_timeout(5000)
                
                # Check if we're on a challenge page
                page_title = await page.title()
                if "Just a moment" in page_title or "404" in page_title:
                    print(f"{gateway_name} Page {page_num}: Challenge/404 page - {page_title}")
                    # Wait longer for challenge to resolve
                    await page.wait_for_timeout(10000)
                    page_title = await page.title()
                    if "Just a moment" in page_title or "404" in page_title:
                        print(f"{gateway_name} Page {page_num}: Still on challenge page, stopping")
                        break
                
                # Wait for complaint cards to load
                try:
                    await page.wait_for_selector('[data-testid="complaint-listagem-v2-title-link"]', timeout=15000)
                except:
                    # Check if there are any complaint cards at all
                    card_count = await page.evaluate("""
                        () => document.querySelectorAll('[data-testid="complaint-listagem-v2-title-link"]').length
                    """)
                    if card_count == 0:
                        print(f"{gateway_name} Page {page_num}: No complaint cards found")
                        # Check page content
                        body_text = await page.evaluate("() => document.body.innerText.substring(0, 500)")
                        print(f"  Page content preview: {body_text}")
                        break
                    await page.wait_for_timeout(2000)
                
                await page.wait_for_timeout(2000)
                
                # Extract titles and URLs
                data = await page.evaluate("""
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
                """)
                results.extend(data)
                print(f"{gateway_name} Page {page_num}: {len(data)} complaints")
                
                # Write incrementally
                with open(f'/Users/robson/Documents/Obsidian Vault/lowticket/{gateway_slug}_complaints.json', 'w') as f:
                    json.dump(results, f, ensure_ascii=False, indent=2)
                
                # If we got fewer than 3 complaints, we might be at the end
                if len(data) < 3:
                    print(f"{gateway_name} Page {page_num}: Only {len(data)} complaints, may be end of list")
                    break
                    
            except Exception as e:
                print(f"{gateway_name} Page {page_num} error: {e}")
        
        await browser.close()
    return results

async def main():
    # Scrape PerfectPay
    print("=== Scraping PerfectPay ===")
    perfectpay = await scrape_gateway("perfectpay", "PerfectPay", 25)
    
    # Scrape Cakto (slug: cakto-pay)
    print("\n=== Scraping Cakto (cakto-pay) ===")
    cakto = await scrape_gateway("cakto-pay", "Cakto", 25)
    
    print(f"\nTotal PerfectPay: {len(perfectpay)}")
    print(f"Total Cakto: {len(cakto)}")

asyncio.run(main())