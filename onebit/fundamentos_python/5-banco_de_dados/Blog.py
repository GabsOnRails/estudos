# Criando a lógica que liga o usuário com os posts

from conexao_orm import Base, engine,session
from User import User
from Post import Post

# Criar as tabelas
Base.metadata.create_all(engine)

# Função para exibir menu de opções

def show_menu():
    print("Menu de opções")
    print("1. Adicionar usuário")
    print("2. Adicionar Post")
    print("3. Consultar usuários e seus posts")
    print("4. Sair")

# Função para adicionar usuário
def add_user():
        print("Adicionar usuário!")
        name = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        user = User(name,email)
        session.add(user)
        session.commit()
        print("Usuário adicionado com sucesso!")

# Função para adicionar post
def add_post():
    print("Adicionar post")
    title = input("Digite o título: ")
    content = input("Conteúdo:\n")
    author_id = input("Id do autor: ")
    user = session.query(User).filter_by(id=author_id).first()
    if user:
         post = Post(title=title,content=content,author=user)
         session.add(post)
         session.commit()
         print("Post adicionado com sucesso!")
    else:
         print("Usuário não encontrado")

# Função para consultar usuários e post
def query_users_posts():
     users = session.query(User).join(User.posts).order_by(User.name).all()
     for user in users:
          print(f'User: {user.name}, Email: {user.email}')
          for post in user.posts:
               print(f'Post: {post.title}, Conteúdo: {post.content}') 
        
