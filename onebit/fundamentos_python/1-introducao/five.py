# Desafio 
'''
Escreva uma função Python que receba uma string e conte o 
número de letras maiúsculas e minúsculas desta string.

Escreva uma função Python para imprimir 
os números pares e ímpares em duas listas separadas para cada uma. 

'''
# Módulos importados e declarando variáveis globais
import re
divisoria = "="

# Contar letras maiúsculas e minúsculas
frase = input('Digite uma frase:\n')
# Usando Regx para achar as maiúsculas 
busca_maiusculas = re.compile('[A-Z]')
lista_maiusculas = busca_maiusculas.findall(frase)
quantidade_letrasma = len(lista_maiusculas)
print(f"As letras maiúsculas são {quantidade_letrasma}, sendo elas: {lista_maiusculas}")
# Usando regx para achar as minúsculas
busca_minusculas = re.compile('[a-z]')
lista_minisculas = busca_minusculas.findall(frase)
quantidade_letrasmi = len(lista_minisculas)
print(f"As letras minúsculas são {quantidade_letrasmi}, sendo elas: {lista_minisculas}")
print(divisoria*100)
    
# Encontrar números pares e impáres

# criando listas para receber os respectivos números
lista_numeros = []
lista_par = []
lista_impar = []

# Criando variável que recebe a quantidade de número que serão adicionados.
quantidade = int(input('Digite a quantidade de números que quer adicionar:\n'))

# Criando função
def par_impar(quantidade):
    for x in range(quantidade): # Laço for para adicionar os números na lista
        qtd_numeros = int(input('Digite o número:\n'))
        lista_numeros.append(qtd_numeros)
    for numeros in lista_numeros: # Laço for para separar os números pares dos impáres
        if numeros % 2 == 0:
            lista_par.append(numeros)
        else:
            lista_impar.append(numeros)      
# Prints
par_impar(quantidade)
print(f"Números pares são: {lista_par}")
print(f"Números impáres são: {lista_impar}")
        

