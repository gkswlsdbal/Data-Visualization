from PyQt5.QtWidgets import *
from PyQt5 import uic
import data
import Absorption_event as ab

form_class1 = uic.loadUiType('FileAbsorption.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'FileAbsorption.ui'
        uic.loadUi(option_ui, self)
        for i in range(0, len(data.fileLinks)):
            self.FileList.addItem(parent.FileList.item(i).text())
        self.myParent = parent
        self.FileList.itemClicked.connect(self.itemClick)
        self.innerBtn.clicked.connect(self.inBtnClick)
        self.leftBtn.clicked.connect(self.leftBtnClick)
        self.rightBtn.clicked.connect(self.rightBtnClick)
        self.fullBtn.clicked.connect(self.fullBtnClick)
        self.show()

    def itemClick(self):
        ab.fileItemClick(self)

    def inBtnClick(self):
        ab.innerBtnClick(self)

    def leftBtnClick(self):
        ab.leftBtnClick(self)

    def rightBtnClick(self):
        ab.rightBtnClick(self)

    def fullBtnClick(self):
        ab.fullBtnClick(self)