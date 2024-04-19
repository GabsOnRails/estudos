'''
Agenda de Contatos

Desenvolva uma agenda de contatos persistindo as informações em arquivo. 
O programa deve seguir as especificidades:
1-> Criar o arquivo Agenda contendo três métodos:
    a-> Um método para adicionar contato;
    b-> Um método para listar contatos;
    c-> Um método para remover contatos.
2 -> Criar um arquivo principal para a aplicação que importar o módulo de agenda
    e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida.
'''
from methods_two import add_contacts,listar,delete_all_contacts

divisoria = "-"

def menu():
    while True:
        print("Escolha uma das opções:")
        print("1-> Adicionar contatos:")
        print("2-> Listar contatos:")
        print("3-> Excluir todos contatos:")
        print("4-> Sair")

        escolha = int(input("> "))

        if escolha == 1:
            add_contacts()
            print(divisoria*40)
            
        elif escolha == 2:
            listar()
            print(divisoria*40)

        elif escolha == 3:
            delete_all_contacts()
            print(divisoria*40)
            
        elif escolha == 4:
            print("Saindo..")
            break

        else:
            print("Opção inválida!")
            print(divisoria*40)

menu()


    

    