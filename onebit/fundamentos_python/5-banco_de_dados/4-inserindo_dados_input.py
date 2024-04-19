# Inserindo dados no DB via input

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

# 3 -> Solicitando dados do usuário
name = input("Nome do filme: ")
year = int(input("Ano do filme: "))
score = float(input("Nota para o filme: "))

# 4 -> Inserindo dados na tabela
cursor.execute("""
    INSERT INTO movies(name,year,score)
    VALUES(?,?,?) 


""",(name,year,score))
'''
Quando vamos usar variáveis como parâmetros usamos o "?" e passamos as variáveis
após as aspas, em formato de tupla.
'''

# 5 -> Gravando dados no DB
conexao.commit()
print("Dados inseridos com sucesso!")

# 6 -> Fechando conexão
conexao.close()