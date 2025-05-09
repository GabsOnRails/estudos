# Arquivo voltado para a criação de Decorators.

# Criando um decorator

def my_decorator(func):
    def wrapper():
        print("Antes de chamar a função")
        func()
        print("Depois de chamar a função")
    return wrapper 


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper