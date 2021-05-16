from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm
import fileData
import pandas as pd
import os.path
import chartPrediction_function as cpf


class ChartDialog(QDialog):

    def __init__(self, parent):

        super(ChartDialog, self).__init__(parent)
        setUI = 'ChartUI.ui'
        loadUi(setUI, self)

        self.fileTreeWidget.clear()
        self.colList.clear()
        self.rowList.clear()
        self.splitter.setStretchFactor(1, 1)
        self.midSplitter.setStretchFactor(1, 1)
        self.fig = plt.figure(3)
        self.fig.set_size_inches(7.8, 3.5)
        self.canvas = FigureCanvas(self.fig)
        self.chartWidget.layout().addWidget(self.canvas)
        path = '/Windows/Fonts/gulim.ttc'
        font_name = fm.FontProperties(fname=path, size=50).get_name()
        plt.rc('font', family=font_name)

        self.fileTreeWidget.itemDoubleClicked.connect(self.addCol)
        self.allClearBtn.clicked.connect(self.allClear)
        self.saveBtn.clicked.connect(self.save)
        self.colList.itemDoubleClicked.connect(lambda: self.delCol(self.colList, self.colList.currentRow()))
        self.colList.currentItemChanged.connect(self.moveCol)
        self.rowList.itemDoubleClicked.connect(lambda: self.delCol(self.rowList, self.rowList.currentRow()))
        self.rowList.currentItemChanged.connect(self.moveRow)

        itemTop = []
        itemChild = []
        for i in range(0, len(fileData.fileName)):

            itemTop.append(QTreeWidgetItem(self.fileTreeWidget))
            itemTop[i].setText(0, fileData.fileName[i])
            fl = fileData.fileLinks[i]
            path, ext = os.path.splitext(fl)
            if ext == ".xlsx":
                df = pd.read_excel(fl)
            elif ext == ".csv":
                df = pd.read_csv(fl)
            j = 0
            for title in list(df.columns):
                itemChild.append(QTreeWidgetItem(itemTop[i]))
                itemChild[j].setText(0, title)
                j += 1
            itemChild = []

        self.show()

    # def saveContextMenu(self):
    #     saveImage = QAction('Save as image')
    #     saveImage.triggered.connect(self.saveAs)
    #
    #     saveXlsx = QAction('Save as xlsx')
    #     saveXlsx.triggered.connect(self.saveAs)
    #
    #     saveCsv = QAction('Save as csv')
    #     saveCsv.triggered.connect(self.saveAs)
    #
    #     contextMenu = QMenu(self)
    #     contextMenu.addAction(saveImage)
    #     contextMenu.addAction(saveXlsx)
    #     contextMenu.addAction(saveCsv)
    #     contextMenu.setContextMenuPolicy(Qt.ActionsContextMenu)
    #
    #     contextMenu.exec_(QCursor().pos())

    def allClear(self):
        reply = QMessageBox.question(self, 'Message',"모든 정보를 삭제하시겠습니까?",
                                               QMessageBox.Yes | QMessageBox.No,)
        if reply == QMessageBox.Yes:
            self.colList.clear()
            self.rowList.clear()
            self.fig.clear()
            self.canvas.draw()

    def save(self):
        img = QFileDialog.getSaveFileName(self, self.tr("Save as Image"), "./",
                                          self.tr('All File(*);; PNG(*.png);; JPG(*.jpg);; SVG(*.svg'))
        if img[0]:
            self.fig.savefig(img[0])

    def addCol(self):
        cpf.addCol(self)
        cpf.graphReFresh(self)

    def moveCol(self):
        print('moveCol')
        cpf.graphReFresh(self)

    def moveRow(self):
        print('moveRow')
        cpf.graphReFresh(self)

    def delCol(self, list, ind):
        list.takeItem(ind)
        cpf.graphReFresh(self)
