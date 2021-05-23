from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEvent
import fileData, data
import Absorption_event as ab


# 새창 띄우는 역할
class OptionWindow(QDialog):
    join = ''
    slctFileRows = {}

    def __init__(self, parent):

        super(OptionWindow, self).__init__(parent)
        option_ui = 'FileAbsorption_new.ui'
        uic.loadUi(option_ui, self)

        self.join = 'inner'
        self.slctFileRows[1] = None
        self.slctFileRows[2] = None

        for i in range(0, len(parent.FileList)):
            self.FileList.addItem(parent.FileList.item(i).text())
        self.myParent = parent

        self.FileList.itemClicked.connect(self.fileClick)
        self.clickable(self.slctFileLabel1).connect(self.delSlctFile1)
        self.clickable(self.slctFileLabel2).connect(self.delSlctFile2)
        self.joinList1.itemClicked.connect(self.joinClick)
        self.joinList2.itemClicked.connect(self.joinClick2)
        self.innerBtn.clicked.connect(self.inner)
        self.outerBtn.clicked.connect(self.full)
        self.leftBtn.clicked.connect(self.left)
        self.rightBtn.clicked.connect(self.right)
        self.buttonBox.accepted.connect(self.save)
        self.buttonBox.rejected.connect(self.close)
        self.clickable(self.cellName1).connect(lambda: self.delCellLabelText(self.cellName1))
        self.clickable(self.cellName2).connect(lambda: self.delCellLabelText(self.cellName2))

        self.innerBtn.toggle()

        self.show()

    def fileClick(self):
        ab.fileItemClick(self)

    def joinClick(self):
        text = self.joinList1.currentItem().text()
        self.cellName1.setText(text)

    def joinClick2(self):
        text = self.joinList2.currentItem().text()
        self.cellName2.setText(text)

    def save(self):
        if self.slctFileLabel1.text() != '' and self.slctFileLabel2.text() != '':
            if self.join == 'inner':
                ab.innerBtnClick(self)
            elif self.join == 'full':
                ab.outerBtnClick(self)
            elif self.join == 'left':
                if self.cellName1.text() == '' or self.cellName2.text() == '':
                    QMessageBox.information(self, '', '열 2개를 선택해 주세요.')
                else:
                    ab.leftBtnClick(self)
            elif self.join == 'right':
                if self.cellName1.text() == '' or self.cellName2.text() == '':
                    QMessageBox.information(self, '', '열 2개를 선택해 주세요.')
                else:
                    ab.rightBtnClick(self)

    def delSlctFile1(self):
        self.slctFileLabel1.setText('')
        # self.slctFileRows[1] = None
        self.cellName1.setText('')
        self.joinList1.clear()

    def delSlctFile2(self):
        self.slctFileLabel2.setText('')
        # self.slctFileRows[2] = None
        self.cellName2.setText('')
        self.joinList2.clear()

    def delCellLabelText(self, label):
        label.setText('')

    def clickable(self, widget):

        class Filter(QObject):
            clicked = pyqtSignal()

            def eventFilter(self, obj, event):
                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

    def inner(self):
        self.setBtnToggle()
        self.join = "inner"
        self.innerBtn.toggle()
        self.joinList1.clear()
        self.joinList2.clear()

    def full(self):
        self.setBtnToggle()
        self.join = "full"
        self.outerBtn.toggle()
        self.joinList1.clear()
        self.joinList2.clear()

    def right(self):
        self.setBtnToggle()
        self.join = "right"
        self.rightBtn.toggle()

        if self.slctFileLabel1.text() != '':
            self.joinList1.clear()
            title = list(fileData.dfs[self.slctFileRows[1]].columns)
            for i in list(range(0, len(title))):
                self.joinList1.addItem(str(title[i]))
        if self.slctFileLabel2.text() != '':
            self.joinList2.clear()
            title = list(fileData.dfs[self.slctFileRows[2]].columns)
            for i in list(range(0, len(title))):
                self.joinList2.addItem(str(title[i]))

    def left(self):
        self.setBtnToggle()
        self.join = "left"
        self.leftBtn.toggle()

        if self.slctFileLabel1.text() != '':
            self.joinList1.clear()
            title = list(fileData.dfs[self.slctFileRows[1]].columns)
            for i in list(range(0, len(title))):
                self.joinList1.addItem(str(title[i]))
        if self.slctFileLabel2.text() != '':
            self.joinList2.clear()
            title = list(fileData.dfs[self.slctFileRows[2]].columns)
            for i in list(range(0, len(title))):
                self.joinList2.addItem(str(title[i]))

    def setBtnToggle(self):
        if self.rightBtn.isChecked():
            self.rightBtn.toggle()
        if self.leftBtn.isChecked():
            self.leftBtn.toggle()
        if self.innerBtn.isChecked():
            self.innerBtn.toggle()
        if self.outerBtn.isChecked():
            self.outerBtn.toggle()

    # def closeEvent(self, event):
        # data.RowList.clear()
        # fileData.fileItemList.clear()
        # data.cmCount = 0
