# Função lambda pode ter inúmeros argumentos, mas apena uma expressão

# Função de potência:
potencia =lambda num: num**2

# Função para verificar se é par:
numero_par = lambda numero: numero % 2 == 0

# Função que divide:
divisao = lambda numero,numero2: numero / numero2

# Inverte a string:
inverte = lambda frase: frase[::-1]

# Prints

print(potencia(5))
print(potencia(12))

print(numero_par(29))
print(numero_par(60))

print(divisao(258,5))
print(divisao(12,2))

print(inverte("Gabriel Felipe"))