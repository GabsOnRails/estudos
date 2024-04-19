# É o recomendado para usar em POO.

# Criando uma classe

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @property # -> é como se fosse o método getter
    def nome(self):
        return self._nome # -> Tem que ficar protegido para não dar erro de recursão.
    
    @nome.setter # -> para modificar um atributo de uma classe
    def nome(self, valor):
        if not isinstance(valor,str):
            raise TypeError("O nome deve ser uma string")
        self._nome = valor

humano = Pessoa("13232",12)
print(vars(humano))