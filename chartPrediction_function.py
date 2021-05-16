import fileData
import pandas as pd
import os.path
import numpy as np

def addCol(self):
    item = self.fileTreeWidget.currentItem().text(0)[-4: len(self.fileTreeWidget.currentItem().text(0))]
    if item != ".csv" and item != "xlsx":
        for i in range(0, self.colList.count()):
            if self.colList.item(i).text() == self.fileTreeWidget.currentItem().text(0):
                return
        self.colList.addItem(self.fileTreeWidget.currentItem().parent().text(0) + '\\' + self.fileTreeWidget.currentItem().text(0))

def graphReFresh(self):
    self.fig.clear()
    self.ax = self.fig.add_subplot(111)
    colnull = False
    if self.colList.count() <= 0:
        colnull = True
    else:
        collist = self.colList.item(0).text()
        colfile = collist[:collist.find('\\')]
        col = collist[collist.find('\\')+1:]
        colfileindex = fileData.fileName.index(colfile)
        colfilelink = fileData.fileLinks[colfileindex]
        path, ext = os.path.splitext(colfilelink)
        if ext == ".xlsx":
            coldf = pd.read_excel(colfilelink)
        elif ext == ".csv":
            coldf = pd.read_csv(colfilelink)
        y = list(coldf[col])
        self.ax.set_ylabel(col)

    if self.rowList.count() <= 0:
        if colnull:
            return
        x = np.arange(1, len(list(coldf[col])) + 1, 1)
    else:
        rowlist = self.rowList.item(0).text()
        rowfile = rowlist[:rowlist.find('\\')]
        row = rowlist[rowlist.find('\\') + 1:]
        rowfileindex = fileData.fileName.index(rowfile)
        rowfilelink = fileData.fileLinks[rowfileindex]
        path, ext = os.path.splitext(rowfilelink)
        if ext == ".xlsx":
            rowdf = pd.read_excel(rowfilelink)
        elif ext == ".csv":
            rowdf = pd.read_csv(rowfilelink)
        x = list(rowdf[row])
        self.ax.set_xlabel(row)
        if colnull:
            y = np.arange(1, len(list(rowdf[row])) + 1, 1)

    self.ax.plot(x, y)
    self.canvas.draw()
