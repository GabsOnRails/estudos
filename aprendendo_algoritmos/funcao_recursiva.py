#  Função recursiva é aquela que chama a sí mesma

def fatorial(x):
    if x == 1:
        return 1
    else:
        resultado = x * fatorial(x-1)
        return resultado
    
numero = int(input('Digite um número para fatorial: '))

print(fatorial(numero))