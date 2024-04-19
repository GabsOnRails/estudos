# Ordenando valores para leitura de dados

nomes = [] # -> Os nomes ficarão em uma lista para que possamos usar a propriedade "sorted".

with open("dados/nomes.txt","r",encoding="utf-8") as file:
    for line in file:
        nomes.append(line.rstrip())

for nome in sorted(nomes): # -> Ordenando a lista
    print(nome)
# print(nomes) -> Se usarmos dessa forma sairá entre [] e na mesma linha, vamos usar um for.
