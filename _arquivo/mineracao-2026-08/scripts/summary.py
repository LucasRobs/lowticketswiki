import json

with open('achados.json', 'r') as f:
    data = json.load(f)

achados = data['achados']
total = len(achados)
quente = sum(1 for a in achados if a['temperatura'] == 'quente')
morna = sum(1 for a in achados if a['temperatura'] == 'morna')
fria = sum(1 for a in achados if a['temperatura'] == 'fria')
marcas = sum(1 for a in achados if a['tipo'] == 'marca')
angulos = sum(1 for a in achados if a['tipo'] == 'angulo')

print(f'Total achados: {total}')
print(f'  Quente: {quente}')
print(f'  Morna: {morna}')
print(f'  Fria: {fria}')
print(f'  Marcas: {marcas}')
print(f'  Ângulos: {angulos}')

# By niche
from collections import defaultdict
nicho_stats = defaultdict(lambda: {'total': 0, 'marca': 0, 'angulo': 0, 'quente': 0, 'morna': 0, 'fria': 0})
for a in achados:
    nicho = a['nicho']
    nicho_stats[nicho]['total'] += 1
    if a['tipo'] == 'marca':
        nicho_stats[nicho]['marca'] += 1
    else:
        nicho_stats[nicho]['angulo'] += 1
    nicho_stats[nicho][a['temperatura']] += 1

print('\nTop 10 nichos:')
for nicho, stats in sorted(nicho_stats.items(), key=lambda x: -x[1]['total'])[:10]:
    print(f'  {nicho}: {stats["total"]} total ({stats["marca"]} marcas, {stats["angulo"]} ângulos) | quente={stats["quente"]}, morna={stats["morna"]}, fria={stats["fria"]}')

# Products with score >= 65
print('\nAchados MONITORAR/TESTAR_IMEDIATO (score >= 65):')
for a in achados:
    if a['score_final'] >= 65:
        print(f'  [{a["score_final"]}] {a["produto"]} ({a["gateway"]}) - {a["acao_recomendada"]} - {a["nicho"]} - {a["faixa_preco"]}')