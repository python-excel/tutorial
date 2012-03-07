from xlwt import Workbook
w = Workbook()
ws = w.add_sheet('Image')
ws.insert_bitmap('python.bmp', 0, 0)
w.save('images.xls')
