from xlwt import Workbook, Formula

book = Workbook()

sheet1 = book.add_sheet('Sheet 1')
sheet1.write(0,0,10)
sheet1.write(0,1,20)
sheet1.write(1,0,Formula('A1/B1'))

sheet2 = book.add_sheet('Sheet 2')
row = sheet2.row(0)
row.write(0,Formula('sum(1,2,3)'))
row.write(1,Formula('SuM(1;2;3)'))
row.write(2,Formula("$A$1+$B$1*SUM('ShEEt 1'!$A$1:$b$2)"))

book.save('formula.xls')
