# Utilizando encapsulamento para proteger os atributos das classes e objetos

class Trabalhador:
    def __init__(self,nome,salario):
        self.nome = nome
        self.__salario = salario # -> O "__" serve para tornar o atributo privado

    def mostrar(self):
        print(f"Nome: {self.nome} - Salário: R$ {self.__salario}")
    
fulano = Trabalhador("Fulano",4000)
sicrano = Trabalhador("Sicrano", 5800)
fulano.nome = "Thor"
fulano.mostrar()
sicrano.mostrar()

fulano.__salario = 81000 # -> Fazendo alteração no salário para ver se vai
# Uma forma interessante de trabalhar com isso é criar a classe em um arquivo diferente
# do qual será usada, assim nem o acesso a classe será feito.