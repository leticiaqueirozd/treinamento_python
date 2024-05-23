class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
    def cumprimentar(self):
        print(f" nome: {self.nome} \n idade: {self.idade} \n sexo: {self.sexo}")
        
p1 = Pessoa('Alice', 30, 'Feminino')
p1.cumprimentar()