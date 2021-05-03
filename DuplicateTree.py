from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic

import SelectColumns
import data, fileData
import design
import MissingDataTree
import preprocessing_Data
import processChart
import process_event


# 중복 행 제거
def function_2(self):
    preprocessing_Data.process = 2
    self.treeWidget_2.clear()
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    itemTop = QTreeWidgetItem(self.treeWidget_2)
    itemTop.setText(0, "")
    itemTop.setDisabled(True)
    itemTop1 = QTreeWidgetItem(self.treeWidget_2)
    itemTop1.setText(0, 'Remove Duplicate Rows')
    Label1 = QLabel('Key column selection')
    Label1.setStyleSheet(
        "margin-top: 30px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")
    itemChild1 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild1, 0, Label1)
    global Label2
    Label2 = QLabel(' Selected columns:\n Launch the selector tool \n to make a selection')
    Label2.setStyleSheet(

        "background-color: rgb(240, 240, 240);"
        "border-style: solid;"
        "border-width: 1px;"
        "margin-top: 3px;"
        "border-color: rgb(120,120,120);"
        "padding-top: 6px;"
        "padding-bottom: 6px;"
        "margin-bottom: 3px;"
        "margin-right: 30px;")

    itemChild2 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild2, 0, Label2)

    global btn1
    btn1 = QPushButton('Launch column selector')
    btn1.setStyleSheet(
        "margin-top: 3px;"
        "border-width: 2px;"
        "border-style: solid;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 5px;"
        "margin-right: 15px;"
        "padding: 8px")
    itemChild3 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild3, 0, btn1)

    # 첫 번째 행이 반환되고 다른행은 삭제
    global checkBox
    checkBox = QCheckBox("Retain first duplicate row")
    checkBox.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-color: rgb(255,255,255,255);"
        "margin-bottom: 10px;"
        "margin-right: 20px;"
        "color: rgb(120, 120, 120);")
    checkBox.toggle()
    itemChild8 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild8, 0, checkBox)
    btn1.clicked.connect(lambda: btnClick(self))
    checkBox.stateChanged.connect(lambda: check())


def btnClick(self):
    SelectColumns.OptionWindow(self)


def check():
    if checkBox.isChecked():
        preprocessing_Data.keep = "first"
    else:
        preprocessing_Data.keep = "last"
