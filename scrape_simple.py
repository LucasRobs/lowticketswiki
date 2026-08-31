import requests
from bs4 import BeautifulSoup
import json

def scrape_gateway(gateway_slug, gateway_name, max_pages=25):
    all_complaints = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'}
    
    for page_num in range(1, max_pages + 1):
        url = f'https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page_num}'
        print(f'Scraping {gateway_name} page {page_num}...')
        try:
            resp = requests.get(url, headers=headers, timeout=30)
            print(f'  Status: {resp.status_code}')
            
            soup = BeautifulSoup(resp.text, 'html.parser')
            links = soup.find_all('a', href=True)
            
            complaints = []
            for link in links:
                href = link['href']
                if '/reclamacao/' in href:
                    title = link.get_text(strip=True)
                    if title and title != 'Ler reclamação completa':
                        # Make sure it's a full URL
                        if href.startswith('/'):
                            href = 'https://www.reclameaqui.com.br' + href
                        complaints.append({'title': title, 'url': href})
            
            if complaints:
                all_complaints.extend(complaints)
                print(f'  Found {len(complaints)} complaints')
            else:
                print(f'  No complaints found, stopping at page {page_num}')
                break
                
        except Exception as e:
            print(f'  Error on page {page_num}: {e}')
            continue
    
    return all_complaints

if __name__ == '__main__':
    perfectpay = scrape_gateway('perfectpay', 'PerfectPay', 25)
    with open('perfectpay_complaints_full.json', 'w') as f:
        json.dump(perfectpay, f, ensure_ascii=False, indent=2)
    print(f'PerfectPay total: {len(perfectpay)} complaints')
    
    cakto = scrape_gateway('cakto-pay', 'Cakto', 25)
    with open('cakto_complaints_full.json', 'w') as f:
        json.dump(cakto, f, ensure_ascii=False, indent=2)
    print(f'Cakto total: {len(cakto)} complaints')