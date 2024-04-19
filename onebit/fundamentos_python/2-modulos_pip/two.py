# Segundo exercício de módulo

'''
Agendar desligamento do PC
-> Criar duas funções em python para agendar o desligamento do computador em uma hora e meia
'''

# Importando módulos
import os
import time

# Criando algoritmo:
def desligamento():
    temporizador = int(input("Digite, em minutos, o tempo até o computador desligar: "))
    print(f"Desligamento agendado para {temporizador} minutos...")
    time.sleep(temporizador*60)
    os.system('poweroff') # -> Estou utilizando esse comando, pois desliga a máquina no exato momento.
                          # -> O comando "shutdown" agenda para 1 minuto depois, e os argumentos -h now, 
                          # -> são extensos, então prefiro utilizar o poweroff.