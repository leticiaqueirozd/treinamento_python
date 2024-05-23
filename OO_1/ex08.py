class FormaGeometrica:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        pass


class Retangulo(FormaGeometrica):
    def calcular_area(self):
        return self.base * self.altura


class Triangulo(FormaGeometrica):
    def calcular_area(self):
        return (self.base * self.altura) / 2

r = Retangulo(5, 10)
print(r.calcular_area()) 

t = Triangulo(5, 10)
print(t.calcular_area())
