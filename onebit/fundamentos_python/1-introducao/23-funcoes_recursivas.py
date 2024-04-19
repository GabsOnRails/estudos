# Usando função recursiva

# Fatorial

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return (numero * fatorial(numero-1)) # chama-se recursiva, pois usamos a função dentro dela mesma.

numero = (int(input('Digite o número para fatorial:\n')))
print(f"O fatorial de {numero} é {fatorial(numero)} ")