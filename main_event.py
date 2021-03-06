# noinspection PyUnresolvedReferences
import os.path
import sys

import chardet
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import function as ft
from PyQt5 import QtWidgets, QtCore
import fileData, data
import cellAbsorption as ca
import fileAbsorption as fa
import setting as st


# insert 버튼 클릭할때 실행
def btnClick(self):
    filename = QFileDialog.getOpenFileNames(self)
    if filename[0]:
        for i in filename[0]:
            file = "".join(i)
            self.fileCheck(file)


# 파일 리스트안에 있는 파일 더블클릭할 때 실행
def fileClick(self):
    i = self.FileList.currentRow()
    self.fileCount = i
    self.fileCheck("".join(fileData.fileLinks[i]))


# 파일리스트에 이미 파일 있는지 검사
def fileCheck(self, file):
    if file in fileData.fileLinks:
        ft.draw(self, file)
    else:
        fileData.fileLinks.append(file)
        site = file.split("/")
        icon = QIcon('img/arrowww.png')
        icon_item = QListWidgetItem(icon, site[-1])
        self.FileList.addItem(icon_item)
        fileData.fileName.append(site[-1])
        if ".xlsx" in site[-1]:
            fileData.excelList.append(site[-1])
        elif ".csv" in site[-1]:
            fileData.csvList.append(site[-1])
        else:  ##추가
            QMessageBox.critical(self, 'Error',
                                "xlsx 혹은 csv 파일만 올려주시기 바랍니다", QMessageBox.Ok)
            fileData.fileLinks.pop()
            self.FileList.takeItem(self.FileList.count()-1)
            fileData.fileName.pop()
            return
        
        ft.draw(self, file)
        path, ext = os.path.splitext(file)
        rawdata = open(file, 'rb').read()
        result = chardet.detect(rawdata)
        charenc = result['encoding']
        if ext == ".xlsx":
            df = pd.read_excel(file)
        elif ext == ".csv":
            df = pd.read_csv(file,encoding=charenc,error_bad_lines=False)
        fileData.dfs.append(df)


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

        for i in link:
            file = "".join(i)
            self.fileCheck(file)

        return False


# 파일 저장
def FileSave(self):
    try:
        path, ext = os.path.splitext(fileData.fileLinks[self.fileCount])
        if self.cellFlag:
            ft.tableChange(self)
        if fileData.fileName[self.fileCount] in fileData.fileLinks[self.fileCount]:
            if ext == ".xlsx":
                fileData.dfs[self.fileCount].to_excel(fileData.fileLinks[self.fileCount], index=None,encoding='utf-8-sig')
            elif ext == ".csv":
                fileData.dfs[self.fileCount].to_csv(fileData.fileLinks[self.fileCount], index=None,encoding='utf-8-sig')
        else:
            newSave(self)
    except:
        QMessageBox.critical(self, 'Error',
                             "저장 가능한 파일이 없습니다!", QMessageBox.Ok)


# 다른이름으로 저장
def newSave(self):
    try:
        newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                              self.tr('All File(*);; Csv File(*.csv);; Data File(*.xlsx)'))
        if newFile[0]:
            if self.cellFlag:
                ft.tableChange(self)
            path, ext = os.path.splitext(newFile[0])
            if ext == ".xlsx":
                fileData.dfs[self.fileCount].to_excel(path + ext, index=None,encoding='utf-8-sig')
            elif ext == ".csv":
                fileData.dfs[self.fileCount].to_csv(path + ext, index=None,encoding='utf-8-sig')
    except:
        QMessageBox.critical(self, 'Error',
                             "저장 가능한 파일이 없습니다!", QMessageBox.Ok)


# 프로그램 종료
def exitAction(self):
    sys.exit()


# 열 병합 실행
def CellAbsorption(self):
    ca.OptionWindow(self)


# 파일 병합 실행
def FileAbsorption(self):
    fa.OptionWindow(self)


def openSettingWindow(self):
    st.SettingDialog(self)
