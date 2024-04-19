# Criando a lógica do programa

# Importando as classes
from classes_exerciciofinal import Contact, Contact_book

agenda_contato = Contact_book() # -> Instanciando a classe

while True:
    divisoria = "-"
    print(f"\n{divisoria*20}Opções da Agenda{divisoria*20}")
    print("1-Opção: Adicionar contatos")
    print("2-Opção: Listar contatos")
    print("3-Opção: Buscar contatos")
    print("4-Opção: Excluir contatos")
    print("5-Opção: Sair")

    escolha = int(input("\nEscolha uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")

        contato = Contact(nome,telefone,email)
        agenda_contato.add_contacts(contato)

        '''-> Chamei o "agenda contato", pois está referenciando a classe
        Contact_book, o "add_contacts" é o método que foi criado dentro da
        classe Contact Book e o contato é o parâmetro anterior passado dentro do "if".'''

        print("Contato adicionado com sucesso!")
        print(divisoria*40)

    elif escolha == 2:
        print(divisoria*40)
        agenda_contato.display_contacts()
        print(divisoria*40)      

    elif escolha == 3:
        print(divisoria*40)
        buscar_nome = input("Qual contato deseja buscar: ")
        buscar_contato = agenda_contato.search_contact(buscar_nome)
        print(buscar_contato)
        print(divisoria*40)
   
    elif escolha == 4:
        print(divisoria*40)
        excluir_nome = input("Qual contato deseja excluir: ")
        excluir_contato = agenda_contato.search_contact(excluir_nome)
        if excluir_contato:
            agenda_contato.remove_contact(excluir_contato)
            print("Contato removido com sucesso!")
            print(divisoria*40)
            
    elif escolha == 5:
        print(divisoria*40)
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida!")