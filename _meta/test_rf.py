#!/usr/bin/env python3
import re

# Test rf-string pattern
gateway_slug = 'perfectpay'
pattern = rf'<a[^>]*href="(/empresa/{gateway_slug}/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
print(f'rf-string pattern: {pattern}')

# What does it actually produce?
import re
test_html = '<a href="/empresa/perfectpay/test" title="Test" data-testid="complaint-listagem-v2-title-link">'
match = re.findall(pattern, test_html)
print(f'Match test: {match}')

# The literal pattern that works
pattern_literal = r'<a[^>]*href="(/perfectpay/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
print(f'\nLiteral pattern: {pattern_literal}')
match2 = re.findall(pattern_literal, test_html)
print(f'Match test: {match2}')