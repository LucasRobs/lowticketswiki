#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

gateway_slug = 'perfectpay'
url = f"https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina=1"
response = scraper.get(url, timeout=30)
print(f'Status: {response.status_code}')
print(f'Length: {len(response.text)}')

# Exact pattern from working debug
pattern = rf'<a[^>]*href="({gateway_slug}/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
print(f'Pattern: {pattern}')
matches = re.findall(pattern, response.text)
print(f'Matches: {len(matches)}')
for url_path, title in matches[:3]:
    print(f'  {url_path} -> {title[:60]}')