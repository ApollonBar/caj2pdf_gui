from os import replace,path
from sys import argv,exit
from traceback import format_exc

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from caj2pdf_GUI import Ui_MainWindow
from cajparser import CAJParser
from utils import add_outlines


class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.file_open_button.clicked.connect(self.open_caj)
        self.show_button.clicked.connect(self.show_caj)
        self.convert.clicked.connect(self.convert_caj)
        self.outlines.clicked.connect(self.outlines_caj)

    def log(self, s):
        self.logger.addItem(s)

    def check_file_exist(self):
        txt = self.line_address.text()
        if path.exists(txt) and path.isfile(txt):
            return True
        self.log('caj文件地址错误')
        return False

    def getDefaultOutput(self):
        txt = self.line_address.text()
        return txt[:-4] + '.pdf'

    def show_caj(self):
        self.log('show')
        if self.check_file_exist() is False:
            self.log('--------')
            return
        caj = CAJParser(self.line_address.text())
        self.log('File: %s' % self.line_address.text())
        self.log('Type: %s' % caj.format)
        self.log('Page count: %s' % caj.page_num)
        self.log('Outlines count: %s' % caj.toc_num)
        self.log('--------')

    def convert_caj(self):
        self.log('convert')
        if self.check_file_exist() is False:
            self.log('--------')
            return
        try:
            caj = CAJParser(self.line_address.text())
            caj.convert(self.getDefaultOutput())
            self.log('output: %s' % self.getDefaultOutput())
        except Exception as e:
            self.log('Exception: %s' % e)
            self.log(format_exc())
        self.log('--------')

    def outlines_caj(self):
        self.log('outlines')
        if self.check_file_exist() is False:
            self.log('--------')
            return
        try:
            caj = CAJParser(self.line_address.text())
            toc = caj.get_toc()
            add_outlines(toc, self.getDefaultOutput(), "tmp.pdf")
            replace("tmp.pdf", self.getDefaultOutput())
            self.log('output: %s' % self.getDefaultOutput())
        except Exception as e:
            self.log('Exception: %s' % e)

        self.log('--------')

    def open_caj(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择caj文件", '.', 'caj file(*.caj)')
        self.line_address.setText(file_path)


if __name__ == '__main__':
    app = QApplication(argv)
    MainWindow = myWindow()  #
    # QMainWindow()
    MainWindow.show()
    exit(app.exec_())
