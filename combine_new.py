#!/usr/bin/env python3
import json

with open('complaint_details_combined.json', 'r') as f:
    existing = json.load(f)

with open('perfectpay_new_details.json', 'r') as f:
    pp_new = json.load(f)

with open('cakto_new_details.json', 'r') as f:
    ck_new = json.load(f)

all_complaints = existing + pp_new + ck_new
print(f'Total complaints after combine: {len(all_complaints)}')

with open('complaint_details_combined.json', 'w') as f:
    json.dump(all_complaints, f, ensure_ascii=False, indent=2)

print('Saved combined complaints')