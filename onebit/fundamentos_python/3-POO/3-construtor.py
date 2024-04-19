# Metódo construtor também conhecido como especial ou BOB.

class Movie:
    def __init__(self,nome,ano,nota,duracao): # -> Self signfica que recebe os atributos
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.nota = nota

    def __str__(self):
        return f"avatar: {self.nome}, Ano: {self.ano}, Duração: {self.duracao}, Nota: {self.nota}"
        # Retorna os dados que eu colocar, quando passo somente o objeto no print. 
        # Interessante para retornar todas informações em um print só
    

avatar = Movie("Avatar 2",2023,8.0,120)
print(avatar.nota) # -> Usando o metódo init
print(avatar) # -> Usando o metódo STR