nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media_geral = float((nota1 + nota2 + nota3) / 3)
media_223 = float((2 * nota1 + 2 * nota2 + 3 * nota3) / (2 + 2 + 3))
media_122 = float((1 * nota1 + 2 * nota2 + 2 * nota3) / (1 + 2 + 2))

print("A média geral é: ", media_geral) 
print("A média ponderada 223 é: ", media_223)
print("A média ponderada 122 é: ", media_122) 
