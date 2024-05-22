def inverter_nome(nome):
    nome_invertido = nome.upper()[::-1]
    return nome_invertido

nome = input("Digite seu nome: ")

nome_invertido = inverter_nome(nome)
print("Seu nome invertido em letras maiúsculas é:", nome_invertido)
