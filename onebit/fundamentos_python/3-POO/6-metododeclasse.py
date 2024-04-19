'''
1 -> O metódo de classe utiliza o parâmetro referente  a classe 'cls'
2 -> O metódo de classe pode acessar ou modificar o  estado da classe
3 -> Usamos o decorator @classmethod para criar um método de classe
'''

class Console:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
    
    @classmethod
    def texto(cls,string): # -> cls é o parâmetro da classe.
        import re
        item = re.findall("é \w*", string)
        nome = item[0][2:]
        preco = item[1][2:]
        return cls(nome,int(preco))

play2 = Console.texto("Meu video game é play2 e o preço é 600 reais") # -> Metódo classe, pois não instanciei
deck = Console.texto("Meu video game é steam-deck e o preço é 3000 reais") 
print(play2.__dict__)
print(deck.__dict__) # -> Transformando em dicionário

