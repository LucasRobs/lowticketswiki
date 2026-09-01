import re
text = 'Comprei o produto "Interactive Live" através da plataforma Perfect Pay'
pattern = r'(?:Método Atlas|Interactive Live|Low Ticket do Zero 2\.0|Low Ticket do Zero|Cloakeuai|Stalkeia|Spygram|HQFlix|Converza\.io|VSA|Retrato da Sua Alma Gêmea|Pack Canva|Mestre do Copão|Chat GPT PLUS|Comunidade VSA|Infinity|Apostila de Psicologia 2025|Fábrica de Low Ticket|ZAP Radar|Zap Radar|Curs[oe] [A-Z][a-z]+)\b'
matches = re.findall(pattern, text, re.IGNORECASE)
print('Matches:', matches)