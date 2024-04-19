# Lendo planilhas através do Python

from openpyxl import load_workbook as lw

# 1 -> Lendo workbook e buscando planilha
wb = lw(filename='files/teste.xlsx')
# print(wb)
planilha1 = wb['Planilha1']

# 2 -> Acessando um valor específico
# print(planilha1['B2'].value) -> Precisa utilizar o '.value' 

# 3 -> Iterando valores por meio do for.
for i in range(2,5): # índice final é exclusivo por isso é sempre +1
    # print(f"{planilha1['A{i}'].value}") -> Retorna um erro
    ano = (planilha1['A%s' %i].value) # -> Formatação place holder
    lucro = (planilha1['B%s' %i].value)
    gastos = (planilha1['C%s' %i].value)
    # print(f"No ano de {ano}, tivemos {lucro} de lucro e {gastos} de gastos.")
    print("{0} teve {1} de lucro e {2} de gastos.".format(ano,lucro,gastos))