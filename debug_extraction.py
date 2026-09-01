import json
import re
from collections import defaultdict

# Load all complaint data
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details.json', 'r') as f:
    old_complaints = json.load(f)

with open('/Users/robson/Documents/Obsidian Vault/lowticket/perfectpay_new_details.json', 'r') as f:
    perfectpay_new = json.load(f)

with open('/Users/robson/Documents/Obsidian Vault/lowticket/cakto_new_details.json', 'r') as f:
    cakto_new = json.load(f)

# Combine all complaints
all_complaints = old_complaints + perfectpay_new + cakto_new

# Deduplicate by URL
seen_urls = set()
unique_complaints = []
for c in all_complaints:
    url = c.get('url', '')
    if url and url not in seen_urls:
        seen_urls.add(url)
        unique_complaints.append(c)

print(f"Total complaints: {len(all_complaints)}")
print(f"Unique complaints: {len(unique_complaints)}")

# Test extraction for each
for c in unique_complaints:
    text = c.get('raw_text', '') + ' ' + c.get('list_title', '')
    list_title = c.get('list_title', '')
    
    # Known products pattern
    pattern = r'(?:Método Atlas|Interactive Live|Low Ticket do Zero 2\.0|Low Ticket do Zero|Cloakeuai|Stalkeia|Spygram|HQFlix|Converza\.io|VSA|Retrato da Sua Alma Gêmea|Pack Canva|Mestre do Copão|Chat GPT PLUS|Comunidade VSA|Infinity|Apostila de Psicologia 2025|Fábrica de Low Ticket|ZAP Radar|Zap Radar|Curs[oe] [A-Z][a-z]+)\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    
    print(f"\n--- URL: {c.get('url', '')[:80]}")
    print(f"  List title: {list_title}")
    print(f"  Known products matches: {matches}")
    
    # Title patterns
    title_patterns = [
        r'^([A-Z][a-zA-Z0-9\s\.]{3,60}?)(?:\s+(?:não|solicita|reclama|falha|impossibil|acesso|demora|cancelamento|dificuldade|cobrança|estorno|reembolso|acessibilidade|clonado|pagamento|compra|produto|aplicativo|app|curso))',
        r'(?:do|da|de|o|a)\s+([A-Z][a-zA-Z0-9\s\.]{3,50})(?:\s+(?:não|solicita|reclama|falha|impossibil|acesso|demora|cancelamento|dificuldade|cobrança|estorno|reembolso))',
    ]
    for tp in title_patterns:
        match = re.search(tp, list_title, re.IGNORECASE)
        if match:
            print(f"  Title pattern match: {match.group(1)}")