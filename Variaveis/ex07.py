def funcao_bernardo(num):
    if num % 2 == 0:
        print("O número deve ser ímpar")
        
    x = (num + 1) // 2
    y = (num - 1) // 2
    
    return x**2, y**2

num = int(input('Digite um valor: '))

quadrado1, quadrado2 = funcao_bernardo(num)
print(f"{quadrado1} - {quadrado2} = {num}")
