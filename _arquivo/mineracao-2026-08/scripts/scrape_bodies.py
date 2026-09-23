import asyncio
from playwright.async_api import async_playwright
import json

async def scrape_complaint_body(page, url):
    """Extract the full complaint body from a complaint URL"""
    try:
        await page.goto(url, wait_until='domcontentloaded', timeout=60000)
        await page.wait_for_timeout(3000)
        
        body = await page.evaluate("""() => {
            // Try multiple selectors for complaint content
            const selectors = [
                '[data-testid="complaint-description"]',
                '.complaint-description',
                '[class*="complaint"] [class*="description"]',
                '[class*="complaint"] [class*="body"]',
                '[class*="complaint"] p',
                '.complaint-body',
                '[class*="text"]',
                'main p',
                'article p'
            ];
            
            for (const sel of selectors) {
                const el = document.querySelector(sel);
                if (el && el.innerText.trim().length > 50) {
                    return el.innerText.trim();
                }
            }
            
            // Fallback: get all text from main content area
            const main = document.querySelector('main') || document.querySelector('article') || document.body;
            const text = main.innerText.trim();
            return text.substring(0, 5000);
        }""")
        
        return body
    except Exception as e:
        print(f"  Error scraping {url}: {e}")
        return ""

async def main():
    # Load complaint URLs
    with open('perfectpay_complaints_full.json') as f:
        perfectpay = json.load(f)
    with open('cakto_complaints_full.json') as f:
        cakto = json.load(f)
    
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
        
        # Scrape PerfectPay complaints
        print("Scraping PerfectPay complaint bodies...")
        for i, complaint in enumerate(perfectpay):
            print(f"  {i+1}/{len(perfectpay)}: {complaint['title'][:60]}")
            body = await scrape_complaint_body(page, complaint['url'])
            complaint['body'] = body
            await asyncio.sleep(1)  # Be polite
        
        # Scrape Cakto complaints
        print("\nScraping Cakto complaint bodies...")
        for i, complaint in enumerate(cakto):
            print(f"  {i+1}/{len(cakto)}: {complaint['title'][:60]}")
            body = await scrape_complaint_body(page, complaint['url'])
            complaint['body'] = body
            await asyncio.sleep(1)
        
        await browser.close()
    
    # Save with bodies
    with open('perfectpay_complaints_full.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    with open('cakto_complaints_full.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone. PerfectPay: {len(perfectpay)}, Cakto: {len(cakto)}")

asyncio.run(main())