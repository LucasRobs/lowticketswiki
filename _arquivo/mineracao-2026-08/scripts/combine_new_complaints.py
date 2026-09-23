#!/usr/bin/env python3
"""Combine new complaint details with existing combined data."""

import json

# Load existing combined data
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_combined.json', 'r') as f:
    existing = json.load(f)

# Load new data
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_new.json', 'r') as f:
    new_data = json.load(f)

# Convert new data format to match existing format
converted = []
for item in new_data:
    converted.append({
        "gateway": item.get("gateway", ""),
        "url": item.get("url", ""),
        "list_title": item.get("title", ""),
        "raw_text": item.get("body", ""),
        "full_text_preview": item.get("body", "")[:500]
    })

# Deduplicate by URL
seen_urls = set()
combined = []
for item in existing + converted:
    url = item.get("url", "")
    if url and url not in seen_urls:
        seen_urls.add(url)
        combined.append(item)

print(f"Existing: {len(existing)}")
print(f"New: {len(converted)}")
print(f"Combined (deduped): {len(combined)}")

# Save combined
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_combined.json', 'w') as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("Saved combined data")