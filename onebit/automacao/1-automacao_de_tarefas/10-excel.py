# Criando planilhas e adicionando dados através do Python

'''
Na biblioteca openpyxl, um workbook é a mesma que o arquivo e as planilhas são worksheet.
'''

from openpyxl import Workbook

# 1 -> Criando um workbook
wb = Workbook()
name = 'files/teste.xlsx'

# 2 -> Utilizando worksheet
ws1 = wb.active
ws1.title = "Planilha1"

# 3 -> Adicionando dados na planilha
data = [
    ['Ano','Lucro','Gastos'],
    [2021, '40%', '15%'],
    [2022, '45%', '25%'],
    [2023, '35%', '12%']

]
for line in data:
    ws1.append(line)

# 4 -> Adicionando outra planilha e valores em células específicas
ws2 = wb.create_sheet(title='Pi')    
ws2 ['D4'] = 3.14

wb.save(filename=name)
