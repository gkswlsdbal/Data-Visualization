
from PyQt5.QtWidgets import *
from PyQt5 import uic
import data, fileData
import Absorption_event as ab

# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'CellAbsorption.ui'
        uic.loadUi(option_ui, self)
        self.myParent = parent

        self.comboBox.addItem('파일 선택')
        for i in range(0, len(fileData.fileLinks)):
            self.comboBox.addItem(parent.FileList.item(i).text())

        self.comboBox.currentIndexChanged.connect(self.BoxClick)
        self.listWidget.itemClicked.connect(self.itemClick)
        self.slctListWidget.itemClicked.connect(self.delSelectedCol)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.close)
        self.leftArrow.setEnabled(False)
        self.rightArrow.setEnabled(False)
        self.show()

    def BoxClick(self):
        data.flag = False
        ab.cellBoxClick(self)

    def itemClick(self):
        ab.cellItemClick(self)

    def delSelectedCol(self):
        ab.delSelectedCol(self)

    def save(self):
        if self.slctListWidget.count() > 0:
            ab.cellBtnClick(self)
