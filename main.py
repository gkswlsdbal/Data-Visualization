import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import main_event as ev
import cellInfo
import addTab

form_class = uic.loadUiType('ProjectUI.ui')[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.insertButton.clicked.connect(self.btnClick)
        self.installEventFilter(self)
        self.setAcceptDrops(True)
        self.FileList.itemDoubleClicked.connect(self.fileClick)
        self.actionCellAbsorption.triggered.connect(self.actionCells)
        self.actionFileAbsorption.triggered.connect(self.actionFiles)
        self.cellList.itemClicked.connect(self.drawCellInfo)
        self.addTabBtn.clicked.connect(self.drawCellInfo)

        self.tabWidget.setCornerWidget(self.addTabBtn, Qt.TopLeftCorner)#변경된 부분

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

    def drawCellInfo(self):
        cellInfo.cellInfo(self)

    def addTab(self):
        addTab.addTab(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
