

import requests

# 1 -> Vendo versão que estou utilizando e os metódos
# print(requests.__version__)
# print(dir(requests))

link = 'https://www.google.com/search?channel=fs&client=ubuntu-sn&q=zatch+bell'
requisicao = requests.get(link)
print(requisicao) # -> Devolve um código
print(requisicao.status_code) # -> Devolve o status code
# print(requisicao.text) # -> Devolve um texto gigante
