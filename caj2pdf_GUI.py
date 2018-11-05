# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caj2pdf_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(382, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 4)
        self.logger = QtWidgets.QListWidget(self.centralwidget)
        self.logger.setObjectName("logger")
        self.gridLayout.addWidget(self.logger, 3, 0, 1, 4)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setMaximumSize(QtCore.QSize(93, 16777215))
        self.convert.setObjectName("convert")
        self.gridLayout.addWidget(self.convert, 2, 1, 1, 1)
        self.outlines = QtWidgets.QPushButton(self.centralwidget)
        self.outlines.setMaximumSize(QtCore.QSize(93, 16777215))
        self.outlines.setObjectName("outlines")
        self.gridLayout.addWidget(self.outlines, 2, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 2)
        self.show_button = QtWidgets.QPushButton(self.centralwidget)
        self.show_button.setMaximumSize(QtCore.QSize(93, 16777215))
        self.show_button.setObjectName("show_button")
        self.gridLayout.addWidget(self.show_button, 2, 0, 1, 1)
        self.line_address = QtWidgets.QLineEdit(self.centralwidget)
        self.line_address.setObjectName("line_address")
        self.gridLayout.addWidget(self.line_address, 1, 0, 1, 3)
        self.file_open_button = QtWidgets.QToolButton(self.centralwidget)
        self.file_open_button.setObjectName("file_open_button")
        self.gridLayout.addWidget(self.file_open_button, 1, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 7, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "caj2pdf"))
        self.label_2.setText(_translate("MainWindow", "caj2pdf 核心项目源码: (转换不了看这里)"))
        self.lineEdit.setText(_translate("MainWindow", "https://github.com/JeziL/caj2pdf"))
        self.label.setText(_translate("MainWindow", "caj文件位置:"))
        self.convert.setToolTip(_translate("MainWindow", "转换文件"))
        self.convert.setText(_translate("MainWindow", "convert"))
        self.outlines.setToolTip(_translate("MainWindow", "<html><head/><body><p>从 CAJ 文件中提取大纲信息并添加至转化后的 PDF 文件</p><p>遇到不支持的文件类型或 Bug 时，可用 CAJViewer 打印 PDF 文件，并用这条命令为其添加大纲</p></body></html>"))
        self.outlines.setText(_translate("MainWindow", "outlines"))
        self.label_3.setText(_translate("MainWindow", "caj2pdf GUI项目源码:"))
        self.show_button.setToolTip(_translate("MainWindow", "打印文件基本信息（文件类型、页面数、大纲项目数）"))
        self.show_button.setText(_translate("MainWindow", "show"))
        self.file_open_button.setText(_translate("MainWindow", "..."))
        self.lineEdit_2.setText(_translate("MainWindow", "https://github.com/cnms520/caj2pdf_gui"))

