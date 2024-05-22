def escada_invertida(nome):
    escada = ''
    for letra in nome:
        escada += letra.upper()
        print(escada)

nome = input("Digite seu nome: ")

print("Nome em formato de escada invertida:")
escada_invertida(nome)
