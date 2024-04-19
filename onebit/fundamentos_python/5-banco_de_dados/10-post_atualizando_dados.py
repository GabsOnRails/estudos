# Atualizando dados no postgreSQL através do Python

# Usando o módulo de integração entre Python e PostgreSQL
from conexao_postgresql import conn

cursor_obj = conn.cursor()


sql = """
    UPDATE games
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql,("YS Origin",5))

conn.commit()
print("Dados atualizados com sucesso!")
conn.close()