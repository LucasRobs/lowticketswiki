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
            ]
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()
        
        for page_num in range(1, max_pages + 1):
            url = f"https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}"
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=60000)
                
                # Wait for complaint cards to load
                await page.wait_for_selector('[data-testid="complaint-listagem-v2-title-link"]', timeout=15000)
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
                
                # If we got fewer than 5 complaints, we might be at the end
                if len(data) < 5:
                    print(f"{gateway_name} Page {page_num}: Only {len(data)} complaints, may be end of list")
                    
            except Exception as e:
                print(f"{gateway_name} Page {page_num} error: {e}")
        
        await browser.close()
    return results

async def main():
    # Scrape PerfectPay
    print("=== Scraping PerfectPay ===")
    perfectpay = await scrape_gateway("perfectpay", "PerfectPay", 25)
    
    # Scrape Cakto
    print("\n=== Scraping Cakto ===")
    cakto = await scrape_gateway("cakto", "Cakto", 25)
    
    # Save results
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_complaints.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto_complaints.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)
    
    print(f"\nTotal PerfectPay: {len(perfectpay)}")
    print(f"Total Cakto: {len(cakto)}")

asyncio.run(main())