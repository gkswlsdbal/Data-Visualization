from PyQt5 import uic, QtGui
from matplotlib import style, gridspec, pyplot
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
        self.label.setText('            NormalizeData Chart')
        self.fig = plt.figure(figsize=(25, 15))
        self.canvas = FigureCanvas(self.fig)
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        if preprocessing_Data.completeFlag:
            col = len(DuplicatePR.NumberDfs.columns)
            title = list(DuplicatePR.NumberDfs.columns)
        else:
            col = len(preprocessing_function.NumberDfs.columns)
            title = list(preprocessing_function.NumberDfs.columns)
        for i in list(range(0, col)):
            self.selectCell.append(str(title[i]))

        if col == 1:

            axs1 = self.fig.add_subplot(1, 2, 1)
            sns.distplot(fileData.dfs[fileIndex][self.selectCell], kde=True, rug=True, ax=axs1)
            plt.title("Normalize 변경 전",fontsize=14)
            axs1.set_ylabel('')
            axs1.set_yticklabels([])
            plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=14, top=True)

            axs2 = self.fig.add_subplot(1,2,2)
            if preprocessing_Data.completeFlag:
                sns.distplot(DuplicatePR.NumberDfs, kde=True, rug=True, ax=axs2)
            else:
                sns.distplot(preprocessing_function.NumberDfs, kde=True, rug=True,ax=axs2)
            plt.title("Normalize 변경 후",fontsize=14)
            plt.subplots_adjust(hspace=0.1, wspace=0.35)
            axs2.set_ylabel('')
            axs2.set_yticklabels([])
            plt.tick_params(axis='x', direction='in', length=3, pad=6, labelsize=14, top=True)

        elif col == 2:
            widths = [4, 1, 4, 1]
            heights = [1, 4]
            spec = self.fig.add_gridspec(ncols=4, nrows=2, width_ratios=widths, height_ratios=heights)
            axs = {}
            for i in range(len(heights) * len(widths)):
                if i == 1 or i == 3:
                    pass
                else:
                    axs[i] = self.fig.add_subplot(spec[i // len(widths), i % len(widths)])

            if preprocessing_Data.completeFlag:
                sns.kdeplot(data=DuplicatePR.NumberDfs, x=self.selectCell[0], y=self.selectCell[1],
                            alpha=0.3, ax=axs[6], zorder=1)
                sns.scatterplot(data=DuplicatePR.NumberDfs, x=self.selectCell[0], y=self.selectCell[1],
                                ax=axs[6], zorder=2)
                sns.kdeplot(data=DuplicatePR.NumberDfs, x=self.selectCell[0], legend=False, zorder=1,
                            fill=True,
                            ax=axs[2])
            else:
                sns.kdeplot(data=preprocessing_function.NumberDfs,x=self.selectCell[0], y=self.selectCell[1],alpha=0.3,ax=axs[6],zorder=1)
                sns.scatterplot(data=preprocessing_function.NumberDfs,x=self.selectCell[0], y=self.selectCell[1],ax=axs[6],zorder=2)
                sns.kdeplot(data=preprocessing_function.NumberDfs, x=self.selectCell[0], legend=False,zorder=1, fill=True,
                            ax=axs[2])

            axs[2].set_xlim(axs[6].get_xlim())
            axs[2].set_xlabel('')
            axs[2].set_ylabel('')
            axs[2].set_title("Normalize 적용 후", fontsize=14)
            axs[2].set_xticklabels([])
            axs[2].spines["left"].set_visible(False)
            axs[2].spines["top"].set_visible(False)
            axs[2].spines["right"].set_visible(False)
            if preprocessing_Data.completeFlag:
                sns.kdeplot(data=DuplicatePR.NumberDfs, y=self.selectCell[1], legend=False, fill=True,
                            ax=axs[7], zorder=1)
            else:
                sns.kdeplot(data=preprocessing_function.NumberDfs, y=self.selectCell[1], legend=False, fill=True,
                            ax=axs[7],zorder=1)
            axs[7].set_ylim(axs[6].get_ylim())
            axs[7].set_xlabel('')
            axs[7].set_ylabel('')
            axs[7].set_yticklabels([])
            axs[7].spines["bottom"].set_visible(False)
            axs[7].spines["top"].set_visible(False)
            axs[7].spines["right"].set_visible(False)


            sns.kdeplot(data=fileData.dfs[fileIndex], x=self.selectCell[0], y=self.selectCell[1], alpha=0.3,
                            ax=axs[4], zorder=1)
            sns.scatterplot(data=fileData.dfs[fileIndex], x=self.selectCell[0], y=self.selectCell[1],
                                ax=axs[4], zorder=2)
            sns.kdeplot(data=fileData.dfs[fileIndex], x=self.selectCell[0], legend=False, zorder=1, fill=True,
                            ax=axs[0])

            axs[0].set_xlim(axs[4].get_xlim())
            axs[0].set_xlabel('')
            axs[0].set_ylabel('')
            axs[0].set_xticklabels([])
            axs[0].spines["left"].set_visible(False)
            axs[0].spines["top"].set_visible(False)
            axs[0].set_title("Normalize 적용 전", fontsize=14)
            axs[0].spines["right"].set_visible(False)

            sns.kdeplot(data=fileData.dfs[fileIndex], y=self.selectCell[1], legend=False, fill=True,
                            ax=axs[5], zorder=1)
            axs[5].set_ylim(axs[4].get_ylim())
            axs[5].set_xlabel('')
            axs[5].set_ylabel('')
            axs[5].set_yticklabels([])
            axs[5].spines["bottom"].set_visible(False)
            axs[5].spines["top"].set_visible(False)
            axs[5].spines["right"].set_visible(False)

            for i in range(len(heights) * len(widths)):
                if i == 1 or i == 3:
                    pass
                else:
                    axs[i].grid("on", color="lightgray", zorder=0)
            plt.subplots_adjust(hspace=0.1, wspace=0.2)

        elif col >= 3 or col == 0:
            spec = self.fig.add_gridspec(ncols=len(self.selectCell), nrows=len(self.selectCell))
            axs = {}
            length = len(self.selectCell)
            for i in range(len(self.selectCell) * len(self.selectCell)):
                axs[i] = self.fig.add_subplot(spec[i])

                if preprocessing_Data.completeFlag:
                    if i % (length + 1) == 0:
                        sns.histplot(DuplicatePR.NumberDfs[self.selectCell[i % length]], ax=axs[i],
                                     alpha=0.5, linewidth=0.7, edgecolor="white")
                    else:
                        sns.scatterplot(data=DuplicatePR.NumberDfs, x=self.selectCell[i % length],
                                        y=self.selectCell[int(i / length)], ax=axs[i], alpha=0.5,
                                        linewidth=0.7, edgecolor="white")
                else:
                    if i%(length+1) == 0:
                        sns.histplot(preprocessing_function.NumberDfs[self.selectCell[i%length]],ax=axs[i],alpha=0.5, linewidth=0.7,edgecolor="white")
                    else:
                        sns.scatterplot(data=preprocessing_function.NumberDfs, x=self.selectCell[i%length], y=self.selectCell[int(i/length)], ax=axs[i], alpha=0.5,
                                     linewidth=0.7, edgecolor="white")
                if i == 0:
                    axs[0].set_ylabel(self.selectCell[0])

                if i % length != 0:
                    axs[i].set_ylabel('')
                    axs[i].set_yticklabels([])

                if int(i / length) != length-1:
                    axs[i].set_xlabel('')
                    axs[i].set_xticklabels([])

            plt.subplots_adjust(hspace=0.2, wspace=0.2)

        self.gridLayout.addWidget(self.canvas)
        self.canvas.draw()
        self.show()
        self.selectCell.clear()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.fig.clear()
