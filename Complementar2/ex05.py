def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

resultado = mdc(a, b)

print(f'O M.D.C entre {a} e {b} é {resultado}')