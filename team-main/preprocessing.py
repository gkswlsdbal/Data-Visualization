from PyQt5.QtWidgets import *
from PyQt5 import uic
import data, fileData
import Absorption_event as ab

form_class1 = uic.loadUiType('preprocessing.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'preprocessing.ui'
        uic.loadUi(option_ui, self)
        self.myParent = parent
        print(len(fileData.excelList))
        if len(fileData.excelList) != 0:
            for i in range(0, len(fileData.excelList)):
                item = QTreeWidgetItem()
                item.setText(1, fileData.excelList[i])
                self.treeWidget.insertTopLevelItem(1, item)

        if len(fileData.csvList) != 0:
            for i in range(0, len(fileData.csvList)):
                item = QTreeWidgetItem()
                item.setText(1, fileData.csvList[i])
                self.treeWidget.insertTopLevelItem(1, item)
        self.show()
