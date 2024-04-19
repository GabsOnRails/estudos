# Usando módulo externo para criar arquivo pdf
from fpdf import FPDF

pdf = FPDF()
pdf.add_page() # -> Adicionar página
pdf.set_font('Arial','B',16)
pdf.cell(40,10,"Hello,Steve!") # -> Adicionar texto dentro da página
pdf.output("pdf/exemplo.pdf") # -> Local que será salvo