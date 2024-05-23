class Figura:
    def __init__(self, cor, preenchida):
        self.cor = cor
        self.preenchida = preenchida

    def informacoes(self):
        print(f"Cor: {self.cor}, Preenchida: {self.preenchida},")


class Circulo(Figura):
    def __init__(self, cor, preenchida, raio):
        super().__init__(cor, preenchida)
        self.raio = raio

    def informacoes(self):
        super().informacoes()
        print(f"Raio: {self.raio}")


class Quadrado(Figura):
    def __init__(self, cor, preenchida, lado):
        super().__init__(cor, preenchida)
        self.lado = lado

    def informacoes(self):
        super().informacoes()
        print(f"Lado: {self.lado}")


c = Circulo('Azul', True, 5)
c.informacoes()  

q = Quadrado('Vermelho', False, 10)
q.informacoes() 
