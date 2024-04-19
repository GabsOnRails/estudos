#  Inserindo dados na tabela através de operações DML

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

# 3 -> Inserindo dados através de uma querry
cursor.execute("""
INSERT INTO movies(name,year,score)
VALUES ('Mario Bross',2023,10) 
"""
)

cursor.execute("""
INSERT INTO movies(name,year,score)
VALUES ('O som do silêncio',2019,9.8) 
"""
)

cursor.execute("""
INSERT INTO movies(name,year,score)
VALUES ('Sede assassina',2023,10) 
"""
)

# 4 -> Gravando dados no DB (database)
conexao.commit()
print("Dados inseridos com sucesso!")

# 5 -> Fechando conexão
conexao.close()

