cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['media'] = float(input(f'Media de {cadastro["nome"]}: '))
if cadastro['media'] >= 7:
    cadastro['situacao'] = 'Aprovado'
elif 5 <= cadastro['media'] < 7:
    cadastro['situacao'] = 'Recuperacao'
else:
    cadastro['situacao'] = 'Reprovado'

for k, v in cadastro.items():
    print(f' - {k} é igual a {v}')
    
    
    
    
