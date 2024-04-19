# Criando gráficos

from openpyxl import Workbook
from openpyxl.chart import AreaChart, Reference, Series

wb = Workbook()
ws = wb.active

rows = [
    ['Ano','Lucro(%)','Gastos(%)'],
    [2017,25,30],
    [2018,35,25],
    [2019,40,38],
    [2020,26,21],
    [2021,23,12],
    [2022,44,27],
    [2023,48,18]
]

for informacoes in rows:
    ws.append(informacoes)

# Criação do gráfico
chart = AreaChart()
chart.title = "Lucro x Custos por Ano"
chart.style = 13
chart.x_axis.title = "Ano"
chart.y_axis.title = "Porcentagem"

categorias = Reference(
    ws,
    min_col=1,
    min_row=1,
    max_row=8
)

dados = Reference(
    ws,
    min_col=2,
    min_row=1,
    max_col=3,
    max_row=8
)

chart.add_data(dados,titles_from_data=True)
chart.set_categories(categorias)
ws.add_chart(chart, 'A10')

wb.save('files/chart.xlsx')



