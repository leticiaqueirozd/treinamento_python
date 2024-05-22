def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso == 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03  # 3% de multa
        juros = valor_prestacao * (0.001 * dias_atraso)  # 0.1% de juros por dia de atraso
        valor_total = valor_prestacao + multa + juros
        return valor_total

def imprimir_relatorio(total_prestacoes, total_valor):
    print("\nRelatório do dia:")
    print("Quantidade de prestações pagas:", total_prestacoes)
    print("Valor total recebido:", total_valor)

total_prestacoes_dia = 0
total_valor_dia = 0

while True:
    valor_prestacao = float(input("\nDigite o valor da prestação (ou 0 para sair): R$"))
    if valor_prestacao == 0:
        break

    dias_atraso = int(input("Digite o número de dias em atraso: "))

    valor_a_pagar = valorPagamento(valor_prestacao, dias_atraso)

    print("Valor a ser pago: R$", valor_a_pagar)

    total_prestacoes_dia += 1
    total_valor_dia += valor_a_pagar

imprimir_relatorio(total_prestacoes_dia, total_valor_dia)
