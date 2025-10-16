# Utilizando o loop for para percorrer um vetor inteiro



# array = [1,2,3,4,6,7,8,10] # 0 ao 7 

# for num in array:
#     print(f"Aluno de número {num}")

# print(array[1])

# Exemplo da aula

numeroMatricula = 1
alunos = []


for estudantes in range(5):
    alunoNovo = input(f"Digite o nome do aluno {numeroMatricula} de 5: ")
    alunos.append(alunoNovo)
    numeroMatricula += 1
   



print(f"Lista de alunos: {alunos}")
