from PyQt5 import uic

import ClipTree
import NormalizeTree
import SmoteTree
import fileData
import preprocessing_Data
from PyQt5.QtWidgets import *
import MissingDataTree
import DuplicateTree


form_class1 = uic.loadUiType('SelectColumnsUI.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):
    Flag = False

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'SelectColumnsUI.ui'
        uic.loadUi(option_ui, self)
        self.listWidget.clear()
        self.listWidget_2.clear()
        global col
        col = 0
        global count
        count = 0
        if preprocessing_Data.NormalFlag:
            col = len(preprocessing_Data.processCell)
            for i in range(0, col):
                self.listWidget.addItem(preprocessing_Data.processCell[i])
        else:
            fileIndex = fileData.fileName.index(preprocessing_Data.filename)
            col = len(fileData.dfs[fileIndex].columns)
            title = list(fileData.dfs[fileIndex].columns)
            for i in range(0, col):
                self.listWidget.addItem(str(title[i]))
        self.label_4.setText("  %i columns available" % col)
        self.pushButton.clicked.connect(self.btnClick1)
        self.pushButton_2.clicked.connect(self.btnClick2)
        self.pushButton_3.clicked.connect(self.btnClick3)
        self.listWidget.itemClicked.connect(self.itemClick1)
        self.listWidget_2.itemClicked.connect(self.itemClick2)
        self.show()

    def btnClick1(self):
        if self.Flag:
            item = self.listWidget.takeItem(self.listWidget.currentRow())
            self.listWidget_2.addItem(item)
            global col
            col -= 1
            global count
            count += 1
            self.label_4.setText("  %i columns available" % col)
            self.label_5.setText("  %i columns selected" % count)
            self.Flag = False

    def btnClick2(self):
        if self.Flag:
            item = self.listWidget_2.takeItem(self.listWidget_2.currentRow())
            self.listWidget.addItem(item)
            global col
            col += 1
            global count
            count -= 1
            self.label_4.setText("  %i columns available" % col)
            self.label_5.setText("  %i columns selected" % count)
            self.Flag = False

    def btnClick3(self):
        preprocessing_Data.selectCell.clear()
        item = ""
        for i in range(0, len(self.listWidget_2)):
            preprocessing_Data.selectCell.append(self.listWidget_2.item(i).text())
            item += self.listWidget_2.item(i).text()+" "
        if preprocessing_Data.process == 1:
            MissingDataTree.Label2.setText(' Selected columns:\n '+item+'\n')
        elif preprocessing_Data.process == 2:
            DuplicateTree.Label2.setText(' Selected columns:\n ' + item + '\n')
        elif preprocessing_Data.process == 3:
            ClipTree.Label6.setText(' Selected columns:\n ' + item + '\n')
        elif preprocessing_Data.process == 4:
            SmoteTree.Label2.setText(' Selected columns:\n ' + item + '\n')
        elif preprocessing_Data.process == 5:
            NormalizeTree.Label2.setText(' Selected columns:\n ' + item + '\n')

        self.close()

    def itemClick1(self):
        self.Flag = True

    def itemClick2(self):
        self.Flag = True
