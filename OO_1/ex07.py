class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self):
        self.salario *= 1.10


class Programador(Funcionario):
    def aumentar_salario(self):
        self.salario *= 1.20


class Analista(Funcionario):
    def aumentar_salario(self):
        self.salario *= 1.30


p = Programador('Alice', 5000)
p.aumentar_salario()
print(p.salario) 

a = Analista('Bob', 5000)
a.aumentar_salario()
print(a.salario) 

f = Funcionario('Carlos', 5000)
f.aumentar_salario()
print(f.salario) 
