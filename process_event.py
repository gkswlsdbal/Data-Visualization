import os.path

from PyQt5.QtWidgets import QTreeWidgetItem, QFileDialog, QMessageBox
import DuplicatePR
import MissingDataTree, preprocessing_Data
import fileData
import function
import preprocessing
import preprocessing_function
from ColumnChart_function import secGraphRefresh


def click(self, item):
    preprocessing.Button.setVisible(False)
    self.listWidget.setVisible(False)
    self.pushButton.setVisible(False)
    self.listWidget_2.setVisible(False)
    self.treeWidget_2.setVisible(False)
    self.name_2.setVisible(False)
    preprocessing_Data.selectCell.clear()

    if '.xlsx' in item.text(0):
        if item.text(0) != self.name.text():
            self.name_2.setText("")
            self.process2 = ""
        self.name.setText("  " + item.text(0))
        preprocessing_Data.filename = item.text(0)
        preprocessing_Data.completeFlag = False
        preprocessing_Data.completeDfs = []
        preprocessing_Data.label = ""
        self.pushButton_3.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_4.setVisible(False)
        preprocessing_Data.itemCount = 0
        self.label_2.setText(preprocessing_Data.label)
    if '.csv' in item.text(0):
        if item.text(0) != self.name.text():
            self.name_2.setText("")
            self.process2 = ""
        self.name.setText("  " + item.text(0))
        preprocessing_Data.filename = item.text(0)
        preprocessing_Data.label = ""
        preprocessing_Data.completeFlag = False
        preprocessing_Data.completeDfs = []
        self.pushButton_3.setVisible(True)
        self.pushButton_2.setVisible(True)
        self.pushButton_4.setVisible(False)
        preprocessing_Data.itemCount = 0
        self.label_2.setText(preprocessing_Data.label)

    if 'Preprocessing_' in item.text(0):
        preprocessing_Data.processCell.clear()
        self.pushButton_4.setVisible(True)
        if len(preprocessing_Data.completeName) == 0:
            file = item.text(0).split("Preprocessing_1")
        for i in range(0,len(preprocessing_Data.completeName)):
            if "Preprocessing_"+str(i+1) in item.text(0):
                file = item.text(0).split("Preprocessing_"+str(i+1))
        fileIndex = fileData.fileName.index(file[-1])
        processIndex = preprocessing_Data.completeName.index(preprocessing_Data.filename)
        try:
            col = len(preprocessing_Data.preprocessingDfs[processIndex].columns)

        except AttributeError:
            QMessageBox.information(self, 'error',
                                    '"list" object has no attribute "columns"')
            
        title = list(preprocessing_Data.preprocessingDfs[processIndex].columns)
        for i in list(range(0, col)):
            preprocessing_Data.processCell.append(str(title[i]))
        function.fileInfo(self, fileData.dfs[fileIndex], fileIndex)
        function.processInfo(self, preprocessing_Data.preprocessingDfs[processIndex])
        function.compare(self)
        preprocessing_Data.processCell.clear()
        self.listWidget.setVisible(True)
        self.pushButton.setVisible(True)
        self.listWidget_2.setVisible(True)
        self.pushButton_3.setVisible(False)
        self.pushButton_2.setVisible(False)


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
    self.listWidget.scrollToTop()
    self.listWidget_2.scrollToTop()

    if preprocessing_Data.process == 1:
        if preprocessing_Data.applyFlag:
            preprocessing_Data.itemCount += 1
        else:
            pass
        if preprocessing_Data.completeFlag:
            DuplicatePR.MissingData(self)
        else:
            preprocessing_function.MissingData(self)

    if preprocessing_Data.process == 2:
        if preprocessing_Data.applyFlag:
            preprocessing_Data.itemCount += 1
        else:
            pass
        if preprocessing_Data.completeFlag:
            DuplicatePR.DuplicateData(self)
        else:
            preprocessing_function.DuplicateData(self)

    if preprocessing_Data.process == 3:
        if preprocessing_Data.applyFlag:
            preprocessing_Data.itemCount += 1
        else:
            pass
        if preprocessing_Data.completeFlag:
            DuplicatePR.ClipData(self)
        else:
            preprocessing_function.ClipData(self)

    if preprocessing_Data.process == 4:
        if preprocessing_Data.applyFlag:
            preprocessing_Data.itemCount += 1
        else:
            pass
        if preprocessing_Data.completeFlag:
            DuplicatePR.SmoteData(self)
        else:
            preprocessing_function.SmoteData(self)

    if preprocessing_Data.process == 5:
        if preprocessing_Data.applyFlag:
            preprocessing_Data.itemCount += 1
        else:
            pass
        if preprocessing_Data.completeFlag:
            DuplicatePR.NormalizeData(self)
        else:
            preprocessing_function.NormalizeData(self)



def Okay(self):

    itemChild1 = QTreeWidgetItem(preprocessing.itemTop3)
    itemChild1.setText(0, "Preprocessing_" + str(len(preprocessing_Data.preprocessingDfs) + 1) + preprocessing_Data.filename)
    preprocessing_Data.completeName.append("Preprocessing_" + str(len(preprocessing_Data.preprocessingDfs) + 1) + preprocessing_Data.filename)
    preprocessing_Data.preprocessingDfs.append(preprocessing_Data.completeDfs)

def Save(self):
    processIndex = preprocessing_Data.completeName.index(preprocessing_Data.filename)
    newFile = QFileDialog.getSaveFileName(self, self.tr("Save Data files"), "./",
                                          self.tr('All File(*);; Csv File(*.csv);; Data File(*.xlsx)'))
    if newFile[0]:
        path, ext = os.path.splitext(newFile[0])
        if ext == ".xlsx":
            preprocessing_Data.preprocessingDfs[processIndex].to_excel(path + ext, index=None)
        elif ext == ".csv":
            preprocessing_Data.preprocessingDfs[processIndex].to_csv(path + ext, index=None)

