
from PyQt5.QtWidgets import *
from PyQt5 import uic
import data, fileData
import Absorption_event as ab
import checkIniFile


form_class1 = uic.loadUiType('CellAbsorption.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'CellAbsorption.ui'
        uic.loadUi(option_ui, self)
        self.listWidget.itemClicked.connect(self.itemClick)
        self.slctListWidget.itemClicked.connect(self.slctItemClick)

        ##변경
        checkIniFile.chckIniCAbsor(self)
        self.buttonBox.accepted.connect(self.btnClick)
        self.buttonBox.rejected.connect(self.close)
        ## 밑에 하나더

        self.myParent = parent
        self.comboBox.addItem('파일 선택')
        for i in range(0, len(fileData.fileLinks)):
            self.comboBox.addItem(parent.FileList.item(i).text())

        self.comboBox.currentIndexChanged.connect(self.BoxClick)
        self.show()
        
    def slctItemClick(self):
        pass

    def BoxClick(self):
        data.flag = False
        ab.cellBoxClick(self)

    def itemClick(self):
        ab.cellItemClick(self)


    def btnClick(self):
        ##변경
        if self.slctListWidget.count() > 0:
            ##
            ab.cellBtnClick(self)
