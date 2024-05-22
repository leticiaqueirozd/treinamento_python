def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area

base = float(input('Insira o tamanho da base do triangulo: '))
altura = float(input('Insira o tamanho da base do triangulo: '))

area = area_triangulo(base,altura)

print(f'A área desse triangulo é: {area}')