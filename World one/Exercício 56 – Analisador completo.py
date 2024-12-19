# Inicializando variáveis
soma_idades = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

# Loop para ler os dados de 4 pessoas
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()
    
    # Soma das idades para calcular a média
    soma_idades += idade

    # Verificar o homem mais velho
    if sexo == 'M' and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        homem_mais_velho = nome

    # Contar mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

# Calculando a média de idade
media_idade = soma_idades / 4

# Exibindo os resultados
print(f'\nA média de idade do grupo é de {media_idade:.1f} anos.')
if homem_mais_velho:
    print(f'O homem mais velho é {homem_mais_velho}, com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo, há {mulheres_menos_20} mulher(es) com menos de 20 anos.')
