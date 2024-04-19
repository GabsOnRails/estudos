# Módulo matemática

# importando módulo
import math

# Número de PI
print(f"{math.pi:.2f}") # -> Formando o número 

# Número de Euler
print(f"{math.e:.2f}")

# Arredondando os números
numero = 10.4
print(math.ceil(numero)) # -> Arredonda para cima
print(math.floor(numero)) # -> Arredonda para baixo

# Fazendo fatorial
numero1 = int(input("Digite o número para fatorial: "))
print(math.factorial(numero1))

# Potência de número
print(math.pow(5,9))

# Raiz quadrada
print(math.sqrt(169))

# MDC
mdc = math.gcd(8,10) # -> Maior divisor comum 
print(mdc)

# Logaritmo
print(math.log(10))