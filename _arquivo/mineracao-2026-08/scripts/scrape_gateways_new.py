#!/usr/bin/env python3
"""Scrape complaint lists from ReclameAqui for PerfectPay and Cakto."""

import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_gateway_list(gateway_slug, gateway_name, max_pages=25):
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
        
        all_complaints = []
        
        for page_num in range(1, max_pages + 1):
            url = f'https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}'
            print(f'Scraping {gateway_name} page {page_num}...')
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
                await page.wait_for_timeout(3000)
                
                complaints = await page.evaluate('''(gateway_slug) => {
                    const results = [];
                    const links = document.querySelectorAll('a[href*="/' + gateway_slug + '/"]');
                    for (const link of links) {
                        const title = link.innerText.trim() || link.getAttribute('title') || '';
                        const href = link.href;
                        if (title && href && !href.includes('/empresa/') && !href.includes('/lista-reclamacoes') && !href.includes('?pagina=')) {
                            results.push({title, url: href});
                        }
                    }
                    return results;
                }''', gateway_slug)
                
                if complaints:
                    all_complaints.extend(complaints)
                    print(f'  Found {len(complaints)} complaints')
                else:
                    print(f'  No complaints found, stopping at page {page_num}')
                    break
                    
            except Exception as e:
                print(f'  Error on page {page_num}: {e}')
                continue
                
        await browser.close()
        return all_complaints

async def main():
    perfectpay = await scrape_gateway_list('perfectpay', 'PerfectPay', 25)
    with open('perfectpay_complaints_new.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    print(f'PerfectPay total: {len(perfectpay)} complaints')
    
    cakto = await scrape_gateway_list('cakto-pay', 'Cakto', 25)
    with open('cakto_complaints_new.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)
    print(f'Cakto total: {len(cakto)} complaints')

if __name__ == '__main__':
    asyncio.run(main())