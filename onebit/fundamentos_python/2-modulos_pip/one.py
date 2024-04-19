# Primeiro exercício de módulos:
'''
Fazer um módulo em python com as seguintes funções:
1 - Inverter uma string;
2 - Retornar apenas letras com índice par;
3 - Retornar apenas letras com índice impar.

'''

def inverter_string():
    frase = input("Digite uma frase para ser invertida:\n")
    resultado = frase[::-1]
    print(f"A frase inicial era:{frase}\n A frase invertida é: {resultado}")

def letras_par():
    frase_par = input("Digite uma frase para retornar as letras pares:\n")
    resultado_par = list(frase_par[0::2])
    print(f"As letras com índice par são: {resultado_par}")

def letras_impar():
    frase_impar = input("Digite uma frase para retornar as letras impares:\n")
    resultado_impar = list(frase_impar[1::2])
    print(f"As letras com índice impar são: {resultado_impar}")

