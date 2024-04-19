# Arquivo que irá executar o algoritmo do blog

from Blog import show_menu, add_post, add_user, query_users_posts

while True:
    show_menu()
    option = int(input("Selecione uma opção: "))

    if option == 1:
        add_user()
    elif option == 2:
        add_post()
    elif option == 3:
        query_users_posts()
    elif option == 4:
        print("Saindo..")
        break
    else:
        print("Informe uma opção válida!")