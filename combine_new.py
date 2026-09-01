import json

# Load existing combined
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_combined.json', 'r') as f:
    existing = json.load(f)

# Load new
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_new.json', 'r') as f:
    new = json.load(f)

# Combine and deduplicate by URL
seen_urls = set()
combined = []
for c in existing + new:
    url = c.get('url', '')
    if url and url not in seen_urls:
        seen_urls.add(url)
        combined.append(c)

print(f"Existing: {len(existing)}, New: {len(new)}, Combined unique: {len(combined)}")

with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_combined.json', 'w') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("Done!")