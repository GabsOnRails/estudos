# Usando módulo json para ler dados

import json

# 1 -> Convertendo strings para dicionários
pessoas = '{"nome": "Gabriel", "linguagens":["Python","HTML"]}' # -> String
print(type(pessoas))
dicionario = json.loads(pessoas)
print(dicionario)
print(dicionario['linguagens'])

# 2 -> Convertendo dicionário para json
convertendo_json = json.dumps(dicionario)
print(convertendo_json)
print(type(convertendo_json)) # -> String

# 3 -> Formatando um Json
print(json.dumps(dicionario,indent=4, sort_keys=True))

# 4 -> Salvando Json em txt | Muito bom para armazenar dados
with open("pessoas.txt","w") as json_file:
    json.dump(dicionario,json_file) 

# 5 -> Lendo json externo | iris dataset(kaggle)
    with open("db.json","r") as texto:
        dados = json.load(texto)
        print(dados)
    