# Criando a conexão entre o python e o ORM sqlalchemy
# Funciona para qualquer SGBD, só alterar as informações 


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

user = 'postgres'
password = '459145707080'
host = 'localhost'
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}/{database}'

engine =  create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()