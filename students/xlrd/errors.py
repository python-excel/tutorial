from xlrd import open_workbook,error_text_from_code

book = open_workbook('types.xls')
sheet = book.sheet_by_index(0)

print error_text_from_code[sheet.cell(5,2).value]
print error_text_from_code[sheet.cell(5,3).value]

