def escada(nome):
    tamanho = len(nome)
    for i in range(tamanho, 0, -1):
        print(nome[:i].upper())

nome = input("Digite seu nome: ")

print("Nome em formato de escada:")
escada(nome)
