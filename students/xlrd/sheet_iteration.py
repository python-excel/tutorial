from xlrd import open_workbook

book = open_workbook('odd.xls')
sheet0 = book.sheet_by_index(0)
sheet1 = book.sheet_by_index(1)

print sheet0.row(0)
print sheet0.col(0)
print
print sheet0.row_slice(0,1)
print sheet0.row_slice(0,1,2)
print sheet0.row_values(0,1)
print sheet0.row_values(0,1,2)
print sheet0.row_types(0,1)
print sheet0.row_types(0,1,2)
print
print sheet1.col_slice(0,1)
print sheet0.col_slice(0,1,2)
print sheet1.col_values(0,1)
print sheet0.col_values(0,1,2)
print sheet1.col_types(0,1)
print sheet0.col_types(0,1,2)
