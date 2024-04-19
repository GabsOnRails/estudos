# Utilizando input

# criando as variáveis 
name = input('Digite o nome do jogo:\n')

'''a função input converte todos os dados em str, por isso quando é um dado númerico precisamos colocar
o int ou float.'''
year_launch = int(input('Digite o ano de lançamento:\n'))

game_price = float(input('Digite o preço do jogo:\n'))

'''a condição "bool" é usada para casos de boleano, ou seja, verdadeiro ou falso.
Porém não iremos utilizar nesse caso.'''
plan_include = (input('Está incluso no plano mensal?\n')).upper()

# prints
print (f"o nome do jogo é {name}")
print (f"O jogo foi lançado em {year_launch}")
print (f"O preço do jogo é R${game_price}")
print (f"O jogo está incluso no plano mensal - {plan_include}")