# Removendo dados com uso da cláusula WHERE e chave primária.

import sqlite3

# Conectando no DB
conexao = sqlite3.connect("titulo.db")

# Criando cursor
cursor = conexao.cursor()

# Recebendo informações para remover
id = int(input("Informe o id do filme que deseja remover: "))


# Removendo dados
cursor.execute("""
    DELETE FROM movies 
    WHERE id = ?
""",(id,)) # -> Quando há apenas um parâmetro em uma tupla DEVEMOS usar a vírgula.

conexao.commit()
print("Filme removido com sucesso!")

# Fechando conexão
conexao.close()