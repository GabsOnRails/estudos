# Dicionário aninhado é o nome dado para um dicionário dentro do outro

import pprint # -> melhora a legibilidade do print.

dicionario_jogos = {
"risk or rain 2": {
    "ano de lancamento":2018,
    "nota": 9.2,
    "genero": ["roguelike","roguelite"]
},
"Children of morta": {
    "ano de lancamento": 2013,
    "nota": 8.5,
    "genero": ["roguelike","estrategia"]
},
"Block 'n load": {
    "ano de lancamento": 2009,
    "nota": 8,
    "genero": ["fps", "estrategia"]
}
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(dicionario_jogos)

print(dicionario_jogos["Children of morta"]["genero"]) # -> Buscar informações.
dicionario_jogos["Children of morta"]["jogadores"] = 2 # -> Adicionar informações.
print(dicionario_jogos["Children of morta"])

del dicionario_jogos["Block 'n load"] # -> excluir um dicionário inteiro.
pp.pprint(dicionario_jogos)