# Criando um módulo para operações de pdf.

import os
import PyPDF2 as pdf
from PyPDF2 import PdfReader,PdfWriter,PdfMerger
from PIL import Image

# 1 -> Função para ler os meta dados do pdf.
def get_pdf_metadata(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        info = reader.metadata
    return info

# 2 -> Função para ler o texto do pdf.
def extract_text_from_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        results = []
        for i in range(0,len(reader.pages)):
            selected_page = reader.pages[i]
            text = selected_page.extract_text()
            results.append(text)
        return ' '.join(results)
    
# 3 -> Separando pdf por páginas
def split_pdf(pdf_path):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        for page_num in range(0,len(reader.pages)):
            selected_page = reader.pages[page_num]
            writer = PdfWriter()
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            new_filename = f'files/{filename}_{page_num+1}.pdf'
            with open(new_filename,'wb') as out:
                writer.write(out)
            print(f'PDF criado com o nome: {new_filename}')

# 4 -> Separando por páginas selecionadas.
def split_pdf_page(pdf_path,start_page:int=0,stop_page:int=0):
    with(open(pdf_path,'rb')) as f: 
        reader = PdfReader(f)
        writer = PdfWriter()
        for page_num in range(start_page,stop_page):
            selected_page = reader.pages[page_num]
            writer.add_page(selected_page)
            filename = os.path.split(pdf_path)[1]
            # print(start_page,stop_page)
            new_filename = f'files/{filename}_from_{start_page+1}_to_{stop_page+1}.pdf'
            with open(new_filename,'wb') as out:
                writer.write(out)

# 5 -> Unindo PDF's
''' Caso tenha algum arquivo corrompido ou vazio, não irá funcionar'''
# Primeiro precisamos retornar todos os arquivos pdf's
def fetch_all_pdf(parent_folder:str):
    target_files = []
    for path,subdirs,files in os.walk(parent_folder):
        for name in files:
            if name.endswith(".pdf"):
                target_files.append(os.path.join(path,name))
    return target_files
# Função merger
def merge_pdf(list_pdfs, output_filename='files/final_pdf.pdf'):
    merger = PdfMerger()
    with open(output_filename,'wb') as f:
        for file in list_pdfs:
            merger.append(file)
        merger.write(f)
# 6 -> Rotacionando pdf 
def rotate_pdf(pdf_path,page_num:int,rotation:int=90):
    with open(pdf_path,'rb') as f:
        reader = PdfReader(f)
        writer = PdfWriter()
        writer.add_page(reader.pages[page_num])
        writer.pages[page_num].rotate(rotation)
        filename = os.path.split(pdf_path)[1]
        new_filename = f'files/{filename}_{rotation}_page_rotated.pdf'
        with open(new_filename,"wb") as out:
            writer.write(out)   

# 7 -> Extraindo imagem do pdf      
def extract_images_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PdfReader(f)
        for page_num in range(0, len(reader.pages)):
            selected_page = reader.pages[page_num]
            for img_file_obj in selected_page.images:
                with open(f"files/{img_file_obj.name}", "wb") as out:
                    out.write(img_file_obj.data)

# 8 -> Converte imagem em pdf 
def convert_img_pdf(image_file):
    my_image = Image.open(image_file)
    img = my_image.convert("RGB")
    filename = f"{os.path.splitext(image_file)[0]}.pdf"
    img.save(filename)

# print(get_pdf_metadata('files/2.pdf'))
# print(extract_text_from_pdf('files/2.pdf'))
# split_pdf('files/teste.pdf')
# split_pdf_page('files/teste.pdf',0,2)
# print(fetch_all_pdf('files'))
        
# pdf_list = fetch_all_pdf('files/')
# merge_pdf(pdf_list)
# rotate_pdf('files/teste.pdf',0,180)
convert_img_pdf('files/bb_preco.png')