# Listas permitem vários tipos de dados no mesmo lugar.

# Criando listas
lista_de_jogos = ["Risk of Rain 2", "Children of morta", "OverCooked 2",
                  "For the King 1"] 

wishlist = ["Notebook Gamer",3000,
            "Dois pares de tênis", 500,
            "Guarda Roupa",1000]

# Prints
print(lista_de_jogos)

# Na lista podemos utilizar as propriedas de string como o slice.
print(lista_de_jogos[-1]) # Apresentar sempre o último item. 
                          # É uma boa prática usar o -1 ao invés da indexação da esquerda para direita.

print(lista_de_jogos[1:]) # Trazer a partir de determinando índice.

divisoria = "="
print(divisoria*100)

print(wishlist)
print(wishlist[-2]) # Trazendo o penúltimo item, sempre usando o índice negativo.
print(wishlist[::-1]) # Inverter a string