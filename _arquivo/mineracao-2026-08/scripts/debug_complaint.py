import asyncio
from playwright.async_api import async_playwright
import json

async def debug_complaint_page(url):
    """Debug a single complaint page structure."""
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
            viewport={'width': 1920, 'height': 1080},
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
        )
        
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            });
        """)
        
        page = await context.new_page()
        
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(5000)
            
            page_title = await page.title()
            print(f"Page title: {page_title}")
            
            if "Just a moment" in page_title:
                await page.wait_for_timeout(10000)
                page_title = await page.title()
                print(f"After wait: {page_title}")
            
            # Get all text content
            body_text = await page.evaluate("() => document.body.innerText")
            print(f"Body text length: {len(body_text)}")
            print(f"Body text preview:\n{body_text[:2000]}")
            
            # Save HTML for inspection
            html = await page.content()
            with open('/Users/robson/Documents/Obsidian Vault/lowticket/debug_complaint.html', 'w') as f:
                f.write(html)
            print("HTML saved to debug_complaint.html")
            
        except Exception as e:
            print(f"Error: {e}")
        finally:
            await browser.close()

# Test with one PerfectPay complaint
url = "https://www.reclameaqui.com.br/perfectpay/cobranca-de-taxa-adicional-nao-combinada-e-falta-de-acesso-ao-produto-comprado__chfFQTX8pupMWB5/"
asyncio.run(debug_complaint_page(url))