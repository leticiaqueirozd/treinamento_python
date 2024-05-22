def media_idade(idades):
    if idades > 0 and idades < 25:
        return 'jovem'
    elif idades > 26 and idades < 60:
       return 'adulta'
    elif idades > 60:
        return 'idosa'

turma = int(input('Insira quantas pessoas tem a turma: '))
faixa_etaria = []

for i in range(turma):
    idade = int(input(f"Digite a idade da pessoa {i+1}: "))
    faixa_etaria.append(idade)
    
idades = sum(faixa_etaria) / turma

media_das_idades = media_idade(idades)

print(f"A média de idade da turma é {idades:.2f}, classificada como turma {media_das_idades}.")

