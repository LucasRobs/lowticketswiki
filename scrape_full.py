#!/usr/bin/env python3
"""Scrape complaint lists and details from ReclameAqui for PerfectPay and Cakto."""

import json
import asyncio
from playwright.async_api import async_playwright

async def scrape_complaint_list(gateway_slug, gateway_name, max_pages=25):
    """Scrape complaint list pages to get titles and URLs."""
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
        seen_urls = set()

        for page_num in range(1, max_pages + 1):
            url = f'https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}'
            print(f'Scraping {gateway_name} page {page_num}...')
            try:
                await page.goto(url, wait_until='domcontentloaded', timeout=60000)
                await page.wait_for_timeout(3000)

                complaints = await page.evaluate("""(gatewaySlug) => {
                    const allLinks = Array.from(document.querySelectorAll('a[href]'));
                    const results = [];
                    for (const link of allLinks) {
                        const href = link.href;
                        const text = link.innerText.trim();
                        // Complaint URLs are like /perfectpay/some-title_id/
                        // Exclude navigation links: /empresa/, /sobre/, /lista-reclamacoes/, /reclamar/, etc.
                        if (href && text && href.includes('/' + gatewaySlug + '/') && 
                            !href.includes('/empresa/') &&
                            !href.includes('/sobre/') &&
                            !href.includes('/lista-reclamacoes') &&
                            !href.includes('/reclamar/') &&
                            !href.includes('reclameaqui.com.br/segmentos/') &&
                            !href.includes('blog.reclameaqui.com.br') &&
                            !href.includes('produtos.reclameaqui.com.br') &&
                            !href.includes('goadopt.io') &&
                            text.length > 5) {
                            results.push({title: text, url: href});
                        }
                    }
                    return results;
                }""", gateway_slug)

                # Deduplicate by URL
                new_complaints = []
                for c in complaints:
                    if c['url'] not in seen_urls:
                        seen_urls.add(c['url'])
                        new_complaints.append(c)

                if new_complaints:
                    all_complaints.extend(new_complaints)
                    print(f'  Found {len(new_complaints)} new complaints (total: {len(all_complaints)})')
                else:
                    print(f'  No new complaints found, stopping at page {page_num}')
                    break

            except Exception as e:
                print(f'  Error on page {page_num}: {e}')
                continue

        await browser.close()
        return all_complaints


async def scrape_complaint_details(complaints, gateway_name):
    """Scrape detailed content from each complaint page."""
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

        detailed = []
        for i, complaint in enumerate(complaints):
            print(f'  Scraping detail {i+1}/{len(complaints)}: {complaint["title"][:60]}...')
            try:
                await page.goto(complaint['url'], wait_until='domcontentloaded', timeout=60000)
                await page.wait_for_timeout(2000)

                detail = await page.evaluate("""() => {
                    const result = {
                        title: '',
                        body: '',
                        date: '',
                        author: '',
                        status: ''
                    };
                    
                    // Title
                    const titleEl = document.querySelector('h1[data-testid="complaint-title"], h1[class*="title"], h1');
                    if (titleEl) result.title = titleEl.innerText.trim();
                    
                    // Body/Description
                    const bodyEl = document.querySelector('[data-testid="complaint-description"], [class*="complaint"] [class*="description"], [class*="description"], .complaint-body, [class*="text"]');
                    if (bodyEl) result.body = bodyEl.innerText.trim();
                    
                    // Date
                    const dateEl = document.querySelector('[data-testid="complaint-date"], time, [class*="date"]');
                    if (dateEl) result.date = dateEl.innerText.trim();
                    
                    // Author
                    const authorEl = document.querySelector('[data-testid="complaint-author"], [class*="author"], [class*="user"]');
                    if (authorEl) result.author = authorEl.innerText.trim();
                    
                    // Status
                    const statusEl = document.querySelector('[data-testid="complaint-status"], [class*="status"]');
                    if (statusEl) result.status = statusEl.innerText.trim();
                    
                    // Fallback: get all text from main content area
                    if (!result.body) {
                        const main = document.querySelector('main, [role="main"], .main-content');
                        if (main) {
                            const texts = Array.from(main.querySelectorAll('p, div, span')).map(e => e.innerText.trim()).filter(t => t.length > 50);
                            result.body = texts.join('\\n');
                        }
                    }
                    
                    return result;
                }""")

                complaint.update(detail)
                detailed.append(complaint)

            except Exception as e:
                print(f'    Error: {e}')
                detailed.append(complaint)

        await browser.close()
        return detailed


async def main():
    # Scrape PerfectPay
    print("=== Scraping PerfectPay ===")
    perfectpay_list = await scrape_complaint_list('perfectpay', 'PerfectPay', 25)
    perfectpay_detail = await scrape_complaint_details(perfectpay_list, 'PerfectPay')
    with open('perfectpay_complaints_full.json', 'w', encoding='utf-8') as f:
        json.dump(perfectpay_detail, f, ensure_ascii=False, indent=2)
    print(f'PerfectPay total: {len(perfectpay_detail)} complaints')

    # Scrape Cakto
    print("\n=== Scraping Cakto ===")
    cakto_list = await scrape_complaint_list('cakto-pay', 'Cakto', 25)
    cakto_detail = await scrape_complaint_details(cakto_list, 'Cakto')
    with open('cakto_complaints_full.json', 'w', encoding='utf-8') as f:
        json.dump(cakto_detail, f, ensure_ascii=False, indent=2)
    print(f'Cakto total: {len(cakto_detail)} complaints')


if __name__ == '__main__':
    asyncio.run(main())