# Desafio três
'''Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
    Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$
    0,35 para viagens mais longas.'''
'''Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
    salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
    15%'''


# primeiro programa:
distancia = float(input('Digite em KM qual a distância a ser percorrida:\n'))
if distancia > 0 and distancia <= 200:
    calculo200 = distancia * 0.50
    print(f"O valor da passagem é de: R${calculo200:.2f}")
elif distancia > 200:
    calculo035 = distancia * 0.35
    print(f"O valor da passagem é de: R${calculo035:.2f}")
else:
    print('Distância negativa, por favor insira outra distância.')

# Segundo programa:
salario = float(input('Digite o valor atual do seu salário:\n'))
if salario > 1250:
    aumento = float(salario*10)/100
    print(f"O seu aumento será de R${aumento}")
    print(f"E seu salário com o aumento será igual a: R${salario+aumento:.2f}")  
elif salario <= 1250 and salario > 0:
    aumento15 = float(salario*15)/100
    print(f"Seu aumento será de R${aumento15}") 
    print(f"Seu salário com o aumento será igual a: R$ {salario+aumento15:.2f}")
else:
    print('Valor inválido.') 
 