def fibonacci(num):
    sequ_fibonacci = [0, 1]
    
    for i in range(2, num + 1):
        termo = sequ_fibonacci[i - 1] + sequ_fibonacci[i - 2]
        sequ_fibonacci.append(termo)
    return sequ_fibonacci[:num]

num_seq = int(input('Digite o número de termos desejado: '))

resultado = fibonacci(num_seq)

print(f'A sequencia com {num_seq} numeros é {resultado}')