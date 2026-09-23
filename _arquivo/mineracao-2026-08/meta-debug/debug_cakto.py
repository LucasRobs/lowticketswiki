#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

# Test cakto-pay page
response = scraper.get('https://www.reclameaqui.com.br/empresa/cakto-pay/lista-reclamacoes/?pagina=1', timeout=30)
print(f'Status: {response.status_code}')
print(f'Length: {len(response.text)}')

# Look for complaint-listagem-v2-title-link
idx = response.text.find('complaint-listagem-v2-title-link')
if idx >= 0:
    print(f'Found at index {idx}')
    print(response.text[idx:idx+500])
else:
    print('NOT FOUND: complaint-listagem-v2-title-link')

# Look for complaint cards
cards = re.findall(r'class="sc-1pe7b5t-0 hFtHyY complaint-listagem-v2-card"[^>]*>(.*?)(?=class="sc-1pe7b5t-0 hFtHyY complaint-listagem-v2-card"|$)', response.text, re.DOTALL)
print(f'\nFound {len(cards)} cards')
for i, card in enumerate(cards[:2]):
    print(f'--- Card {i+1} (first 1500 chars) ---')
    print(card[:1500])
    print()

# Also check hrefs
hrefs = re.findall(r'href="(/cakto-pay/[^"]+)"', response.text)
print(f'\nCakto-pay hrefs: {len(hrefs)}')
for h in hrefs[:10]:
    print(f'  {h}')