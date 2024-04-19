# Criando listas
lista_de_jogos = ["Risk of Rain 2", "Children of morta", "OverCooked 2",
                  "For the King 1"]

print(len(lista_de_jogos)) # 1 - Tamanho da lista.
print(lista_de_jogos.index("For the King 1")) # 2 - Recuperar o índice de um item através do nome.
lista_de_jogos.append("Into the Breach") # 3 - Adicionar item ao FINAL da lista.
lista_de_jogos.sort() # 4 - Ordenar lista.
jogos_zerados = lista_de_jogos.copy() # 5 - Copiar itens de uma lista para outra.
jogos_zerados.remove("Children of morta") # 6 - Removendo itens. Remove apenas um item por vez :/
print(jogos_zerados)
jogos_zerados.clear() # 7 - Remove todos os itens da lista.
print(jogos_zerados)

# Além desses metódos podemos utilizar também o slice nas listas.