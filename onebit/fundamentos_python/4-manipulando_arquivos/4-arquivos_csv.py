# Realizando a leitura de arquivos CSV

with open("dados/cursos.csv","r",encoding="utf-8") as file:
    for line in file:
        # -> declarando o nome dos dois valores 
        language, category = line.rstrip().split(",") 
        print(f"{language}-{category}")