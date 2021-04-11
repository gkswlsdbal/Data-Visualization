import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt
import main_event as ev
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import function
import cellInfo
import addTab

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
        self.cellList.itemClicked.connect(self.cellClick)
        self.fig = plt.figure()
        self.fig.set_size_inches(5.5, 4)
        self.canvas = FigureCanvas(self.fig)
        self.graphLayout.addWidget(self.canvas)

        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)
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
        self.colInfoListWidget.clear()
        ev.fileClick(self)

    def fileCheck(self, file):
        ev.fileCheck(self, file)
    def actionCells(self):
        ev.CellAbsorption(self)
    def actionFiles(self):
        ev.FileAbsorption(self)

    def actionSaves(self):
        ev.FileSave(self)
    def drawCellInfo(self):
        cellInfo.cellInfo(self)

    def newSaves(self):
        ev.newSave(self)
    def addTab(self):
        addTab.addTab(self)

    def cellClick(self):
        function.cellInfo(self)
        function.cellClick(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()