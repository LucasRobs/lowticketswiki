#!/usr/bin/env python3
import cloudscraper

scraper = cloudscraper.create_scraper(browser='chrome')

# Try common slug variations for Cakto
slugs = ['cakto', 'cakto-pagamentos', 'cakto-pay', 'cakto-gateway', 'cakto-com-br']

for slug in slugs:
    url = f'https://www.reclameaqui.com.br/empresa/{slug}/lista-reclamacoes/?pagina=1'
    response = scraper.get(url, timeout=30)
    print(f'{slug}: HTTP {response.status_code} (len={len(response.text)})')
    
    # Check if it has complaint cards
    if 'complaint-listagem-v2-title-link' in response.text:
        print(f'  -> HAS COMPLAINTS!')
    elif 'Nenhuma reclamação' in response.text or 'nenhuma reclamação' in response.text:
        print(f'  -> No complaints')
    elif response.status_code == 404:
        print(f'  -> 404 Not Found')