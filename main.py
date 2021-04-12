import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
import main_event as ev
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import function

form_class = uic.loadUiType('ProjectUI.ui')[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):
    fileCount = 0
    cellFlag = False

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
        self.tableWidget.cellDoubleClicked.connect(self.cellChange)
        self.barGraphBtn.clicked.connect(self.barGraphBtnClick)
        self.lineGraphBtn.clicked.connect(self.lineGraphBtnClick)
        self.pieChartBtn.clicked.connect(self.pieChartBtnClick)
        self.scatterChartBtn.clicked.connect(self.scatterChartBtnClick)
        self.actionExit.triggered.connect(self.exitAction)
        self.tabWidget.setCornerWidget(self.addTabBtn, Qt.TopRightCorner)
        self.tabWidget.resize(1300, 1000)

        self.fig = plt.figure()
        self.fig.set_size_inches(5.5, 4)
        self.canvas = FigureCanvas(self.fig)
        self.graphLayout.addWidget(self.canvas)
        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)

    def eventFilter(self, object, event):
        if object is self:
            ev.eventFilter(self, object, event)
        return False

    def btnClick(self):
        ev.btnClick(self)

    def fileClick(self):
        self.cellFlag = False
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

    def newSaves(self):
        ev.newSave(self)

    def cellClick(self):
        function.cellInfo(self)
        function.cellClick(self)

    def cellChange(self):
        self.cellFlag = True

    def barGraphBtnClick(self):
        function.barGraphBtnClick(self)

    def lineGraphBtnClick(self):
        function.lineGraphBtnClick(self)

    def pieChartBtnClick(self):
        function.pieChartBtnClick(self)

    def scatterChartBtnClick(self):
        function.scatterChartBtnClick(self)

    def exitAction(self):
        ev.exitAction(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
