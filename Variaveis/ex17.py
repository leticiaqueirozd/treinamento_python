valor_casa = float(input('Digite o valor da casa a comprar: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = int(input('Digite o valor de anos a pagar: '))

meses = anos * 12
prestacao = valor_casa / meses 
limite = salario * 0.3

if prestacao <= limite:
    print(f'Aprovado! O valor da prestação é de: R${prestacao:.2f}')
else:
    print('O empréstimo NÃO foi aprovado.')