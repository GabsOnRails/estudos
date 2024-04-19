# pelo que entendi dá para usar laços dentro da lista, deixando o código mais otimizado.

# retorne os valores menores que 4
divisoria = "="
# Fazendo com laço for:
for numeros in range(10):
    if numeros < 4:
        print(numeros)
print(divisoria*50)

# Fazendo com list comprehesion:
lista_numeros = [numeros for numeros in range(10) if numeros < 4] 
print(lista_numeros)
print(divisoria*50)
# o primeiro paramêtro é o que queremos retornar, depois fazemos o laço for normalmente.

# Outro exemplo, retornando jogos com determinado caractere
lista_jogos = ["dbd","ror2","minecraft","lol","rust","among us"]
nova_lista = [jogo for jogo in lista_jogos if "a" in jogo]
print(nova_lista)
print(divisoria*50)

# Laço for
for jogos in lista_jogos:
    if "a" in jogos:
        print(jogos)
print(divisoria*50)

# Jogos zerados
jogos_zerados = [jogos for jogos in lista_jogos if jogos != "among us"]
print(jogos_zerados)
print(divisoria*50)