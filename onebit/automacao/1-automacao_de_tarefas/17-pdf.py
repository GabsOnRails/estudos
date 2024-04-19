# Trabalhando com pdf

import PyPDF2 as pdf
from PyPDF2 import PdfReader

# 1 -> Listando versão e metódos disponíveis na biblioteca
# print(pdf.__version__)
# print(dir(pdf))

# 2 -> Importando arquivo PDF
file = open('files/2.pdf','rb')
reader = PdfReader(file)
print(reader)
# print(reader.metadata)
info = reader.metadata

# 3 -> extraindo informações
print(info.title)
print(info.author)
print(info.subject)
print(info.creator)
print(len(reader.pages)) # -> para saber a quantidade de páginas no pdf.
print(reader.pages[0].extract_text()) # -> para extrair o texto de acordo com o índice.