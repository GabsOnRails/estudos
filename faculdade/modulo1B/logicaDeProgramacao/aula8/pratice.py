# Desenvolva um algoritmo que some cada valor de uma posição da matriz com 2. Mostre o resultado na tela.
# Dica 1: soma=soma+2
# Dica 2: Use mais dois laços para mostrar na tela o resultado.

import random
n_linhas = int(input("Digite o número de linhas: "))
n_colunas = int(input("Digite o número de colunas: "))


def matriz(n_linhas, n_colunas):
    matriz = [] # Matriz
    linha = [] # Linha

    while len(matriz) != n_linhas: # Quando o número de elementos da matriz(linhas) forem diferentes da quantidade máxima definida pelo usuário, ele ficará rodando.
        n = random.randint(0,99) # Utilizei random para adicionar os valores
        print(n)
        soma = n+2
        linha.append(soma) # Adiciono n à linha

        if len(linha) == n_colunas: # Se a quantidade de elementos for igual à quantidade de colunas definida pelo usuário :
            matriz.append(linha) # Adiciono a linha à matriz
            linha = [] # E zero a "linha" para adicionar outra à matriz
    return matriz # Retorno a mesma


print(matriz(n_linhas,n_colunas))