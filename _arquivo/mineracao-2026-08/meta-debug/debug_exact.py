#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

# Test with the EXACT same pattern that worked before
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# The EXACT pattern from the working debug script
pattern = r'<a[^>]*href="(/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches = re.findall(pattern, response.text)
print(f'Exact literal pattern: {len(matches)} matches')

# Check if the HTML is different
idx = response.text.find('complaint-listagem-v2-title-link')
if idx >= 0:
    print(f'Found at index {idx}')
    print(response.text[idx:idx+300])
else:
    print('NOT FOUND in HTML')

# Count occurrences
count = response.text.count('complaint-listagem-v2-title-link')
print(f'Total occurrences: {count}')