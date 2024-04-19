'''
Nos arquivos nomeados como "laboratorio" irei escrever códigos testando o que aprendi.
Esse algoritmo tem como objetivo criar um programa com 3 opções:
1 -> Criar um arquivo;
2 -> Adicionar informações em um arquivo;
3 -> Listar um arquivo.
'''

divisoria = "-"
def menu():
    print("Olá, as seguintes opções estão disponíveis:")
    print("Opção 1 - Criar arquivo")
    print("Opção 2 - Adicionar informações")
    print("Opção 3 - Ler arquivos")
    print("Opção 4 - Sair")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        criar_arquivo()
        print(divisoria*45)
        menu()
    elif escolha == 2:
        adicionar_informacoes()
        print(divisoria*45)
        menu()
    elif escolha == 3:
        ler_arquivo()
        print(divisoria*45)
        menu()
    elif escolha == 4:
        exit
    else:
        print("Opção inválida!")
        print(divisoria*45)

def criar_arquivo():
    proprietario = input("Digite seu nome: ")
    nome_arquivo = input("Digite o nome do arquivo com a extensão txt.\nO nome do arquivo deve começar com 'dados/': ")
    with open (nome_arquivo,"a",encoding="utf-8") as file:
        file.write(f"Arquivo feito por {proprietario.title()}")
    print("Arquivo criado!")
    print(divisoria*45)

def adicionar_informacoes():
    arquivo = input("Qual arquivo deseja adcionar as informações - ex'dados/teste.txt': ")
    dados = int(input("Quantas informações deseja adicionar: "))
    print(divisoria*45)   

    contador = 0

    while contador < dados:
        informacao = input("Digite a informação que deseja adicionar: ")
        print(divisoria*45)
        contador += 1
        with open (arquivo,"a",encoding="utf-8") as file:
            file.write(f"\n{informacao}")

def ler_arquivo():
    ler = input("Qual arquivo deseja ler - ex 'dados/leitura.txt': ")
    print(divisoria*45)
    with open(ler,"r",encoding="utf-8") as file:
        for linhas in file:
            print(linhas.rstrip())

menu()

