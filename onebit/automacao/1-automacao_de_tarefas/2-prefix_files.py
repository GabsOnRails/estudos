#  Adicionando prefixo nos arquivos de forma automática

from pathlib import Path

root_dir = Path('dados')
file_path = root_dir.iterdir()
for path in file_path:
    new_filename = f'new-{path.stem}{path.suffix}' # Mudando o nome apenas visual, sem realizar a alteração
    print(new_filename)
    new_filepath = path.with_name(new_filename) # -> Selecioando os arquivos renomeados
    path.rename(new_filepath) # -> Realizando a renomeação