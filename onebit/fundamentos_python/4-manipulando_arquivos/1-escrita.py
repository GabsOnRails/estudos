# Iremos aprender a persistir os dados, ou seja, salvá-los para consultas posteriores.and

nome = input('Digite seu nome: ')

'''
1 - Opção w - write (escrever/sobreescrever os dados)
2 - Opção r - read (ler)
3 - Opção a - append (adicionar/armazenar)
'''

# Alternativa 1
# file = open("nomes.txt","a")
# file.write(f"{nome.title()}\n") # -> Escrevendo (salvando) a variável "nome" no arquivo txt.
# file.close()

# Alternativa 2 -> Mais utilizada
with open("dados/nomes.txt","a") as file:
    file.write(f"{nome.title()}\n")