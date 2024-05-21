nomes = ['teclado_lidinho', 'Germa66', '1º_lugar', 'PlayerID', 'class']

for nome in nomes:
    if nome.isidentifier():
        print(f'{nome}: válido')
    else:
        print(f'{nome}: inválido')
