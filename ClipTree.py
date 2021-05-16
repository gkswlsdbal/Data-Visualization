from PyQt5.QtWidgets import *

import fileData
import preprocessing_Data
import SelectColumns


# 누락 값 처리

def function_3(self):
    preprocessing_Data.process = 3
    self.treeWidget_2.clear()
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    itemTop = QTreeWidgetItem(self.treeWidget_2)
    itemTop.setText(0, "")
    itemTop.setDisabled(True)
    global itemTop1
    itemTop1 = QTreeWidgetItem(self.treeWidget_2)
    itemTop1.setText(0, "Clip Values")
    Label1 = QLabel('Set of thresholds')
    Label1.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")

    itemChild1 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild1, 0, Label1)

    comboBox = QComboBox()
    comboBox.addItem(" ClipPeaks")
    comboBox.addItem(" ClipSubpeaks")
    comboBox.addItem(" ClipPeakAndSubpeaks")
    itemChild2 = QTreeWidgetItem(itemTop1)
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
    self.treeWidget_2.setItemWidget(itemChild2, 0, comboBox)
    global Label2
    Label2 = QLabel('Upper threshold')
    Label2.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")

    itemChild3 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild3, 0, Label2)

    global comboBox2
    comboBox2 = QComboBox()
    comboBox2.addItem(" Constant")  # 상수
    comboBox2.addItem(" percentile")  # 백분위 수
    itemChild4 = QTreeWidgetItem(itemTop1)
    comboBox2.setStyleSheet(
        "margin-top: 3px;"
        "border-width: 2px;"
        "border-style: solid;"
        "border-color: rgb(120,120,120);"
        "padding-top: 3px;"
        "padding-bottom: 3px;"
        "margin-bottom: 5px;"
        "margin-right: 5px;"
        "selection-background-color: lightgray")
    self.treeWidget_2.setItemWidget(itemChild4, 0, comboBox2)

    global Label3
    Label3 = QLabel('Constant value for upper threshold')
    Label3.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")

    itemChild5 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild5, 0, Label3)

    global LineEdit
    LineEdit = QLineEdit("1")
    LineEdit.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 10px;"
        "margin-right: 15px;")
    itemChild6 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild6, 0, LineEdit)

    global Label4
    Label4 = QLabel('Upper substitute value')
    Label4.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")

    itemChild7 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild7, 0, Label4)

    comboBox3 = QComboBox()
    comboBox3.addItem(" Mean")
    comboBox3.addItem(" Median")
    comboBox3.addItem(" Delete")
    itemChild8 = QTreeWidgetItem(itemTop1)
    comboBox3.setStyleSheet(
        "margin-top: 3px;"
        "border-width: 2px;"
        "border-style: solid;"
        "border-color: rgb(120,120,120);"
        "padding-top: 3px;"
        "padding-bottom: 3px;"
        "margin-bottom: 5px;"
        "margin-right: 5px;"
        "selection-background-color: lightgray")
    self.treeWidget_2.setItemWidget(itemChild8, 0, comboBox3)

    Label5 = QLabel('List of columns')
    Label5.setStyleSheet(
        "margin-top: 10px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")

    itemChild9 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild9, 0, Label5)

    global Label6
    Label6 = QLabel(' Selected columns:\n Column type:Numeric All')
    Label6.setStyleSheet(

        "background-color: rgb(240, 240, 240);"
        "border-style: solid;"
        "border-width: 1px;"
        "margin-top: 3px;"
        "border-color: rgb(120,120,120);"
        "padding-top: 6px;"
        "padding-bottom: 6px;"
        "margin-bottom: 3px;"
        "margin-right: 30px;")

    itemChild10 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild10, 0, Label6)

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
    itemChild11 = QTreeWidgetItem(itemTop1)
    comboBox.currentIndexChanged.connect(lambda: indexChanged(comboBox.currentIndex()))
    self.treeWidget_2.setItemWidget(itemChild11, 0, btn1)
    comboBox2.currentIndexChanged.connect(lambda: indexChanged2(comboBox2.currentIndex()))
    btn1.clicked.connect(lambda: btnCheck(self))
    comboBox3.currentIndexChanged.connect(lambda: indexChanged3(comboBox3.currentIndex()))




def btnCheck(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    preprocessing_Data.processingDfs = fileData.dfs[fileIndex]
    preprocessing_Data.processCell.clear()
    col = len(fileData.dfs[fileIndex].columns)
    title = list(fileData.dfs[fileIndex].columns)
    for i in list(range(0, col)):
        if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
            preprocessing_Data.processCell.append(str(title[i]))
    preprocessing_Data.NormalFlag = True
    SelectColumns.OptionWindow(self)


def indexChanged2(index):
    if preprocessing_Data.clipIndex == 0:
        if index == 0:
            Label3.setText('Constant value for upper threshold')
            LineEdit.setText('1')
            preprocessing_Data.threshold = index
        else:
            Label3.setText('Percentile value for upper threshold')
            LineEdit.setText('90')
            preprocessing_Data.threshold = index

    if preprocessing_Data.clipIndex == 1:
        if index == 0:
            Label3.setText('Constant value for lower threshold')
            LineEdit.setText('1')
            preprocessing_Data.threshold = index
        else:
            Label3.setText('Percentile value for lower threshold')
            LineEdit.setText('10')
            preprocessing_Data.threshold = index

    if preprocessing_Data.clipIndex == 2:
        if index == 0:
            Label3.setText('Constant value for threshold')
            LineEdit.setText('1')
            preprocessing_Data.threshold = index
        else:
            Label3.setText('Percentile value for threshold')
            LineEdit.setText('90')
            preprocessing_Data.threshold = index

def indexChanged(index):
    preprocessing_Data.clipIndex = index
    if index == 0:
        Label2.setText('Upper threshold')
        if preprocessing_Data.threshold == 0:
            Label3.setText('Constant value for Upper threshold')
            LineEdit.setText('1')
        else:
            Label3.setText('Percentile value for Upper threshold')
            LineEdit.setText('90')
        Label4.setText('Upper substitute value')

    elif index == 1:
        Label2.setText('Lower threshold')
        if preprocessing_Data.threshold == 0:
            Label3.setText('Constant value for lower threshold')
            LineEdit.setText('1')
        else:
            Label3.setText('Percentile value for lower threshold')
            LineEdit.setText('10')

        Label4.setText('Lower substitute value')
    elif index == 2:
        Label2.setText('threshold')
        if preprocessing_Data.threshold == 0:
            Label3.setText('Constant value for threshold')
            LineEdit.setText('1')
        else:
            Label3.setText('Percentile value for threshold')
            LineEdit.setText('90')

        Label4.setText('substitute value')

def indexChanged3(index):
    if index == 0:
        preprocessing_Data.clipValue = 0
    elif index == 1:
        preprocessing_Data.clipValue = 1
    elif index == 2:
        preprocessing_Data.clipValue = 2
