import random

def lista_vazia(lista):
    return len(lista) == 0

def preencher_lista_quantidade(lista, quantidade):
    if lista_vazia(lista):
        lista.extend(random.randint(1, 100) for _ in range(quantidade))

minha_lista = []
numeros = int(input('Insira uma quantidade de valores para a lista: '))

preencher_lista_quantidade(minha_lista, numeros)
print(f"Lista preenchida com mais {numeros} valores aleatórios:", minha_lista)