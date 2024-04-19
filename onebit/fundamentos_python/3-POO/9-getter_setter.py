# Metódos usados para alterar e modificar atributos privados

class Trabalhador:
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario # -> O "__" serve para tornar o atributo privado

    def mostrar(self):
        print(f"Nome: {self.nome} - Salário: R$ {self.__salario}")
    
    # Método para buscar dados
    def get_salario(self):
        return self.__salario # -> atributo que quero os dados

    # Método para modificar atributo privado
    def set_salario(self, salario):
        self.__salario = salario

fulano = Trabalhador("Fulano", 4000)
sicrano = Trabalhador("Sicrano", 7500)
fulano.nome = "Fulano 2"

fulano.mostrar()
sicrano.mostrar()

fulano.set_salario(78000) # -> Alterando atributo através do método
fulano.mostrar()
