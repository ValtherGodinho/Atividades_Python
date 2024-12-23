print('=== Cadastro de Pessoas ===')
continuar = 'S'
homens_maiores18 = 0  # Número de homens com mais de 18 anos
total_homens = 0      # Número total de homens cadastrados
mulheres_maiores20 = 0  # Número de mulheres com mais de 20 anos

while continuar == 'S':
    # Solicita e valida a idade
    while True:
        try:
            idade = int(input('Digite a idade: '))
            if idade < 0:
                print("Idade não pode ser negativa. Tente novamente.")
                continue
            break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")
    
    # Solicita e valida o sexo
    while True:
        sexo = input('Digite o sexo [M/F]: ').strip().upper()
        if sexo in ['M', 'F']:
            break
        else:
            print("Entrada inválida. Digite 'M' para masculino ou 'F' para feminino.")
    
    # Incrementa os contadores
    if idade >= 18 and sexo == 'M':
        homens_maiores18 += 1

    if sexo == 'M':
        total_homens += 1

    if idade > 20 and sexo == 'F':
        mulheres_maiores20 += 1

    # Pergunta se o usuário deseja continuar
    while True:
        continuar = input('Quer continuar? [S/N]: ').strip().upper()
        if continuar in ['S', 'N']:
            break
        else:
            print("Entrada inválida. Digite 'S' para sim ou 'N' para não.")

# Resultados finais
print('\n=== Resultados ===')
print(f'Número de homens com mais de 18 anos: {homens_maiores18}')
print(f'Número total de homens cadastrados: {total_homens}')
print(f'Número de mulheres com mais de 20 anos: {mulheres_maiores20}')
print('FIM')
