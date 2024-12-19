n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while True:
    print('''Escolha uma opção:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    
    opcao = int(input('>>>>> Qual é a sua opção? '))
    
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O produto entre {n1} e {n2} é {produto}.')
    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}.')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}.')
        else:
            print(f'Os números {n1} e {n2} são iguais.')
    elif opcao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida. Tente novamente.')
