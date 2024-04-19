# Desafio final
import time
times = {} # Declarando o dicionário.
done = False # Variável que irá controlar o loop.
divisoria = "-" # Variável global usada nas funções.

'''Espaço para as funções'''
def menu():
    print("Escolha uma opção:")
    print("1 - Criar time")
    print("2 - Excluir time")
    print("3 - Listar times")
    print("4 - Adicionar jogadores")
    print("5 - Excluir jogadores")
    print("6 - Listar jogadores")
    print("7 - Sair")

def criar_time():
       nome_time = input('Digite o nome do time: ')
       times[nome_time] = {'nome': nome_time, 'jogadores':[]}
       print(f"O time {nome_time} foi adicionado com sucesso!")
       print(divisoria*50)

def excluir_time():
       listar_times()
       indice_time = int(input("Informe o número do time que irá remover:\n"))
       if indice_time <= len(times):
              nome_time = list(times.keys())[indice_time-1]
              del times[nome_time]
              print(f"O {nome_time} foi removido com sucesso!")

def listar_times():
       print(divisoria*50)
       print("Times existentes:")
       for indice, time in enumerate(times.values()):
              print(f"{indice+1}. {time['nome']} ({len(time['jogadores'])} jogadores)")
       print(divisoria*50)

def adicionar_jogadores():
       listar_times()
       time_numero = int(input("Informe o número do time que deseja adicionar o jogador: "))
       if time_numero <= len(times):
              nome_time = list(times.keys())[time_numero-1]
              nome_jogador = input("Informe o nome do jogador: ")
              times[nome_time]['jogadores'].append(nome_jogador)
              print("Jogador adicionado com sucesso!")
              print(divisoria*50)

def excluir_jogadores():
       listar_times()
       time_numero = int(input("Informe o número do time que deseja remover o jogador: "))
       if time_numero <= len(times):
              time_nome = list(times.keys())[time_numero-1]
              print(times[time_nome])
              numero_jogadores = int(input("Informe o número do jogador: "))
              if numero_jogadores <= len(times[time_nome]['jogadores']):
                     del times[time_nome]['jogadores'][numero_jogadores-1]
                     print("Jogador removido com sucesso!")
                     print(divisoria*50)
              else:
                     print("Número do jogador inválido!")
       else:
              print("Número do time inválido!")

def listar_jogadores():
       listar_times()
       indice_time = int(input("Digite o número do time para ver a escalação: "))
       if indice_time <= len(times):
              nome_time = list(times.keys()) [indice_time-1]
              print(times[nome_time])
              print(divisoria*50)
       else:
              print("Número do time inválido!")

# Loop
while not done:
    menu()
    escolha=int(input('> '))
    if escolha == 1:
        criar_time()
    elif escolha == 2:
            excluir_time()
    elif escolha == 3:
            listar_times()
    elif escolha == 4:
            adicionar_jogadores()
    elif escolha == 5:
            excluir_jogadores()
    elif escolha == 6:
            listar_jogadores()
    elif escolha == 7:
            print('Saindo do programa..')
            time.sleep(2)
            done = True
    else:
           print('Opção digitada inválida')