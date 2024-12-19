soma = 0
cont = 0
# Loop de 1 até 500
for c in range(1, 501, 2):
    # Verifica se o número é múltiplo de 3
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1

# Exibe o resultado
print(f'A soma dos múltiplos de 3 entre 1 e 500 é: {soma}')

