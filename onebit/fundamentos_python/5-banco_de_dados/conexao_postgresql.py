''' 
Criando a integração entre Python e o PostgreSQL atráves da biblioteca
"psycopg2"
'''
import psycopg2

conn = psycopg2.connect(
    database = 'fliperama',
    user = 'postgres',
    password = '459145707080',
    host = 'localhost',
    port = '5432'
)