# Criando tabela com o SQLITE

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

# 3 -> Criando a tabela
cursor.execute('''
CREATE TABLE movies(
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               year INTEGER NOT NULL,
               score REAL NOT NULL
);
''')

# 4 -> Fechando a conexão
print("Tabela criada!")
conexao.close() # -> Para ganhar uma perfomance melhor.
'''
Para visualizar o banco de dados precisamos instalar a extensão
"sqlite viewer".
'''



