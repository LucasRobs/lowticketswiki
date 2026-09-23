#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

# Test perfectpay page again
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)
print(f'PerfectPay Status: {response.status_code}')

# Check href pattern for perfectpay
hrefs = re.findall(r'href="(/perfectpay/[^"]+)"', response.text)
print(f'PerfectPay hrefs (first 5):')
for h in hrefs[:5]:
    print(f'  {h}')

# Check if it has /empresa/ prefix
empresa_hrefs = [h for h in hrefs if h.startswith('/empresa/')]
direct_hrefs = [h for h in hrefs if not h.startswith('/empresa/')]
print(f'  With /empresa/: {len(empresa_hrefs)}')
print(f'  Direct: {len(direct_hrefs)}')

# Test the regex pattern
pattern = r'<a[^>]*href="(/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches = re.findall(pattern, response.text)
print(f'\nPattern matches: {len(matches)}')
for url_path, title in matches[:3]:
    print(f'  {url_path} -> {title[:60]}')