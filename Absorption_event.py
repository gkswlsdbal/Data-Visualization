import pandas as pd
from PyQt5.QtWidgets import *
import data


# 해당 데이터프레임 열제목불러오기
def cellBoxClick(self):
    i = self.comboBox.currentIndex() - 1
    data.cmCount = i
    if data.flag:
        data.checkfl.append(i)
    else:
        data.flag = True
    col = len(data.dfs[i].columns)
    title = list(data.dfs[i].columns)
    self.listWidget.clear()

    for i in list(range(0, col)):
        self.listWidget.addItem(str(title[i]))


# 해당 열 제목 리스트 클릭
def cellItemClick(self):
    text = self.listWidget.currentItem().text()

    if text not in data.Itemlist:
        data.Itemlist.append(text)
        self.listWidget_2.addItem(self.listWidget.currentItem().text())
    elif data.cmCount not in data.checkfl:
        data.Itemlist.append(text)
        self.listWidget_2.addItem(self.listWidget.currentItem().text())

    dfi = data.dfs[data.cmCount][text]
    data.dfsList.append(dfi)
    data.fileCount += 1


# 파일 병합 버튼 클릭
def cellBtnClick(self):
    for i in range(0, data.fileCount):
        if i < (data.fileCount - 1):
            mixDf = pd.concat([data.dfsList[i], data.dfsList[i + 1]], axis=1)
            data.dfsList[i + 1] = mixDf

    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          self.tr("Data Files (*.csv *.xls *.xlsx))"))

    newline = "".join(newFile[0])
    data.links.append(newline)
    newlineSite = newline.split("/")
    data.dfs.append(data.dfsList[-1])
    data.dfs[-1].to_csv(newline, index=None)
    data.dfsList.clear()
    self.myParent.FileList.addItem(newlineSite[-1])
    self.myParent.repaint()
    self.close()
