import random

def lista_vazia(lista):
    return len(lista) == 0

def preencher_lista(lista):
    if lista_vazia(lista):
        lista.extend(random.randint(1, 100) for _ in range(5))

minha_lista = []

preencher_lista(minha_lista)
print("Lista com 5 valores aleatórios:", minha_lista)      
        