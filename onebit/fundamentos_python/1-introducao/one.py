""" Antecessor e Sucessor de um número:
        Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido,
        utilizando operadores de atribuição.
 Média de 4 notas:
        Escreva um programa em Python que leia quatro números e calcule a média entre esses números """


# Antecessor e sucessor

# Criando variáveis
numero = int(input('Digite um número inteiro:\n'))
antecessor = numero - 1
sucessor = numero + 1

# prints
print(f"O sucessor de {numero} é {sucessor} | O antecessor de {numero} é {antecessor}")

# Média 

# Criando variáveis
divisoria = "="
print(divisoria*60)

contador_de_notas = 1
notas = []

# Criando loop para adicionar 4 notas e retornar a média.
while contador_de_notas <= 4:
    valores_notas = float (input(f'Digite a nota {contador_de_notas} entre 0 e 10:\n'))
    notas.append(valores_notas)
    contador_de_notas += 1
    
soma = sum(notas)
media = soma /len(notas)
print (f'A média das notas é: {media:.2f}')
