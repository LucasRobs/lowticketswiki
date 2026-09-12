#!/usr/bin/env python3
"""
Coleta reclamações do ReclameAqui para gateways de pagamento.
Usa cloudscraper para bypass Cloudflare.
"""

import cloudscraper
import json
import re
from datetime import datetime
from typing import List, Dict
import time

# Gateway slugs no ReclameAqui (usados nas URLs das reclamações)
GATEWAY_SLUGS = {
    'perfectpay': 'perfectpay',
    'cakto': 'cakto-pay',
}

def extract_complaints_from_html(html: str, gateway_slug: str) -> List[Dict]:
    """Extrai títulos e URLs das reclamações do HTML da página de lista."""
    complaints = []
    
    # Padrão: O href é DIRETO /gateway/... (COM / inicial, SEM /empresa/ prefix)
    pattern = rf'<a[^>]*href="(/{gateway_slug}/[^"]+)"[^>]*title="([^"]+)"[^>]*data-testid="complaint-listagem-v2-title-link"'
    matches = re.findall(pattern, html)
    
    for url_path, title in matches:
        title = title.strip()
        if not title or len(title) < 5:
            continue
        # Filtrar links que não são reclamações
        if any(skip in url_path for skip in ['?pagina=', 'ordenar=', 'filtro', '/sobre/', '/lista-reclamacoes/']):
            continue
            
        # Garantir que a URL está completa
        if url_path.startswith('http'):
            full_url = url_path
        elif url_path.startswith('/empresa/'):
            full_url = f"https://www.reclameaqui.com.br{url_path}"
        else:
            full_url = f"https://www.reclameaqui.com.br/empresa{url_path}"
            
        complaints.append({
            'title': title,
            'url': full_url
        })
    
    # Deduplicar por URL
    seen = set()
    unique = []
    for c in complaints:
        if c['url'] not in seen:
            seen.add(c['url'])
            unique.append(c)
    
    return unique

def extract_complaint_body_from_listing(html: str) -> List[str]:
    """Extrai os corpos das reclamações direto da página de listagem."""
    # <p class="sc-1pe7b5t-3 jUwpCk">texto...</p>
    pattern = r'class="sc-1pe7b5t-3[^"]*"[^>]*>([^<]+)</p>'
    matches = re.findall(pattern, html)
    bodies = []
    for m in matches:
        m = m.replace('"', '"').replace('&apos;', "'").replace('&', '&')
        m = m.replace('<', '<').replace('>', '>').replace('&nbsp;', ' ')
        m = re.sub(r'\s+', ' ', m).strip()
        if len(m) > 30:
            bodies.append(m[:3000])
    return bodies

def extract_complaint_body(html: str) -> str:
    """Extrai o corpo da reclamação da página individual."""
    # Primeiro tentar pegar da listagem (já vem no card)
    bodies = extract_complaint_body_from_listing(html)
    if bodies:
        return bodies[0]  # Retorna o primeiro (mais relevante)
    
    # Fallback: buscar na página individual
    patterns = [
        r'"description":"([^"]+)"',
        r'data-testid="complaint-description"[^>]*>([^<]+)<',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, html, re.DOTALL)
        if matches:
            best = max(matches, key=len)
            best = best.replace('"', '"').replace('&apos;', "'").replace('&', '&')
            best = best.replace('<', '<').replace('>', '>').replace('&nbsp;', ' ')
            best = re.sub(r'\s+', ' ', best).strip()
            if len(best) > 30:
                return best[:3000]
    
    return ""

def collect_gateway_complaints(gateway_name: str, pages: int = 25, delay: float = 1.0) -> List[Dict]:
    """Coleta reclamações de um gateway específico."""
    gateway_slug = GATEWAY_SLUGS.get(gateway_name, gateway_name)
    scraper = cloudscraper.create_scraper(browser='chrome')
    all_complaints = []
    
    print(f"Coletando {gateway_name} (slug: {gateway_slug}) - {pages} páginas...")
    
    for page in range(1, pages + 1):
        url = f"https://www.reclameaqui.com.br/empresa/{gateway_slug}/lista-reclamacoes/?pagina={page}"
        
        try:
            response = scraper.get(url, timeout=30)
            if response.status_code != 200:
                print(f"  Página {page}: HTTP {response.status_code}")
                break
            
            complaints = extract_complaints_from_html(response.text, gateway_slug)
            
            # Extrair corpos direto da listagem (já vêm nos cards)
            bodies = extract_complaint_body_from_listing(response.text)
            for i, c in enumerate(complaints):
                if i < len(bodies):
                    c['body'] = bodies[i]
                else:
                    c['body'] = ""
            
            if not complaints:
                print(f"  Página {page}: nenhuma reclamação (fim da lista)")
                break
            
            all_complaints.extend(complaints)
            print(f"  Página {page}: {len(complaints)} reclamações")
            
            time.sleep(delay)
            
        except Exception as e:
            print(f"  Página {page}: erro - {e}")
            break
    
    print(f"  Total {gateway_name}: {len(all_complaints)} reclamações")
    return all_complaints

def fetch_complaint_bodies(complaints: List[Dict], max_parallel: int = 10) -> List[Dict]:
    """Busca o corpo de cada reclamação visitando a página individual (para as que não têm)."""
    scraper = cloudscraper.create_scraper(browser='chrome')
    enriched = []
    
    # Filtrar só as que não têm corpo
    need_body = [c for c in complaints if not c.get('body')]
    have_body = [c for c in complaints if c.get('body')]
    
    print(f"  {len(have_body)} já têm corpo, buscando {min(len(need_body), max_parallel)} restantes...")
    
    for i, complaint in enumerate(need_body[:max_parallel]):
        try:
            response = scraper.get(complaint['url'], timeout=30)
            if response.status_code == 200:
                body = extract_complaint_body(response.text)
                complaint['body'] = body
            else:
                complaint['body'] = ""
        except Exception as e:
            complaint['body'] = ""
            print(f"  Erro ao buscar {complaint['url']}: {e}")
        
        enriched.append(complaint)
        time.sleep(0.5)
    
    # Adicionar as restantes sem corpo
    for complaint in need_body[max_parallel:]:
        complaint['body'] = ""
        enriched.append(complaint)
    
    return have_body + enriched

def main():
    gateways = ['perfectpay', 'cakto']
    pages_per_gateway = 25
    
    all_data = {
        'data_varredura': datetime.now().strftime('%Y-%m-%d'),
        'gateways': [],
        'achados_raw': []
    }
    
    for gateway in gateways:
        complaints = collect_gateway_complaints(gateway, pages_per_gateway)
        
        # Buscar corpo das que não têm (máx 10)
        enriched = fetch_complaint_bodies(complaints, max_parallel=10)
        
        gateway_slug = GATEWAY_SLUGS.get(gateway, gateway)
        gateway_data = {
            'nome': gateway.capitalize(),
            'slug': gateway_slug,
            'reclamacoes_ativas': len(complaints),
            'paginas_varridas': pages_per_gateway,
            'reclamacoes_com_corpo': sum(1 for c in enriched if c.get('body'))
        }
        all_data['gateways'].append(gateway_data)
        
        for c in enriched:
            c['gateway'] = gateway.capitalize()
            all_data['achados_raw'].append(c)
    
    # Salvar dados brutos
    output_file = f"/Users/robson/Documents/Obsidian Vault/lowticket/radar_raw_{datetime.now().strftime('%Y%m%d')}.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)
    
    print(f"\nDados brutos salvos em: {output_file}")
    print(f"Total de reclamações: {len(all_data['achados_raw'])}")
    print(f"Com corpo: {sum(1 for c in all_data['achados_raw'] if c.get('body'))}")

if __name__ == '__main__':
    main()