import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
import data, fileData

form_class1 = uic.loadUiType('JoinUi.ui')[0]

JoinTextList = []


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'JoinUi.ui'
        uic.loadUi(option_ui, self)
        self.setGeometry(880, 440, 416, 310)
        self.myParent = parent

        self.JoinList.itemClicked.connect(self.JoinClick)
        self.JoinList2.itemClicked.connect(self.JoinClick2)
        self.innerBtn.clicked.connect(self.innerClick)
        self.leftBtn.clicked.connect(self.leftClick)
        self.rightBtn.clicked.connect(self.rightClick)
        self.fullBtn.clicked.connect(self.fullClick)

        self.fileName.setText(fileData.fileName[data.RowList[0]])
        self.fileName2.setText(fileData.fileName[data.RowList[1]])

        col = len(fileData.dfs[data.RowList[0]].columns)
        title = list(fileData.dfs[data.RowList[0]].columns)

        col2 = len(fileData.dfs[data.RowList[1]].columns)
        title2 = list(fileData.dfs[data.RowList[1]].columns)

        self.JoinList.clear()
        self.JoinList2.clear()

        for i in list(range(0, col)):
            self.JoinList.addItem(str(title[i]))
        for i in list(range(0, col2)):
            self.JoinList2.addItem(str(title2[i]))
        self.show()

    # 조인리스트 출력
    def JoinClick(self):
        text = self.JoinList.currentItem().text()
        self.cellName.setText(text)
        self.myParent.JoinCellList.insert(0, text)
        JoinTextList.append(text)

    def JoinClick2(self):
        text = self.JoinList2.currentItem().text()
        self.cellName2.setText(text)
        self.myParent.JoinCellList.insert(1, text)
        JoinTextList.append(text)

    # 버튼 이미지 바꾸기
    def innerClick(self):
        self.myParent.JoinBtn.setIcon(QIcon(os.getcwd()+'/absorptionImg/innerjoin.png'))
        self.myParent.repaint()
        self.myParent.Join = 'Inner'
        self.close()

    def leftClick(self):
        print(os.getcwd())
        self.myParent.JoinBtn.setIcon(QIcon(os.getcwd()+'/absorptionImg/leftouter.png'))
        self.myParent.repaint()
        self.myParent.Join = 'left'
        self.close()

    def rightClick(self):
        self.myParent.JoinBtn.setIcon(QIcon(os.getcwd()+'/absorptionImg/rightouter.png'))
        self.myParent.repaint()
        self.myParent.Join = 'right'
        self.close()

    def fullClick(self):
        self.myParent.JoinBtn.setIcon(QIcon(os.getcwd()+'/absorptionImg/fullouter.png'))
        self.myParent.repaint()
        self.myParent.Join = 'full'
        self.close()

    def closeEvent(self, event):
        self.fileName.setText("")
        self.fileName2.setText("")
        self.cellName.setText("")
        self.cellName.setText("")
        self.JoinList.clear()
        self.JoinList2.clear()

