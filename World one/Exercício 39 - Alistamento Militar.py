from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento em {}'.format(ano))
    

