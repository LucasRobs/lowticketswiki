#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# The href is like /perfectpay/... not /empresa/perfectpay/...
# Test pattern with /perfectpay/
pattern = r'<a[^>]*href="(/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches = re.findall(pattern, response.text)
print(f'Pattern matches: {len(matches)}')
for url_path, title in matches:
    print(f'  {url_path} -> {title[:80]}')

# Also test cakto
print('\n--- Testing Cakto ---')
response2 = scraper.get('https://www.reclameaqui.com.br/empresa/cakto/lista-reclamacoes/?pagina=1', timeout=30)
print(f'Status: {response2.status_code}')
print(f'Length: {len(response2.text)}')

# Check if cakto exists
if 'cakto' in response2.text.lower():
    print('Cakto found in page')
else:
    print('Cakto NOT found - might be different slug')
    # Try to find the correct slug
    import re
    empresa_links = re.findall(r'/empresa/([^/]+)/', response2.text)
    print(f'Empresa links found: {set(empresa_links)}')