# Fazendo script de cálculo

# soma
def soma():
    num1 = float(input("digite o primeiro número para somar: "))   
    num2 = float(input("digite o segundo número para somar: "))
    resultadosoma = num1 + num2
    print(f"A soma de {num1} e {num2} é: {resultadosoma:.2f}")

def subtracao():
    sub1 =float(input("Digite o primeiro número para subtração: "))
    sub2 =float(input("Digite o segundo número para subtração: "))
    resultadosub = sub1 -sub2
    print(f"O resultado da subtração de {sub1} e {sub2} é: {resultadosub:.2f}")

def multiplicacao():
    mult1 = float(input("Digite o primeiro número para multiplicar: "))
    mult2 = float(input("Digite o segundo número para multiplicar: "))
    resultadomul = mult1*mult2
    print(f"O resultado da multiplicação entre {mult1} e {mult2} é: {resultadomul:.2f}")

def divisao():
    div1 = float(input("Digite o primeiro numero da divisão: "))
    div2 = float(input("Digite o segundo numero da divisão: "))
    resultadodiv = div1 / div2
    print(f"O resultado da divisão entre {div1} e {div2} é: {resultadodiv:.2f}")
