#  Metódos do exercício two

import os # -> usado para verificação
def add_contacts():
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    with open("dados/agenda.txt","a",encoding="utf-8") as file:
        file.write(f"Nome: {nome.title()} - Telefone {telefone} - Email: {email}\n")
        print(f"\nContato {nome} adicionado com sucesso!")
        

def listar():
        if not os.path.exists("dados/agenda.txt"):
             print("Agenda Vazia!")
             return
        with open("dados/agenda.txt","r",encoding="utf-8") as file:
             agenda = file.read()
             print("Agenda:")
             print(agenda)

def delete_all_contacts():
     if not os.path.exists("dados/agenda.txt"):
          print("Agenda Vazia!")
          return
     with open("dados/agenda.txt","w",encoding="utf-8") as file:
          file.write("")
          print("Todos os contatos foram excluidos!")