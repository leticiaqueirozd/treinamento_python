class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

class Turma:
    def __init__(self, alunos):
        self.alunos = alunos

    def media(self):
        total_notas = 0
        total_alunos = 0

        for aluno in self.alunos:
            total_notas += sum(aluno.notas)
            total_alunos += len(aluno.notas)

        return total_notas / total_alunos if total_alunos > 0 else 0

a1 = Aluno('Alice', [8, 7, 6])
a2 = Aluno('Bob', [9, 8, 7])
turma = Turma([a1, a2])
print(turma.media())
