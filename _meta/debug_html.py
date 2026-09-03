#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# Find complaint cards and their content
cards = re.findall(r'class="sc-1pe7b5t-0 hFtHyY complaint-listagem-v2-card"[^>]*>(.*?)(?=class="sc-1pe7b5t-0 hFtHyY complaint-listagem-v2-card"|$)', response.text, re.DOTALL)
print(f'Found {len(cards)} cards')

for i, card in enumerate(cards[:3]):
    print(f'--- Card {i+1} (first 2000 chars) ---')
    print(card[:2000])
    print()