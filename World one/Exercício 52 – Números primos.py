# Solicita que o usuário digite um número
num = int(input('Digite um número: '))

# Considera que o número é primo até que se prove o contrário
primo = True

# Verifica se o número é menor que 2 (não é primo)
if num < 2:
    primo = False
else:
    # Verifica se o número tem divisores além de 1 e ele mesmo
    for c in range(2, num):
        if num % c == 0:  # Se for divisível por c, não é primo
            primo = False
            break

# Exibe se o número é primo ou não
if primo:
    print(f'O número {num} é primo.')
else:
    print(f'O número {num} não é primo.')
