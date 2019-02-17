from docx import Document
from docx.shared import Inches

document = Document()

document.add_heading('Document Title', 0)

p = document.add_paragraph('A plain paragraph having some ')
p.add_run('bold').bold = True
p.add_run(' and some ')

document.add_heading('Example Heading', level=1)
document.add_paragraph('Intense quote', style='Intense Quote')

document.add_line_break()

document.save('demo.docx')