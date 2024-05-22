def gerador_tabuada(numero):
    print(f"Tabuada do {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")

numero = int(input("Digite UM número entre 1 e 10 para ver a tabuada: "))

if numero < 1 or numero > 10:
    print("Insira um número entre 1 e 10.")
else:
    gerador_tabuada(numero)
