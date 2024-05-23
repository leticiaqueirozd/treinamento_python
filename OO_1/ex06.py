class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def informacoes(self):
        print(f"Nome: {self.nome}, Espécie: {self.especie}")


class Mamifero(Animal):
    def __init__(self, nome, especie, cor_pelo):
        super().__init__(nome, especie)
        self.cor_pelo = cor_pelo

    def informacoes(self):
        super().informacoes()
        print(f"Cor do pelo: {self.cor_pelo}")


class Reptil(Animal):
    def __init__(self, nome, especie, tipo_escama):
        super().__init__(nome, especie)
        self.tipo_escama = tipo_escama

    def informacoes(self):
        super().informacoes()
        print(f"Tipo de escama: {self.tipo_escama}")

a = Animal('Rex', 'Cachorro')
a.informacoes() 

m = Mamifero('Rex', 'Cachorro', 'Marrom')
m.informacoes()

r = Reptil('Snake', 'Cobra', 'Lisas')
r.informacoes() 
