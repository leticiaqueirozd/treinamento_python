class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacoes(self):
        print(f"{self.marca} {self.modelo},")


class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def informacoes(self):
        super().informacoes()
        print(f"{self.numero_portas} portas")


class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def informacoes(self):
        super().informacoes()
        print(f"{self.cilindradas} cilindradas")


c = Carro('Fiat', 'Uno', 4)
c.informacoes()  
m = Moto('Honda', 'Biz', 125)
m.informacoes() 
