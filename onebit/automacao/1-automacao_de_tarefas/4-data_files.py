# Criando algoritmo para obter metadados do arquivo

from pathlib import Path
from datetime import datetime



path = Path('files','dados','teste2.txt')
# print(path.stat())

# Obtendo metadados de criação e transformando eles em dados legiveis
stats = path.stat()
second_created = stats.st_ctime 
date_created = datetime.fromtimestamp(second_created) # timestamp retorna a data e hora, para que cada arquivo seja exclusivo
# print(date_created)
# Formando como os dados serão mostrados
date_created_str = date_created.strftime('%d-%m-%Y %H:%M:%S')
print(date_created_str)