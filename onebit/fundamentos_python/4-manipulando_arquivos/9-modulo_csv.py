'''
Usando o módulo CSV, dessa maneira o título da tabela csv não irá aparecer no print.
Esse mesmo título precisa ser passado quando for adicionar as informações no dicionário criado,
no meu caso o título está como "language,category".
'''

# importando módulo
import csv

cursos = []

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for linhas in reader:
        cursos.append({"language":linhas['language'],"category":linhas['category']})
        # Aqui precisamos passar o parâmetro que está na tabela CSV, caso contrário irá dar erro.

for curso in sorted(cursos,key=lambda curso: curso ['language']):
    print(f"{curso['language']}-{curso['category']}")
