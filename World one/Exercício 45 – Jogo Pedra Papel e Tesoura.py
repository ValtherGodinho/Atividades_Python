from random import randint
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Opções do jogo
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)  # Computador escolhe uma jogada aleatória

# Menu para o jogador
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

# Entrada do jogador
jogador = int(input('Qual é a sua jogada? '))

# Separador visual
print('-=' * 11)

# Mostrar as escolhas
if 0 <= jogador <= 2:  # Verifica se a jogada do jogador é válida
    print(f'Computador jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-=' * 11)

    # Determinar o vencedor
    if computador == jogador:
        print('EMPATE!')
    elif (jogador == 0 and computador == 2) or \
         (jogador == 1 and computador == 0) or \
         (jogador == 2 and computador == 1):
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
else:
    print('JOGADA INVÁLIDA! Tente novamente.')
    
