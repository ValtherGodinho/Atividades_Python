sal = float(input('Qual é o salario do funcionario? '))
if sal <= 1250:
    n = sal + (sal * 15 / 100)
else:
    n = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(sal, n))

