#!/usr/bin/env python3
"""Fetch details for new complaints from scraped lists."""

import asyncio
from playwright.async_api import async_playwright
import json

async def fetch_complaint(url, gateway):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=['--disable-blink-features=AutomationControlled', '--disable-dev-shm-usage', '--no-sandbox'])
        context = await browser.new_context(user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36', viewport={'width': 1920, 'height': 1080}, locale='pt-BR', timezone_id='America/Sao_Paulo')
        await context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined});")
        page = await context.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=60000)
            await page.wait_for_timeout(5000)
            title = await page.title()
            if "Just a moment" in title or "404" in title:
                await page.wait_for_timeout(15000)
                title = await page.title()
                if "Just a moment" in title or "404" in title:
                    return {"url": url, "gateway": gateway, "error": "Cloudflare challenge"}
            
            data = await page.evaluate("""() => {
                const getText = (sel) => {
                    const el = document.querySelector(sel);
                    return el ? el.innerText.trim() : '';
                };
                let raw_text = '';
                const selectors = [
                    '[data-testid="complaint-detail-description"]',
                    '.complaint-detail__description',
                    '[class*="complaint"][class*="description"]',
                    'main section:first-of-type'
                ];
                for (const sel of selectors) {
                    const text = getText(sel);
                    if (text && text.length > 50) {
                        raw_text = text;
                        break;
                    }
                }
                if (!raw_text) {
                    raw_text = document.body.innerText.substring(0, 3000);
                }
                const list_title = getText('[data-testid="complaint-detail-title"]') || getText('h1') || document.title;
                const full_text = document.body.innerText;
                return {
                    url: window.location.href,
                    list_title: list_title,
                    raw_text: raw_text,
                    full_text_preview: full_text.substring(0, 500)
                };
            }""")
            await browser.close()
            return {"gateway": gateway, **data}
        except Exception as e:
            await browser.close()
            return {"url": url, "gateway": gateway, "error": str(e)}

async def fetch_all(urls, gateway, output_file):
    results = []
    for url in urls:
        print(f"Fetching: {url}")
        result = await fetch_complaint(url, gateway)
        results.append(result)
        print(f"  -> {'OK' if 'error' not in result else 'ERROR: ' + result.get('error', '')}")
    
    with open(output_file, 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved to {output_file}")

async def main():
    # Load URLs from scraped files
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_complaints_new.json', 'r') as f:
        pp_complaints = json.load(f)
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto_complaints_new.json', 'r') as f:
        ck_complaints = json.load(f)
    
    # Deduplicate URLs (each appears twice - title + "Ler reclamação completa")
    pp_urls = []
    seen = set()
    for c in pp_complaints:
        if c['url'] not in seen and 'ler reclamação' not in c['title'].lower():
            pp_urls.append(c['url'])
            seen.add(c['url'])
    
    ck_urls = []
    seen = set()
    for c in ck_complaints:
        if c['url'] not in seen and 'ler reclamação' not in c['title'].lower():
            ck_urls.append(c['url'])
            seen.add(c['url'])
    
    print(f"PerfectPay unique URLs: {len(pp_urls)}")
    print(f"Cakto unique URLs: {len(ck_urls)}")
    
    await fetch_all(pp_urls, "PerfectPay", "/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_new_details.json")
    await fetch_all(ck_urls, "Cakto", "/Users/robson/Documents/Obsidian Vault/lowticket/cakto_new_details.json")

asyncio.run(main())