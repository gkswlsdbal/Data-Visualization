# noinspection PyUnresolvedReferences
import os.path
import pandas as pd
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
import data, fileData
import numpy as np
import math
import preprocessing

# 표 그리는 함수
def draw(self, fl):
    path, ext = os.path.splitext(fl)
    if ext == ".xlsx":
        df = pd.read_excel(fl)
    elif ext == ".csv":
        df = pd.read_csv(fl)
    fileData.dfs.append(df)
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

# 셀 정보를 출력하는 함수
def cellInfo(self):
    self.colInfoListWidget.clear()
    datas = []
    headerlist = []
    for i in range(0, self.tableWidget.columnCount()):
        headerlist.append(self.tableWidget.horizontalHeaderItem(i).text())
    # 셀 내용 채우기
    for i in range(0, self.tableWidget.rowCount()):
        datas.append([])
        for j in range(0, self.tableWidget.columnCount()):
            a = (self.tableWidget.item(i, j))
            datas[i].append(a.text())
    data_df = pd.DataFrame(datas, columns=headerlist)

    coltitle = self.cellList.currentItem().text()  # 열 제목
    roundnum = 4  # 평균을 구할 때 소수점 아래로 남길 숫자 개수
    collist = list(data_df[coltitle])  # 열을 리스트 타입으로 바꿉니다.
    collist = deleteSpaceVal(collist)

    coltable = pd.DataFrame(collist)  # 정리된 리스트를 다시 dataframe으로 바꿉니다.
    coltable.columns = [coltitle]

    # 열 이름, 행 개수
    self.colInfoListWidget.addItem(str("Title: " + coltitle))
    self.colInfoListWidget.addItem(str("Row: " + str(self.tableWidget.rowCount())))

    # 열의 타입이 숫자일 경우 열의 평균값, 중간값, 최대값, 열의 최소값, 타입을 출력합니다.
    if isNumber(coltable, coltitle):

        try:
            collist = list(map(int, collist))
        except:
            collist = list(map(float, collist))

        collist = [x for x in collist if math.isnan(x) == False]  # nan 제거

        self.colInfoListWidget.addItem(str("Average: ") + str(round(sum(collist) / len(collist), roundnum)))
        self.colInfoListWidget.addItem(str("Median: ") + str(np.median(collist)))
        self.colInfoListWidget.addItem(str("Max: ") + str(max(collist)))
        self.colInfoListWidget.addItem(str("Min:  ") + str(min(collist)))
        self.colInfoListWidget.addItem("Type: Number")
    else:  # 숫자가 아니면 타입만 출력합니다.
        self.colInfoListWidget.addItem("Type: String")

    # 빈 값 개수입니다.
    self.colInfoListWidget.addItem(str("Missing: ") + str(countEmptyRow(data.tableDf[coltitle])))


# 데이터프레임변수 열의 타입이 실수인지 확인합니다.
def isNumber(coltable, title):
    try:
        coltable = coltable.astype({title: 'int'})
        return True
    except ValueError:
        try:
            coltable = coltable.astype({title: 'float'})
            return True
        except ValueError:
            return False


# 리스트에 스페이스 값이 들어있으면 지웁니다.
def deleteSpaceVal(collist):
    a = 0
    while a < len(collist) - 1:
        if str(collist[a]).isspace():
            del collist[a]
        else:
            a += 1
    return collist


# nan과 빈칸 개수를 셉니다.
def countEmptyRow(df):
    empty = df.isnull().sum().sum()
    for i in list(df):
        if str(i).isspace():
            empty += 1
    return empty


# 데이터 프레임 수정
def tableChange(self):
    data = []
    headerlist = []
    for i in range(0, self.tableWidget.columnCount()):
        headerlist.append(self.tableWidget.horizontalHeaderItem(i).text())
    # 셀 내용 채우기
    for i in range(0, self.tableWidget.rowCount()):
        data.append([])
        for j in range(0, self.tableWidget.columnCount()):
            a = (self.tableWidget.item(i, j))
            data[i].append(a.text())
    data_df = pd.DataFrame(data, columns=headerlist)
    fileData.dfs[self.fileCount] = data_df.copy()


