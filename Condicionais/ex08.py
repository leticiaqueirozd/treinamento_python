intervalo_1 = 0
intervalo_2 = 0
intervalo_3 = 0
intervalo_4 = 0

while True: 
    numero = int(input('Digite um valor: '))
    if numero < 0:
        break
    
    if 0 <= numero <= 25:
        intervalo_1 += 1
    elif 26 <= numero <= 50:
        intervalo_1 += 1
    elif 51 <= numero <= 75:
        intervalo_1 += 1
    elif 76 <= numero <= 100:
        intervalo_1 += 1

print(f'A quantidade de números positivos entre 0 e 25 é de: {intervalo_1}')
print(f'A quantidade de números positivos entre 26 e 50 é de: {intervalo_2}')
print(f'A quantidade de números positivos entre 51 e 75 é de: {intervalo_3}')
print(f'A quantidade de números positivos entre 76 e 100 é de: {intervalo_4}')


