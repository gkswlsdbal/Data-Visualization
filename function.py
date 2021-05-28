# noinspection PyUnresolvedReferences
import os.path

import chardet
import pandas as pd
from PIL.ImageQt import rgb
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtWidgets import QListWidgetItem, QLabel, QListWidget, QMessageBox

import data, fileData
import numpy as np
import math
import preprocessing_Data


# 표 그리는 함수

def draw(self, fl):
    path, ext = os.path.splitext(fl)
    rawdata = open(fl,'rb').read()
    result = chardet.detect(rawdata)
    charenc = result['encoding']
    if ext == ".xlsx":
        df = pd.read_excel(fl)
    elif ext == ".csv":
        df = pd.read_csv(fl,encoding=charenc,error_bad_lines=False)
    data.tableDf = df

    # 리스트로 변환후 파일이름 가져오기
    table = self.tableWidget
    self.tableWidget.scrollToTop()
    table.setSortingEnabled(True)

    # 표의 크기를 지정
    col = len(df.columns)
    row = len(df)
    table.setColumnCount(col)
    table.setRowCount(row)

    # 열 제목 지정
    title = list(df.columns)
    self.cellList.clear()
    line = []
    for i in list(range(0, col)):
        header = QtWidgets.QTableWidgetItem(title[i])
        header.setBackground(Qt.yellow)
        table.setHorizontalHeaderItem(i, header)
        if str(type(df[title[i]][0])) == "<class 'str'>":
            icon = QIcon('img/파이.png')
            icon_item = QListWidgetItem(icon, str(title[i]))
            self.cellList.addItem(icon_item)
        else:
            icon = QIcon('img/막대2.png')
            icon_item = QListWidgetItem(icon, str(title[i]))
            self.cellList.addItem(icon_item)
        line.append(str(title[i]))
    data.dfsCell.append(line)

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
        coltable = coltable.astype({title: 'int64'})
        return True
    except (ValueError, OverflowError):
        try:
            coltable = coltable.astype({title: 'float64'})
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


def fileInfo(self, dfs, index):
    self.listWidget.scrollToTop()
    self.listWidget_2.scrollToTop()
    self.listWidget.clear()
    self.listWidget.addItem("")
    Label = QLabel(' rows         columns')
    Label.setStyleSheet(
        "color: rgb(64,129,194,255);"
        "font-weight: bold;")
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item1 = QListWidgetItem(self.listWidget)
    self.listWidget.setItemWidget(item1, Label)
    Label2 = QLabel(" " + str(len(dfs)) + "              " + str(len(dfs.columns)))
    Label2.setFont(QtGui.QFont("맑은 고딕", 12))
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item2 = QListWidgetItem(self.listWidget)
    self.listWidget.setItemWidget(item2, Label2)
    for i in range(0, len(data.dfsCell[index])):
        self.listWidget.addItem("")
        coltitle = data.dfsCell[index][i]  # 열 제목
        roundnum = 4  # 평균을 구할 때 소수점 아래로 남길 숫자 개수
        collist = list(dfs[coltitle])  # 열을 리스트 타입으로 바꿉니다.
        collist = deleteSpaceVal(collist)

        coltable = pd.DataFrame(collist)  # 정리된 리스트를 다시 dataframe으로 바꿉니다.
        coltable.columns = [coltitle]

        # 열 이름, 행 개수
        i = QListWidgetItem(str("Title: " + coltitle))
        i.setBackground(QColor(120, 120, 120, 50))
        self.listWidget.addItem(i)
        self.listWidget.addItem(str("Row: " + str(len(coltable))))

        # 열의 타입이 숫자일 경우 열의 평균값, 중간값, 최대값, 열의 최소값, 타입을 출력합니다.
        if isNumber(coltable, coltitle):

            try:
                collist = list(map(int, collist))
            except:
                collist = list(map(float, collist))

            collist = [x for x in collist if math.isnan(x) == False]  # nan 제거
            self.listWidget.addItem(str("Average: ") + str(round(sum(collist) / len(collist), roundnum)))
            self.listWidget.addItem(str("Median: ") + str(np.median(collist)))
            self.listWidget.addItem(str("Max: ") + str(max(collist)))
            self.listWidget.addItem(str("Min:  ") + str(min(collist)))
            self.listWidget.addItem("Type: Number")
        else:  # 숫자가 아니면 타입만 출력합니다.
            self.listWidget.addItem("Type: String")

        # 빈 값 개수입니다.
        self.listWidget.addItem(str("Missing: ") + str(countEmptyRow(coltable)))


def processInfo(self, dfs):
    self.listWidget.scrollToTop()
    self.listWidget_2.scrollToTop()
    self.listWidget_2.clear()
    self.listWidget_2.addItem("")
    Label = QLabel(' rows         columns')
    Label.setStyleSheet(
        "color: rgb(64,129,194,255);"
        "font-weight: bold;")
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item1 = QListWidgetItem(self.listWidget_2)
    self.listWidget_2.setItemWidget(item1, Label)
    Label2 = QLabel(" " + str(len(dfs)) + "              " + str(len(dfs.columns)))
    Label2.setFont(QtGui.QFont("맑은 고딕", 12))
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item2 = QListWidgetItem(self.listWidget_2)
    self.listWidget_2.setItemWidget(item2, Label2)
    for i in range(0, len(preprocessing_Data.processCell)):
        self.listWidget_2.addItem("")
        coltitle = preprocessing_Data.processCell[i]  # 열 제목
        roundnum = 4  # 평균을 구할 때 소수점 아래로 남길 숫자 개수
        collist = list(dfs[coltitle])  # 열을 리스트 타입으로 바꿉니다.
        collist = deleteSpaceVal(collist)

        coltable = pd.DataFrame(collist)  # 정리된 리스트를 다시 dataframe으로 바꿉니다.
        coltable.columns = [coltitle]

        # 열 이름, 행 개수
        i = QListWidgetItem(str("Title: " + coltitle))
        i.setBackground(QColor(120, 120, 120, 50))
        self.listWidget_2.addItem(i)
        self.listWidget_2.addItem(str("Row: " + str(len(coltable))))

        # 열의 타입이 숫자일 경우 열의 평균값, 중간값, 최대값, 열의 최소값, 타입을 출력합니다.
        if isNumber(coltable, coltitle):

            try:
                collist = list(map(int, collist))
            except:
                collist = list(map(float, collist))

            collist = [x for x in collist if math.isnan(x) == False]  # nan 제거
            try:
                self.listWidget_2.addItem(str("Average: ") + str(round(sum(collist) / len(collist), roundnum)))
                self.listWidget_2.addItem(str("Median: ") + str(np.median(collist)))
                self.listWidget_2.addItem(str("Max: ") + str(max(collist)))
                self.listWidget_2.addItem(str("Min:  ") + str(min(collist)))
                self.listWidget_2.addItem("Type: Number")
            except:
                self.listWidget_2.addItem("Type: NoneType")
        else:  # 숫자가 아니면 타입만 출력합니다.
            self.listWidget_2.addItem("Type: String")

        # 빈 값 개수입니다.
        self.listWidget_2.addItem(str("Missing: ") + str(countEmptyRow(coltable)))


def SmoteInfo(self, dfs, dfs2):
    self.listWidget.scrollToTop()
    self.listWidget_2.scrollToTop()
    self.listWidget.clear()
    self.listWidget.addItem("")
    Label = QLabel(' rows         columns')
    Label.setStyleSheet(
        "color: rgb(64,129,194,255);"
        "font-weight: bold;")
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item1 = QListWidgetItem(self.listWidget)
    self.listWidget.setItemWidget(item1, Label)
    Label2 = QLabel(" " + str(len(dfs)) + "              " + str(len(dfs.columns)))
    Label2.setFont(QtGui.QFont("맑은 고딕", 12))
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item2 = QListWidgetItem(self.listWidget)
    self.listWidget.setItemWidget(item2, Label2)
    self.listWidget.addItem("")
    i = QListWidgetItem(str("원본 데이터의 클래스 비율"))
    i.setBackground(QColor(120, 120, 120, 50))
    self.listWidget.addItem(i)

    self.listWidget_2.clear()
    self.listWidget_2.addItem("")
    Label = QLabel(' rows         columns')
    Label.setStyleSheet(
        "color: rgb(64,129,194,255);"
        "font-weight: bold;")
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item1 = QListWidgetItem(self.listWidget_2)
    self.listWidget_2.setItemWidget(item1, Label)
    Label2 = QLabel(" " + str(len(dfs2)) + "              " + str(len(dfs2.columns)))
    Label2.setFont(QtGui.QFont("맑은 고딕", 12))
    Label.setFont(QtGui.QFont("맑은 고딕", 12))
    item2 = QListWidgetItem(self.listWidget_2)
    self.listWidget_2.setItemWidget(item2, Label2)
    self.listWidget.setItemWidget(item2, Label2)
    self.listWidget_2.addItem("")
    i = QListWidgetItem(str("SMOTE 결과"))
    i.setBackground(QColor(120, 120, 120, 50))
    self.listWidget_2.addItem(i)


def compare(self):
    for i in range(0, len(self.listWidget_2)):
        if self.listWidget.item(i):
            if self.listWidget.item(i).text() != self.listWidget_2.item(i).text():
                self.listWidget_2.item(i).setBackground(QColor('#BBD1E8'))
        else:
            self.listWidget_2.item(i).setBackground(QColor('#BBD1E8'))


