while True:
    try:
        x = int(input('Quer ver a tabuada de que numero: '))
        if x <= 0:
            raise ValueError("O número deve ser positivo!")
        for i in range (0 , 11, 1):
            m = i * x
            print(f'{x} x {i} = {m}')
    except ValueError:  # Captura o erro de entrada inválida
        print('Entrada inválida! Por favor, digite apenas números inteiros.')
            

