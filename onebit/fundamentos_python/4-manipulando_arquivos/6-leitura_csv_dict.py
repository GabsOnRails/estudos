# Incluindo um dict dentro da leitura do CSV

cursos = []

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    for lines in file:
        language, category = lines.rstrip().split(",")
        curso = {}
        curso["language"] = language
        curso["category"] = category
        cursos.append(curso)

for curso in cursos: # -> Precisa colocar "for 'dicionário' in 'lista'.."
    print(f"{curso['language']}-{curso['category']}")