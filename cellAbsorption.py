from PyQt5 import uic
from PyQt5.QtWidgets import *

import Absorption_event as ab
import data

form_class1 = uic.loadUiType('CellAbsorption.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'CellAbsorption.ui'
        uic.loadUi(option_ui, self)
        self.listWidget.itemClicked.connect(self.itemClick)
        self.abButton.clicked.connect(self.btnClick)
        self.myParent = parent
        self.comboBox.addItem('파일 선택')
        for i in range(0, len(data.fileLinks)):
            self.comboBox.addItem(parent.FileList.item(i).text())

        self.comboBox.currentIndexChanged.connect(self.BoxClick)
        self.show()

    def BoxClick(self):
        data.flag = False
        ab.cellBoxClick(self)

    def itemClick(self):
        ab.cellItemClick(self)

    def btnClick(self):
        ab.cellBtnClick(self)
