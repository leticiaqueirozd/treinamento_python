def vertical(nome):
    for letra in nome:
        print(letra.upper())

nome = input("Digite seu nome: ")

print("Nome na vertical:")
vertical(nome)
