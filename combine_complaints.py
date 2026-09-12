import json

with open('complaint_details.json', 'r') as f:
    old_details = json.load(f)
with open('perfectpay_new_details.json', 'r') as f:
    pp_new = json.load(f)
with open('cakto_new_details.json', 'r') as f:
    cakto_new = json.load(f)

all_complaints = old_details + pp_new + cakto_new
seen = set()
unique = []
for c in all_complaints:
    url = c.get('url', '')
    if url and url not in seen:
        seen.add(url)
        unique.append(c)

print(f'Total: {len(all_complaints)}, Unique: {len(unique)}')

with open('complaint_details_combined.json', 'w') as f:
    json.dump(unique, f, ensure_ascii=False, indent=2)

for c in unique:
    print(f"  {c.get('gateway', '?')}: {c.get('list_title', c.get('title', 'No title'))[:60]}...")