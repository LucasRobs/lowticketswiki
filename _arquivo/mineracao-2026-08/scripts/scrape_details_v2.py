import asyncio
from playwright.async_api import async_playwright
import json
import re

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
            
            # Extract complaint details using body text
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

def extract_info(body_text, gateway, url, list_title):
    """Extract product info from complaint body text."""
    info = {
        "gateway": gateway,
        "url": url,
        "list_title": list_title,
        "produto": "sem nome",
        "produtor": "",
        "valor_pago": "",
        "data_compra": "",
        "descricao": "",
        "raw_text": body_text[:2000]
    }
    
    # Extract date from text (format: DD/MM/YYYY às HH:MM)
    date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+às\s+\d{2}:\d{2})', body_text)
    if date_match:
        info["data_compra"] = date_match.group(1)
    
    # Extract complaint ID
    id_match = re.search(r'ID:\s*(\d+)', body_text)
    if id_match:
        info["reclamacao_id"] = id_match.group(1)
    
    # Extract product name - look for patterns
    # Pattern: "O nome da empresa é X", "produto X", "compra de X", "produto chamado X"
    product_patterns = [
        r'O nome da empresa é\s+([^.\n]+)',
        r'nome do produto[:\s]+([^.\n]+)',
        r'produto\s+([A-Z][a-zA-Z0-9\s\.]{2,30})',
        r'compra de\s+([A-Z][a-zA-Z0-9\s\.]{2,30})',
        r'adquiri\s+([A-Z][a-zA-Z0-9\s\.]{2,30})',
        r'serviço\s+([a-zA-Z0-9\s]{2,30})',
        r'app\s+([A-Z][a-zA-Z0-9\s\.]{2,20})',
    ]
    
    for pattern in product_patterns:
        match = re.search(pattern, body_text, re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            # Clean up
            candidate = re.sub(r'[.!?]+$', '', candidate)
            if len(candidate) > 2 and len(candidate) < 100:
                info["produto"] = candidate
                break
    
    # Extract price - look for R$ XX,XX or R$ XX
    price_match = re.search(r'R\$\s*(\d+(?:[.,]\d{2})?)', body_text)
    if price_match:
        info["valor_pago"] = f"R$ {price_match.group(1)}"
    
    # Extract description - first few sentences of the complaint
    # Remove common prefixes
    desc = body_text
    for prefix in ['RA Ads', 'Veja também', 'todas as reclamações', 'não respondidas', 'respondidas', 'finalizadas']:
        desc = desc.replace(prefix, '')
    
    # Get the complaint narrative (between title and company info)
    lines = desc.split('\n')
    complaint_lines = []
    in_complaint = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if any(kw in line.lower() for kw in ['realizei', 'comprei', 'adquiri', 'paguei', 'solicitei', 'o nome', 'o produto']):
            in_complaint = True
        if in_complaint:
            complaint_lines.append(line)
        if any(kw in line for kw in ['RA Ads', 'Reputação da empresa', 'Compare', 'Compartilhe', 'Controle sua privacidade']):
            break
    
    info["descricao"] = ' '.join(complaint_lines[:5])[:500]
    
    return info

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
        
        if detail.get('error'):
            print(f"  Error: {detail['error']}")
            continue
        
        body_text = detail.get('bodyText', '')
        extracted = extract_info(body_text, complaint['gateway'], complaint['url'], complaint['title'])
        results.append(extracted)
        
        print(f"  Produto: {extracted['produto']}")
        print(f"  Valor: {extracted['valor_pago']}")
        print(f"  Data: {extracted['data_compra']}")
        print(f"  Descrição: {extracted['descricao'][:150]}")
    
    with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details.json', 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print("\n\nDone! Results saved.")

asyncio.run(main())