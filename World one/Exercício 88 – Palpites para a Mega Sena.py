from random import randint
lista = list()
jogos = list()
print('JOGA NA MEGA SENA')
cont = 0
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    
print(f'Os numeros sorteados foram {jogos}')
    
    
        