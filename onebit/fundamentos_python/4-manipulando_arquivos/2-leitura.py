# Como ler arquivos

'''
A opção "open" tem três tipos de argumentos, sendo eles:
open("nome do arquivo","modo de abertura","enconding") -> o encoding diz
respeito sobre a compreensão do texto, como caracteres especiais(utf-8).
'''

with open("dados/nomes.txt","r",encoding="utf-8") as file:
    for line in file:
        print(f"Olá, {line.rstrip()}") # -> rstrip serve para remover linhas vazias