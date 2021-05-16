from PyQt5.QtWidgets import *

import fileData
import preprocessing_Data
import SelectColumns


# 누락 값 처리

def function_1(self):
    preprocessing_Data.process = 1
    self.treeWidget_2.clear()
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    itemTop = QTreeWidgetItem(self.treeWidget_2)
    itemTop.setText(0, "")
    itemTop.setDisabled(True)
    itemTop1 = QTreeWidgetItem(self.treeWidget_2)
    itemTop1.setText(0, "Clean Missing Data")
    Label1 = QLabel('Columns to be cleaned')
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
    Label2 = QLabel(' Selected columns:\n\n All columns\n')
    Label2.setStyleSheet(
        "background-color: rgb(240, 240, 240);"
        "border-style: solid;"
        "border-width: 1px;"
        "padding-top: 6px;"
        "margin-top: 3px;"
        "border-color: rgb(120,120,120);"
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

    Label3 = QLabel('Cleaning mode')
    Label3.setStyleSheet(
        "margin-top: 5px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")
    itemChild4 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild4, 0, Label3)
    itemChild4 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild4, 0, Label3)

    comboBox = QComboBox()
    comboBox.addItem(" Custom substitution value")  # 내가 지정한 값
    comboBox.addItem(" Replace with mean")  # 평균처리
    comboBox.addItem(" Replace with median")  # 중앙 값 처리
    comboBox.addItem(" Replace with mode")  # 최빈값 처리
    comboBox.addItem(" Remove entire row")  # 행 처리
    comboBox.addItem(" Remove entire column")  # 열처리
    itemChild5 = QTreeWidgetItem(itemTop1)
    comboBox.setStyleSheet(
        "margin-top: 3px;"
        "border-width: 2px;"
        "border-style: solid;"
        "border-color: rgb(120,120,120);"
        "padding-top: 3px;"
        "padding-bottom: 3px;"
        "margin-bottom: 5px;"
        "margin-right: 5px;"
        "selection-background-color: lightgray")
    self.treeWidget_2.setItemWidget(itemChild5, 0, comboBox)

    global Label4
    Label4 = QLabel('Replacement value')
    Label4.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")
    itemChild6 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild6, 0, Label4)

    global LineEdit
    LineEdit = QLineEdit("0")
    LineEdit.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 10px;"
        "margin-right: 15px;")
    itemChild7 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild7, 0, LineEdit)

    global checkBox
    checkBox = QCheckBox("Replace categorical\n data with mode")
    checkBox.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-color: rgb(255,255,255,255);"
        "margin-bottom: 10px;"
        "margin-right: 20px;"
        "color: rgb(120, 120, 120);")
    itemChild8 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild8, 0, checkBox)
    LineEdit.textChanged.connect(lambda: lineEditChanged(LineEdit.text()))
    comboBox.currentIndexChanged.connect(lambda: indexChanged(comboBox.currentText(), comboBox.currentIndex()))
    checkBox.setDisabled(True)
    checkBox.stateChanged.connect(lambda: check())
    btn1.clicked.connect(lambda: btnCheck(self))


def btnCheck(self):
    SelectColumns.OptionWindow(self)


def EditChange():
    Label4.clear()
    Label4.setText("Threshold Value")
    LineEdit.setText("1")
    preprocessing_Data.cleanValue = "0"


def lineEditChanged(_str):
    preprocessing_Data.cleanValue = _str


def indexChanged(_str, index):
    preprocessing_Data.comboBoxIndex = index
    preprocessing_Data.comboBox = _str
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)

    if preprocessing_Data.comboBoxIndex == 0:
        LineEdit.setText("0")
        LineEdit.setDisabled(False)
        checkBox.setDisabled(True)
        btn1.setDisabled(False)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False

    elif preprocessing_Data.comboBoxIndex == 1:
        LineEdit.setText("0")
        LineEdit.setDisabled(True)
        checkBox.setDisabled(False)
        btn1.setDisabled(False)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False

    elif preprocessing_Data.comboBoxIndex == 2:
        LineEdit.setText("0")
        LineEdit.setDisabled(True)
        checkBox.setDisabled(False)
        btn1.setDisabled(False)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False

    elif preprocessing_Data.comboBoxIndex == 4:
        Label4.setText("Threshold Value")
        Label2.setText('\n Selected columns:\n\n All columns\n')
        LineEdit.setText(str(len(fileData.dfs[fileIndex].columns)))
        preprocessing_Data.cleanValue = str(len(fileData.dfs[fileIndex].columns))
        LineEdit.setDisabled(False)
        checkBox.setDisabled(True)
        btn1.setDisabled(True)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False

    elif preprocessing_Data.comboBoxIndex == 5:
        Label4.setText("Threshold Value")
        Label2.setText('\n Selected columns:\n\n All columns\n')
        LineEdit.setText(str(len(fileData.dfs[fileIndex])))
        preprocessing_Data.cleanValue = str(len(fileData.dfs[fileIndex]))
        LineEdit.setDisabled(False)
        checkBox.setDisabled(True)
        btn1.setDisabled(True)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False

    else:
        LineEdit.clear()
        LineEdit.setDisabled(True)
        checkBox.setDisabled(False)
        btn1.setDisabled(False)
        if preprocessing_Data.checkFlag:
            checkBox.toggle()
        preprocessing_Data.checkFlag = False
        LineEdit.setDisabled(True)


def check():
    if checkBox.isChecked():
        preprocessing_Data.checkFlag = True
    else:
        preprocessing_Data.checkFlag = False
