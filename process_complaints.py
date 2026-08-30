import json
import re
from datetime import datetime
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

# Extract product info from each complaint using regex patterns
def extract_product_info(complaint):
    text = complaint.get('raw_text', '') + ' ' + complaint.get('list_title', '')
    gateway = complaint.get('gateway', '')
    url = complaint.get('url', '')
    
    # Extract product name patterns
    product_patterns = [
        r'(?:produto|aplicativo|app|serviço|compra de)\s+(?:chamado|chamada|chamados?)\s+["\']?([^"\'\.]+)["\']?',
        r'(?:produto|aplicativo|app|serviço)\s+["\']?([^"\'\.]+)["\']?',
        r'(?:Stalkeia|Stalkea|Stalker|Spygram|hqflix|Chat GPT|PLANO FREELANCER)[\w\s\.]*',
        r'["\']([^"\']+)["\']',
    ]
    
    produto = "sem nome"
    for pattern in product_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            produto = matches[0].strip()
            break
    
    # Clean up product name
    produto = re.sub(r'\s+', ' ', produto).strip()
    if len(produto) > 60:
        produto = produto[:60]
    
    # Extract value
    valor_match = re.search(r'R\$\s*([\d.,]+)', text)
    valor = f"R$ {valor_match.group(1)}" if valor_match else "desconhecido"
    
    # Extract date
    date_match = re.search(r'(\d{2}/\d{2}/\d{4})', text)
    data = date_match.group(1) if date_match else ""
    
    # Determine niche and angles based on content
    nicho = "Outros"
    angulos = []
    sinais_cloaker = []
    
    text_lower = text.lower()
    
    # Espionagem/monitoramento
    if any(kw in text_lower for kw in ['espion', 'monitor', 'spy', 'stalke', 'whatsapp', 'rastreador', 'acesso a perfis', 'direct']):
        nicho = "Espionagem e rastreamento"
        angulos = ["curiosidade_voyeurismo", "medo_traiçao", "facilidade_tecnologica"]
        if 'pix' in text_lower and 'mais' in text_lower:
            sinais_cloaker.append("taxa_adicional_para_desbloquear")
    
    # Streaming
    elif any(kw in text_lower for kw in ['streaming', 'hqflix', 'vitalício', 'filme', 'série']):
        nicho = "Streaming e entretenimento"
        angulos = ["facilidade", "ganância_acesso_vitalicio"]
    
    # IA/ChatGPT
    elif any(kw in text_lower for kw in ['chat gpt', 'chatgpt', 'ia ', 'inteligência artificial', 'gpt plus', 'infinity']):
        nicho = "Ferramentas de IA / Produtividade"
        angulos = ["facilidade", "novidade", "autoridade"]
    
    # Freelancer/trabalho remoto
    elif any(kw in text_lower for kw in ['freelancer', 'trabalho remoto', 'trabalhar de casa', 'ganhar dinheiro']):
        nicho = "Ganhar dinheiro online / trabalho remoto"
        angulos = ["ganância_renda_extra", "facilidade"]
        if 'taxa' in text_lower or 'adicional' in text_lower:
            sinais_cloaker.append("taxa_adicional_para_desbloquear")
    
    # Seguidores/social media
    elif any(kw in text_lower for kw in ['seguidor', 'instagram', 'engajamento', 'brazileiros']):
        nicho = "Crescimento em redes sociais"
        angulos = ["vaidade", "prova_social", "facilidade"]
    
    # Consultoria/cursos
    elif any(kw in text_lower for kw in ['consultoria', 'curso', 'mentoria', 'accenture']):
        nicho = "Educação e consultoria"
        angulos = ["autoridade", "ganância_carreira"]
    
    # Reembolso/suporte genérico
    elif any(kw in text_lower for kw in ['reembolso', 'estorno', 'cancelamento', 'suporte', 'atendimento']):
        nicho = "Infoprodutos - suporte e reembolso"
        angulos = ["medo_perda_dinheiro", "confiança_quebrada"]
    
    # Pagamentos não recebidos
    elif any(kw in text_lower for kw in ['pagamento não recebido', 'não recebi', 'cobrança indevida', 'taxa']):
        nicho = "Serviços financeiros / Pix"
        angulos = ["medo_perda_dinheiro", "indignação"]
    
    # Conta digital produtor
    elif any(kw in text_lower for kw in ['conta digital', 'produtor', 'transferir saldo', 'validacao']):
        nicho = "Serviços financeiros / conta digital"
        angulos = ["medo_perda_dinheiro", "frustração_operacional"]
    
    # Mecânica de monetização
    mecanica = "front simples"
    if 'upsell' in text_lower or 'adicional' in text_lower or 'mais pix' in text_lower or 'outra compra' in text_lower:
        mecanica = "upsell | order bump"
    if 'recorrência' in text_lower or 'mensal' in text_lower or 'anual' in text_lower:
        mecanica = "recorrência"
    if 'crédito' in text_lower:
        mecanica = "créditos"
    
    # Termo de busca otimizado
    termo_busca = produto
    for suffix in ['.ai', '.com', '.app', ' app', ' ai', ' pro', ' max', ' premium']:
        termo_busca = termo_busca.replace(suffix, '')
    termo_busca = termo_busca.strip()
    
    # Descrição
    descricao = text[:300].replace('\n', ' ').strip()
    
    return {
        "produto": produto,
        "produtor": "desconhecido",
        "valor_pago": valor,
        "data_compra": data,
        "nicho": nicho,
        "angulos": angulos,
        "mecanica_monetizacao": mecanica,
        "sinais_cloaker": sinais_cloaker,
        "termo_busca": termo_busca,
        "descricao": descricao,
        "evidencia_url": url,
        "gateway": gateway
    }

# Process all complaints
extracted = []
for c in unique_complaints:
    info = extract_product_info(c)
    extracted.append(info)

# Group by termo_busca (fuzzy dedup)
groups = defaultdict(list)
for item in extracted:
    key = item['termo_busca'].lower().strip()
    groups[key].append(item)

print(f"\nGroups found: {len(groups)}")
for k, v in groups.items():
    print(f"  {k}: {len(v)} mentions")

# Build final achados with scoring
achados = []
today = datetime.now().strftime('%Y-%m-%d')

for termo, items in groups.items():
    if not termo or termo in ['sem nome', 'pelo reclame aqui', 'ra ads previous slide next slid', 'digital. tenho mais de r', 'que comprei', 'pelo reclame aqui']:
        continue
    
    gateway = items[0]['gateway']
    nicho = items[0]['nicho']
    angulos = []
    for item in items:
        angulos.extend(item['angulos'])
    angulos = list(set(angulos))
    
    mencoes = len(items)
    valores = [item['valor_pago'] for item in items if item['valor_pago'] != 'desconhecido']
    faixa_preco = ", ".join(valores[:3]) if valores else ""
    
    # Score calculation: (menções × 0.4) + (dias_diferentes × 0.3) + (multi_gateway × 0.2) + (preço_alto × 0.1)
    # Simplified: dias_diferentes = 1 for now, multi_gateway = 0
    dias_diferentes = len(set(item['data_compra'] for item in items if item['data_compra']))
    multi_gateway = 0  # would need cross-gateway matching
    preco_alto = 0
    for v in valores:
        try:
            match = re.search(r'[\d.]+', v.replace(',', '.'))
            if match:
                price = float(match.group())
                if price > 100:
                    preco_alto = 1
                    break
        except (ValueError, AttributeError):
            pass
    
    score = (mencoes * 0.4) + (dias_diferentes * 0.3) + (multi_gateway * 0.2) + (preco_alto * 0.1)
    score = min(100, max(0, score * 10))  # Scale to 0-100
    
    if score >= 80:
        temperatura = "quente"
        acao = "TESTAR_IMEDIATO"
    elif score >= 65:
        temperatura = "morna"
        acao = "MONITORAR"
    else:
        temperatura = "fria"
        acao = "DESCARTAR"
    
    # Tipo: marca if specific product name, angulo if generic
    tipo = "marca" if any(kw in termo.lower() for kw in ['stalkeia', 'spygram', 'hqflix', 'freelancer', 'chat gpt', 'infinity', 'accenture']) else "angulo"
    
    # Producer info (simplified)
    produtor_nome = "desconhecido"
    if 'ks digital' in ' '.join(items[0].get('descricao', '').lower() for _ in range(1)):
        produtor_nome = "KS Digital SA"
    
    achado = {
        "produto": items[0]['produto'],
        "tipo": tipo,
        "gateway": gateway,
        "nicho": nicho,
        "score_final": round(score),
        "temperatura": temperatura,
        "mencoes": mencoes,
        "faixa_preco": faixa_preco,
        "termo_busca": termo,
        "descricao": items[0]['descricao'],
        "evidencia_url": items[0]['evidencia_url'],
        "validacao_ad_library": {
            "ad_count": 0,
            "dias_rodando_max": 0,
            "criativos_unicos": 0,
            "paises": [],
            "fontes_trafego": [],
            "score_ajustado": round(score)
        },
        "angulos_detectados": angulos,
        "cloaker_suspeito": len(items[0]['sinais_cloaker']) > 0,
        "produtor": {
            "nome": produtor_nome,
            "cnpj": "",
            "outras_ofertas": [],
            "gateways_historico": [gateway],
            "portfolio_size_est": "1-2 ofertas ativas"
        },
        "funil_estimado": {
            "front": faixa_preco.split(',')[0] if faixa_preco else "R$ 27-97",
            "order_bump": "",
            "upsell_1": "",
            "upsell_2": "",
            "recorrencia": ""
        },
        "acao_recomendada": acao
    }
    achados.append(achado)

# Sort by score descending
achados.sort(key=lambda x: x['score_final'], reverse=True)

# Build final output
output = {
    "data_varredura": today,
    "gateways": [
        {"nome": "PerfectPay", "slug": "perfectpay", "reclamacoes_ativas": 287224, "paginas_varridas": 1},
        {"nome": "Cakto", "slug": "cakto-pay", "reclamacoes_ativas": 0, "paginas_varridas": 1}
    ],
    "achados": achados
}

with open('/Users/robson/Documents/Obsidian Vault/lowticket/achados.json', 'w') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nGenerated {len(achados)} achados")
for a in achados:
    print(f"  [{a['score_final']}] {a['produto']} ({a['gateway']}) - {a['acao_recomendada']}")