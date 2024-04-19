# Usando função lambda para retornar a chave de ordenação do dicionário

cursos = []

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    for lines in file:
        language, category = lines.rstrip().split(",")
        curso = {}
        curso["language"] = language
        curso["category"] = category
        cursos.append(curso)

for curso in sorted(cursos,key= lambda course: curso["language"]): # -> Usando função lambda
    # -> Para organizar um dicionário é preciso passar o valor da chave e usamos uma função para ter esse valor.
    print(f"{curso['language']}-{curso['category']}")