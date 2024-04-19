# Usando o laço for

lista_jogos = ["Ror2","Children of morta","DBD","Lol","R6"]
divisoria = "="

for jogos in lista_jogos: # Iterando itens, a variável "jogos" poderia ter qualquer nome
    print(jogos)
print(divisoria*50)

for jogos in lista_jogos: # Parando o loop de acordo com o critério.
    if jogos == "Lol":
        break
    print(jogos)
print(divisoria*50)

for jogos in lista_jogos: # Usando "continue" para pular o item escolhido.
    if jogos == "DBD":
        continue
    print(jogos)
print(divisoria*50)

# Fazendo programa de avaliação

nome_jogos = input("Digite o nome do jogo:\n")
avaliacoes = int(input("Digite quantas avaliações irá fazer:\n"))

soma = 0
for notas in range(avaliacoes):
    nota = float(input("Digite a nota para o jogo:\n"))
    soma += nota
print(f"A média para o jogo {nome_jogos} é: {soma/avaliacoes:.2f}")