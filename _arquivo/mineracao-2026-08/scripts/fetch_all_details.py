#!/usr/bin/env python3
"""Fetch details for all complaints from both gateways."""

import asyncio
from playwright.async_api import async_playwright
import json

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
    # Load all complaints
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_complaints.json', 'r') as f:
        perfectpay = json.load(f)
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto-pay_complaints.json', 'r') as f:
        cakto = json.load(f)
    
    all_complaints = []
    for c in perfectpay:
        c['gateway'] = 'PerfectPay'
        all_complaints.append(c)
    for c in cakto:
        c['gateway'] = 'Cakto'
        all_complaints.append(c)
    
    print(f"Total complaints to fetch: {len(all_complaints)}")
    
    results = []
    for complaint in all_complaints:
        print(f"\nScraping: {complaint['gateway']} - {complaint['title'][:60]}...")
        detail = await scrape_complaint_details(complaint['url'], complaint['gateway'])
        
        if detail.get('error'):
            print(f"  Error: {detail['error']}")
            continue
        
        body_text = detail.get('bodyText', '')
        results.append({
            "gateway": complaint['gateway'],
            "url": complaint['url'],
            "list_title": complaint['title'],
            "raw_text": body_text
        })
        
        print(f"  Body length: {len(body_text)} chars")
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nDone! Saved {len(results)} complaint details.")

asyncio.run(main())