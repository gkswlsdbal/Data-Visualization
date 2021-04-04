import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtWidgets import *

import main_event as ev

form_class = uic.loadUiType('ProjectUI.ui')[0]

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    fileCount = 0
    currentData = ''
    newData = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.insertButton.clicked.connect(self.btnClick)
        self.installEventFilter(self)
        self.setAcceptDrops(True)
        self.FileList.itemDoubleClicked.connect(self.fileClick)
        self.actionCellAbsorption.triggered.connect(self.actionCells)
        self.actionFileAbsorption.triggered.connect(self.actionFiles)
        self.menuSave.triggered.connect(self.actionSaves)
        self.actionSave.triggered.connect(self.newSaves)

    # 파일 드레그앤 드랍
    def eventFilter(self, object, event):
        if object is self:
            ev.eventFilter(self, object, event)
        return False

    def btnClick(self):
        ev.btnClick(self)

    def fileClick(self):
        ev.fileClick(self)

    def fileCheck(self, file):
        ev.fileCheck(self, file)

    def actionCells(self):
        ev.CellAbsorption(self)

    def actionFiles(self):
        ev.FileAbsorption(self)

    def actionSaves(self):
        ev.FileSave(self)

    def newSaves(self):
        ev.newSave(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
