'''
Exercício final

Desenvolva uma agenda de contatos
utilizando Programação Orientada a Objetos. O programa deve seguir as especificidades:

1 -> Ter uma classe Contact contendo os atributos: name, phone e email.
2 -> Ter uma classe ContactBook contendo quatro métodos:
        Um método para adicionar contato. Uma função com o self do método init.
        Um método para listar contatos.
        Um método para buscar contatos.
        Um método para remover contatos.
3 -> Criar um arquivo principal para a aplicação que deve instanciar as duas classes criadas
     anteriormente e desenvolver e chamar cada um dos métodos desenvolvidos de acordo com a 
     opção escolhida.
'''
# Criando classe Contact
class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f'Nome: {self.name}\nPhone: {self.phone}\nEmail: {self.email}'

# Criando classe Contact_Book
class Contact_book:
    def __init__(self):
        self.contacts = []

    def add_contacts(self,contact): # -> Torna-se um método, pois recebe o "self" do init.
        self.contacts.append(contact)

    def remove_contact(self,contact):
        self.contacts.remove(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Lista de contatos vazia!")
        else:
            for contact in self.contacts:
                print(contact)
                print("----------------------------")
    
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return contact
            else:
                print("Contato não encontrado")



