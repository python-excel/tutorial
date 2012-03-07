from xlrd import open_workbook

def cell_contents(sheet,row_x):
    result = []
    for col_x in range(2,sheet.ncols):
        cell = sheet.cell(row_x,col_x)
        result.append((cell.ctype,cell,cell.value))
    return result

sheet = open_workbook('types.xls').sheet_by_index(0)

print 'XL_CELL_TEXT',cell_contents(sheet,1)
print 'XL_CELL_NUMBER',cell_contents(sheet,2)
print 'XL_CELL_DATE',cell_contents(sheet,3)
print 'XL_CELL_BOOLEAN',cell_contents(sheet,4)
print 'XL_CELL_ERROR',cell_contents(sheet,5)
print 'XL_CELL_BLANK',cell_contents(sheet,6)
print 'XL_CELL_EMPTY',cell_contents(sheet,7)

print
sheet = open_workbook(
            'types.xls',formatting_info=True
            ).sheet_by_index(0)

print 'XL_CELL_TEXT',cell_contents(sheet,1)
print 'XL_CELL_NUMBER',cell_contents(sheet,2)
print 'XL_CELL_DATE',cell_contents(sheet,3)
print 'XL_CELL_BOOLEAN',cell_contents(sheet,4)
print 'XL_CELL_ERROR',cell_contents(sheet,5)
print 'XL_CELL_BLANK',cell_contents(sheet,6)
print 'XL_CELL_EMPTY',cell_contents(sheet,7)

