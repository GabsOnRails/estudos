# Ordenando o arquivo CSV
 
cursos = [] # -> Criando lista vazia para adicionar os valores e orderná-los

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    for lines in file:
        languagens, courses = lines.rstrip().split(",") # -> Dois valores são declarados, pois a coluna de CSV contêm dois valores.
        cursos.append(f"{languagens} - {courses}")

for linhas in sorted(cursos): # -> Se usar a propriedade "reverse" após o parâmetro, a lista ficará em ordem decrescente
    print(linhas)