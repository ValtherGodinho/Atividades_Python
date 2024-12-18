import random
print('Vamos jogar de acertar o numero.')
n = random.randint(0, 5)
m = int(input('Digite um numero de 0 a 5: '))
print('Você Venceu' if n == m else 'Você Perdeu')
print('O correto era  o numero:{} '.format(n))

        
