''' 
A composição é usada para estabelecer relacionamentos entre classes e objetos.
Relacionamento do tipo: Faz parte, exemplo gato faz parte da casa. 
É complementar a herança.
'''

class Animal: # -> Classe pai
    def __init__ (self,nome,categoria):
        self.nome = nome
        self.categoria = categoria

class Peixe(Animal): # -> Classe filho
    raca = ""

class Passaros(Animal):
    cor = ""

class Zoo:
    def __init__(self):
        self.animais_dict = {} # -> Composição

    def add_animal(self,animal):
        self.animais_dict[animal.nome] = animal.categoria # -> Valor
        # -> O nome está sendo usado como base, portando não podemos utilizar nomes iguais.

    def total_categoria (self, categoria):
        resultado = 0
        for animal in self.animais_dict.values(): # Animal = categoria
            if animal == categoria:
                resultado += 1
        return f"No nosso zoológico temos {resultado} quantidade de {categoria}"

zoo = Zoo()
peixe = Peixe("Brutos","mamíferos")
peixe2 = Peixe("Palhaço","mamíferos")
papagaio = Passaros("Tu tubarao","aves")
print(vars(peixe))
print(vars(papagaio))
zoo.add_animal(peixe)
zoo.add_animal(peixe2)
zoo.add_animal(papagaio)
print(zoo.total_categoria("aves"))
print(zoo.total_categoria("mamíferos"))