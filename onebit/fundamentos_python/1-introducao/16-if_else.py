# Trabalhando com condicional

nome_do_jogo = input('Digite o nome_do_jogo do jogo:\n')
ano_de_lancamento = int(input('Digite o ano de lançamento do jogo:\n'))
classificacao = float(input('Digite a nota de classificação:\n'))

if classificacao >= 8.0:
    print(f"O jogo {nome_do_jogo} é bom, pode jogar!")
else:
    print(f" O jogo {nome_do_jogo} não é bom :(")