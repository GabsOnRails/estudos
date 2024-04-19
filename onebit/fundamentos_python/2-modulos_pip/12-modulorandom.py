import random
# Módulo para randomizar os valores da lista

# 1 -> Escolher número aleatório
lista = (7,6,8,10,15)
print(random.choice(lista))

# 2 -> Gerar número aleatório
aleatorio = random.randint(0,15)
print(aleatorio)

# 3 -> selecionar caractere aleatório de uma string
nome = "Curso Python"
letra_aleatoria = random.choice(nome)
print(letra_aleatoria)

# 4 -> Selecionar mais de um valor aleatório
# Sintaxe: random.sample(sequencia,quantidade de itens para retornar)
print(random.sample(lista,2))