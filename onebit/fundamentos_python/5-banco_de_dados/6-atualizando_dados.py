# Atualizando dados no DB.
'''
Atualização de dados e exclusão precisam da chave primária .
Usamos a cláusula WHERE.
'''
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

# 3 -> Recebendo informações para atualizar
id = int(input("Informe o id do filme que deseja alterar: "))
nome = input("Informe o nome do filme: ")

# 4 -> Atualizando os dados com cláusula WHERE para atualizar um dado específico.
cursor.execute("""
    UPDATE movies set name = ?
    WHERE id = ?
""",(nome,id))

conexao.commit() # -> Commitando os dados.
print("Dados atualizados com sucesso!")


# 5 -> Fechando conexão
conexao.close()