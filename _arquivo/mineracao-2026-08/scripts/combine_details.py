import json

# Load existing combined details
with open('complaint_details_combined.json', 'r') as f:
    combined = json.load(f)

# Load new PerfectPay details
with open('perfectpay_new_details.json', 'r') as f:
    perfectpay_new = json.load(f)

# Load new Cakto details
with open('cakto_new_details.json', 'r') as f:
    cakto_new = json.load(f)

# Convert new format to combined format
for item in perfectpay_new:
    if 'error' not in item:
        combined.append({
            'title': item.get('list_title', ''),
            'url': item.get('url', ''),
            'body': item.get('raw_text', ''),
            'gateway': item.get('gateway', 'PerfectPay')
        })

for item in cakto_new:
    if 'error' not in item:
        combined.append({
            'title': item.get('list_title', ''),
            'url': item.get('url', ''),
            'body': item.get('raw_text', ''),
            'gateway': item.get('gateway', 'Cakto')
        })

# Deduplicate by URL
seen_urls = set()
unique_combined = []
for c in combined:
    url = c.get('url', '')
    if url and url not in seen_urls:
        seen_urls.add(url)
        unique_combined.append(c)

print(f'Total combined: {len(combined)}')
print(f'Unique combined: {len(unique_combined)}')

# Save
with open('complaint_details_combined.json', 'w') as f:
    json.dump(unique_combined, f, ensure_ascii=False, indent=2)

print('Saved combined details')