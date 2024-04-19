# Dicionário utiliza chave e valor e pode conter lista como um valor.and

dicionario_jogos = {"nome": "Ror2",
    "preco": 25,
    "lançamento": 2015,
    "nota": 9.2,
    "genero": ["Roguelite","Roguelike"]
}
print(len(dicionario_jogos)) 
print(type(dicionario_jogos))
print(dicionario_jogos)

print(dicionario_jogos['genero']) # -> Recuperando através de fatiamento.
print(dicionario_jogos.get('nome')) # -> Recuperando através do get.

print(dicionario_jogos.keys()) # -> Recuperando apenas as chaves.
print(dicionario_jogos.values()) # -> Recuperando apenas os valores.

dicionario_jogos["jogadores"] = 4 # -> Adicionar itens no dicionário
print(dicionario_jogos)
dicionario_jogos.update({"jogadores":6}) # -> Atualizando itens no dicionário

dicionario_jogos.pop("genero") # -> Remover item no dicionário
print(dicionario_jogos)