def contrario(num):
    return int(str(num)[::-1])

num = int(input('Insira um numero: '))

contrario_num = contrario(num)
print(f"{num} -> {contrario_num}")