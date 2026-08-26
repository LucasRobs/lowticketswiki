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
            
            # Check for Cloudflare
            page_title = await page.title()
            if "Just a moment" in page_title:
                await page.wait_for_timeout(10000)
            
            # Extract complaint details
            data = await page.evaluate("""
                () => {
                    // Find the complaint body
                    const bodySelectors = [
                        '[data-testid="complaint-description"]',
                        '.complaint-description',
                        '[class*="complaint"] [class*="description"]',
                        '[class*="complaint"] p',
                        'article [class*="text"]',
                    ];
                    
                    let fullText = '';
                    let title = '';
                    
                    // Get title
                    const titleEl = document.querySelector('h1, [data-testid="complaint-title"], [class*="complaint-title"]');
                    if (titleEl) title = titleEl.innerText.trim();
                    
                    // Get full text from complaint body
                    for (const selector of bodySelectors) {
                        const elements = document.querySelectorAll(selector);
                        elements.forEach(el => {
                            fullText += el.innerText.trim() + '\n';
                        });
                        if (fullText.length > 500) break;
                    }
                    
                    // If still no text, get all text from main content area
                    if (fullText.length < 200) {
                        const main = document.querySelector('main, [role="main"], article, .complaint-detail');
                        if (main) {
                            fullText = main.innerText.trim();
                        }
                    }
                    
                    return { title, fullText: fullText.substring(0, 5000) };
                }
            """)
            
            return data
            
        except Exception as e:
            return {"title": "", "fullText": "", "error": str(e)}
        finally:
            await browser.close()

async def main():
    # Priority complaints to scrape
    priority_complaints = [
        # PerfectPay
        {
            "gateway": "PerfectPay",
            "title": "Cobrança de taxa adicional não combinada e falta de acesso ao produto comprado.",
            "url": "https://www.reclameaqui.com.br/perfectpay/cobranca-de-taxa-adicional-nao-combinada-e-falta-de-acesso-ao-produto-comprado__chfFQTX8pupMWB5/"
        },
        {
            "gateway": "PerfectPay",
            "title": "Compra de IA STALKER travou no WhatsApp pedindo mais Pix, caracterizando [Editado pelo Reclame Aqui] e solicitação de estorno.",
            "url": "https://www.reclameaqui.com.br/perfectpay/compra-de-ia-stalker-travou-no-whatsapp-pedindo-mais-pix-caracterizando-editado-pelo-reclame-aqui-e-solicitacao-de-estorno_1-kgmoEucjwYlzke/"
        },
        {
            "gateway": "PerfectPay",
            "title": "Solicitação de estorno de PIX por propaganda enganosa do produto Stalkeia App.",
            "url": "https://www.reclameaqui.com.br/perfectpay/solicitacao-de-estorno-de-pix-por-propaganda-enganosa-do-produto-stalkeia-app_we2sfgSop5jGx37G/"
        },
        # Cakto
        {
            "gateway": "Cakto",
            "title": "Usuário solicita estorno por não conseguir mais acessar o serviço hqflix, que foi anunciado como acesso vitalício.",
            "url": "https://www.reclameaqui.com.br/cakto-pay/usuario-solicita-estorno-por-nao-conseguir-mais-acessar-o-servico-hqflix-que-foi-anunciado-como-acesso-vitalicio_7zfD-D4s6GauY3fc/"
        },
        {
            "gateway": "Cakto",
            "title": "Plano Freelancer Imediato: Pagamento adicional exigido após compra inicial para liberação de acesso.",
            "url": "https://www.reclameaqui.com.br/cakto-pay/plano-freelancer-imediato-pagamento-adicional-exigido-apos-compra-inicial-para-liberacao-de-acesso_Aa7b4b27tHVPApDH/"
        },
    ]
    
    results = []
    for complaint in priority_complaints:
        print(f"\nScraping: {complaint['gateway']} - {complaint['title'][:60]}...")
        detail = await scrape_complaint_details(complaint['url'], complaint['gateway'])
        detail['gateway'] = complaint['gateway']
        detail['list_title'] = complaint['title']
        detail['url'] = complaint['url']
        results.append(detail)
        print(f"  Title: {detail.get('title', 'N/A')[:80]}")
        print(f"  Text preview: {detail.get('fullText', 'N/A')[:200]}")
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n\nDone! Results saved.")

asyncio.run(main())