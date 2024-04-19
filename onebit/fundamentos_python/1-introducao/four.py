# Desafio 4
'''Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
   O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.
   
   Faça um programa que calcule a tabuada de um número,
   com valores iniciais e finais informados pelo usuário
'''

'''PS: para utilizar o beep no Ubuntu é necessário usar o comando "sudo modprobe pcspkr" previamente
ou então desativar o blacklist pcspkr e reiniciar o computador.'''
# importando módulos e declarando variáveis global
import time
import os
divisoria = "="

# Exercício 1:
contagem = 10
while contagem >= 0:
    print(contagem)
    contagem -= 1
    time.sleep(0.5)
os.system("beep -f 2000 -l 1500")
print(divisoria*50)

# Exercício 2:
numero_tabuada = int(input('Digite o número da tabuada:\n'))
limite_tabuada = int(input('Digite até qual número você quer que a tabuada vá:\n'))
print(divisoria*50)

inicio = 0
while inicio <= limite_tabuada:
    resultado_tabuada = numero_tabuada * inicio
    print(f"{numero_tabuada} * {inicio} é = {resultado_tabuada}")
    time.sleep(1.0)
    inicio += 1

