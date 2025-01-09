listanum = []
maio = men = 0
for c in range(0 ,5):
    listanum.append(int(input(f'Digite um valor para a Posicao {c}: ')))
    if c == 0:
        maio = men = listanum[c]
    else:
        if listanum[c] > maio:
            maio = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {maio}')
print(f'O menor valor digitado foi {men}')
            