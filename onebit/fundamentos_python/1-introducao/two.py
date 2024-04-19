'''
primeiro desafio: Escrever um programa para obter uma string em que todas as
ocorrências de seu primeiro caractere foram alteradas para "$"
Exemplo: Fifa 2023 -> Fi$a 2023 | Restart -> Resta$t


segundo desafio: Obter uma única string a partir de duas strings separadas por um 
espaço e trocar os dois primeiro caracteres de cada string.
Exemplo: abc xyz -> xyc abz
'''

# desafio 1
nome_jogo = input("Digite o nome do jogo:\n")

# Encontrando a letra para ser substituida
primeira_letra = nome_jogo[0].lower()

# substituindo
substituindo = nome_jogo.replace(primeira_letra,"$")
substituindo = primeira_letra + substituindo[1:]

# prints
print(f"Frase Inicial: {nome_jogo}")
print(f"Frase final: {substituindo}")
divisoria = "="
print(divisoria*24)

# desafio 2
frase1 = input('Digite a primeira frase:\n')
frase2 = input('Digite a segunda frase:\n')
print(f"Frase inicial 1: {frase1} | Frase inicial 2: {frase2}")

# encontrando letras
frase1_letras = frase1 [:2]
frase2_letras = frase2 [:2]

#novas frases
frase_final1 = frase1.replace(frase1_letras,frase2_letras)
frase_final2 = frase2.replace(frase2_letras,frase1_letras)

# prints
print(f"Frase final 1: {frase_final1} | Frase final 2: {frase_final2}")