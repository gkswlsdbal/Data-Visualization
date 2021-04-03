from PyQt5.QtWidgets import *
import function as ft
from PyQt5 import QtWidgets, QtCore
import data
import cellAbsorption as ca
import fileAbsorption as fa
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np

# insert 버튼 클릭할때 실행
def btnClick(self):
    filename = QFileDialog.getOpenFileNames(self)
    file = "".join(filename[0])
    self.fileCheck(file)


# 파일 리스트안에 있는 파일 더블클릭할 때 실행
def fileClick(self):
    i = self.FileList.currentRow()
    self.fileCheck("".join(data.fileLinks[i]))


# 파일리스트에 이미 파일 있는지 검사
def fileCheck(self, file):
    if file in data.fileLinks:
        ft.draw(self, file)
    else:
        data.fileLinks.append(file)
        site = file.split("/")
        self.FileList.addItem(site[-1])
        data.fileName.append(site[-1])
        ft.draw(self, file)


# 파일 드레그앤 드랍
def eventFilter(self, object, event):
    if event.type() == QtCore.QEvent.DragEnter:
        if event.mimeData().hasUrls():
            event.accept()

        else:
            event.ignore()

    if event.type() == QtCore.QEvent.Drop:
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            link = []
            for url in event.mimeData().urls():
                link.append(str(url.toLocalFile()))

        file = "".join(link)
        self.fileCheck(file)

        return False


# 열 병합 실행
def CellAbsorption(self):
    ca.OptionWindow(self)


# 파일 병합 실행
def FileAbsorption(self):
    fa.OptionWindow(self)

#셀리스트의 셀제목을 클릭했을때 실행
def cellClick(self):
    self.fig.clear()
    table = self.tableWidget
    col = table.columnCount()
    y = []
    for i in range(0, col-1):
        aa = table.item(i, self.cellList.currentRow()).text()
        y.append(float(aa))
    x = np.arange(0, col-1, 1)
    ax = self.fig.add_subplot(111)
    ax.bar(x, y)
    ax.set_xlabel("x")
    ax.set_xlabel("y")
    ax.set_title(self.cellList.currentItem().text())
    self.canvas.draw()