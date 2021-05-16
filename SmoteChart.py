from PyQt5 import uic, QtGui
from matplotlib import style, gridspec, pyplot
from matplotlib.backends.backend_template import FigureCanvas
import numpy as np
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import DuplicatePR
import preprocessing_Data
import preprocessing_function

form_class1 = uic.loadUiType('SmoteChart.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'SmoteChart.ui'
        uic.loadUi(option_ui, self)

        self.pushButton_3.clicked.connect(self.btnClick1)
        self.pushButton_2.clicked.connect(self.btnClick2)

        style.use('ggplot') or plt.style.use('ggplot')
        plt.style.use('fivethirtyeight')
        plt.rc('font', family='Malgun Gothic')
        plt.rc('axes', unicode_minus=False)
        self.fig = plt.figure(2, figsize=(15,8))
        self.canvas = FigureCanvas(self.fig)
        self.gridLayout.addWidget(self.canvas)
        self.show()

    def btnClick1(self):
        self.fig.clear()

        spec = gridspec.GridSpec(ncols=2, nrows=1,
                                 width_ratios=[1, 1])
        axes3 = self.fig.add_subplot(spec[0])
        if preprocessing_Data.completeFlag:
            pyplot.bar(DuplicatePR.counter.keys(), DuplicatePR.counter.values())
        else:
            pyplot.bar(preprocessing_function.counter.keys(), preprocessing_function.counter.values())

        plt.title("SMOTE 전", fontsize=12)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        axes4 = self.fig.add_subplot(spec[1])
        if preprocessing_Data.completeFlag:
            pyplot.bar(DuplicatePR.counter1.keys(), DuplicatePR.counter1.values())
        else:
            pyplot.bar(preprocessing_function.counter1.keys(), preprocessing_function.counter1.values())
        plt.title("SMOTE 후", fontsize=12)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
        plt.subplots_adjust(left=0.1, bottom=0.16, top=0.9, wspace=0.35)
        self.canvas.draw()

    def btnClick2(self):
        self.fig.clear()

        spec = gridspec.GridSpec(ncols=2, nrows=1,
                                 width_ratios=[1, 1])
        axes = self.fig.add_subplot(spec[0])

        plt.title("SMOTE 전", fontsize=15)
        if preprocessing_Data.completeFlag:
            label = np.unique(np.array(DuplicatePR.data_y))
        else:
            label = np.unique(np.array(preprocessing_function.data_y))
        if preprocessing_Data.completeFlag:
            if len(label) <= 2:
                plt.scatter(DuplicatePR.data_X[:, 0], DuplicatePR.data_X[:, 1],
                            c=DuplicatePR.data_y, edgecolors='black', cmap='Blues_r', alpha=0.7)
            else:
                plt.scatter(DuplicatePR.data_X[:, 0], DuplicatePR.data_X[:, 1],
                            c=DuplicatePR.data_y, edgecolors='black', cmap=plt.cm.get_cmap('Blues', preprocessing_Data.SmoteDfs[preprocessing_Data.selectCell].nunique()),
                            alpha=0.7)
        else:
            if len(label) <= 2:
                plt.scatter(preprocessing_function.data_X[:, 0], preprocessing_function.data_X[:, 1],
                            c=preprocessing_function.data_y, edgecolors='black', cmap='Blues_r',alpha=0.7)
            else:
                plt.scatter(preprocessing_function.data_X[:, 0], preprocessing_function.data_X[:, 1],
                            c=preprocessing_function.data_y, edgecolors='black', cmap=plt.cm.get_cmap('Blues', preprocessing_Data.SmoteDfs[preprocessing_Data.selectCell].nunique()),
                            alpha=0.7)

        cb = plt.colorbar(label='class')
        cb.set_ticks(label)
        if preprocessing_Data.completeFlag:
            cb.set_ticklabels(np.unique(np.array(DuplicatePR.target)))
        else:
            cb.set_ticklabels(np.unique(np.array(preprocessing_function.target)))
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)

        axes2 = self.fig.add_subplot(spec[1])
        plt.title("SMOTE 후", fontsize=15)

        if preprocessing_Data.completeFlag:
            if len(label) <= 2:
                plt.scatter(DuplicatePR.smoteData_X[:, 0], DuplicatePR.smoteData_X[:, 1],
                            c=DuplicatePR.smoteData_y, edgecolors='black', cmap='Blues_r', alpha=0.7)
            else:
                plt.scatter(DuplicatePR.smoteData_X[:, 0], DuplicatePR.smoteData_X[:, 1],
                            c=DuplicatePR.smoteData_y, edgecolors='black', cmap=plt.cm.get_cmap('Blues',preprocessing_Data.SmoteDfs[preprocessing_Data.selectCell].nunique()),
                            alpha=0.7)

        else:
            if len(label) <= 2:
                plt.scatter(preprocessing_function.smoteData_X[:, 0], preprocessing_function.smoteData_X[:, 1],
                            c=preprocessing_function.smoteData_y, edgecolors='black', cmap='Blues_r',alpha=0.7)
            else:
                plt.scatter(preprocessing_function.smoteData_X[:, 0], preprocessing_function.smoteData_X[:, 1],
                            c=preprocessing_function.smoteData_y, edgecolors='black', cmap=plt.cm.get_cmap('Blues',  preprocessing_Data.SmoteDfs[ preprocessing_Data.selectCell].nunique()),
                            alpha=0.7)

        cb = plt.colorbar(label='class')
        cb.set_ticks(label)
        if preprocessing_Data.completeFlag:
            cb.set_ticklabels(np.unique(np.array(DuplicatePR.target)))
        else:
            cb.set_ticklabels(np.unique(np.array(preprocessing_function.target)))
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)


        plt.subplots_adjust(left=0.05, bottom=0.16, top=0.9, wspace=0.3)

        self.canvas.draw()


    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.fig.clear()
