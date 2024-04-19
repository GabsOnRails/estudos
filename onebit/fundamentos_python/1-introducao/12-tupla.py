# Tupla tem mais limitações que a lista.
# Não podemos repetir os valores;
# Não podemos adicionar valores em uma tupla;
# Não podemos remover valores em uma tupla;
# Não podemos  ordenar valores em uma tupla.

# Podemos usar as propriedades de fatiamento (slice) na tupla.

jogos_tupla = ("Rust","Day Z", "DBD", "Fall Guys")
print(type(jogos_tupla)) # Ver o tipo de classe.

# Exemplos de slice na tupla:
print(jogos_tupla[:2]) # Buscar os dois primeiros itens.
print(jogos_tupla[-1]) # Buscar o último item.
print(jogos_tupla[:3]) # Buscar até uma determinada posição.
print(jogos_tupla[1:]) # Buscar a partir de uma posição.
print(jogos_tupla.index("DBD")) # Retornar o índice de um item através do nome.