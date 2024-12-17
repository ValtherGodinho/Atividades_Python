frase = str(input('Digitar a frase: ')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A posicao que a letra aparece pela primeira vez na posicao: {}'.format(frase.find('A')+1))
print('A posicao que a letra aparece pela ultima vez na posicao {}'.format(frase.rfind('A')+1))



