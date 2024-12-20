soma = contagem = 0
while True:
    try:
        x = int(input(' Digite um numero inteiro: '))
        if x == 999:
            break
        soma += x
        contagem += 1
    except ValueError:  # Captura o erro de entrada inválida
        print('Entrada inválida! Por favor, digite apenas números inteiros.')
print('FIM!')
print(f'foram digitados: {contagem} numeros e sua soma é {soma}')
