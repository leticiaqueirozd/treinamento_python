def retangulo(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    for i in range(linhas):
        if i == 0 or i == linhas - 1:
            print('+' + '-' * (colunas - 2) + '+')
        else:
            print('|' + ' ' * (colunas - 2) + '|')

linhas = int(input("Digite um número entre 1 e 20 para linhas: "))
colunas = int(input("Digite um número entre 1 e 20 para colunas: "))

print("Desenho:")
retangulo(linhas, colunas)
