# EXercício desenvolvido por mim.

'''
Escreva um programa Python para ler as primeiras 'n' linhas de um arquivo.
1-> O nome do arquivo e a quantidade de linhas devem ser passadas via parâmetro na função.
'''
lista = [] # -> Criando lista para usar o índice na iteração e retornar o número de linhas solicitadas.

# Criando variáveis para input e parâmetro da função.
nome_arquivo = input("Digite o nome do arquivo que deseja ler: ")
indice = int(input(f"Até qual linha deseja ler: "))
# Criando variável para numerar os nomes quando utilizar o for.
# contador = 0 -> Se utilizado na função precisa ser declarado dentro da função.

# Variável para divisão do texto que irá aparecer no terminal.
divisoria = "-"
print(divisoria*40)

# Parte lógica do código.
def ler_linhas(nome_arquivo,indice):
    contador = 0 # -> Declarando dentro da função para funcionar.
    with open(nome_arquivo.lower(),"r",encoding="utf-8") as file:
        for lines in file:
            lista.append(lines.rstrip()) # -> Adicionando dados do arquivo para a lista.

    # -> Criando condição para leitura apenas dos dados que estão na lista.
    if indice <= len(lista) and indice > 0:
        for nomes in (lista[:indice]): # -> para ordenar basta colocar o "sorted".
            contador += 1
            print(f"{contador} - {nomes}")
    else:
        print(f"Quantidade de linhas para leitura não correspondente as no arquivo - {len(lista)}.")

ler_linhas(nome_arquivo, indice)
