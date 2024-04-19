'''
O desafio é criar um programa em Python
que organiza arquivos de acordo com os seguintes tipos de arquivo:
 - exe
 - csv
 - jpg
 - pdf
 - zip
'''
from pathlib import Path
from datetime import datetime

# Criando lógica para obter os caminhos presente no diretório   
root_dir = Path('files','exe1')

# Irá ler tudo dentro da pasta
file_paths = root_dir.glob("**/*") 
for path in file_paths:
    # print(path)
    if path.is_file(): # -> Se existir arquivo
        # print(path.parts[-2]) # -> Para retornar partes especificas, no caso o nome do diretório
        parent_folder = path.parts[-2] # -> Descobrindo o nome da pasta
        stats = path.stat()
        second_created = stats.st_ctime
        date_created = datetime.fromtimestamp(second_created)
        date_created_str = date_created.strftime('%d-%m-%Y %H:%M:%S')
        new_filename = f'{date_created_str}-{path.name}.{parent_folder}'
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)
print("Alterações realizadas com sucesso!")
        
    

