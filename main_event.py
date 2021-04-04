# noinspection PyUnresolvedReferences
import os.path
from PyQt5.QtWidgets import *
import function as ft
from PyQt5 import QtWidgets, QtCore
import data
import cellAbsorption as ca
import fileAbsorption as fa

# insert 버튼 클릭할때 실행
def btnClick(self):
    filename = QFileDialog.getOpenFileNames(self)
    if filename[0]:
        file = "".join(filename[0])
        self.fileCheck(file)


# 파일 리스트안에 있는 파일 더블클릭할 때 실행
def fileClick(self):
    i = self.FileList.currentRow()
    self.fileCount = i
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


# 파일 저장
def FileSave(self):
    if data.fileName[self.fileCount] in data.fileLinks[self.fileCount]:
        data.dfs[-1].to_excel(data.fileLinks[self.fileCount], index=None)
    else:
        newSave(self)

# 다른이름으로 저장
def newSave(self):
    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          'All File(*);; Csv File(*.csv);; Data File(*.xlsx)')
    if newFile[0]:
        path, ext = os.path.splitext(newFile[0])
        if ext == ".xlsx":
            print(data.fileLinks[self.fileCount])
            data.dfs[-1].to_excel(path+ext, index=None)
        elif ext == ".csv":
            data.dfs[-1].to_csv(path+ext, index=None)
        self.repaint()


# 열 병합 실행
def CellAbsorption(self):
    ca.OptionWindow(self)


# 파일 병합 실행
def FileAbsorption(self):
    fa.OptionWindow(self)
