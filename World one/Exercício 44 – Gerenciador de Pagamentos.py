# Entrada de dados
preco = float(input('Digite o preço do produto: R$ '))
print('''Escolha a condição de pagamento:
[1] À vista dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (preço normal)
[4] Em 3x ou mais no cartão (20% de juros)''')

condicao = int(input('Escolha a opção de pagamento: '))

# Calculando o valor a ser pago com base na condição escolhida
if condicao == 1:
    # À vista dinheiro/cheque
    desconto = preco * 0.10
    preco_final = preco - desconto
    print(f'O valor a ser pago será R$ {preco_final:.2f}, com 10% de desconto.')
elif condicao == 2:
    # À vista no cartão
    desconto = preco * 0.05
    preco_final = preco - desconto
    print(f'O valor a ser pago será R$ {preco_final:.2f}, com 5% de desconto.')
elif condicao == 3:
    # Em até 2x no cartão
    print(f'O valor a ser pago será R$ {preco:.2f}, sem desconto ou juros.')
elif condicao == 4:
    # Em 3x ou mais no cartão
    juros = preco * 0.20
    preco_final = preco + juros
    print(f'O valor a ser pago será R$ {preco_final:.2f}, com 20% de juros.')
else:
    print('Opção inválida. Tente novamente.')
