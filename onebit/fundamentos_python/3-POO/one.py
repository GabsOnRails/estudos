# Criar uma funcionalidade que permite o usuário avaliar o filme e retorna a média de avaliação.

# Variáveis globais
done = False
nota_total = 0
avaliadores = 0

# Criando inputs para paramêtros da classe Movie
nome_filme = input("Qual o nome do filme que deseja avaliar?\n")
ano_filme = int(input("Qual o ano de lancamento do filme? - "))
duracao_filme = int(input("Qual a duração do filme em minutos? - "))

# -> Criando o loop para avaliar o filme
while not done:
    avaliacao = input(f"Deseja avaliar o filme {nome_filme.title()}? S/N - ")
    if avaliacao.upper() == "S":
        nota_avaliacao = float(input("Digite uma nota: "))
        nota_total += nota_avaliacao
        avaliadores += 1
    elif avaliacao.upper() == "N":
        print("Obrigado!\n")
        done = True
    else:
        print("Opção inválida..")

 # -> Criando condicional caso ninguém avalie o filme 
if nota_total == 0:
   notal_total = 1
   avaliadores = 1

# -> Criando a média de avaliações
media = nota_total / avaliadores 

# Metódo para retornar todas informações em um único print.
class Movie:
    def __init__(self,nome,ano,media,duracao): # -> Self signfica que recebe os atributos
        self.nome = nome
        self.ano = ano
        self.duracao = duracao
        self.nota = media # -> Precisamos criar a classe Movie com o atributo self para inseri-lo na ficha tecnica

    def ficha_tecnica(self):
        print("##Dados do filme##")
        print(f"Nome do filme: {nome_filme.title()}")
        print(f"Ano de lançamento: {ano_filme}")
        print(f"Nota do filme: {media:.2f}")
        print(f"Duração do filme: {duracao_filme} minutos")

filme = Movie(nome_filme,ano_filme,media,duracao_filme)
filme.ficha_tecnica()