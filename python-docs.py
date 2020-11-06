# 반드시 python-docs를 설치할것.
from docx import Document
from docx.shared import Inches

document = Document()

with open('law.txt','r',encoding='utf-8') as f:
    file_list = list()
    for line in f:
        if line != '\n':
            file_list.append(line[:-1])
    table = document.add_table(rows = len(file_list), cols = 1)
    for index,file_element in enumerate(file_list):
        row_cell = table.rows[index].cells
        row_cell[0].text = file_element
    document.add_page_break()
    document.save("law_table.docx")
