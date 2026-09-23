import re
text = """Veja também
todas as reclamações
não respondidas
respondidas
finalizadas
Reembolso negado e prazo expirado devido à burocracia da Perfect Pay

Respondida

PerfectPay

Mesquita - RJ

31/08/2026 às 12:25

ID: 257816301

Comprei o produto "Interactive Live" através da plataforma Perfect Pay, que atuou como processadora de pagamento da venda."""

pattern = r'(?:Método Atlas|Interactive Live|Low Ticket do Zero 2\.0|Low Ticket do Zero|Cloakeuai|Stalkeia|Spygram|HQFlix|Converza\.io|VSA|Retrato da Sua Alma Gêmea|Pack Canva|Mestre do Copão|Chat GPT PLUS|Comunidade VSA|Infinity|Apostila de Psicologia 2025|Fábrica de Low Ticket|ZAP Radar|Zap Radar|Curs[oe] [A-Z][a-z]+)\b'
matches = re.findall(pattern, text, re.IGNORECASE)
print('Matches:', matches)