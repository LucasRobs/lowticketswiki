import json

with open('radar_raw_20260903.json', 'r') as f:
    raw_data = json.load(f)

complaints = []
for item in raw_data['achados_raw']:
    complaints.append({
        'title': item['title'],
        'url': item['url'],
        'body': item.get('body', ''),
        'gateway': item['gateway'].replace('Perfectpay', 'PerfectPay').replace('Cakto', 'Cakto')
    })

with open('complaint_details_combined.json', 'w') as f:
    json.dump(complaints, f, ensure_ascii=False, indent=2)

print(f"Converted {len(complaints)} complaints")
print(f"Gateways: {set(c['gateway'] for c in complaints)}")