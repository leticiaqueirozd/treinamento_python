def calculo_divida(valor_inicial_divida, juro_mensal, pagamento_mensal):
    meses = 0
    total_pago = 0
    total_juros =  0
    saldo_devedor = valor_inicial_divida

    while saldo_devedor > 0:
        meses += 1
        juros_pago = saldo_devedor * juro_mensal
        total_juros += juros_pago
        saldo_devedor -= pagamento_mensal
        total_pago += pagamento_mensal

    return meses, total_pago, total_juros

valor_inicial_divida = float(input('Qual o valor inicial da dívida: R$'))
juro_mensal = float(input('Insira o juro mensal dividindo por 100: '))
pagamento_mensal = float(input('Qual será o valor pago? R$'))

meses_a_pagar, total_pago, total_juros = calculo_divida(valor_inicial_divida, juro_mensal, pagamento_mensal)

print("Meses para pagar a dívida:", meses_a_pagar)
print("Total pago:", total_pago)
print("Total de juros pago:", total_juros)
