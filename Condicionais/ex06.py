quantidade_turmas = int(input('Digite a quantidade de turmas: '))
quantidade_alunos = int(input('Digite a quantidade de alunos: '))

media_alunos_por_turma = quantidade_alunos / quantidade_turmas

if media_alunos_por_turma > 41:
    print('O limite de 40 alunos por turma foi excedido')
else:
    print(f'A média de alunos por turma é de: {media_alunos_por_turma}')