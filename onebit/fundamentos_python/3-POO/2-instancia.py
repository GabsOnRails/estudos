# Instanciando a classe para torna-se um objeto


class Movie: # Usamos a primeira letra maiúscula para nomear uma clase
    nome = "" # -> Atributos da classe Movie
    ano_de_lancamento = 0
    duracao = 0
    nota = 0

# Primeiro filme
filme = Movie() # -> Para fazer um objeto o código precisa estar fora da identação da classe
filme.nome = "O menino e a garça" # -> Definindo os atributos da classe Movie
filme.ano_de_lancamento = 2024
filme.duracao = 124
filme.nota = 7.5

print("##Dados do filme##")
print(f"Nome do filme: {filme.nome}\nNota do filme: {filme.nota}")
# Tudo isso é o primeiro objeto