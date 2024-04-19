
nome_jogo = "torchlight"

descricao = """
Rain of risk 2 ou RoR2 é um roguelike
muito bom
"""

# How it's works - string[begin:end:increment] | start in 0 and end in -1 (because it's exclusive)

# Search all string from first position until the last
print(nome_jogo[0:])

# Search all string until the last
print(nome_jogo[:])

# Search all string from three position until the last
print(nome_jogo[2:])

# Search all string in pair numbers (increment 2 characters)
print(nome_jogo[::2])

# Search all string in odds numbers
print(nome_jogo[1::2])

# Reverse string
print(nome_jogo[::-1])
