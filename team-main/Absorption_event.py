import pandas as pd
from PyQt5.QtWidgets import *
import data


# 해당 데이터프레임 열제목불러오기
def cellBoxClick(self):
    i = self.comboBox.currentIndex() - 1
    data.cmCount = i
    if data.flag:
        data.checkFl.append(i)
    else:
        data.flag = False
    col = len(data.dfs[i].columns)
    title = list(data.dfs[i].columns)
    self.listWidget.clear()

    for i in list(range(0, col)):
        self.listWidget.addItem(str(title[i]))


# 해당 열 제목 리스트 클릭
def cellItemClick(self):
    text = self.listWidget.currentItem().text()
    if text not in data.cellItemList:
        data.cellItemList.append(text)
        self.listWidget_2.addItem(self.listWidget.currentItem().text())
    elif data.cmCount not in data.checkFl:
        data.cellItemList.append(text)
        self.listWidget_2.addItem(self.listWidget.currentItem().text())

    dfi = data.dfs[data.cmCount][text]
    data.dfsList.append(dfi)
    data.fileCount += 1


# 확인 버튼 클릭
def cellBtnClick(self):
    for i in range(0, data.fileCount):
        if i < (data.fileCount - 1):
            mixDf = pd.concat([data.dfsList[i], data.dfsList[i + 1]], axis=1)
            data.dfsList[i + 1] = mixDf

    AbsorptionSave(self, data.dfsList[-1])
    data.dfsList.clear()
    data.checkFl.clear()
    data.fileCount = 0
    self.close()


RowList = []


# 파일 리스트 클릭
def fileItemClick(self):
    text = self.FileList.currentItem().text()
    if text not in data.fileItemList:
        if data.cmCount == 0:
            RowList.append(self.FileList.currentRow())
            data.fileItemList.append(text)
            self.abList.addItem(self.FileList.currentItem().text())
            data.cmCount += 1
        elif data.cmCount < 2:
            RowList.append(self.FileList.currentRow())
            data.fileItemList.append(text)
            self.abList_2.addItem(self.FileList.currentItem().text())
            data.cmCount += 1


def innerBtnClick(self):
    i = RowList[0]
    j = RowList[1]
    inner = pd.concat([data.dfs[i], data.dfs[j]], join='inner', ignore_index=True)
    AbsorptionSave(self, inner)
    data.fileItemList.clear()
    data.cmCount = 0
    self.close()


def leftBtnClick(self):
    i = RowList[0]
    j = RowList[1]
    inner = pd.concat([data.dfs[i], data.dfs[j]], join='inner')
    title = list(inner.columns)
    print(title[2])
    merge_inner = pd.merge(data.dfs[i], data.dfs[j], how='left', on=title[2], indicator=True)
    AbsorptionSave(self, merge_inner)
    data.fileItemList.clear()
    data.cmCount = 0
    self.close()


def rightBtnClick(self):
    i = RowList[0]
    j = RowList[1]
    inner = pd.concat([data.dfs[i], data.dfs[j]], join='inner')
    title = list(inner.columns)
    merge_inner = pd.merge(data.dfs[i], data.dfs[j], how='left', on=title[0], axis=1)
    AbsorptionSave(self, merge_inner)
    data.fileItemList.clear()
    data.cmCount = 0
    self.close()


def fullBtnClick(self):
    i = RowList[0]
    j = RowList[1]
    outer = pd.concat([data.dfs[i], data.dfs[j]], join='outer', axis=1)
    AbsorptionSave(self, outer)
    data.fileItemList.clear()
    data.cmCount = 0
    self.close()


def AbsorptionSave(self, dataFrame):
    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          self.tr("Data Files (*.csv *.xls *.xlsx))"))
    newline = "".join(newFile[0])
    data.fileLinks.append(newline)
    newlineSite = newline.split("/")
    data.dfs.append(dataFrame)
    data.dfs[-1].to_csv(newline, index=None)
    if newlineSite[-1] not in data.fileName:
        self.myParent.FileList.addItem(newlineSite[-1])
    data.fileName.append(newlineSite[-1])
    self.myParent.repaint()

