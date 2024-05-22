def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) // mdc(a, b)

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))

resultado = mmc(a, b)

print(f'O M.M.C entre {a} e {b} é {resultado}')