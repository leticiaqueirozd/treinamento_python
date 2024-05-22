import random

def lista_vazia(lista):
    return len(lista) == 0

def preencher_lista(lista):
    if lista_vazia(lista):
        lista.extend(random.randint(1, 100) for _ in range(5))

minha_lista = []

preencher_lista(minha_lista)
print("Lista com 5 valores aleatórios: ", minha_lista)      

def ordenar_lista_decrescente(lista):
    lista.sort(reverse=True)

ordenar_lista_decrescente(minha_lista)
print("Lista ordenada de forma decrescente: ", minha_lista)