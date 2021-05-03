from PyQt5.QtWidgets import QTreeWidgetItem

import MissingDataTree, preprocessing_Data
import preprocessing
import preprocessing_function


def click(self, item):
    preprocessing.Button.setVisible(False)
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    self.treeWidget_2.setVisible(False)
    self.name_2.setVisible(False)

    if '.xlsx' in item.text(0):
        if item.text(0) != self.name.text():
            self.name_2.setText("")
            self.process2 = ""
        self.name.setText("  " + item.text(0))
        preprocessing_Data.filename = item.text(0)
    if '.csv' in item.text(0):
        if item.text(0) != self.name.text():
            self.name_2.setText("")
            self.process2 = ""
        self.name.setText("  " + item.text(0))
        preprocessing_Data.filename = item.text(0)

    for s in ['Missing_', 'Duplicate_', 'SMOTE_']:
        if s in item.text(0):
            preprocessing_Data.completeFlag = True

    functions = {'Clean Missing Data': self.function_1,
                 'Remove Duplicate Rows': self.function_2,
                 'Clip Values': self.function_3,
                 'SMOTE': self.function_4,
                 'Normalize': self.function_5}
    if item.text(0) in functions:
        self.process = item.text(0)
        func = functions[item.text(0)]
        func()


def apply(self):
    if preprocessing_Data.process == 1:
        itemChild1 = QTreeWidgetItem(preprocessing.itemTop3)
        itemChild1.setText(0, "Missing_"+preprocessing_Data.filename)
        preprocessing_function.MissingData(self)
        preprocessing_Data.completeName.append("Missing_"+preprocessing_Data.filename)
        preprocessing_Data.itemCount += 1
    if preprocessing_Data.process == 2:
        itemChild1 = QTreeWidgetItem(preprocessing.itemTop3)
        itemChild1.setText(0, "Duplicate_"+preprocessing_Data.filename)
        preprocessing_function.DuplicateData(self)
        preprocessing_Data.completeName.append("Duplicate_" + preprocessing_Data.filename)
        preprocessing_Data.itemCount += 1
    if preprocessing_Data.process == 4:
        itemChild1 = QTreeWidgetItem(preprocessing.itemTop3)
        itemChild1.setText(preprocessing_Data.itemCount, "SMOTE_"+preprocessing_Data.filename)
        preprocessing_function.SmoteData(self)
        preprocessing_Data.completeName.append("SMOTE_" + preprocessing_Data.filename)
        preprocessing_Data.itemCount += 1


