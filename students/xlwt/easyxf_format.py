from datetime import date
from xlwt import Workbook, easyxf

book = Workbook()
sheet = book.add_sheet('A Date')

sheet.write(1,1,date(2009,3,18),easyxf(
    'font: name Arial;'
    'borders: left thick, right thick, top thick, bottom thick;'
    'pattern: pattern solid, fore_colour red;',
    num_format_str='YYYY-MM-DD'
    ))

book.save('date.xls')
