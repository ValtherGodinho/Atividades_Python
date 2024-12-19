r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# Verificando se os segmentos podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!', end=' ')
    
    # Verificando o tipo de triângulo
    if r1 == r2 == r3:
        print('O triângulo é EQUILÁTERO.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo é ISÓSCELES.')
    else:
        print('O triângulo é ESCALENO.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')
