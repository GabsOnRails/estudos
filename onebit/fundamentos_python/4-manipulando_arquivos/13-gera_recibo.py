'''
Todas informações contidas nesse algoritmo são fictícias.
O objetivo desse algoritmo é gerar um recibo em pdf com informações definidas
através do código em Python.
'''
# importando módulos externos e builtin.
from fpdf import FPDF
from num2words import num2words
from datetime import date

# Variáveis
nome_cliente = input("Informe o nome do cliente: ")
consulta = input("Informe o tipo de consulta: ")
valor_consulta = input("Informe o valor da consulta: ")
valor_extenso = num2words(float(valor_consulta),lang="pt-br")
mensagem_valor = f'{valor_consulta} reais'
mensagem_valor_extenso = f"{valor_extenso} reais"
data = date.today() # -> Usando o modulo builtin para pegar a data
dia = data.day
mes = data.month
ano = data.year
 

# Layout do recibo
pdf = FPDF()
pdf.add_page() # -> Adicionando página
pdf.set_font("Arial","",20) # -> Definindo a fonte e tamanho.
pdf.image("dados/rec.jpg", x=0, y=0) # -> Usando uma imagem como background.
pdf.text(162,45,mensagem_valor)# -> Definindo onde os dados ficarão em relação ao pdf. Precisa ser str
pdf.text(80,86,nome_cliente.title()) # -> Definindo onde os dados ficarão em relação ao pdf. Precisa ser str
pdf.text(80,108,mensagem_valor_extenso)# -> Definindo onde os dados ficarão em relação ao pdf. Precisa ser str
pdf.text(80,135,consulta)# -> Definindo onde os dados ficarão em relação ao pdf. Precisa ser str
pdf.set_text_color(255,255,255) # -> Definindo, em RGB, a cor da data para branco
pdf.text(30,193,str(dia))
pdf.text(50,193,str(mes))
pdf.text(70,193,str(ano))
nome_recibo = f"{nome_cliente.strip()}_{dia}_{mes}_{ano}" # -> Criando nome único para o arquivo.
pdf.output(f"pdf/{nome_recibo}.pdf") # -> Nome e local que o pdf será salvo.
print("Recibo gerado!")