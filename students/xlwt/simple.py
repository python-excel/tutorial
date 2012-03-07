from tempfile import TemporaryFile
from xlwt import Workbook

book = Workbook()
sheet1 = book.add_sheet('Sheet 1')
book.add_sheet('Sheet 2')

sheet1.write(0,0,'A1')
sheet1.write(0,1,'B1')
row1 = sheet1.row(1)
row1.write(0,'A2')
row1.write(1,'B2')
sheet1.col(0).width = 10000

sheet2 = book.get_sheet(1)
sheet2.row(0).write(0,'Sheet 2 A1')
sheet2.row(0).write(1,'Sheet 2 B1')
sheet2.flush_row_data()
sheet2.write(1,0,'Sheet 2 A3')
sheet2.col(0).width = 5000
sheet2.col(0).hidden = True

book.save('simple.xls')
book.save(TemporaryFile())
