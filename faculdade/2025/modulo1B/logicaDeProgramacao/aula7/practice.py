# escreva um algoritmo que receba 5 notas de 5 alunos diferentes e some as notas e as medias da turma.

notas = 0
alunos = 1

# algoritmo para armazenar as notas de cada aluno
for a in range(5):
    notasAlunos = float(input(f"Digite a nota do aluno {alunos}: "))
    notas += notasAlunos
    alunos += 1

mediaSala = notas/5
print(f"A media da sala é {mediaSala:.2f}")


