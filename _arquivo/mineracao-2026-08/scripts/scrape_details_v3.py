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
        "raw_text": body_text[:3000]
    }
    
    # Extract date
    date_match = re.search(r'(\d{2}/\d{2}/\d{4}\s+às\s+\d{2}:\d{2})', body_text)
    if date_match:
        info["data_compra"] = date_match.group(1)
    
    # Extract complaint ID
    id_match = re.search(r'ID:\s*(\d+)', body_text)
    if id_match:
        info["reclamacao_id"] = id_match.group(1)
    
    # Extract product name - improved patterns
    product_patterns = [
        r'O nome da empresa é\s+([^.\n]+)',
        r'o produto\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'produto\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'compra de\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'adquiri\s+(?:a\s+)?(?:compra\s+do\s+)?([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'serviço\s+([a-zA-Z0-9\s\.\-]{2,40})',
        r'app\s+([A-Z][a-zA-Z0-9\s\.\-]{2,30})',
        r'chamado\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'anunciado como\s+([^.\n]+)',
    ]
    
    for pattern in product_patterns:
        match = re.search(pattern, body_text, re.IGNORECASE)
        if match:
            candidate = match.group(1).strip()
            candidate = re.sub(r'[.!?]+$', '', candidate)
            candidate = re.sub(r'\s+', ' ', candidate)
            if len(candidate) > 2 and len(candidate) < 100:
                # Check if it's not a generic phrase
                generic = ['não', 'outra', 'nova', 'mesma', 'certa', 'errada', 'grande', 'pequena']
                if not any(candidate.lower().startswith(g) for g in generic):
                    info["produto"] = candidate
                    break
    
    # Extract price
    price_match = re.search(r'R\$\s*(\d+(?:[.,]\d{2})?)', body_text)
    if price_match:
        info["valor_pago"] = f"R$ {price_match.group(1).replace(',', '.')}"
    
    # Extract description - find the complaint narrative
    lines = body_text.split('\n')
    complaint_lines = []
    in_complaint = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        # Start capturing when we see complaint language
        if any(kw in line.lower() for kw in ['realizei', 'comprei', 'adquiri', 'paguei', 'solicitei', 'o nome da empresa', 'o produto', 'foi anunciado', 'não consegui', 'travou', 'pedindo mais']):
            in_complaint = True
        if in_complaint:
            complaint_lines.append(line)
        # Stop at ads/footer
        if any(kw in line for kw in ['RA Ads', 'Reputação da empresa', 'Compare', 'Compartilhe', 'Controle sua privacidade', 'Política de Privacidade']):
            break
    
    info["descricao"] = ' '.join(complaint_lines[:8])[:500]
    
    # Clean up produto from list_title if still "sem nome"
    if info["produto"] == "sem nome":
        # Try to extract from list_title
        title_patterns = [
            r'produto\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
            r'serviço\s+([a-zA-Z0-9\s\.\-]{2,40})',
            r'app\s+([A-Z][a-zA-Z0-9\s\.\-]{2,30})',
            r'do\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        ]
        for pattern in title_patterns:
            match = re.search(pattern, list_title, re.IGNORECASE)
            if match:
                candidate = match.group(1).strip()
                candidate = re.sub(r'[.!?]+$', '', candidate)
                if len(candidate) > 2 and len(candidate) < 100:
                    info["produto"] = candidate
                    break
    
    return info

async def main():
    # All complaints from both gateways (page 1)
    all_complaints = [
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
            "title": "Tomei [Editado pelo Reclame Aqui]",
            "url": "https://www.reclameaqui.com.br/perfectpay/tomei-editado-pelo-reclame-aqui_PCEkQCMzbA-5dwgy/"
        },
        {
            "gateway": "PerfectPay",
            "title": "Solicitação de estorno de PIX por propaganda enganosa do produto Stalkeia App.",
            "url": "https://www.reclameaqui.com.br/perfectpay/solicitacao-de-estorno-de-pix-por-propaganda-enganosa-do-produto-stalkeia-app_we2sfgSop5jGx37G/"
        },
        {
            "gateway": "PerfectPay",
            "title": "Reclamação sobre recusa de reembolso e atendimento genérico pela Perfect Pay",
            "url": "https://www.reclameaqui.com.br/perfectpay/reclamacao-sobre-recusa-de-reembolso-e-atendimento-generico-pela-perfect-pay_BFp4AxOI5U-r8e8Q/"
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
        {
            "gateway": "Cakto",
            "title": "Cliente alega ter sido [Editado pelo Reclame Aqui] pela Cakto Pay após solicitação de pagamento não recebido.",
            "url": "https://www.reclameaqui.com.br/cakto-pay/cliente-alega-ter-sido-editado-pelo-reclame-aqui-pela-cakto-pay-apos-solicitacao-de-pagamento-nao-recebido_iGkp9DgcxElv0_2Y/"
        },
        {
            "gateway": "Cakto",
            "title": "Reclamação sobre falta de resposta e dificuldade de reembolso na Cakto",
            "url": "https://www.reclameaqui.com.br/cakto-pay/reclamacao-sobre-falta-de-resposta-e-dificuldade-de-reembolso-na-cakto_jiJdywNvdI1eyqGx/"
        },
        {
            "gateway": "Cakto",
            "title": "Produtor da Cakto não consegue transferir saldo de vendas devido a falha na validação da Conta Digital",
            "url": "https://www.reclameaqui.com.br/cakto-pay/produtor-da-cakto-nao-consegue-transferir-saldo-de-vendas-devido-a-falha-na-validacao-da-conta-digital_4DnOrKwoT1hMSEch/"
        },
    ]
    
    results = []
    for complaint in all_complaints:
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