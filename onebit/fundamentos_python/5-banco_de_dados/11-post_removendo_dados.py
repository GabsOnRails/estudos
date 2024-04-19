# Finalizando as operações de CRUD com Python 

# Usando o módulo de integração entre Python e PostgreSQL
from conexao_postgresql import conn

cursor_obj = conn.cursor()

sql = """
    DELETE FROM games
    WHERE id = %s
"""

cursor_obj.execute(sql,(6,)) # A vírgula está alí para que reconheça como uma tupla

conn.commit()
print("Dado removido com sucesso!")
conn.close()