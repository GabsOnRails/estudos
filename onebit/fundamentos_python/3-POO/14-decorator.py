''' 
Permite adicionar um comportamento a um objeto já existente em tempo de execução.
Oferecem uma alternativa flexível ao uso da herança para estender uma funcionalidade.

'''

#Importand decorators
from criando_decorator import my_decorator, uppercase_decorator, split_string

# Exemplo 1
@my_decorator # -> Usando o decorator que criei | a função está como o parâmetro do decorator.
def my_function():
    print("Dentro da função")

my_function()

# Exemplo 2
@uppercase_decorator # -> Precisamos declarar o decorator para utilizá-lo 
def text():
    return "Hello World"
print(text())

# Exemplo 3
@split_string # -> Usando dois decorators
@uppercase_decorator
def split():
    return "Aprendendo Python, massa demais!"

print(split())
