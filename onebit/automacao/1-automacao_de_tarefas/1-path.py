# Usando a biblioteca pathlib (builtin)


from pathlib import Path


p1 = Path('dados','teste.txt') # -> Listando arquivo.
print(p1)

print(type(p1))
print(p1.name) # -> Retorna o nome do arquivo
print(p1.stem) # -> Retorna o que vem antes do ponto | nome do arquivo
print(p1.suffix) # -> Retorna o que vem depois do ponto | tipo do arquivo
print(p1.exists()) # -> Teste para ver se o arquivo existe | Retorna booleano

# Criando condicional para ler o conteúdo do arquivo
if p1.exists():
    with open(p1,'r',encoding='utf-8') as file:
        print(file.read())

p2 = Path('dados')
print(list(p2.iterdir())) # -> Serve para mostrar quais arquivos estão dentro do caminho passado