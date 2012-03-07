from datetime import date,time,datetime
from decimal import Decimal
from xlwt import Workbook,Style

wb = Workbook()

ws = wb.add_sheet('Type examples')

ws.row(0).write(0,u'\xa3')
ws.row(0).write(1,'Text')

ws.row(1).write(0,3.1415)
ws.row(1).write(1,15)
ws.row(1).write(2,265L)
ws.row(1).write(3,Decimal('3.65'))
ws.row(2).set_cell_number(0,3.1415)
ws.row(2).set_cell_number(1,15)
ws.row(2).set_cell_number(2,265L)
ws.row(2).set_cell_number(3,Decimal('3.65'))

ws.row(3).write(0,date(2009,3,18))
ws.row(3).write(1,datetime(2009,3,18,17,0,1))
ws.row(3).write(2,time(17,1))
ws.row(4).set_cell_date(0,date(2009,3,18))
ws.row(4).set_cell_date(1,datetime(2009,3,18,17,0,1))
ws.row(4).set_cell_date(2,time(17,1))

ws.row(5).write(0,False)
ws.row(5).write(1,True)
ws.row(6).set_cell_boolean(0,False)
ws.row(6).set_cell_boolean(1,True)

ws.row(7).set_cell_error(0,0x17)
ws.row(7).set_cell_error(1,'#NULL!')

ws.row(8).write(
    0,'',Style.easyxf('pattern: pattern solid, fore_colour green;'))
ws.row(8).write(
    1,None,Style.easyxf('pattern: pattern solid, fore_colour blue;'))
ws.row(9).set_cell_blank(
    0,Style.easyxf('pattern: pattern solid, fore_colour yellow;'))

ws.row(10).set_cell_mulblanks(
    5,10,Style.easyxf('pattern: pattern solid, fore_colour red;')
    )

wb.save('types.xls')
