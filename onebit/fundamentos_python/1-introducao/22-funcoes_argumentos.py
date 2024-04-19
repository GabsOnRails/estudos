# Usando argumentos nas funções
divisoria = "="


def nome_completo(nome,sobrenome):
    print(f"Nome completo: {nome.title()} {sobrenome.title()}")
nome = input('Qual seu nome?\n')
sobrenome = input ('\nQual seu sobrenome?\n')
      
nome_completo(nome,sobrenome)
print(divisoria*50)

''' Os argumentos são passados entre (), precisam ser colocados em ordem ao chamar a função e
    as variáveis dos argumentos ser declaradas antes de usar na função.'''

# Fazendo soma através de argumentos
def soma(a,b):
    return a+b
print(soma(4,8))
print(divisoria*50)

# Podemos definir um argumento como padrão

def endereco(pais="Brasil"):
    print(f"Eu moro em {pais}")
endereco()
endereco("São Paulo") # -> Mas podemos dar um novo valor ao argumento também.
print(divisoria*50)

# Criando avaliador de jogos


def media_jogos(avaliacoes):
    nome_jogo = input('Digite o nome do jogo:\n')
    soma = 0
    for contador in range(avaliacoes):
        nota = float(input(f'Digite uma nota para o jogo {nome_jogo}:\n'))
        soma += nota
    print(f"A média do jogo {nome_jogo} é: {soma/avaliacoes:.2f}")

avaliacoes = int(input('Digite quantas avaliações quer fazer:\n'))
media_jogos(avaliacoes)