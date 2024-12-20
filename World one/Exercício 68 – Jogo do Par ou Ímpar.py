import random
vitoria = 0
while True:
    y = str(input('Escolher PAR OU IMPAR: [P/I]').upper().strip()[0])
    if y not in ['P', 'I']:
        print('Opção inválida! Escolha "P" para Par ou "I" para Ímpar.')
        continue
    x = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    soma = x + computador
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print(f'Voce escolheu {x} e o computador escolheu {computador}.A soma é {soma}, que é {resultado}. ')
    if x == resultado:
        print('Voce ganhou esta rodada!')
        vitoria += 1
    else:
        print('Voce perdeu!')
        break
print(f'Você teve {vitoria} vitórias consecutivas.')


    

