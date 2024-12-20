print('O programa só vai parar quando o usuário digitar o valor 999')

soma = 0
while True:  # Loop infinito; só sai quando chamamos "break"
    try:
        # Solicita a entrada do usuário e tenta converter para inteiro
        x = int(input('Digite um número inteiro: '))
        
        if x == 999:  # Condição para sair do loop
            break  # Sai do loop se o usuário digitar 999
        
        soma += x  # Soma o número válido à variável soma
        print(f'A soma dos números digitados é {soma}')
    
    except ValueError:  # Captura o erro de entrada inválida
        print('Entrada inválida! Por favor, digite apenas números inteiros.')

print('FIM')
