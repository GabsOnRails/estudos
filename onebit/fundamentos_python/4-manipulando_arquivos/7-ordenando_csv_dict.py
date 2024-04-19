# Ordenando o dicionário dentro da lista através de chaves.

cursos = []

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    for lines in file:
        language, category = lines.rstrip().split(",")
        curso = {}
        curso["language"] = language
        curso["category"] = category
        cursos.append(curso)

# Funções para retornar o valor que será usado na ordenação do dicionário.
def get_language(curso): # -> Dicionário "curso"
    return curso["language"] # -> Chave "language"

def get_category (curso): # -> Dicionário "curso"
    return curso["category"] # -> Chave "category"

for curso in sorted(cursos,key=language): # -> Podemos usar o "reverse=True" para ordenar em forma decrescente.
 # -> Para organizar um dicionário é preciso passar o valor da chave e usamos uma função para ter esse valor.
    print(f"{curso['language']}-{curso['category']}")