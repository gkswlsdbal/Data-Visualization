from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

import DuplicateTree
import SmoteChart
import SmoteTree
import data, fileData
import design
import MissingDataTree
import processChart
import process_event
import preprocessing_Data

form_class1 = uic.loadUiType('preprocessing.ui')[0]


# 새창 띄우는 역할
class OptionWindow(QDialog):
    process = " "
    process2 = " "

    def __init__(self, parent):
        super(OptionWindow, self).__init__(parent)
        option_ui = 'preprocessing.ui'
        uic.loadUi(option_ui, self)
        self.myParent = parent
        self.treeWidget.header().setVisible(False)
        self.treeWidget.itemClicked.connect(self.itemClick)
        self.listWidget.setVisible(False)
        self.pushButton.setVisible(False)
        self.listWidget_2.setVisible(False)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.apply)
        self.name.setStyleSheet(
            "padding-top: 10px;"
            "margin-bottom: 5px;"
            "background-color: rgb(240, 240, 240);"
            "color:rgb(92, 92, 92);")
        self.name_2.setStyleSheet(
            "padding-left: 10px;"
            "background-color: rgb(240, 240, 240);"
            "color:rgb(122, 122, 122);")
        design.setProcess(self)

        global Button
        Button = QPushButton(self)
        Button.setGeometry(910, 485, 40, 40)
        Button.setStyleSheet(
            "background-color: rgb(240, 240, 240);"
            "border-style: solid;"
            "border-width: 1px;"
            "border-color: rgb(240,240,240);")
        Button.setIcon(QIcon('img/chart.png'))
        Button.setIconSize(QSize(40, 40))
        Button.clicked.connect(self.btnClick)
        Button.setVisible(False)

        itemTop = QTreeWidgetItem(self.treeWidget)
        itemTop.setText(0, "")
        itemTop.setDisabled(True)
        itemTop1 = QTreeWidgetItem(self.treeWidget)
        itemTop1.setText(0, "Saved Datasets")
        itemTop1.setIcon(0, QIcon('img/Datasets.png'))
        itemTop = QTreeWidgetItem(self.treeWidget)
        itemTop.setText(0, "")
        itemTop.setDisabled(True)
        itemTop2 = QTreeWidgetItem(self.treeWidget)
        itemTop2.setText(0, "Data Transformation")
        itemTop2.setIcon(0, QIcon('img/Transform.png'))
        itemTop = QTreeWidgetItem(self.treeWidget)
        itemTop.setText(0, "")
        itemTop.setDisabled(True)
        global itemTop3
        itemTop3 = QTreeWidgetItem(self.treeWidget)
        itemTop3.setText(0, "PreProcess Data")
        itemTop3.setIcon(0, QIcon('img/processData.png'))

        itemChild1 = QTreeWidgetItem(itemTop1)
        itemChild1.setText(0, "excel")
        itemChild2 = QTreeWidgetItem(itemTop1)
        itemChild2.setText(0, "csv")

        item2Child1 = QTreeWidgetItem(itemTop2)
        item2Child1.setText(0, "Clean Missing Data")
        item2Child1 = QTreeWidgetItem(itemTop2)
        item2Child1.setText(0, 'Remove Duplicate Rows')
        item2Child1 = QTreeWidgetItem(itemTop2)
        item2Child1.setText(0, 'Clip Values')
        item2Child1 = QTreeWidgetItem(itemTop2)
        item2Child1.setText(0, 'SMOTE')
        item2Child1 = QTreeWidgetItem(itemTop2)
        item2Child1.setText(0, 'Normalize')

        if len(fileData.excelList) != 0:
            for i in range(0, len(fileData.excelList)):
                item = QTreeWidgetItem(itemChild1)
                item.setText(0, fileData.excelList[i])
                self.treeWidget.insertTopLevelItem(0, item)

        if len(fileData.csvList) != 0:
            for i in range(0, len(fileData.csvList)):
                item = QTreeWidgetItem(itemChild2)
                item.setText(0, fileData.csvList[i])
                self.treeWidget.insertTopLevelItem(0, item)
        self.show()

    # 누락값 처리
    def function_1(self):
        self.treeWidget_2.setVisible(True)
        MissingDataTree.function_1(self)

    # 중복 행 제거
    def function_2(self):
        self.treeWidget_2.setVisible(True)
        DuplicateTree.function_2(self)

    # 불균형한 결과값 처리
    def function_3(self):
        self.treeWidget_2.clear()
        self.listWidget.setVisible(False)
        self.pushButton.setVisible(False)
        self.listWidget_2.setVisible(False)
        itemTop1 = QTreeWidgetItem(self.treeWidget_2)
        itemTop1.setText(0, "Saved Datasets")
        itemTop1.setIcon(0, QIcon('img/Datasets.png'))

    # 표준화
    def function_4(self):
        self.treeWidget_2.setVisible(True)
        SmoteTree.function_4(self)

    # 아웃라이어 제거
    def function_5(self):
        self.treeWidget_2.clear()
        self.listWidget.setVisible(False)
        self.pushButton.setVisible(False)
        self.listWidget_2.setVisible(False)
        itemTop1 = QTreeWidgetItem(self.treeWidget_2)
        itemTop1.setText(0, "Saved Datasets")
        itemTop1.setIcon(0, QIcon('img/Datasets.png'))

    def itemClick(self, item):
        process_event.click(self, item)

    def apply(self):
        process_event.apply(self)

    def btnClick(self):
        if preprocessing_Data.process == 1:
            processChart.OptionWindow(self)
        elif preprocessing_Data.process == 4:
            SmoteChart.OptionWindow(self)