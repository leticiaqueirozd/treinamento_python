dias = float(input("Quantos dias foram rodados pelo cliente? "))
km = float(input("Quantos km foram rodados pelo cliente? "))

valor_dias = dias * 90
valor_km = (km - 100) * 12

if km < 100:
    print("O valor total a ser pago é de: R$", valor_dias)
else:
    print("O valor total a ser pago é de: R$", float(valor_dias + valor_km))
