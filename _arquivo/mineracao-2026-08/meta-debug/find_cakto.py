#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

# Search for cakto on ReclameAqui
response = scraper.get('https://www.reclameaqui.com.br/busca/?q=cakto', timeout=30)
print(f'Search status: {response.status_code}')
print(f'Length: {len(response.text)}')

# Look for empresa links
empresa_links = re.findall(r'/empresa/([^/\"]+)', response.text)
print(f'Empresa slugs found: {set(empresa_links)}')

# Also check for cakto variations
for term in ['cakto', 'kaakto', 'cacto']:
    if term in response.text.lower():
        print(f'Found {term} in search results')

# Save for inspection
with open('/tmp/cakto_search.html', 'w') as f:
    f.write(response.text)
print('Saved to /tmp/cakto_search.html')