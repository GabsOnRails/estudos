# Importando módulo OS, posteriormente preciso ver mais sobre, é um módulo interessante

import os

# help('os') # -> Consultar funcionalidades do módulo

# Retornar a pasta atual
print(os.getcwd())

# Listar arquivos e pastas
print(os.listdir())

# Apresentar versão SO (Kernel).
os.system('uname -r') # -> Não usamos o print porque é como um script, relacionado ao próprio sistema.

# Configurações da máquina
os.system('lsb_release -a') # -> Código para Linux.

# Limpar a tela
# os.system('clear') -> Código para Linux.

