# // Devemos realizar um algoritmo com entrada que recebe n1 e n2 e exibe
#  o resultado a multiplicação entre eles, além de exibir os números que
#  foram digitados.
# -------------------------------------------------------------------------

# Atividade pratica

# Declando variável de entrada
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

print(f"O primeiro número digitado foi {numero1}")
print(f"O segundo número digitado foi {numero2}")
print(f"O terceiro número digitado foi {numero3}")

resultado = numero1+numero2+numero3
media = resultado/3

print(f"O resultado da soma é: {resultado}")
print(f"A média é: {media:.2f}")