def lista_sem_repetidos(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    lista_sem_repetidos = list(conjunto1.union(conjunto2))

    return lista_sem_repetidos

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

lista_resultante = lista_sem_repetidos(lista1, lista2)
print("Lista resultante sem elementos repetidos:", lista_resultante)
