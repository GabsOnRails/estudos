# Escrevendo arquivo CSV através do módulo csv

# Importando o módulo
import csv

nome = input("Digite o nome da linguagem que irá aprender\n")
category = input("Qual categoria a linguagem se encaixa?\n")

with open("dados/cursos.csv","a",encoding="utf-8") as file: # -> Criando arquivo que irá receber os dados.
    writer = csv.writer(file,lineterminator="\n") # -> Passando em qual local irá escrever "file" e o padrão "lineterminator".
    writer.writerow([nome.title(),category.title()]) # -> Indicando quais informações serão escritas e a ordem.