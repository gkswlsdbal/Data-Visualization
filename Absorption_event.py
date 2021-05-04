# noinspection PyUnresolvedReferences
import os.path
import pandas as pd
from PyQt5.QtWidgets import *
import data
import fileData


# 해당 데이터프레임 열제목불러오기
def cellBoxClick(self):
    i = self.comboBox.currentIndex() - 1
    data.cmCount = i
    if data.flag:
        data.checkFl.append(i)
    else:
        data.flag = False
    col = len(fileData.dfs[i].columns)
    title = list(fileData.dfs[i].columns)
    self.listWidget.clear()

    for i in list(range(0, col)):
        self.listWidget.addItem(str(title[i]))


# 해당 열 제목 리스트 클릭
def cellItemClick(self):
    text = self.listWidget.currentItem().text()
    if text not in data.cellItemList:
        data.cellItemList.append(text)
        self.slctListWidget.addItem(self.listWidget.currentItem().text())
    elif data.cmCount not in data.checkFl:
        data.cellItemList.append(text)
        self.slctListWidget.addItem(self.listWidget.currentItem().text())

    dfi = fileData.dfs[data.cmCount][text]
    data.dfsList.append(dfi)
    fileData.fileCount += 1


# 확인 버튼 클릭
def cellBtnClick(self):
    for i in range(0, fileData.fileCount):
        if i < (fileData.fileCount - 1):
            mixDf = pd.concat([data.dfsList[i], data.dfsList[i + 1]], axis=1)
            data.dfsList[i + 1] = mixDf

    AbsorptionSave(self, data.dfsList[-1])
    data.dfsList.clear()
    data.checkFl.clear()
    fileData.fileCount = 0
    self.close()


# 파일 리스트 클릭
def fileItemClick(self):
    text = self.FileList.currentItem().text()
    if text not in fileData.fileItemList:
        if data.cmCount == 0:
            data.RowList.append(self.FileList.currentRow())
            fileData.fileItemList.append(text)
            self.abList.addItem(self.FileList.currentItem().text())
            data.cmCount += 1
        elif data.cmCount < 2:
            data.RowList.append(self.FileList.currentRow())
            fileData.fileItemList.append(text)
            self.abList2.addItem(self.FileList.currentItem().text())
            data.cmCount += 1


def innerBtnClick(self):
    inner = pd.merge(fileData.dfs[data.RowList[0]], fileData.dfs[data.RowList[1]], how='inner', on=self.JoinCellList[0])
    AbsorptionSave(self, inner)
    fileData.fileItemList.clear()
    data.cmCount = 0
    self.close()


def leftBtnClick(self):
    merge_inner = pd.merge(fileData.dfs[data.RowList[0]], fileData.dfs[data.RowList[1]], how='left',
                           left_on=self.JoinCellList[0], right_on=self.JoinCellList[1])
    AbsorptionSave(self, merge_inner)
    fileData.fileItemList.clear()
    data.cmCount = 0
    self.close()


def rightBtnClick(self):
    merge_inner = pd.merge(fileData.dfs[data.RowList[0]], fileData.dfs[data.RowList[1]], how='right',
                           left_on=self.JoinCellList[0], right_on=self.JoinCellList[1])
    AbsorptionSave(self, merge_inner)
    fileData.fileItemList.clear()
    data.cmCount = 0
    self.close()


def fullBtnClick(self):
    outer = pd.merge(fileData.dfs[data.RowList[0]], fileData.dfs[data.RowList[1]], how='outer', on=self.JoinCellList[0])
    AbsorptionSave(self, outer)
    fileData.fileItemList.clear()
    data.cmCount = 0
    self.close()


def AbsorptionSave(self, dataFrame):

    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          self.tr('All File(*);; Csv File(*.csv);; Data File(*.xlsx)'))
    if newFile[0]:
        path, ext = os.path.splitext(newFile[0])
        newline = "".join(newFile[0])
        fileData.fileLinks.append(newline)
        newlineSite = newline.split("/")
        fileData.dfs.append(dataFrame)
        if ext == ".xlsx":
            fileData.dfs[-1].to_excel(path + ext, index=None)
        elif ext == ".csv":
            fileData.dfs[-1].to_csv(path + ext, index=None)
        if newlineSite[-1] not in fileData.fileName:
            self.myParent.FileList.addItem(newlineSite[-1])
        fileData.fileName.append(newlineSite[-1])
        self.myParent.repaint()
