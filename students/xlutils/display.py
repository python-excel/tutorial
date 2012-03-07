from xlrd import open_workbook
from xlutils.display import quoted_sheet_name
from xlutils.display import cell_display

wb = open_workbook('source.xls')

print quoted_sheet_name(wb.sheet_names()[0])
print repr(quoted_sheet_name(u'Price(\xa3)','utf-8'))
print quoted_sheet_name(u'My Sheet')
print quoted_sheet_name(u"John's Sheet")

sheet = wb.sheet_by_index(0)
print cell_display(sheet.cell(1,1))
print cell_display(sheet.cell(1,3),wb.datemode)
