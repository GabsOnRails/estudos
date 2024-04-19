# Lendo dados do DB.

import sqlite3

# 1 -> Conectando no banco de dados
'''
PS: O comando 'connect' quando não existe um banco de dados ele cria, mas
quando existe um BD serve para fazer a conexão.
'''
conexao = sqlite3.connect("titulo.db") # -> Conectando no banco de dados.

# 2-> Criando um cursor
'''
Um cursor é um interador que permite navegar e
manipular os registros de um BD (DML ou DDL).
'''
cursor = conexao.cursor()

# 3 -> Lendo dados da tabela
data = cursor.execute("SELECT name,year,score FROM movies")
print(data.fetchall()) # -> Todos os dados da instrução acima e apresente via print. Vem em tuplas dentro de uma lista.

# 4 -> Iterando dados
for row in cursor.execute("SELECT * FROM movies"):
    print(f"{row}")

# 5 -> Ordenando dados pelo Score
for row in cursor.execute("SELECT * FROM movies ORDER BY score desc"): # desc -> descendente
    print(f"{row}")

# 6 -> Fechando conexão
conexao.close()