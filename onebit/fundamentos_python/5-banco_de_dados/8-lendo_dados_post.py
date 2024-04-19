# Lendo dados do postgre no Python.

# Usando o módulo de integração entre Python e PostgreSQL
from conexao_postgresql import conn

cursor_obj = conn.cursor()

cursor_obj.execute("SELECT * FROM games")

result = cursor_obj.fetchall()
print(result)