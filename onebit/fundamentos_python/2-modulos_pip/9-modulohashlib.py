# Módulo para criptografia

import hashlib

# 1- Verificar os algoritmos disponíveis:
# print(hashlib.algorithms_available)

# 2- Verificar os que posso usar de acordo com meu SO:
# print(hashlib.algorithms_guaranteed)

# 3- Usando o Sha256 -> Recomendado hoje em dia / de 256 pra frente.
algoritmo = hashlib.sha256()
mensagem = "Mash cabeça de cogumelo".encode()
algoritmo.update(mensagem)
print(algoritmo.hexdigest()) # -> Trabalhando com hexa digítos
