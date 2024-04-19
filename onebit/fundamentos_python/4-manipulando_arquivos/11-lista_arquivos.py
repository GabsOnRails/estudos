# Listar arquivos dentro de diretorios

# Importando módulos built-in.
import glob,os,zipfile

# 1 -> Pegar o caminho do diretorio atual
os.getcwd()

# 2 -> Listar arquivos dentro de um diretorio
for file in glob.glob("dados/*.txt"): # -> "*"" Lista todos os arquivos do diretorio atual
    print(file)

# 3 -> Compactar arquivos
    with zipfile.ZipFile("nomes.zip",'w') as zip:
        for file in glob.glob("dados/*.txt"):
            zip.write(file)

# 4 -> Compactar todos os arquivos do diretorio atual:
    with zipfile.ZipFile("code.zip",'w') as zip:
        for file in glob.glob("*"):
            zip.write(file)