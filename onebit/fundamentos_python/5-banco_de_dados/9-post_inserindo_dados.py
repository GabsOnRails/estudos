# Inserindo dados no postgreSQL através do Python

# Usando o módulo de integração entre Python e PostgreSQL
from conexao_postgresql import conn

cursor_obj = conn.cursor()

# As informações precisam ser passadas em tuplas dentro de uma lista -> [()]
games = [
    ("YS",2012,8.9),
    ("Stray",2022,9.5)

]

# Criando iteração para inserir os dados na tabela do postgreSQL
for game in games:
    cursor_obj.execute("""
    INSERT into games(name,year,score)
    VALUES (%s,%s,%s)
""",game)

conn.commit()
print("Dados inseridos com sucesso!")
conn.close()