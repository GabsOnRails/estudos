# Encontre o maior número da lista


lista = []

# Adicionando valores a lista
criar_lista = int(input("Quantos números deseja adicionar a lista: "))
for x in range(0,criar_lista):
     numero = float(input("Digite o número: ")) # -> Float aceita apenas um ponto. ex 12454.45
     lista.append(numero)

# # Condição para caso a lista esteja vazia.
# if len(lista) == 0:
#     print("Lista vazia!")

# # Lógica do algoritmo
# def maior_numero(lista):
#     while len(lista) > 0: 
#         y = lista[0] # -> Usando o primeiro número como base para comparação.
#         for x in lista:
#             numero = x
#         if y > x: # -> Para fazer o menor número basta trocar essa condição para 'if y < x".
#             print(f"O maior número é {y}") # -> e trocar as frases de maior para menor.
#             break
#         else:
#             print(f"O maior número é {x}")
#             break

# maior_numero(lista)

'''
Correção do livro
'''
def maximo(lista):
    if len(lista) == 2: # -> Precisa de dois número para comparar.
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:]) # -> 1 para frente, pois só cai nessa condição senão retornar o índice 1.
    return lista[0] if lista[0] > sub_max else sub_max # -> Comparando o índice 0 com os demais da lista.

print(f"O maior número é {maximo(lista)}")
