# Set (conjunto) não pode utilizar fatiamento.
# Não podemos repetir os valores.

conjunto = {"Risk of Rain 2", "Children of morta", "OverCooked 2", "For the King "}

print(len(conjunto))

conjunto_exemplo = {"Ror2", True, 1, 95} # No conjunto os valores 1 e True são considerados o mesmo.
print(conjunto_exemplo)

conjunto.update(conjunto_exemplo) # Adicionar itens, não existentes, de outro set.

conjunto.remove(True) # Remover itens.
conjunto.remove(95)
print(conjunto)

