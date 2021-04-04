# noinspection PyUnresolvedReferences
import os.path
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import data
import math
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


# 표 그리는 함수
def draw(self, fl):
    path, ext = os.path.splitext(fl)
    if ext == ".xlsx":
        df = pd.read_excel(fl)
    elif ext == ".csv":
        df = pd.read_csv(fl)
    data.dfs.append(df)
    data.tableDf = df

    # 리스트로 변환후 파일이름 가져오기
    table = self.tableWidget
    table.setSortingEnabled(True)

    # 표의 크기를 지정
    col = len(df.columns)
    row = len(df)
    table.setColumnCount(col)
    table.setRowCount(row)

    # 열 제목 지정
    title = list(df.columns)
    self.cellList.clear()
    for i in list(range(0, col)):
        header = QtWidgets.QTableWidgetItem(title[i])
        header.setBackground(Qt.yellow)
        table.setHorizontalHeaderItem(i, header)
        self.cellList.addItem(str(title[i]))

    # 셀 내용 채우기
    for i in list(range(0, col)):
        a = list(df[title[i]])
        for j in list(range(0, row)):
            s = str(a[j])
            if s == 'nan':
                s = ''
            table.setItem(j, i, QtWidgets.QTableWidgetItem(s))


# 차트 그리는 함수

# 셀리스트의 셀제목을 클릭했을때 실행
def cellClick(self):
    self.fig.clear()
    table = self.tableWidget
    col = table.columnCount()
    y = []
    for i in range(0, col - 1):
        aa = table.item(i, self.cellList.currentRow()).text()
        y.append(float(aa))
    x = np.arange(0, col - 1, 1)
    ax = self.fig.add_subplot(111)
    ax.bar(x, y)
    ax.set_xlabel("x")
    ax.set_xlabel("y")
    ax.set_title(self.cellList.currentItem().text())
    self.canvas.draw()
