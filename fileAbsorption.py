from PyQt5.QtWidgets import *
from PyQt5 import uic
import data
import Absorption_event as ab
import Join
from tkinter import messagebox as msg, Tk

form_class1 = uic.loadUiType('FileAbsorption.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):
    Join = ''
    JoinCellList = []

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'FileAbsorption.ui'
        uic.loadUi(option_ui, self)
        for i in range(0, len(data.fileLinks)):
            self.FileList.addItem(parent.FileList.item(i).text())
        self.myParent = parent
        self.FileList.itemClicked.connect(self.itemClick)
        self.JoinBtn.clicked.connect(self.JoinClick)
        self.saveBtn.clicked.connect(self.saveClick)
        self.show()

    def itemClick(self):
        ab.fileItemClick(self)

    def JoinClick(self):
        Join.OptionWindow(self)

    def saveClick(self):
        if self.Join == 'Inner':
            ab.innerBtnClick(self)
            self.JoinCellList.clear()

        elif self.Join == 'left':
            ab.leftBtnClick(self)
            self.JoinCellList.clear()

        elif self.Join == 'right':
            ab.rightBtnClick(self)
            self.JoinCellList.clear()

        elif self.Join == 'full':
            ab.fullBtnClick(self)
            self.JoinCellList.clear()

