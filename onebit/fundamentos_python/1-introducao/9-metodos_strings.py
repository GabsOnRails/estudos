nome_jogo = "torchlight"

descricao = """
torchlight é um roguelike
muito bom, asmei,
"""

# prints
print(nome_jogo.upper())# uppercase
print(nome_jogo.lower())# lowercase

# Just first letter in upper
print (nome_jogo.capitalize())
print(nome_jogo.title())

print(nome_jogo.center(14,'-')) # Center the string with fill characters
print(nome_jogo.find("t")) # Find the character and return the position of the first apparition
print(descricao.count("k")) # Count the number of letters in string
print(descricao.replace("torchlight","Ror2")) # Replace elements
print(descricao.split(',')) # Split the string according the parameters