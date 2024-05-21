def seq_numeros(num):
    for i in range(1, num + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print('\n')
num = int(input('Digite um valor: '))
seq_numeros(num)