#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# Test the pattern
pattern = r'data-testid="complaint-listagem-v2-title-link"[^>]*href="([^"]+)"[^>]*title="([^"]+)"'
matches = re.findall(pattern, response.text)
print(f'Pattern matches: {len(matches)}')

# Let's look for the actual pattern in the HTML
# Search for complaint-listagem-v2-title-link
idx = response.text.find('complaint-listagem-v2-title-link')
if idx >= 0:
    print(f'Found at index {idx}')
    print(response.text[idx:idx+500])
else:
    print('NOT FOUND: complaint-listagem-v2-title-link')
    # Search for similar
    for term in ['complaint-listagem', 'title-link', 'data-testid']:
        idx = response.text.find(term)
        if idx >= 0:
            print(f'Found "{term}" at {idx}: {response.text[idx:idx+200]}')
        else:
            print(f'NOT FOUND: {term}')

# Also check the href pattern
href_matches = re.findall(r'href="(/perfectpay/[^"]+)"', response.text)
print(f'\nAll perfectpay hrefs: {len(href_matches)}')
for h in href_matches[:10]:
    print(f'  {h}')