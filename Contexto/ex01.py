class Livros:
    def __init__(self, titulo, autor, copias):
        self.titulo = titulo
        self.autor = autor
        self.copias = copias
        self.emprestados = []
    
    def emprestar(self, membro):
        if self.copias > 0:
            self.copias -= 1
            self.emprestados.append(membro)
            membro.livros_emprestados.append(self)
            self.infos_salvas(f'{membro.nome} pegou o livro {self.titulo} emprestado. Existem {self.copias} deste livro')
            return True
        else:
            return False
        
    def devolver(self, membro):
        if membro in self.emprestados:
            self.copias += 1
            self.emprestados.remove(membro)
            membro.livros_emprestados.remove(self)
            self.infos_salvas(f'{membro.nome} devolveu o livro {self.titulo}. Existem {self.copias} deste livro')
            return True
        else:
            return False
    
    def infos_salvas(self, mensagem):
        with open('log_biblioteca.txt', 'a') as arquivo:
            arquivo.write(f'{mensagem}\n')
        
class Membros:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.livros_emprestados = []

livro1 = Livros('Dom Casmurro', 'Machado de Assis', 2)
livro2 = Livros('O cortiço', 'Aluísio Azevedo', 1)
livro3 = Livros('Iracema', 'José de Alencar', 3)
livro4 = Livros('Memórias Póstumas de Brás Cubas', 'Machado de Assis', 2)
livro5 = Livros('O Guarani', 'José de Alencar', 1)
livro6 = Livros('O Alienista', 'Machado de Assis', 2)
livro7 = Livros('O Ateneu', 'Raul Pompeia', 1)
livro8 = Livros('Senhora', 'José de Alencar', 3)

membro1 = Membros('Lucas', 1)
membro2 = Membros('Ivson', 2)
membro3 = Membros('Felipe', 3)
membro4 = Membros('Jefferson', 4)

print(livro1.emprestar(membro1))
#True
print(livro1.emprestar(membro1))
#False
print(livro1.copias)
#1
print(livro1.devolver(membro1))
#True
print(livro1.copias)
#2
print(livro1.devolver(membro1))
# False
print(livro8.emprestar(membro1))
# True
print(livro8.emprestar(membro2))
# True
print(livro8.emprestar(membro3))
# True
print(livro8.emprestar(membro4))
# False
