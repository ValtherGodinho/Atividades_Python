print("Sequência de Fibonacci v1.0")
n = int(input("Digite o número de termos que deseja exibir: "))

# Inicializando os dois primeiros termos
t1 = 0
t2 = 1
contador = 1

print(f"Os {n} primeiros termos da sequência de Fibonacci são:")

while contador <= n:
    if contador == 1:
        print(t1, end="")  # Primeiro termo
    elif contador == 2:
        print(f" - {t2}", end="")  # Segundo termo
    else:
        t3 = t1 + t2
        print(f" - {t3}", end="")  # Próximos termos
        # Atualizando os valores
        t1 = t2
        t2 = t3
    contador += 1
print()  # Para finalizar com uma nova linha

