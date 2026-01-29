#Algoritmo que calcula a soma de 4 notas,
#retorna a média e diz se o alumo foi aprovado.


#variaveis
contador = 1
somaNotas = 0

#loop de repetição com valor pré definido
for nota in range(4):    
    notas = float(input(f"Digite a nota {contador}: ")) #entrada de dados
    somaNotas += notas #atribuição e soma das notas
    contador +=1 #atribuição ao contador 
media = somaNotas/4 # valor final da média

#algoritmo condicional para aprovação ou não.
if media >= 7.5:
    print(f"A media do aluno foi {media:.2f} e está aprovado(a)")
else:
    print(f"A media do aluno(a) foi {media:.2f} e está reprovado(a)")


