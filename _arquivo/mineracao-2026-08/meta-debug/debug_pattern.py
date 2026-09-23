#!/usr/bin/env python3
import cloudscraper
import re

scraper = cloudscraper.create_scraper(browser='chrome')

# Test with the actual function logic
gateway_slug = 'perfectpay'

response = scraper.get('https://www.reclameaqui.com.br/empresa/perfectpay/lista-reclamacoes/?pagina=1', timeout=30)

# The actual pattern used in function (with f-string)
pattern = rf'<a[^>]*href="(/empresa/{gateway_slug}/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches = re.findall(pattern, response.text)
print(f'Pattern 1 (/empresa/{gateway_slug}/...): {len(matches)} matches')

# The fallback pattern (direct /gateway/...)
pattern2 = rf'<a[^>]*href="({gateway_slug}/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
matches2 = re.findall(pattern2, response.text)
print(f'Pattern 2 ({gateway_slug}/...): {len(matches2)} matches')

# Print actual matches
for url_path, title in matches2[:3]:
    print(f'  {url_path} -> {title[:80]}')