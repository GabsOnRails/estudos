'''
Para herdar uma classe é só colocar entre ().
Classe especialista -> Herda atributos da classe pai, mas tem seus próprios.
O relacionamento de herança é do tipo: "é um..", exemplo: O gato é um.. animal[herdado].
'''

class Animal: # -> Criando classe principal
    nome = ""
    tamanho = ""
    cor = ""

    def eat(self): # -> Criando função que será compartilhada
        print("Alimentando-se")

class Cavalo(Animal): # -> Herdando atributos da classe Animal
    raca = ""

    def fugir(self):
        print("Cavalo fugindo!")

class Leao(Animal): # -> Herdando atributos da classe Animal
    juba = True

    def cacar(self):
        print("Leão caçando!")

cavalinho = Cavalo()
cavalinho.nome = "Pé de pano"
cavalinho.cor = "Branco"
cavalinho.fugir()
cavalinho.eat()

leo = Leao()
leo.nome = "Luminus"
leo.cor = "Azul"
leo.cacar()


