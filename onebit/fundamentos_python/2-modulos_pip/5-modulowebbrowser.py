# Módulo usado para acessar sites 

# Importando módulos
import webbrowser
import time

# Variável global
divisoria = "-"
# Criando função para o loop
def menu():
    print(divisoria*50)
    print("Olá, escolha uma opção:")
    print(divisoria*50)
    print("1 - Ver anime")
    print("2 - Ir para estudos em Python")
    print("3 - Visitar site do SESC")
    print("4 - Ir para o Youtube")
    print("5 - Sair")

# Criando variável para controle do loop
done = False

# Criando o loop
while not done:
    # Criando variável para input no loop
    menu()
    opcao = int(input("> "))

    if opcao == 1:
        webbrowser.open("https://www.crunchyroll.com/pt-br")
    elif opcao == 2:
        webbrowser.open("https://cursos.onebitcode.com")
    elif opcao == 3:
        webbrowser.open("https://www.sescsp.org.br/")
    elif opcao == 4:
        webbrowser.open("https://www.youtube.com")
    elif opcao == 5:
        print("Saindo do programa...")
        time.sleep(0.3)
        done=True
    else:
        print("Opção inválida...")
        time.sleep(0.3)
        
