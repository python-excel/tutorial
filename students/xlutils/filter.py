import os

from xlutils.filter import BaseReader,BaseFilter,BaseWriter,process

class Reader(BaseReader):
    def get_filepaths(self):
        return [os.path.abspath('source.xls')]

class Writer(BaseWriter):
    def get_stream(self,filename):
        return file(filename,'wb')

class Filter(BaseFilter):

    pending_row = None
    wtrowxi = 0
    
    def workbook(self,rdbook,wtbook_name):
        self.next.workbook(rdbook,'filtered-'+wtbook_name)
        
    def row(self,rdrowx,wtrowx):
        self.pending_row = (rdrowx,wtrowx)
        
    def cell(self,rdrowx,rdcolx,wtrowx,wtcolx):
        if rdcolx==0:
            value = self.rdsheet.cell(rdrowx,rdcolx).value
            if value.strip().lower()=='x':
                self.ignore_row = True
                self.wtrowxi -= 1
            else:
                self.ignore_row = False
                rdrowx, wtrowx = self.pending_row
                self.next.row(rdrowx,wtrowx+self.wtrowxi)
        elif not self.ignore_row:
            self.next.cell(
                rdrowx,rdcolx,wtrowx+self.wtrowxi,wtcolx-1
                )        

process(Reader(),Filter(),Writer())
