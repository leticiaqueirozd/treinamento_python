def funcao_pn(num):
    if num > 0:
        return 'P'
    elif num <= 0:
        return 'N'

num = int(input('Insira um valor: '))
resultado = funcao_pn(num)
print(resultado)