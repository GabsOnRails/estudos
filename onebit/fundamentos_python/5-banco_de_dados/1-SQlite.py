'''
1-> É um banco de dados embutido nativo do Python e por isso não é necessário
utilizar um Sistema de Gerenciamento de Banco de Dados (SGBD) externo.
2-> Muito utilizado em Sos móveis como o android.
3-> Armazena a base de dados em um único arquivo. Por isso deve ser utilizado
para programas simples.
4-> 
'''

# Importando o módulo sqlite
import sqlite3

# 1-> Criando o banco de dados
conexao = sqlite3.connect("titulo.db")

# 2-> Verificar se houve alguma alteração na base de dados.

print(conexao.total_changes)