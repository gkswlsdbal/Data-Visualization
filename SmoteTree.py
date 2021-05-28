
from PyQt5.QtWidgets import *
import SelectColumns
import preprocessing_Data


# 불균형한 결과값 처리
def function_4(self):
    preprocessing_Data.process = 4
    self.treeWidget_2.clear()
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    itemTop = QTreeWidgetItem(self.treeWidget_2)
    itemTop.setText(0, "")
    itemTop.setDisabled(True)
    itemTop1 = QTreeWidgetItem(self.treeWidget_2)
    itemTop1.setText(0, 'SMOTE')
    Label1 = QLabel('Label columns')
    Label1.setStyleSheet(
        "color: rgb(120, 120, 120);"
        "margin-top: 20px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;")
    itemChild1 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild1, 0, Label1)
    global Label2
    Label2 = QLabel(' Selected columns:\n select key label')
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
    btn1.clicked.connect(lambda: btnClick(self))

    Label3 = QLabel('sampling_strategy')
    Label3.setStyleSheet(
        "color: rgb(120, 120, 120);"
        "margin-top: 6px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;")
    itemChild4 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild4, 0, Label3)
    global LineEdit
    LineEdit = QLineEdit(" 0.1")
    LineEdit.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 10px;"
        "margin-right: 15px;")
    itemChild5 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild5, 0, LineEdit)

    Label4 = QLabel('Number of nearest neighbors')
    Label4.setStyleSheet(
        "color: rgb(120, 120, 120);"
        "margin-top: 6px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;")
    itemChild6 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild6, 0, Label4)

    global LineEdit2
    LineEdit2 = QLineEdit(" 1")
    LineEdit2.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 10px;"
        "margin-right: 15px;")
    itemChild7 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild7, 0, LineEdit2)

    Label5 = QLabel('Random seed')
    Label5.setStyleSheet(
        "color: rgb(120, 120, 120);"
        "margin-top: 6px;"
        "margin-bottom: 3px;"
        "margin-right: 15px;"
        "border-style: solid;"
        "border-width: 1px;"
        "border-color: rgb(255,255,255);"
        "font-weight: 500;")
    itemChild8 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild8, 0, Label5)

    global LineEdit3
    LineEdit3 = QLineEdit(" 0")
    LineEdit3.setStyleSheet(
        "margin-top: 3px;"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(120,120,120);"
        "margin-bottom: 10px;"
        "margin-right: 15px;")
    itemChild9 = QTreeWidgetItem(itemTop1)
    self.treeWidget_2.setItemWidget(itemChild9, 0, LineEdit3)

def btnClick(self):
    #if not 'Preprocessing_' in preprocessing_Data.filename:
    SelectColumns.OptionWindow(self)


