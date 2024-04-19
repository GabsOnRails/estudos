# criando as variáveis 
name = input('Digite o nome do jogo:\n')

year_launch = int(input('Digite o ano de lançamento:\n'))

game_price = float(input('Digite o preço do jogo:\n'))

plan_include = (input('Está incluso no plano mensal?(s/n)\n')).upper()

# prints concatenados
divisoria = "="
print('###Dados dos jogos###')
print(divisoria*21)

# primeira forma de concatenar: Com virgúla
print("Nome do jogo:",name)
# segunda forma de concatenar: Com virgúla, mas no mesmo print
print ("Ano de lançamento",year_launch, "\nPreço do jogo: R$", game_price)
# terceira forma de concatenar: Com f string
print (f"Está incluso no serviço mensal? - {plan_include}")