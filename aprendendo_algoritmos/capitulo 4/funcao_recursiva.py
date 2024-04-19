# Escrever uma função recursiva que conte o número de itens de uma lista

lista = []

# Adicionando valores a lista
criar_lista = int(input("Quantos números deseja adicionar a lista: "))
for x in range(0,criar_lista):
     numero = float(input("Digite o número: ")) # -> Float aceita apenas um ponto. ex 12454.45
     lista.append(numero)

'''
Algoritmo retirado do livro
'''

def conta(lista):
     if lista == []:
          return 0
     return 1 + conta(lista[1:]) # -> Isso irá funcionar como um for e ficará em loop até o último item.

# Condicional para verificar a forma correta das palavras. 
if len(lista) > 1:
     palavra = "têm"
     palavra2 = "itens"
else:
     palavra = "tem"
     palavra2 = "item"

print(f"A lista {palavra} {conta(lista)} {palavra2}.")

