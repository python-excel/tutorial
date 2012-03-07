from xlwt import Workbook, easyxf

style1 = easyxf('font: name Times New Roman')
style2 = easyxf('font: name Times New Roman')
style3 = easyxf('font: name Times New Roman')

def write_cells(book):
    sheet = book.add_sheet('Content')
    sheet.write(0,0,'A1',style1)
    sheet.write(0,1,'B1',style2)
    sheet.write(0,2,'C1',style3)
    
book = Workbook()
write_cells(book)
book.save('3xf3fonts.xls')

book = Workbook(style_compression=1)
write_cells(book)
book.save('3xf1font.xls')

book = Workbook(style_compression=2)
write_cells(book)
book.save('1xf1font.xls')
