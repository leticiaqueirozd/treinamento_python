class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def informacoes(self):
        pass

class ClientePessoaFisica(Cliente):
    def __init__(self, nome, idade, cpf):
        super().__init__(nome, idade)
        self.cpf = cpf

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CPF: {self.cpf}")

class ClientePessoaJuridica(Cliente):
    def __init__(self, nome, idade, cnpj):
        super().__init__(nome, idade)
        self.cnpj = cnpj

    def informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, CNPJ: {self.cnpj}")

pf = ClientePessoaFisica('Alice', 30, '123.456.789-00')
pf.informacoes()

pj = ClientePessoaJuridica('Empresa', 10, '123.456.789/0001-00')
pj.informacoes()

c = Cliente('Alice', 30)
c.informacoes() 
