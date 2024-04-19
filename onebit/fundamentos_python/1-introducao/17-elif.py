# Trabalhando com elif

primeiro_numero = float(input('Digite o primeiro número:\n')) 
segundo_numero = float(input('Digite o segundo número:\n'))
operacao = input('Digite qual operação deseja realizar ( + - * /)\n')

if operacao == "+":
    resultado_soma = primeiro_numero + segundo_numero
    print(f"O resultado da soma entre {primeiro_numero} e {segundo_numero} é {resultado_soma}")

elif operacao == "-":
    resultado_subtracao = primeiro_numero - segundo_numero
    print(f"O resultado da subtração entre {primeiro_numero} e {segundo_numero} é {resultado_subtracao}")

elif operacao == "*":
    resultado_mult = primeiro_numero * segundo_numero
    print(f"O resultado da multiplicação entre {primeiro_numero} e {segundo_numero} é {resultado_mult}")
elif operacao == "/":
    resultado_div =  primeiro_numero / segundo_numero
    print(f"O resultado da divisão entre {primeiro_numero} e {segundo_numero} é {resultado_div:.2f}")
else:
    print("Operação não encontrada..")