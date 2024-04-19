# Renomeando arquivos de acordo com o diretório que está inserido

from pathlib import Path

# Criando lógica para obter os caminhos presente no diretório   
root_dir = Path('files')
# file_paths = root_dir.iterdir() # Pegando as pastas dentro do diretório
# for path in file_paths:
#     print(path)
#     for filepath in path.iterdir(): # Retornando arquivos dentro das pastas
#         print(filepath)

file_paths = root_dir.glob("**/*") # Irá ler tudo dentro da pasta
for path in file_paths:
    # print(path)
    if path.is_file(): # -> Se existir arquivo
        # print(path) # -> Somente pastas com arquivos
        # print(path.parts[-2]) # -> Para retornar partes especificas
        parent_folder = path.parts[-2] # -> Descobrindo o nome da pasta
        new_filename = f'{parent_folder}-{path.name}' # -> Renomeando arquivo
        print(new_filename)
        new_filepath = path.with_name(new_filename) # -> Lógica para efetivar a mudança de nome
        path.rename(new_filepath)
