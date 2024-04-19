'''
Comecarei a organizar os arquivos por cápitulo, assim ficará mais fácil.
'''

# Função soma -> Soma o primeiro valor com o resultado da soma dos demais valores.

lista = []

# # Função que realiza o cálculo.
# def calculo(lista):
#     primeiro=lista[0]
#     restantes = lista[1:]
#     total = 0
#     for x in restantes:
#         total += x
#     soma = primeiro+total
#     print(f"O resultado da soma da lista é: {soma}")

# # Lógica do algoritmo
    
numerador = int(input("Quantos números deseja adicionar a lista: "))
for x in range(0,numerador):
     numero = float(input("Digite o número: "))
     lista.append(numero)
     
# if len(lista) == 0:
#         print("Lista vazia!")
# else:
#      calculo(lista)

'''
Correção exercício
'''

def soma(lista):
    if lista == []:
        return 0
    return lista[0] + soma(lista[1:])

print(soma(lista))

