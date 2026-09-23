#!/usr/bin/env python3
"""Scrape full complaint bodies from ReclameAqui URLs."""

import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_complaint_body(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
        )
        context = await browser.new_context(
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            viewport={'width': 1920, 'height': 1080},
            locale='pt-BR',
            timezone_id='America/Sao_Paulo',
        )
        await context.add_init_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
        page = await context.new_page()
        
        try:
            await page.goto(url, wait_until='domcontentloaded', timeout=60000)
            await page.wait_for_timeout(3000)
            
            body = await page.evaluate("""() => {
                // Try multiple selectors for the complaint body
                const selectors = [
                    '[data-testid="complaint-description"]',
                    '.complaint-description',
                    '[class*="complaint"] [class*="description"]',
                    '.complaint-body',
                    '[class*="text"]',
                    'main article',
                    'article'
                ];
                
                for (const selector of selectors) {
                    const el = document.querySelector(selector);
                    if (el && el.innerText.trim().length > 50) {
                        return el.innerText.trim();
                    }
                }
                
                // Fallback: get all text from main content area
                const main = document.querySelector('main') || document.querySelector('article') || document.body;
                return main.innerText.trim();
            }""")
            
            await browser.close()
            return body
        except Exception as e:
            await browser.close()
            return f"ERROR: {str(e)}"

async def main():
    # Load URLs
    with open('perfectpay_complaints_new.json', 'r') as f:
        pp_complaints = json.load(f)
    with open('cakto_complaints_new.json', 'r') as f:
        cakto_complaints = json.load(f)
    
    # Deduplicate by URL
    seen = set()
    pp_unique = []
    for c in pp_complaints:
        if c['url'] not in seen:
            seen.add(c['url'])
            pp_unique.append(c)
    
    seen = set()
    cakto_unique = []
    for c in cakto_complaints:
        if c['url'] not in seen:
            seen.add(c['url'])
            cakto_unique.append(c)
    
    print(f"PerfectPay unique: {len(pp_unique)}")
    print(f"Cakto unique: {len(cakto_unique)}")
    
    # Scrape bodies for PerfectPay
    pp_results = []
    for i, c in enumerate(pp_unique):
        print(f"Scraping PerfectPay {i+1}/{len(pp_unique)}: {c['title'][:50]}...")
        body = await scrape_complaint_body(c['url'])
        c['body'] = body
        c['gateway'] = 'PerfectPay'
        pp_results.append(c)
        await asyncio.sleep(1)
    
    # Scrape bodies for Cakto
    cakto_results = []
    for i, c in enumerate(cakto_unique):
        print(f"Scraping Cakto {i+1}/{len(cakto_unique)}: {c['title'][:50]}...")
        body = await scrape_complaint_body(c['url'])
        c['body'] = body
        c['gateway'] = 'Cakto'
        cakto_results.append(c)
        await asyncio.sleep(1)
    
    # Save
    all_results = pp_results + cakto_results
    with open('complaint_details_new.json', 'w') as f:
        json.dump(all_results, f, ensure_ascii=False, indent=2)
    
    print(f"Total complaints with bodies: {len(all_results)}")

if __name__ == '__main__':
    asyncio.run(main())