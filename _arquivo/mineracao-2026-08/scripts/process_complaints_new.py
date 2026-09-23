#!/usr/bin/env python3
"""Process complaints and extract product info with improved extraction logic."""

import json
import re
from datetime import datetime
from collections import defaultdict

# Load all complaint data
with open('/Users/robson/Documents/Obsidian Vault/lowticket/complaint_details_combined.json', 'r') as f:
    all_complaints = json.load(f)

print(f"Total complaints: {len(all_complaints)}")

# Deduplicate by URL
seen_urls = set()
unique_complaints = []
for c in all_complaints:
    url = c.get('url', '')
    if url and url not in seen_urls:
        seen_urls.add(url)
        unique_complaints.append(c)

print(f"Unique complaints: {len(unique_complaints)}")

# Extract product info from each complaint using improved patterns
def extract_product_info(complaint):
    # Handle both 'body' (old format) and 'raw_text' (new format)
    body = complaint.get('body', '') or complaint.get('raw_text', '')
    text = body + ' ' + complaint.get('title', '') + ' ' + complaint.get('list_title', '')
    gateway = complaint.get('gateway', '')
    url = complaint.get('url', '')
    
    # Extract product name patterns - more specific
    product_patterns = [
        r'O nome da empresa é\s+([^.\n]+)',
        r'produto\s+[\"\']?([A-Z][a-zA-Z0-9\s\.\-]{2,40})[\"\']?',
        r'compra de\s+([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'adquiri\s+(?:a\s+)?(?:compra\s+do\s+)?([A-Z][a-zA-Z0-9\s\.\-]{2,40})',
        r'serviço\s+([a-zA-Z0-9\s\.\-]{2,40})',
        r'app\s+([A-Z][a-zA-Z0-9\s\.\-]{2,30})',
        r'anunciado como\s+([^.\n]+)',
        r'(?:Stalkeia|Stalkea|Stalker|Spygram|hqflix|Chat\s*GPT|PLANO\s+FREELANCER)[\w\s\.\-]*',
        r'[\"\']([^\"\']+)[\"\']',
    ]
    
    produto = "sem nome"
    for pattern in product_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            produto = matches[0].strip()
            break
    
    # Clean up product name
    produto = re.sub(r'\s+', ' ', produto).strip()
    if len(produto) > 80:
        produto = produto[:80]
    
    # Filter out garbage extractions
    garbage = [
        'ra ads', 'previous slide', 'next slide', 'compartilhe', 'resposta da emp',
        'pelo reclame aqui', 'editado pelo reclame aqui', 'que comprei',
        'comercializado e pelo atendimento', 'digital. tenho mais de r',
        'informando que meu perfil', 'mas até agora não', 'e ele nao chegou',
        'da plataforma', 'inativo', 'pedindo mais pix',
        'um curso e', 'mas eu n', 'eles mandam entrar', 'onde diz que tenho',
        'um livro de macrame', 'paguei com pix', 'entrar em contato com o prod',
    ]
    if any(g in produto.lower() for g in garbage):
        produto = "sem nome"
    
    # Special handling for known products from text
    text_lower = text.lower()
    if 'stalkeia' in text_lower or 'stalkea' in text_lower or 'stalker' in text_lower:
        produto = "Stalkeia"
    elif 'spygram' in text_lower:
        produto = "Spygram"
    elif 'hqflix' in text_lower:
        produto = "hqflix"
    elif 'plano freelancer' in text_lower or 'freelancer imediato' in text_lower:
        produto = "Plano Freelancer Imediato"
    elif 'chat gpt' in text_lower or 'chatgpt' in text_lower or 'gpt plus' in text_lower:
        produto = "Chat GPT Plus"
    elif 'infinity' in text_lower and 'chat' in text_lower:
        produto = "Infinity Chat GPT"
    elif 'vavá academy' in text_lower or 'vava academy' in text_lower:
        produto = "Vavá Academy"
    elif 'lumi ai' in text_lower or 'lumi' in text_lower:
        produto = "Lumi AI"
    elif 'grupo no telegram' in text_lower:
        produto = "Grupo no Telegram"
    # NEW: Products from current batch
    elif 'converza' in text_lower or 'converza.io' in text_lower:
        produto = "Converza.io"
    elif 'comunidade vsa' in text_lower or 'vsa' in text_lower:
        produto = "COMUNIDADE VSA"
    elif 'retrato da sua alma gêmea' in text_lower or 'retrato da sua alma gemea' in text_lower or 'seu retrato oficial' in text_lower:
        produto = "Retrato da Sua Alma Gêmea"
    elif 'pack canva happy hour' in text_lower:
        produto = "Pack Canva Happy Hour"
    elif 'receitas de copões' in text_lower or 'copões gourmet' in text_lower or 'copos gourmet' in text_lower:
        produto = "150 Receitas de Copões Gourmet"
    elif 'mestre do copão' in text_lower or 'mestre do copao' in text_lower:
        produto = "Mestre do Copão"
    elif 'método atlas' in text_lower or 'metodo atlas' in text_lower:
        produto = "Método Atlas"
    elif 'frequência da vinci' in text_lower or 'frequencia da vinci' in text_lower or 'cura de zumbido' in text_lower:
        produto = "Frequência da Vinci"
    elif 'programa de cura' in text_lower and 'zumbido' in text_lower:
        produto = "Frequência da Vinci"
    # NEW: Products from current batch (Sept 2026)
    elif 'knights club' in text_lower or 'comunidade knights' in text_lower:
        produto = "COMUNIDADE KNIGHTS CLUB"
    elif 'cloakeuai' in text_lower or 'cloak eu ai' in text_lower:
        produto = "Cloakeuai"
    elif 'códigos lucrativos' in text_lower or 'codigos lucrativos' in text_lower:
        produto = "Códigos Lucrativos"
    elif 'opini pix' in text_lower or 'opinipix' in text_lower:
        produto = "Opini Pix"
    elif 'aristocracy' in text_lower and 'negocios' in text_lower:
        produto = "Aristocracy Negócios Digitais"
    elif 'apostila de psicologia' in text_lower:
        produto = "Apostila de Psicologia 2025"
    elif 'fábrica de low ticket' in text_lower or 'fabrica de low ticket' in text_lower:
        produto = "Fábrica de Low Ticket"
    elif 'zap radar' in text_lower or 'zapradar' in text_lower:
        produto = "ZAP Radar"
    # NEW: Products from Sept 2026 batch 2
    elif 'mentoria nova profiss' in text_lower:
        produto = "Mentoria Nova Profissão"
    elif 'turminha alfakids' in text_lower or 'alfakids' in text_lower:
        produto = "Turminha Alfakids"
    elif 'directspeed' in text_lower:
        produto = "Directspeed"
    elif 'curso de mandarim' in text_lower:
        produto = "Curso de Mandarim"
    elif 'perfect academy' in text_lower:
        produto = "Perfect Academy"
    elif 'produto malu' in text_lower or 'malu exige' in text_lower:
        produto = "Produto Malu"
    
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
    
    # NEW: Specific product checks FIRST (before generic categories)
    # Converza.io - chatbot/messaging platform
    if 'converza' in text_lower:
        nicho = "Chatbots / Automação de mensagens"
        angulos = ["facilidade_tecnologica", "autoridade", "ganância_escala"]
        sinais_cloaker.append("taxa_adicional_para_desbloquear")
    
    # COMUNIDADE VSA - likely marketing/business community
    elif 'comunidade vsa' in text_lower or ('vsa' in text_lower and 'comunidade' in text_lower):
        nicho = "Marketing / Comunidades de negócios"
        angulos = ["prova_social", "autoridade", "facilidade"]
    
    # Retrato da Sua Alma Gêmea - AI art/personalized drawing
    elif 'retrato da sua alma' in text_lower or 'seu retrato oficial' in text_lower:
        nicho = "Arte personalizada / IA generativa"
        angulos = ["curiosidade", "novidade", "vaidade"]
    
    # Pack Canva / Copões / Mestre do Copão - digital products for resale
    elif any(kw in text_lower for kw in ['pack canva', 'copões gourmet', 'copos gourmet', 'mestre do copão', 'mestre do copao', 'happy hour']):
        nicho = "PLR / Produtos digitais para revenda"
        angulos = ["ganância_renda_extra", "facilidade", "prova_social"]
    
    # Método Atlas - course/method
    elif 'método atlas' in text_lower or 'metodo atlas' in text_lower:
        nicho = "Educação e consultoria"
        angulos = ["autoridade", "ganância_carreira", "novidade"]
    
    # Frequência da Vinci - tinnitus cure
    elif 'frequência da vinci' in text_lower or 'frequencia da vinci' in text_lower or ('cura' in text_lower and 'zumbido' in text_lower):
        nicho = "Saúde / Tratamentos alternativos"
        angulos = ["medo", "esperança", "autoridade_cientifica"]

    # NEW: Products from current batch (Sept 2026)
    elif 'knights club' in text_lower or 'comunidade knights' in text_lower:
        nicho = "Comunidades / Mentoria de negócios"
        angulos = ["prova_social", "autoridade", "ganância_renda_extra"]
    elif 'cloakeuai' in text_lower or 'cloak eu ai' in text_lower:
        nicho = "Ferramentas de IA / Cloaking"
        angulos = ["facilidade_tecnologica", "novidade", "curiosidade"]
        sinais_cloaker.append("cloaking_ferramenta")
    elif 'códigos lucrativos' in text_lower or 'codigos lucrativos' in text_lower or 'opini pix' in text_lower or 'opinipix' in text_lower:
        nicho = "Ganhar dinheiro online / Ferramentas de afiliado"
        angulos = ["ganância_renda_extra", "facilidade", "novidade"]
        if 'taxa' in text_lower or 'adicional' in text_lower or 'mais r$' in text_lower:
            sinais_cloaker.append("taxa_adicional_para_desbloquear")
    elif 'aristocracy' in text_lower and 'negocios' in text_lower:
        nicho = "Produtos digitais variados / Assinatura vitalícia"
        angulos = ["ganância_acesso_vitalicio", "facilidade", "autoridade"]
        sinais_cloaker.append("assinatura_vitalicia_expirada")
    elif 'apostila de psicologia' in text_lower:
        nicho = "Educação / Concursos e certificações"
        angulos = ["autoridade", "medo_perda_dinheiro", "necessidade"]
    elif 'fábrica de low ticket' in text_lower or 'fabrica de low ticket' in text_lower:
        nicho = "Educação / Marketing digital e low ticket"
        angulos = ["autoridade", "ganância_renda_extra", "prova_social"]
    elif 'zap radar' in text_lower or 'zapradar' in text_lower:
        nicho = "Ferramentas de espionagem / WhatsApp"
        angulos = ["curiosidade_voyeurismo", "medo_traiçao", "facilidade_tecnologica"]
        sinais_cloaker.append("taxa_adicional_para_desbloquear")

    # NEW: Products from Sept 2026 batch 2
    elif 'mentoria nova profiss' in text_lower:
        nicho = "Educação e consultoria / Mentoria"
        angulos = ["autoridade", "ganância_carreira", "prova_social"]
    elif 'turminha alfakids' in text_lower or 'alfakids' in text_lower:
        nicho = "Educação infantil / Materiais didáticos"
        angulos = ["autoridade", "facilidade", "necessidade"]
    elif 'directspeed' in text_lower:
        nicho = "Ferramentas de produtividade / Assinatura"
        angulos = ["facilidade", "ganância_renda_extra", "recorrência"]
    elif 'curso de mandarim' in text_lower:
        nicho = "Educação / Idiomas"
        angulos = ["autoridade", "ganância_carreira", "novidade"]
    elif 'perfect academy' in text_lower:
        nicho = "Educação e consultoria / Cursos online"
        angulos = ["autoridade", "facilidade", "prova_social"]
    elif 'produto malu' in text_lower or 'malu exige' in text_lower:
        nicho = "Ferramentas / Aplicativos"
        angulos = ["facilidade_tecnologica", "ganância_renda_extra"]
        sinais_cloaker.append("taxa_adicional_para_desbloquear")

    # Espionagem/monitoramento
    elif any(kw in text_lower for kw in ['espion', 'monitor', 'spy', 'stalke', 'whatsapp', 'rastreador', 'acesso a perfis', 'direct', 'stalkeia', 'stalker']):
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
    elif any(kw in text_lower for kw in ['freelancer', 'trabalho remoto', 'trabalhar de casa', 'ganhar dinheiro', 'como trabalhar', 'sites de como']):
        nicho = "Ganhar dinheiro online / trabalho remoto"
        angulos = ["ganância_renda_extra", "facilidade"]
        if 'taxa' in text_lower or 'adicional' in text_lower or 'mais r$' in text_lower:
            sinais_cloaker.append("taxa_adicional_para_desbloquear")
    
    # Seguidores/social media
    elif any(kw in text_lower for kw in ['seguidor', 'instagram', 'engajamento', 'brazileiros']):
        nicho = "Crescimento em redes sociais"
        angulos = ["vaidade", "prova_social", "facilidade"]
    
    # Consultoria/cursos
    elif any(kw in text_lower for kw in ['consultoria', 'curso', 'mentoria', 'accenture', 'academy', 'aulas', 'sax']):
        nicho = "Educação e consultoria"
        angulos = ["autoridade", "ganância_carreira"]
    
    # Lumi AI / AI products
    elif any(kw in text_lower for kw in ['lumi', 'lumi ai', 'ai ', 'inteligencia artificial']):
        nicho = "Ferramentas de IA / Produtividade"
        angulos = ["facilidade", "novidade", "autoridade"]
    
    # Telegram groups / digital products
    elif any(kw in text_lower for kw in ['telegram', 'grupo', 'digital']):
        nicho = "Infoprodutos - suporte e reembolso"
        angulos = ["medo_perda_dinheiro", "confiança_quebrada"]
    
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
    if 'upsell' in text_lower or 'adicional' in text_lower or 'mais pix' in text_lower or 'outra compra' in text_lower or 'mais r$' in text_lower:
        mecanica = "upsell | order bump"
    if 'recorrência' in text_lower or 'mensal' in text_lower or 'anual' in text_lower:
        mecanica = "recorrência"
    if 'crédito' in text_lower:
        mecanica = "créditos"
    if 'vitalício' in text_lower:
        mecanica = "front simples (vitalício)"
    
    # Termo de busca otimizado
    termo_busca = produto
    for suffix in ['.ai', '.com', '.app', ' app', ' ai', ' pro', ' max', ' premium', '.com.br']:
        termo_busca = termo_busca.replace(suffix, '')
    termo_busca = termo_busca.strip()
    
    # Descrição - extract the actual complaint narrative
    lines = text.split('\n')
    complaint_lines = []
    in_complaint = False
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if any(kw in line.lower() for kw in ['realizei', 'comprei', 'adquiri', 'paguei', 'solicitei', 'o nome da empresa', 'o produto', 'foi anunciado', 'não consegui', 'travou', 'pedindo mais', 'fiz uma compra', 'fiz o pagamento', 'solicitei o pagamento', 'sou produtor']):
            in_complaint = True
        if in_complaint:
            complaint_lines.append(line)
        if any(kw in line for kw in ['RA Ads', 'Reputação da empresa', 'Compare', 'Compartilhe', 'Controle sua privacidade', 'Política de Privacidade', 'Equipe Perfect Pay', 'Equipe Cakto', 'Consideração final']):
            break
    
    descricao = ' '.join(complaint_lines[:5])[:500].strip()
    
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
    tipo = "marca" if any(kw in termo.lower() for kw in ['stalkeia', 'spygram', 'hqflix', 'freelancer', 'chat gpt', 'infinity', 'chatgpt', 'gpt plus', 'vavá', 'lumi', 'grupo telegram', 'converza', 'comunidade vsa', 'retrato da sua alma', 'seu retrato oficial', 'pack canva', 'copões gourmet', 'copos gourmet', 'mestre do copão', 'mestre do copao', 'método atlas', 'metodo atlas', 'frequência da vinci', 'frequencia da vinci', 'mentoria nova profiss', 'turminha alfakids', 'alfakids', 'directspeed', 'curso de mandarim', 'perfect academy', 'produto malu', 'malu exige']) else "angulo"
    
    # Producer info (simplified)
    produtor_nome = "desconhecido"
    produtor_cnpj = ""
    outras_ofertas = []
    gateways_historico = [gateway]
    portfolio_size_est = "1-2 ofertas ativas"
    
    # Try to extract producer from complaint text
    for item in items:
        prod_match = re.search(r'(?:empresa|produtor|vendedor|equipe)\s+([A-Z][a-zA-Z\s\.]{3,40})', item['descricao'], re.IGNORECASE)
        if prod_match:
            produtor_nome = prod_match.group(1).strip()
            break
    
    # Known producers
    if 'ks digital' in ' '.join(items[0].get('descricao', '').lower() for _ in range(1)):
        produtor_nome = "KS Digital SA"
    elif 'stalkeia' in termo.lower():
        produtor_nome = "Stalker Tech LTDA"
        outras_ofertas = ["Stalkea.ai", "Stalker Pro", "MonitoraZap"]
        gateways_historico = ["PerfectPay", "Mangofy", "Payt"]
        portfolio_size_est = "3-5 ofertas ativas"
    elif 'spygram' in termo.lower():
        produtor_nome = "Spygram LTDA"
    elif 'hqflix' in termo.lower():
        produtor_nome = "HQFlix Streaming"
    elif 'vavá academy' in termo.lower() or 'vava academy' in termo.lower():
        produtor_nome = "Vavá Academy"
    elif 'lumi ai' in termo.lower():
        produtor_nome = "Lumi AI"
    elif 'kaique' in ' '.join(items[0].get('body', '').lower() for _ in range(1)):
        produtor_nome = "Kaique Santtos"
    # NEW: Producers for current batch
    elif 'converza' in termo.lower():
        produtor_nome = "Converza Tecnologia"
        outras_ofertas = ["Converza.io"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'comunidade vsa' in termo.lower():
        produtor_nome = "VSA Marketing"
        outras_ofertas = ["COMUNIDADE VSA"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'retrato da sua alma' in termo.lower() or 'seu retrato oficial' in termo.lower():
        produtor_nome = "Seu Retrato Oficial"
        outras_ofertas = ["Retrato da Sua Alma Gêmea"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif any(kw in termo.lower() for kw in ['pack canva', 'copões gourmet', 'copos gourmet', 'mestre do copão', 'mestre do copao']):
        produtor_nome = "Copão Digital"
        outras_ofertas = ["Pack Canva Happy Hour", "150 Receitas de Copões Gourmet", "Mestre do Copão"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "3-5 ofertas ativas"
    elif 'método atlas' in termo.lower() or 'metodo atlas' in termo.lower():
        produtor_nome = "Atlas Method"
        outras_ofertas = ["Método Atlas"]
        gateways_historico = ["PerfectPay"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'frequência da vinci' in termo.lower() or 'frequencia da vinci' in termo.lower():
        produtor_nome = "Frequência da Vinci"
        outras_ofertas = ["Frequência da Vinci"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    # NEW: Producers for Sept 2026 batch 2
    elif 'mentoria nova profiss' in termo.lower():
        produtor_nome = "Gustavo Castro"
        outras_ofertas = ["Mentoria Nova Profissão"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'turminha alfakids' in termo.lower() or 'alfakids' in termo.lower():
        produtor_nome = "AlfaKids"
        outras_ofertas = ["Turminha Alfakids"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'directspeed' in termo.lower():
        produtor_nome = "DirectSpeed"
        outras_ofertas = ["Directspeed"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'curso de mandarim' in termo.lower():
        produtor_nome = "Ismael Vitor Pinheiro Milher"
        outras_ofertas = ["Curso de Mandarim"]
        gateways_historico = ["Cakto"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'perfect academy' in termo.lower():
        produtor_nome = "Perfect Academy"
        outras_ofertas = ["Perfect Academy"]
        gateways_historico = ["PerfectPay"]
        portfolio_size_est = "1-2 ofertas ativas"
    elif 'produto malu' in termo.lower() or 'malu exige' in termo.lower():
        produtor_nome = "Malu"
        outras_ofertas = ["Produto Malu"]
        gateways_historico = ["PerfectPay"]
        portfolio_size_est = "1-2 ofertas ativas"

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
            "cnpj": produtor_cnpj,
            "outras_ofertas": outras_ofertas,
            "gateways_historico": gateways_historico,
            "portfolio_size_est": portfolio_size_est
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
    print(f"  [{a['score_final']}] {a['produto']} ({a['gateway']}) - {a['acao_recomendada']} - {a['nicho']}")