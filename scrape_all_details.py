#!/usr/bin/env python3
"""Scrape complaint details for all unique complaints from both gateways."""

import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_complaint_details(url, gateway_name):
    """Scrape a single complaint page for product details."""
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
            if "Just a moment" in page_title:
                await page.wait_for_timeout(10000)
            
            data = await page.evaluate("""
                () => {
                    const bodyText = document.body.innerText;
                    return { bodyText };
                }
            """)
            
            body_text = data.get('bodyText', '')
            return {"bodyText": body_text, "error": None}
            
        except Exception as e:
            return {"bodyText": "", "error": str(e)}
        finally:
            await browser.close()

async def main():
    # Load complaints from both gateways
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_complaints_new.json', 'r') as f:
        perfectpay_complaints = json.load(f)
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto_complaints_new.json', 'r') as f:
        cakto_complaints = json.load(f)
    
    # Filter out "Ler reclamação completa" duplicates
    def filter_unique(complaints):
        seen = set()
        unique = []
        for c in complaints:
            url = c.get('url', '')
            title = c.get('title', '')
            if url and url not in seen and 'Ler reclamação completa' not in title:
                seen.add(url)
                unique.append(c)
        return unique
    
    pp_unique = filter_unique(perfectpay_complaints)
    ck_unique = filter_unique(cakto_complaints)
    
    print(f"PerfectPay unique complaints: {len(pp_unique)}")
    print(f"Cakto unique complaints: {len(ck_unique)}")
    
    all_complaints = []
    for c in pp_unique:
        c['gateway'] = 'PerfectPay'
        all_complaints.append(c)
    for c in ck_unique:
        c['gateway'] = 'Cakto'
        all_complaints.append(c)
    
    results = []
    for complaint in all_complaints:
        print(f"\nScraping: {complaint['gateway']} - {complaint['title'][:60]}...")
        detail = await scrape_complaint_details(complaint['url'], complaint['gateway'])
        
        if detail.get('error'):
            print(f"  Error: {detail['error']}")
            continue
        
        body_text = detail.get('bodyText', '')
        result = {
            "gateway": complaint['gateway'],
            "url": complaint['url'],
            "list_title": complaint['title'],
            "raw_text": body_text
        }
        results.append(result)
        print(f"  Got {len(body_text)} chars")
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_new.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Saved {len(results)} complaint details.")

asyncio.run(main())