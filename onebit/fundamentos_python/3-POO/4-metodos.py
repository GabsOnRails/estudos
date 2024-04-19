# Metódo para retornar todas informações em um único print.

class Movie:
    def __init__(self,nome,ano,nota,duracao): # -> Self signfica que recebe os atributos
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.nota = nota # -> Precisamos criar a classe Movie com o atributo self para inseri-lo na ficha tecnica



    def ficha_tecnica(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {self.nome}")
        print(f"Ano de lançamento: {self.ano}")
        print(f"Nota do filme: {self.nota}")
        print(f"Duração do filme: {self.duracao} minutos")

duna = Movie("Duna",2021,8,155)
duna.ficha_tecnica()