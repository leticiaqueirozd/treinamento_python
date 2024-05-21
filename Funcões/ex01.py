def valor_gorjeta(conta):
    gorjeta = conta * 0.10
    print(f'O valor da gorjeta é de: R${gorjeta:.2f}')

conta = float(input('Digite o valor da conta: '))
valor_gorjeta(conta)