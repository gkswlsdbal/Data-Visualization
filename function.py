import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import data


# 표 그리는 함수
def draw(self, fl):
    df = pd.read_csv(fl)
    data.dfs.append(df)

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
