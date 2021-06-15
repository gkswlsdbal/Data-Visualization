import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtCore
import chart_function
import fileData
import main_event as ev
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import function
import preprocessing
import ColumnChart_function as ccf
import checkIniFile
import chartPrediction


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
        self.setWindowIcon(QIcon('img/Dash.png'))
        self.setWindowTitle("Dash")
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
        self.tabWidget.resize(200, 300)
        self.tabWidget.currentChanged.connect(self.tabChange)

        self.fig = plt.figure(1)
        self.fig.set_size_inches(7.8, 3.5)
        self.canvas = FigureCanvas(self.fig)
        self.graphLayout.addWidget(self.canvas)
        self.tabOneSplitter.setStretchFactor(0, 1)
        self.cid = self.canvas.mpl_connect('motion_notify_event', self.move_cursor)
        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)

        self.fig_sec = plt.figure(2)
        
        self.fig_sec.set_size_inches(8, 8)
        self.fig_sec.subplots_adjust(left=0.1,
                                     bottom=0.05,
                                     right=0.99,
                                     top=0.95,
                                     wspace=0.23,
                                     hspace=0.23)
        self.canvas_sec = FigureCanvas(self.fig_sec)
        self.fig.set_facecolor(QColor(244, 244, 244).name())
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.canvas_sec)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.secGraphLayout.addWidget(self.scroll)

        self.secChartCombo.currentIndexChanged.connect(self.secChartComboChanged)
        self.showBtn.clicked.connect(self.secShowBtn)
        self.notshowBtn.clicked.connect(self.secNotShowBtn)
        self.showingColList.itemDoubleClicked.connect(self.secShowCellClick)
        self.unshowingColList.itemDoubleClicked.connect(self.secNotShowCellClick)

        self.actionSetting.triggered.connect(self.UISetting)
        self.secColListLeftTitle.setAlignment(Qt.AlignCenter)
        self.secColListRightTitle.setAlignment(Qt.AlignCenter)

        saveAction = QAction(QIcon('img/save.png'), 'Save', self)
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.contextMenu)

        a = QLabel("")
        a.setStyleSheet("padding-left:5px;")
        b = QLabel("")
        b.setStyleSheet("padding-left:5px;")
        c = QLabel("")
        c.setStyleSheet("padding-left:5px;")
        d = QLabel("")
        d.setStyleSheet("padding-left:5px;")
        e = QLabel("")
        e.setStyleSheet("padding-left:5px;")
        f = QLabel("")
        f.setStyleSheet("padding-left:5px;")
        g = QLabel("")
        g.setStyleSheet("padding-left:5px;")

        fAbsorAction = QAction(QIcon('img/diffrence.png'), 'File absorption', self)
        fAbsorAction.setStatusTip('File absorption')
        fAbsorAction.triggered.connect(self.actionFiles)

        cAbsorAction = QAction(QIcon('img/intersect.png'), 'Cell absorption', self)
        cAbsorAction.setStatusTip('Cell absorption')
        cAbsorAction.triggered.connect(self.actionCells)

        #self.settAction = QAction(QIcon('img/setting.png'), 'Setting', self)
        #self.settAction.setStatusTip('Setting')
        #self.settAction.triggered.connect(self.UISetting)

        exitAction = QAction(QIcon('img/exit.png'), 'Exit', self)
        exitAction.setStatusTip('Exit')
        exitAction.triggered.connect(self.exitAction)

        preprocessAction = QAction(QIcon('img/preprocessing.png'), 'preprocessing', self)
        preprocessAction.setStatusTip('preprocessing')
        preprocessAction.triggered.connect(self.preprocessAction)

        chartAction = QAction(QIcon('img/chartPop.png'), 'Chart', self)
        chartAction.setStatusTip('Chart')
        chartAction.triggered.connect(self.chartAction)

        image = QPushButton(QIcon('img/Dash2.png'),'',self)
        image.setStyleSheet('margin-left:1150px;'" border-style: solid;"
            "border-width: 1px;"
            "border-color: rgb(68,68,68);")

        Label = QLabel(" Dash")
        Label.setStyleSheet('font: 87 14pt "Arial Black"; color:white;')
        self.toolbar = self.addToolBar('toolBar')
        self.toolbar.addWidget(a)
        self.toolbar.addAction(chartAction)
        self.toolbar.addWidget(b)
        self.toolbar.addAction(saveAction)
        self.toolbar.addWidget(c)
        self.toolbar.addAction(preprocessAction)
        self.toolbar.addWidget(d)
        self.toolbar.addAction(fAbsorAction)
        self.toolbar.addWidget(e)
        self.toolbar.addAction(cAbsorAction)
        self.toolbar.addWidget(f)
        #self.toolbar.addAction(self.settAction)
        self.toolbar.addAction(exitAction)
        self.toolbar.addWidget(image)
        self.toolbar.addWidget(Label)
        self.toolbar.setMovable(False)

        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{"
                                                          "font: 800 12pt '맑은 고딕';"
                                                          "background-color:rgb(241,241,241);""}")
        self.tableWidget.verticalHeader().setStyleSheet("QHeaderView::section{"
                                                          "font: 800 12pt '맑은 고딕';"
                                                          "margin-left:18px;"
                                                          "background-color:rgb(241,241,241);""}")
        self.tableWidget.verticalHeader().setMinimumWidth(45)
        #self.toolbar.setStyleSheet("QToolBar {background-color: white;}")

        #self.chckIniFile()

    def tabChange(self, index):
        if index == 0:
            self.tableWidget.resize(750,300)
            self.tableWidget.setVisible(True)
        else:
            self.tableWidget.resize(0,0)
            self.tableWidget.setVisible(False)


    def chckIniFile(self):
        checkIniFile.chckInitFst(self)

    def changeBorder(self):
        checkIniFile.chgToolBarBorder(self)
        
    def closeEvent(self, event):
        # # 창이 닫힐때 진짜 닫을 껀지 물어봅니다.
        # reply = QMessageBox.question(self, 'Message',"종료하시겠습니까?",
        #                                        QMessageBox.Yes | QMessageBox.No,)
        # if reply == QMessageBox.Yes:
        #     event.accept()
        # else:
        #     event.ignore()

        checkIniFile.writeIniLast(self)

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

    def chartAction(self):
        chartPrediction.ChartDialog(self)

    def eventFilter(self, object, event):
        if object is self:
            ev.eventFilter(self, object, event)
        return False

    def btnClick(self):
        ev.btnClick(self)

    def fileClick(self):
        self.cellFlag = False
        self.fig.clear()
        self.canvas.draw()
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

    def UISetting(self):
        ev.openSettingWindow(self)
        self.actionSetting.setEnabled(False)

    def cellClick(self):
        function.cellInfo(self)
        chart_function.cellClick(self)

    def cellChange(self):
        self.cellFlag = True

    def barGraphBtnClick(self):
        chart_function.barGraphBtnClick(self)

    def lineGraphBtnClick(self):
        chart_function.lineGraphBtnClick(self)

    def pieChartBtnClick(self):
        chart_function.pieChartBtnClick(self)

    def scatterChartBtnClick(self):
        chart_function.scatterChartBtnClick(self)

    def exitAction(self):
        ev.exitAction(self)

    def preprocessAction(self):
        preprocessing.OptionWindow(self)

    def move_cursor(self, event):
        chart_function.move_cursor(self, event)

    def secChartComboChanged(self):
        ccf.secChartComboChanged(self)

    def secShowBtn(self):
        ccf.secShowBtn(self)

    def secNotShowBtn(self):
        ccf.secNotShowBtn(self)

    def secShowCellClick(self):
        ccf.secShowCellClick(self)

    def secNotShowCellClick(self):
        ccf.secNotShowCellClick(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    myWindow = WindowClass()
    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()
