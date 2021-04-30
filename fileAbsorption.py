from PyQt5.QtWidgets import *
from PyQt5 import uic
import fileData, data
import Absorption_event as ab
import Join
import checkIniFile

form_class1 = uic.loadUiType('FileAbsorption.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):
    Join = ''
    JoinCellList = []

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'FileAbsorption.ui'
        uic.loadUi(option_ui, self)
        for i in range(0, len(fileData.fileLinks)):
            self.FileList.addItem(parent.FileList.item(i).text())
        self.myParent = parent
        self.FileList.itemClicked.connect(self.itemClick)
        self.JoinBtn.clicked.connect(self.JoinClick)

        ##변경
        #self.Join = 'inner'
        self.buttonBox.accepted.connect(self.saveClick)
        self.buttonBox.rejected.connect(self.close)
        checkIniFile.chckIniFAbsor(self)
        ##
        self.show()

    def itemClick(self):
        ab.fileItemClick(self)

    def JoinClick(self):
        ##변경
        if self.abList.count() > 0 and self.abList_2.count() > 0:
            ##
            Join.OptionWindow(self)

    def saveClick(self):
        ##변경
        if self.abList.count() > 0 and self.abList_2.count() > 0:
            ##
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

    def closeEvent(self, event):
        data.RowList.clear()
        fileData.fileItemList.clear()
        data.cmCount = 0