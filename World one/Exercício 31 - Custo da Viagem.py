dis = float(input('Qual é a distancia de sua viagem? '))
print('Voce esta  prestes a comecar uma viagem de {}Km'.format(dis))
p = dis * 0.5 if dis <= 200 else dis *0.45
print('E o preco da sua passagem sera de R${:.2f}'.format(p))


