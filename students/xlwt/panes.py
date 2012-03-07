from xlwt import Workbook
from xlwt.Utils import rowcol_to_cell

w = Workbook()
sheet = w.add_sheet('Freeze')
sheet.panes_frozen = True
sheet.remove_splits = True
sheet.vert_split_pos = 2
sheet.horz_split_pos = 10
sheet.vert_split_first_visible = 5
sheet.horz_split_first_visible = 40

for col in range(20):
    for row in range(80):
        sheet.write(row,col,rowcol_to_cell(row,col))

w.save('panes.xls')
