import json

with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_new_details.json', 'r') as f:
    perfectpay = json.load(f)

with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto_new_details.json', 'r') as f:
    cakto = json.load(f)

# Check Fábrica de Low Ticket
for c in cakto:
    if 'fábrica' in c.get('list_title', '').lower() or 'fabrica' in c.get('list_title', '').lower():
        print("=== Fábrica de Low Ticket ===")
        print(f"Title: {c.get('list_title')}")
        print(f"Raw text (first 500): {c.get('raw_text', '')[:500]}")
        print()

# Check Apostila de Psicologia
for c in cakto:
    if 'psicologia' in c.get('list_title', '').lower():
        print("=== Apostila de Psicologia ===")
        print(f"Title: {c.get('list_title')}")
        print(f"Raw text (first 500): {c.get('raw_text', '')[:500]}")
        print()

# Check ZAP Radar
for c in perfectpay:
    if 'zap radar' in c.get('list_title', '').lower() or 'zap radar' in c.get('raw_text', '').lower():
        print("=== ZAP Radar ===")
        print(f"Title: {c.get('list_title')}")
        print(f"Raw text (first 500): {c.get('raw_text', '')[:500]}")
        print()

# Check garbage terms
for c in perfectpay + cakto:
    title = c.get('list_title', '').lower()
    if 'inicial e' in title or 'continua ativo' in title or 'de seguran' in title:
        print(f"=== Garbage: {c.get('list_title')} ===")
        print(f"Raw text (first 300): {c.get('raw_text', '')[:300]}")
        print()