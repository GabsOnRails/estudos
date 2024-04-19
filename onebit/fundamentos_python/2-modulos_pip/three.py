# Terceiro exercício:
"""
Escreva um programa em Python para verificar se uma string contém apenas um determinado
conjunto de caracteres (neste caso, a-z, A-Z e 0-9).

"""
# Importando módulo
import re

# Criando variáveis:
frase1 = input("Digite uma frase:\n")

# Criando algoritmo para verificar o conteúdo da string
padrao1 = re.compile("[a-z]")
padrao2 = re.compile("[A-Z]")
padrao3 = re.compile("[0-9]")

# Criando verificação e resultados
verificar1 = padrao1.findall(frase1)
verificar2 = padrao2.findall(frase1)
verificar3 = padrao3.findall(frase1)
# Resultados
resultado1 = len(verificar1)
resultado2 = len(verificar2)
resultado3 = len(verificar3)

# Tratando os resultados
print(f"As letras minúsculas são {resultado1}, sendo elas: {verificar1}")
print(f"As letras  maiúsculas são {resultado2}, sendo elas: {verificar2}")
print(f"Os números são {resultado3}, sendo eles: {verificar3}")

'''
outra forma de resolver:
def teste(frase):
    padrao = re.compile(r'^a-zA-Z0-9')
    resultado = padrao.findall(frase)
    print(resultado)
frase = input('Digite uma frase: ')
teste()
'''