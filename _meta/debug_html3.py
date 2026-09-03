#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')
response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# The <a> tag has href, title, and data-testid - but order varies
# Let's find all <a> tags that have complaint-listagem-v2-title-link
pattern = r'<a[^>]*data-testid="complaint-listagem-v2-title-link"[^>]*href="([^"]+)"[^>]*title="([^"]+)"'
matches = re.findall(pattern, response.text)
print(f'Pattern 1 matches: {len(matches)}')

# Try alternative order
pattern2 = r'<a[^>]*href="([^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches2 = re.findall(pattern2, response.text)
print(f'Pattern 2 matches: {len(matches2)}')

# Try more flexible - any order
pattern3 = r'<a[^>]*data-testid="complaint-listagem-v2-title-link"[^>]*>'
tags = re.findall(pattern3, response.text)
print(f'Pattern 3 tag matches: {len(tags)}')
for tag in tags[:3]:
    print(f'  Tag: {tag[:200]}')

# Extract href and title from each tag
for tag in tags:
    href_match = re.search(r'href="([^"]+)"', tag)
    title_match = re.search(r'title="([^"]+)"', tag)
    if href_match and title_match:
        print(f'  HREF: {href_match.group(1)}')
        print(f'  TITLE: {title_match.group(1)}')

# Also try: find all hrefs that look like complaint URLs
complaint_hrefs = [h for h in re.findall(r'href="(/perfectpay/[^"]+)"', response.text) 
                   if not any(skip in h for skip in ['/sobre/', '/lista-reclamacoes/', '?pagina=', 'ordenar=', 'filtro'])]
print(f'\nFiltered complaint hrefs: {len(set(complaint_hrefs))}')
for h in sorted(set(complaint_hrefs))[:10]:
    print(f'  {h}')