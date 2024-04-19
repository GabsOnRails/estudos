# Usando o laço while

# Criando variavéis
nome_jogo = input('Digite o nome do jogo:\n')
contador_avaliacoes = 0
notas = 0
total_notas = 0
media = 0

while(notas != 404):
    print('Para fazer uma avaliação digite uma nota entre 0 e 10. Caso queira sair digite "404"')
    notas = float(input('Digite a nota de avaliação:\n')) 
    if notas != 404:
        total_notas += notas
        contador_avaliacoes += 1 
        media = total_notas / contador_avaliacoes
print(f'A média de notas para o jogo {nome_jogo} é: {media}')