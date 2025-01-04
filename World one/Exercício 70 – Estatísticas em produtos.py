print('Estatísticas em produtos')
continuar = 'S'
contador = 0
while continuar == 'S':
    produto = str(input('nome do produto: '))
    preco = float(input('preco do produto: '))
    produto_barato = produto
    if produto < produto_barato:
        produto_barato = produto
    if preco < 1000:
        contador = contador + 1
    continuar = str(input('Deseja Continuar o cadastro? ').strip().upper())

print('O numero de produto que custam menos que R$1000: {} e o produto mais barato é {}'.format(contador, produto_barato))
