# A atividade será usar os laços de repetição para fazer contas
# Atividade A - Usar o for, receber 5 números e fazer a multiplicação deles
# Atividade B - Fazer a mesma coisa que na atividade A, mas usando for e while
# ---------------------------------------------------------------------------------------

# Declarando variaveis
multiplicacao = 1

for i in range(5):
    numero = float(input("Digite um número para multiplicar: "))
    resultado = multiplicacao * numero
    multiplicacao = resultado
    
print(f"o resultado da multiplicação é: {multiplicacao}")

# Usando while

validador = False

while validador == False:
    for i in range(5):
        numero = float(input("Digite um número para multiplicar: "))
        resultado = multiplicacao * numero
        multiplicacao = resultado
        validador = True
print(f"o resultado da multiplicação é: {multiplicacao}")

    