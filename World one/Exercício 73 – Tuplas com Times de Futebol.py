times = (
     'Palmeiras', 'São Paulo', 'Corinthians', 'Grêmio', 
    'Atlético-MG', 'Cruzeiro', 'Santos', 'Internacional', 'Botafogo',
    'Fluminense', 'Vasco', 'Bahia', 'Fortaleza', 'Ceará', 
    'Athletico-PR', 'Coritiba', 'Goiás', 'Sport', 'Chapecoense', 'América-MG'
)

print(f'Lista de times do Brasileirao: {times}')
print(f'Os 5 primeiros sao {times[0:5]}')
print(f'Os 4 ultimos sao {times[-4:0]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O time Chapecoense esta na posicao: {times.index('Chapecoense')+1}º')

