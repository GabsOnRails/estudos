# # Fazer um algoritmo que identifica qual número é maior
# # a partir da entrada do usuário e retorna esse número.

# # Desenvolvimento do algoritmo

# #Declarando var onde usuário digita os números
# print("Olá, bem vindo(a)")

# # Primeiro Número
# num1 = float (input("Digite o primeiro número: "))

# # Segundo Número
# num2 = float (input("Digite o segundo número: "))

# if num1 > num2:
#     print(f"\nO numéro {num1} é maior que o número {num2}")
# else:
#     print(f"\nO número {num2} é maior que o número {num1}")

# # -----------------------------------------------------------------
# # Prática dois:
# # Escrever um algoritmo que recebe dois número e caso o primeiro
# # numéro seja maior, retornar o print "o primeiro número é maior"
# # caso contrário retornaŕa "o segundo número é maior"
# # Plus - mostrar a escolha feita pelo usuário.

# # Desenvolvimento do algoritmo 2
# # Mensagem para diferenciar os algoritmos
# print("\nSegunda execução")


# # Input do primeiro numero
# numero1 = float(input("Digite o primeiro número: "))
# # Input do segundo numero
# numero2 = float(input("Digite o segundo numero: "))

# # lógica para exibição da mensagem
# if numero1 > numero2:
#     print("O primeiro número é maior!")
# else:
#     print("O segundo número é maior!")

# Prática três
# Plus - mostrar a escolha feita pelo usuário.

#Algoritmo simples que mostra uma escolha feita pelo usuário
# e retorna uma mensagem

# Mensagem para diferenciar os algoritmos

validator = False

while validator == False:
    print("\nTerceira execução")
    
    # Menu de seleção
    menu = print ("\n______________Menu______________\n" \
    "1 - Calcular a soma dos números" \
    "\n2 - Calcular a subtração do números" \
    "\n3 - Multiplicar os números" \
    "\n4 - Dividir os números | PS: Não pode ser dividido por 0" \
    "\n5 - Sair\n")
    # Input que recebe a escolha do usuário
    escolha_usuario = int(input("Digite a opção escolhida: "))
    # Retorno que exibe qual opção foi escolhida
    opcao_escolhida = print(f"Opção escolhida pelo usuário: {escolha_usuario}")

    if escolha_usuario == 5:
        print("Saindo...")
        validator = True
    else: 
        numero3 = float(input("Digite um número: "))
        numero4 = float(input("Digite outro número: "))
     # Loop para retorna o resultado desejado pelo usuário
        if escolha_usuario == 1:
            print(f"\nResultado da soma: {numero3+numero4}")
        elif escolha_usuario == 2:
            print(f"\nResultado da subtração: {numero3-numero4}")
        elif escolha_usuario == 3:
            print (f"\nResultado da multiplicação: {numero3*numero4:.2f}")
        elif escolha_usuario == 4:
            if numero3 and numero4 != 0:
                resultado_divisao = numero3/numero4
                print(f"\nResultado da divisão: {resultado_divisao}")
            else:
                print("\nOs numéros precisam ser diferenters de 0!")
        else:
            print("Opção inválida")
        # Entrada de dados
    

    

    
   

