from PyQt5.QtWidgets import *
import SelectColumns
import fileData
import preprocessing_Data


# 특성 표준화
def function_5(self):
    preprocessing_Data.process = 5
    self.treeWidget_2.clear()
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    itemTop = QTreeWidgetItem(self.treeWidget_2)
    itemTop.setText(0, "")
    itemTop.setDisabled(True)
    itemTop1 = QTreeWidgetItem(self.treeWidget_2)
    itemTop1.setText(0, 'Normalize Data')
    Label1 = QLabel('Transformation method')
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

    comboBox = QComboBox()
    comboBox.addItem(" ZScore")
    comboBox.addItem(" MinMax")
    comboBox.addItem(" Robust")
    comboBox.addItem(" Logistic")
    comboBox.addItem(" LogNormal")
    comboBox.addItem(" Tanh")
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

    Label1 = QLabel('Columns to transform')
    Label1.setStyleSheet(
        "margin-top: 20px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;"
        "color: rgb(120, 120, 120);")
    itemChild4 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild4, 0, Label1)

    global Label2
    Label2 = QLabel(' Selected columns:\n Column type:Numeric All')
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

    itemChild5 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild5, 0, Label2)

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
    btn1.clicked.connect(lambda: btnClick(self))
    comboBox.currentIndexChanged.connect(lambda: indexChanged(comboBox.currentText(), comboBox.currentIndex()))


def btnClick(self):
    if not 'Preprocessing_' in preprocessing_Data.filename:
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


def indexChanged(_str, index):
    preprocessing_Data.comboBoxIndex = index
    preprocessing_Data.comboBox = _str
