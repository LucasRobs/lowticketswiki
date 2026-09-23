#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# Find all hrefs around complaint-listagem-v2-title-link
pattern = r'href="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches = re.findall(pattern, response.text)
print(f'Hrefs from title-link:')
for m in matches[:5]:
    print(f'  {m}')

# Also check the full anchor tag
pattern2 = r'<a[^>]*href="(/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches2 = re.findall(pattern2, response.text)
print(f'\nPattern /perfectpay/...: {len(matches2)}')
for url_path, title in matches2[:3]:
    print(f'  {url_path} -> {title[:60]}')

# Check with /empresa/
pattern3 = r'<a[^>]*href="(/empresa/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches3 = re.findall(pattern3, response.text)
print(f'\nPattern /empresa/perfectpay/...: {len(matches3)}')
for url_path, title in matches3[:3]:
    print(f'  {url_path} -> {title[:60]}')