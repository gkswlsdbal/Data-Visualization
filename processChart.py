from PyQt5 import uic, QtGui
from matplotlib import style, gridspec
from matplotlib.backends.backend_template import FigureCanvas
import missingno as msno

import DuplicatePR
import fileData
import preprocessing_Data
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


form_class1 = uic.loadUiType('processChartUI.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'processChartUI.ui'
        uic.loadUi(option_ui, self)

        self.pushButton_3.clicked.connect(self.btnClick1)
        self.pushButton_2.clicked.connect(self.btnClick2)
        self.pushButton_4.clicked.connect(self.btnClick3)
        self.pushButton_5.clicked.connect(self.btnClick4)
        self.pushButton_6.clicked.connect(self.btnClick5)
        self.pushButton_7.clicked.connect(self.btnClick6)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)

        style.use('ggplot') or plt.style.use('ggplot')
        plt.style.use('fivethirtyeight')
        plt.rc('font', family='Malgun Gothic')
        plt.rc('axes', unicode_minus=False)
        self.fig = plt.figure(2,figsize=(15,8))
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)
        self.show()

    def btnClick1(self):
        self.fig.clear()
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        spec = gridspec.GridSpec(ncols=2, nrows=1,
                                 width_ratios=[1, 1])
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)

        ax = self.fig.add_subplot(spec[0])
        df_missing = fileData.dfs[fileIndex].isna().sum()
        df_missing.plot.bar(color='gray', figsize=(12, 6.22), rot=0, ax=ax)
        plt.title("결측치 Bar", fontsize=12)
        plt.xticks(rotation=90,fontsize=8)
        plt.yticks(fontsize=8)

        ax2 = self.fig.add_subplot(spec[1])
        if preprocessing_Data.completeFlag:
            df_missing = preprocessing_Data.completeDfs.isna().sum()
        else:
            df_missing = preprocessing_Data.processingDfs.isna().sum()
        df_missing.plot.bar(color='gray', rot=0, ax=ax2)
        plt.title("결측치 제거 Bar", fontsize=12)
        plt.xticks(rotation=90,fontsize=8)
        plt.yticks(fontsize=8)
        plt.subplots_adjust(left=0.04,bottom=0.26, top=0.9, wspace=0.3)
        self.canvas.draw()

    def btnClick2(self):

        self.fig.clear()
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        spec = gridspec.GridSpec(ncols=2, nrows=1,
                                 width_ratios=[1, 1])
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        ax1 = self.fig.add_subplot(spec[0])
        msno.matrix(fileData.dfs[fileIndex],fontsize=8,ax=ax1)
        plt.xticks(rotation=45)
        plt.xlabel("결측치 Matrix")
        ax3 = self.fig.add_subplot(spec[1])
        if preprocessing_Data.completeFlag:
            msno.matrix(preprocessing_Data.completeDfs, fontsize=8, ax=ax3)
        else:
            msno.matrix(preprocessing_Data.processingDfs, fontsize=8, ax=ax3)
        plt.xticks(rotation=45)
        plt.xlabel("결측치 제거 Matrix")
        plt.subplots_adjust(left=0.04, bottom=0.2, right=0.9,top=0.7, wspace=0.3)
        self.canvas.draw()

    def btnClick3(self):
        self.fig.clear()

        spec = gridspec.GridSpec(ncols=1, nrows=1,
                                 )
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        ax1 = self.fig.add_subplot(spec[0])
        msno.heatmap(fileData.dfs[fileIndex], fontsize=12, ax=ax1)
        plt.xticks(rotation=90,fontsize=6)
        plt.yticks(fontsize=8)
        plt.title("결측치 HeatMap",fontsize=15)
        plt.subplots_adjust(left=0.2, bottom=0.3, top=0.9)
        self.pushButton_6.setVisible(True)
        self.canvas.draw()

    def btnClick4(self):
        self.fig.clear()
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(False)
        spec = gridspec.GridSpec(ncols=2, nrows=1,
                                 width_ratios=[1, 1])
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        ax1 = self.fig.add_subplot(spec[0])
        msno.dendrogram(fileData.dfs[fileIndex], fontsize=8, ax=ax1)
        plt.xticks(rotation=45)
        plt.xlabel("결측치 dendrogram")
        ax3 = self.fig.add_subplot(spec[1])
        if preprocessing_Data.completeFlag:
            msno.dendrogram(preprocessing_Data.completeDfs, fontsize=8, ax=ax3)
        else:
            msno.dendrogram(preprocessing_Data.processingDfs, fontsize=8, ax=ax3)
        plt.xticks(rotation=45)
        plt.xlabel("결측치 제거 dendrogram")
        plt.subplots_adjust(left=0.04,bottom=0.2,top=0.7, wspace=0.2)
        self.canvas.draw()

    def btnClick5(self):
        self.fig.clear()

        spec = gridspec.GridSpec(ncols=1, nrows=1,
                                 )
        ax3 = self.fig.add_subplot(spec[0])
        if preprocessing_Data.completeFlag:
            msno.heatmap(preprocessing_Data.completeDfs, fontsize=8, ax=ax3)
        else:
            msno.heatmap(preprocessing_Data.processingDfs, fontsize=8, ax=ax3)
        plt.xticks(rotation=90, fontsize=6)
        plt.yticks(fontsize=8)
        plt.title("결측치 제거 HeatMap", fontsize=15)
        plt.subplots_adjust(left=0.2, bottom=0.3, top=0.9)
        self.pushButton_6.setVisible(False)
        self.pushButton_7.setVisible(True)
        self.canvas.draw()

    def btnClick6(self):
        self.fig.clear()
        self.pushButton_7.setVisible(False)
        spec = gridspec.GridSpec(ncols=1, nrows=1,
                                 )
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        ax1 = self.fig.add_subplot(spec[0])
        msno.heatmap(fileData.dfs[fileIndex], fontsize=12, ax=ax1)
        plt.xticks(rotation=90,fontsize=6)
        plt.yticks(fontsize=8)
        plt.title("결측치 HeatMap",fontsize=15)
        plt.subplots_adjust(left=0.2, bottom=0.3, top=0.9)
        self.pushButton_6.setVisible(True)
        self.canvas.draw()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.fig.clear()