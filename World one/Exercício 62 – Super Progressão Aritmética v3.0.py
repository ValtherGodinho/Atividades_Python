print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
while True:
    mais_termos = int(input('Gostaria de mais termos? Quantos? (Digite 0 para parar): '))
    if mais_termos == 0:
        break
    for _ in range(mais_termos):
        print('{} -> '.format(termo), end='')
        termo += razao
    print('FIM')

