'''
Criar um programa que recebe os produtos e aplica descontos.
Precisa utilizar o metódo construtor e dundle str
'''

nome_produto = input('Digite o nome do produto: ')
preco_produto = float(input('Digite o preço do produto: R$ '))
desconto = int(input("Digite em % quanto será o desconto: "))

calculo_desconto = (preco_produto*desconto) / 100
valor_final = preco_produto - calculo_desconto


class Desconto:
    def __init__(self,nome,preco,desconto):
        self.nome = nome
        self.preco = preco
        self.desconto = desconto
       
    def __str__(self):
        return f"\nProduto {nome_produto} - R$ {preco_produto}"


    def tabela_desconto(self):
        print("\n##Aplicar descontos##")
        print(f'O produto {nome_produto} tem o desconto de {desconto}%\nO valor final é R$ {valor_final:.2f}')
tabela = Desconto(nome_produto,preco_produto,desconto)
print(tabela)
tabela.tabela_desconto()