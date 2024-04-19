# Algoritmo para coletar informações das ações de mercado do ibovespa

import yfinance as yf
from datetime import datetime
from matplotlib import pyplot as plt

end_data = datetime.now().strftime('%Y-%m-%d')
# bb -> Branco do Brasil
bb = yf.Ticker('BBAS3.SA') # -> Esse ticker é encontrado em pesquisa 'yahoo tickers'
data_bb = bb.history(
    start ="2020-07-16",
    end = end_data
) 
data_bb['Close'].plot()
plt.savefig('bb_preco.png') # -> Salvando o gráfico