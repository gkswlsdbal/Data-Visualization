import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
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
        self.tabWidget.resize(200, 300)

        self.fig = plt.figure(1)
        self.fig.set_size_inches(6.5, 4)
        self.canvas = FigureCanvas(self.fig)
        self.graphLayout.addWidget(self.canvas)
        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)


        #추가
        self.actionSetting.triggered.connect(self.UISetting)
        self.secColListLeftTitle.setAlignment(Qt.AlignCenter)
        self.secColListRightTitle.setAlignment(Qt.AlignCenter)
        self.menuBar().setStyleSheet("""
                                        QMenuBar::item:pressed {background: rgb(90, 120, 215);}
                                        QMenu::item:selected {background: rgb(90, 120, 215);}
                                        QMenuBar {border: 1px solid;
                                                  border-bottom-color: %s;
                                                  border-top-color: transparent;
                                                  border-left-color: transparent;
                                                  border-right-color: transparent;
                                                  }
                                     """ % (QColor(221, 221, 221).name()))

        saveAction = QAction(QIcon('img/save.png'), 'Save', self)
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.contextMenu)

        fAbsorAction = QAction(QIcon('img/diffrence.png'), 'File absorption', self)
        fAbsorAction.setStatusTip('File absorption')
        fAbsorAction.triggered.connect(self.actionFiles)

        cAbsorAction = QAction(QIcon('img/intersect.png'), 'Cell absorption', self)
        cAbsorAction.setStatusTip('Cell absorption')
        cAbsorAction.triggered.connect(self.actionCells)

        settAction = QAction(QIcon('img/setting.png'), 'Setting', self)
        settAction.setStatusTip('Setting')
        settAction.triggered.connect(self.UISetting)

        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(self.exitAction)

        self.toolbar = self.addToolBar('toolBar')
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(fAbsorAction)
        self.toolbar.addAction(cAbsorAction)
        self.toolbar.addAction(settAction)
        self.toolbar.addAction(exitAction)


    def contextMenu(self):
        saveAction = QAction('Save')
        saveAction.triggered.connect(self.actionSaves)

        saveAsAction = QAction('Save as')
        saveAsAction.triggered.connect(self.newSaves)

        contextMenu = QMenu(self)
        contextMenu.addAction(saveAction)
        contextMenu.addAction(saveAsAction)
        contextMenu.setContextMenuPolicy(Qt.ActionsContextMenu)

        contextMenu.exec_(QCursor().pos())


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

    #추가
    def UISetting(self):
        ev.openSettingWindow(self)
        self.actionSetting.setEnabled(False)


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

    #창이 닫힐때 진짜 닫을 껀지 물어봅니다.
    #지금은 귀찮으니까 주석처리하고 마지막 점검 때 다시 풀읍시다.
    # def closeEvent(self, event):
    #     reply = QtWidgets.QMessageBox.question(self, 'Message',"종료하시겠습니까?",
    #                                        QMessageBox.Yes | QMessageBox.No,)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
