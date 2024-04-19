"""
Utilizamos *args quando não temos certeza de quantos argumentos serão necessários.
Os argumentos são passados em uma tupla.

o **kwargs além  dos valores podemos passar também as respectivas chaves.
Os argumentos são passados como um dicionário.
"""

# Usando arg

divisoria="="
def soma(*num):
    soma_total = 0
    for numeros in num:
        soma_total += numeros
    print(f"A soma total é {soma_total}")
soma(7,9,8,1)
soma(4,5,8,9,6,1,8,7,5)
print(divisoria*50)

def cursos(**dados):
    for key,values in dados.items():
        print(f"{key} - {values}")
cursos(nome="Python",categoria="Backend",nivel="Intermediário")
print(divisoria*50)
cursos(nome="HTML",categoria="Front-End",nivel="Iniciante")
print(divisoria*50)
cursos(nome="AWS",categoria="Cloud Computing",nivel="Avançado")
print(divisoria*50)