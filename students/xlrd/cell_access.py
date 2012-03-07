from xlrd import open_workbook,XL_CELL_TEXT

book = open_workbook('odd.xls')
sheet = book.sheet_by_index(1)

cell = sheet.cell(0,0)
print cell
print cell.value
print cell.ctype==XL_CELL_TEXT

for i in range(sheet.ncols):
    print sheet.cell_type(1,i),sheet.cell_value(1,i)
