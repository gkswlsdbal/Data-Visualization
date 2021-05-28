# noinspection PyUnresolvedReferences
import os.path
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import pandas

import data
import fileData


##
##cell absorption event
##
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

def delSelectedCol(self):
    text = self.slctListWidget.currentItem().text()
    del data.cellItemList[self.slctListWidget.currentRow()]
    del data.dfsList[self.slctListWidget.currentRow()]
    self.slctListWidget.takeItem(self.slctListWidget.currentRow())
    fileData.fileCount -= 1

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


##
##file absorption event
##

# 파일 리스트 클릭
def fileItemClick(self):
    if self.slctFileLabel1.text() == '' and self.FileList.currentRow() != self.slctFileRows[2]:
        self.slctFileLabel1.setText(self.FileList.currentItem().text())
        self.slctFileRows[1] = self.FileList.currentRow()

        self.joinList1.clear()
        if self.join != 'inner' and self.join != 'full':
            title = list(fileData.dfs[self.slctFileRows[1]].columns)
            for i in list(range(0, len(title))):
                self.joinList1.addItem(str(title[i]))

    elif self.slctFileLabel2.text() == '' and self.FileList.currentRow() != self.slctFileRows[1]:
        self.slctFileLabel2.setText(self.FileList.currentItem().text())
        self.slctFileRows[2] = self.FileList.currentRow()

        self.joinList2.clear()
        if self.join != 'inner' and self.join != 'full':
            title = list(fileData.dfs[self.slctFileRows[2]].columns)
            for i in list(range(0, len(title))):
                self.joinList2.addItem(str(title[i]))


def innerBtnClick(self):
    try:
        inner = pd.merge(fileData.dfs[self.slctFileRows[1]], fileData.dfs[self.slctFileRows[2]])
        AbsorptionSave(self, inner)
        self.close()
    except pandas.errors.MergeError:
        QMessageBox.information(self, 'No Same Column',
                                '두 파일 사이에 겹치는 열이 없어 교집합을 사용할 수 없습니다.')


def outerBtnClick(self):
    try:
        outer = pd.merge(fileData.dfs[self.slctFileRows[1]], fileData.dfs[self.slctFileRows[2]], how='outer')
        AbsorptionSave(self, outer)
        self.close()
    except pandas.errors.MergeError:
        QMessageBox.information(self, 'No Same Column',
                                '두 파일 사이에 겹치는 열이 없어 합집합을 사용할 수 없습니다.')


def leftBtnClick(self):
    left_outer = pd.merge(fileData.dfs[self.slctFileRows[1]], fileData.dfs[self.slctFileRows[2]],
                          how='left',
                          left_on=self.cellName1.text(), right_on=self.cellName2.text())
    AbsorptionSave(self, left_outer)
    self.close()


def rightBtnClick(self):
    right_outer = pd.merge(fileData.dfs[self.slctFileRows[1]], fileData.dfs[self.slctFileRows[2]],
                           how='right',
                           left_on=self.cellName1.text(), right_on=self.cellName2.text())
    AbsorptionSave(self, right_outer)
    self.close()


def AbsorptionSave(self, dataFrame):
    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          self.tr('All File(*);; Csv File(*.csv);; Data File(*.xlsx)'))
    if newFile[0]:
        path, ext = os.path.splitext(newFile[0])
        newline = "".join(newFile[0])

        if not newline in fileData.fileLinks:
            fileData.fileLinks.append(newline)
            fileData.dfs.append(dataFrame)

        newlineSite = newline.split("/")
        if ext == ".xlsx":
            fileData.dfs[-1].to_excel(path + ext, index=None,encoding='utf-8-sig')
        elif ext == ".csv":
            fileData.dfs[-1].to_csv(path + ext, index=None,encoding='utf-8-sig')
        if newlineSite[-1] not in fileData.fileName:
            icon = QIcon('img/arrowww.png')
            icon_item = QListWidgetItem(icon, newlineSite[-1])
            self.myParent.FileList.addItem(icon_item)
        fileData.fileName.append(newlineSite[-1])
        self.myParent.repaint()
