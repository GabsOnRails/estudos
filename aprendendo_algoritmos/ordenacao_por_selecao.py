# Esse algoritmo tem como objetivo fazer uma ordenação de uma lista
# PS: ESSE ALGORITMO É GENIAL!!!!!

# O algoritmo é divido em duas partes:
# primeira parte do algoritmo:
def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor)) # -> remove o menor item no 'arr' e o adiciona em "novo_arr"
    return novo_arr


# Função para encontrar o menor valor
def busca_menor(arr):
    menor = arr[0] # 
    menor_indice = 0 # assume o menor número após o for.
    for numero in range(1, len(arr)): # começa com o índice 1 para sempre comparar com o índice 0.
        if arr[numero] < menor: # -> se o primeiro número for menor que o número de índice 0.
            menor = arr[numero] # -> menor número passa a ser arr[1] - vezes que o 'for' foi executado.  
            menor_indice = numero # -> menor indice é o número |for| que foi retornado.
    return menor_indice

print(ordenacao_por_selecao([4,5,3,6,2,10]))