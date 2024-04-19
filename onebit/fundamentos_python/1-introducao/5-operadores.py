# Criando variáveis

num1 = int (input('Digite o primeiro número inteiro:\n'))
num2 = int (input('Digite o segundo número inteiro:\n'))

# Operadores Aritméticos:
soma = num1 + num2
subtracao = num1 - num2
divisao = num1 / num2
multiplicacao = num1 * num2

# Aqui é retornado o valor restante de uma divisão, exemplo: 3/2 resta 1, logo 3%2 = 1.
restante = num1 % num2
# Um número elevado ao outro, exemplo 4 ** 2 = 4*4
exponenciacao = num1 ** num2

# prints
divisoria = "="
print(divisoria*32)
print(f" A soma de {num1} e {num2} é: {soma}")
print(f" A subtração de {num1} e {num2} é: {subtracao}")
print(f" A multiplicação de {num1} por {num2} é: {multiplicacao}")
print(f" A divisão de {num1} por {num2} é: {divisao:.1f}")

print (f" O resto da divisão entre {num1} por {num2} é: {restante}")
print (f" A potência entre {num1} e {num2} é igual: {exponenciacao}")

# Operadores de comparação (retornam valores boleanos - Verdadeiro ou Falso):
maiorque = num1 > num2
menorque = num1 < num2
igual = num1 == num2
diferente = num1 != num2
maior_ou_igual = num1 >= num2
menor_ou_igual = num1 <= num2

# Atribuição
num1 += 1 # num1 = num1 + 1
num1 -= 1 # num1 = num1 - 1
num1 *= 1 # num1 = num1 * 1
num1 /= 1 # num1 = num1 / 1