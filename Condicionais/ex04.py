pares = 0
impares = 0

for i in range(10):
    numero = int(input(f'Digite o número {i + 1}: '))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Quantidade de pares é de: {pares} \n Quantidade de ímpares é de: {impares}')