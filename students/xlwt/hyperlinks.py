from xlwt import Workbook,easyxf,Formula

style = easyxf('font: underline single')

book = Workbook()
sheet = book.add_sheet('Hyperlinks')

sheet.write(
    0, 0,
    Formula('HYPERLINK("http://www.python.org";"Python")'),
    style)

sheet.write(
    1,0,
    Formula('HYPERLINK("mailto:python-excel@googlegroups.com";"help")'),
    style)

book.save("hyperlinks.xls")
