nome = str(input('Digite o nome: ')).strip()
frase = nome.split()
print('O primeiro nome é {} e o ultimo nome é {} '.format(frase[0], frase[len(frase) - 1]))

