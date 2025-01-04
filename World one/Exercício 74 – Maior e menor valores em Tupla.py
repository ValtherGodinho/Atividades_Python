from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numeros} ', end='')
maior = menor = numeros[0]
for n in numeros:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f'O maior numero gerado foi: {maior} e o menor numero gerado foi: {menor}')
