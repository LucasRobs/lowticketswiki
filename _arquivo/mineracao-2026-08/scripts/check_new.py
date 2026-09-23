import json

with open('achados.json', 'r') as f:
    data = json.load(f)

print(f'Total achados: {len(data["achados"])}')
for a in data['achados']:
    if 'malu' in a['produto'].lower() or 'instagram' in a['produto'].lower() or 'visualiza' in a['produto'].lower() or 'yoga' in a['produto'].lower() or 'planilha' in a['produto'].lower() or 'codigo' in a['produto'].lower() or 'ferramenta' in a['produto'].lower() or 'ia' in a['produto'].lower() or 'ia academy' in a['produto'].lower():
        print(f'  [{a["score_final"]}] {a["produto"]} ({a["gateway"]}) - {a["acao_recomendada"]} - {a["nicho"]}')