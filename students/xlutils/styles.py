from xlrd import open_workbook
from xlutils.styles import Styles

book = open_workbook('source.xls',formatting_info=True)
styles = Styles(book)
sheet = book.sheet_by_index(0)

print styles[sheet.cell(1,1)].name
print styles[sheet.cell(1,2)].name

A1_style = styles[sheet.cell(0,0)]
A1_font = book.font_list[A1_style.xf.font_index]
print book.colour_map[A1_font.colour_index]
