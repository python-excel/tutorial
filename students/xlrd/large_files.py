from xlrd import open_workbook

book = open_workbook('simple.xls',on_demand=True)

for name in book.sheet_names():
    if name.endswith('2'):
        sheet = book.sheet_by_name(name)
        print sheet.cell_value(0,0)
        book.unload_sheet(name)
