salario_inicial = float(input('Digite o salário inicial: '))
ano_contratacao = 1995
hoje = 2024

salario_atual = salario_inicial
aumento = 0.015

for ano in range(ano_contratacao + 1, hoje + 1):
    salario_atual += salario_atual * aumento
    aumento *= 2 
    
print(f'O salário atual em {hoje} é de R${salario_atual:.2f}')

