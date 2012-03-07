from xlrd import open_workbook

book = open_workbook('simple.xls')

print book.nsheets

for sheet_index in range(book.nsheets):
    print book.sheet_by_index(sheet_index)

print book.sheet_names()
for sheet_name in book.sheet_names():
    print book.sheet_by_name(sheet_name)

for sheet in book.sheets():
    print sheet
