# Exercício para permitir que o usuário possa escolhar a opção e 
# o programa irá seguir de acordo com o que foi escolhido.

#Declarando as variáveis

#Número escolhido pelo usuário

numero_usuario = float(input("Digite um número que será utilizado para multiplicação: "))

print("Escolha uma opção:\n")
print("Opção 1: Multiplicar por dois(2)\n")
print("Opção 2: Multiplicar por dois(3)\n")

escolha_usuario = int(input("Digite a opção desejada: "))

# Algoritmo para trazer o resultado desejado
if escolha_usuario == 1 :
   resultado_escolha_1 = numero_usuario * 2
   print(f"Resultado: {resultado_escolha_1}")
elif escolha_usuario == 2 :
    resultado_escolha_2 = numero_usuario * 3
    print(f"Resultado: {resultado_escolha_2:.2f}")
else:
    print("Opção inválida, escolha outra.")
    