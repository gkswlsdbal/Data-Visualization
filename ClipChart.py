from PyQt5 import uic, QtGui
from matplotlib.backends.backend_template import FigureCanvas
import seaborn as sns
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import DuplicatePR
import fileData
import preprocessing_Data
import preprocessing_function


form_class1 = uic.loadUiType('NormalizeChart.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):
    selectCell = []

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'NormalizeChart.ui'
        uic.loadUi(option_ui, self)
        plt.style.use('seaborn')
        plt.rc('font', family='Malgun Gothic')
        plt.rc('axes', unicode_minus=False)
        self.label.setText('            ClipData Chart')
        self.fig = plt.figure(figsize=(25, 15))
        self.canvas = FigureCanvas(self.fig)
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        axs = self.fig.add_subplot(1, 2, 1)
        if preprocessing_Data.completeFlag:
            sns.boxplot(data=preprocessing_Data.completeDfs[preprocessing_Data.selectCell], ax=axs)
        else:
            sns.boxplot(data=fileData.dfs[fileIndex][preprocessing_Data.selectCell], ax=axs)
        plt.title("이상치 제거 전",  fontsize=14)

        axs1 = self.fig.add_subplot(1, 2, 2)
        sns.boxplot(data=preprocessing_Data.processingDfs[preprocessing_Data.selectCell], ax=axs1)
        plt.title("이상치 제거 후", fontsize=14)
        axs1.set_ylim(axs.get_ylim())

        self.gridLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.show()
        self.selectCell.clear()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.fig.clear()
