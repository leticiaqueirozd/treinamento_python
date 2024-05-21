valor_de_mercadoria = float(input("Digite o valor total das mercadorias: "))

if valor_de_mercadoria < 500:
    print("Tá salvo! Sem imposto")
else:
    print("O valor do imposto é de : ", ((valor_de_mercadoria - 500) * 0.5))