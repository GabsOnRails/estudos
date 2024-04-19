# Criando planilha a partir de arquivo txt.

from openpyxl import Workbook

print("Lendo dados do arquivo de texto")

# 1 -> Lendo dados do arquivo txt
file_txt = open('files/gastos.txt','r',encoding='utf-8')
file = file_txt.read()
# print(file)
list_data = file.splitlines() # -> Coloca os valores de cada linha em uma lista.

# 2 -> Iterando valores da lista
for i in range(0,len(list_data)):
    list_data[i] = list_data[i].split(',') # -> separando através das vírgulas. Valores adicionados a "list_data"

# 3 -> Criando planilha
wb = Workbook()
ws = wb.active # -> Ativando o ws
ws.title = "Gastos" # -> Defindo título da ws

for row in list_data:
    ws.append(row) # ws -> worksheet

wb.save('files/gastos.xlsx')