from PyQt5.QtWidgets import *
from PyQt5 import uic
import data
form_class1 = uic.loadUiType('FileAbsorption.ui')[0]

# 새창 띄우는 역할
class OptionWindow(QDialog):

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'FileAbsorption.ui'
        uic.loadUi(option_ui, self)
        for i in range(0, len(data.links)):
            self.FileList.addItem(parent.FileList.item(i).text())
        self.show()

