def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista) - 1 

    while baixo <= alto:
        media = (baixo+alto) / 2 # -> Igual a n/2, sempre pegará o item do meio, pois arrendonda.
        meio = int(media) # -> Precisei converter o float em int para conseguir fazer a iteração.
        chute = lista[meio] # -> lista[2] Literalmente o meio. Mas retornar o índice.
        if chute == item:
            return meio # -> Retorna o número do meio.
        if chute > item:
            alto = meio -1 # Retorna o indíce 1 ou 0. Conta será o índice depois.
        else:
            baixo = meio + 1 # Retorna o índice 3 ou 4.
    return None
minha_lista = [1,3,5,7,9]

print(pesquisa_binaria(minha_lista,7)) # -> O resultado retorna o número do índice, exemplo 9 = 4

'''
Uma forma de deixar mais interessante é colocar a lista com números aleatórios e
o "item" com um input.

'''