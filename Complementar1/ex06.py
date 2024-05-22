def fibonacci(num):
    fibonacci_series = [1, 1]

    for i in range(2, num):
        termo = fibonacci_series[i-1] + fibonacci_series[i-2]
        fibonacci_series.append(termo)

    return fibonacci_series[:num] 

num = int(input("Digite um valor para gerar a série de Fibonacci até o termo: "))

if num <= 0:
    print("Insira um valor maior que 0.")
else:
    serie_fibonacci = fibonacci(num)
    print("Série de Fibonacci até o", num, "º termo:", serie_fibonacci)
