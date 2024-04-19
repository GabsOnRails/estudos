'''
Advinhe o Número

Escreva um programa em Python que gera um número aleatório para que o usuário tente acertar o número.
Algumas sugestões para o programa:

1. Utilizar um laço de repetição para que o programa execute até que o usuário informe um 
   número referente a opção para sair do programa.
2. Utilizar o módulo random para gerar valores aleatórios dentro de um intervalo. Ex: 1 a 10.
3. Lê o número que o usuário digitar via input e comparar se é o mesmo número que o programa sorteou.

'''
import random
import time

# Declarando variáveis globais
num_minimo = 0
num_max = 100
tentativas = 0
numero_aleatorio = random.randint(num_minimo,num_max) # -> Variável que cria o número aleatório
done = False # -> Variável para controlar o loop



while not done:
    # Condicional para tentativas
    if tentativas > 1:
        texto = "tentativas"
    else:
        texto = "tentativa"

    chute = int(input(f'Chute um número entre {num_minimo} e {num_max}: '))
    if chute == numero_aleatorio:
        tentativas += 1 
        print(f'Parabéns, você acertou usando {tentativas} {texto}!')
        print('Saindo do jogo...')
        time.sleep(0.3)
        done = True
    elif chute > numero_aleatorio:
        print("Não foi dessa vez, o número aleatório é menor\n")
        tentativas += 1
    elif chute < numero_aleatorio:
         print("Não foi dessa vez, o número aleatório é maior\n")
         tentativas +=1

        

