from xlwt import Workbook

w = Workbook()

ws = w.add_sheet('Normal')
ws.write(0,0,'Some text')
ws.normal_magn = 75

ws = w.add_sheet('Page Break Preview')
ws.write(0,0,'Some text')
ws.preview_magn = 150
ws.page_preview = True

w.save('zoom.xls')
