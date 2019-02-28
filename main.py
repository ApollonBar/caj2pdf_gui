from os import path
from shutil import move
from sys import argv, exit
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

        self.caj_file_open_button.clicked.connect(self.open_caj)
        self.pdf_file_open_button.clicked.connect(self.open_pdf)
        self.show_button.clicked.connect(self.show_caj)
        self.convert.clicked.connect(self.convert_caj)
        self.outlines.clicked.connect(self.outlines_caj)

    def log(self, s):
        self.logger.addItem(s)

    def check_file_exist(self, txt, suffix):
        if path.exists(txt) and path.isfile(txt) and txt[-4:] == suffix:
            return True
        self.log(suffix + '文件地址错误')
        return False

    def getDefaultOutput(self):
        txt = self.caj_address.text()
        return txt[:-4] + '.pdf'

    def show_caj(self):
        self.logger.clear()
        self.log('show')
        if self.check_file_exist(self.caj_address.text(), '.caj') is False:
            self.log('--------')
            return
        caj = CAJParser(self.caj_address.text())
        self.log('File: %s' % self.caj_address.text())
        self.log('Type: %s' % caj.format)
        self.log('Page count: %s' % caj.page_num)
        self.log('Outlines count: %s' % caj.toc_num)
        self.log('--------')

    def convert_caj(self):
        self.log('convert')
        if self.check_file_exist(self.caj_address.text(), '.caj') is False:
            self.log('--------')
            return
        try:
            caj = CAJParser(self.caj_address.text())
            caj.convert(self.getDefaultOutput())
            self.log('output: %s' % self.getDefaultOutput())
        except Exception as e:
            self.log('Exception: %s' % e)
            self.log(format_exc())
        self.log('--------')

    def outlines_caj(self):
        self.log('outlines')
        if self.check_file_exist(self.caj_address.text(), '.caj') is False:
            self.log('--------')
            return
        if self.check_file_exist(self.pdf_address.text(), '.pdf') is False:
            self.log('--------')
            return
        try:
            caj = CAJParser(self.caj_address.text())
            toc = caj.get_toc()
            add_outlines(toc, self.pdf_address.text(), "tmp.pdf")
            move("tmp.pdf", self.pdf_address.text())
            self.log('output: %s' % self.pdf_address.text())
        except Exception as e:
            self.log('Exception: %s' % e)

        self.log('--------')

    def open_caj(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择caj文件", '.', 'caj file(*.caj)')
        self.caj_address.setText(file_path)

    def open_pdf(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "选择需要添加outlines的pdf文件", '.', 'pdf file(*.pdf)')
        self.pdf_address.setText(file_path)


if __name__ == '__main__':
    app = QApplication(argv)
    MainWindow = myWindow()  #
    # QMainWindow()
    MainWindow.show()
    exit(app.exec_())
