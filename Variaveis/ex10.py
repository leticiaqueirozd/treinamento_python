def montante(capital, taxa, periodos):
    formula = capital * (1 + taxa)**periodos
    return formula

capital_inicial = 1000.00
taxas = 0.0002
dias = 35

montante_final = montante(capital_inicial, taxas, dias)
print(f'O montante de Joãozinho será de R${montante_final:.2f}')