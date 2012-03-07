from xlrd import open_workbook,empty_cell

print empty_cell.value

book = open_workbook('types.xls')
sheet = book.sheet_by_index(0)
empty = sheet.cell(6,2)
blank = sheet.cell(7,2)
print empty is blank, empty is empty_cell, blank is empty_cell

book = open_workbook('types.xls',formatting_info=True)
sheet = book.sheet_by_index(0)
empty = sheet.cell(6,2)
blank = sheet.cell(7,2)
print empty.ctype,repr(empty.value)
print blank.ctype,repr(blank.value)
