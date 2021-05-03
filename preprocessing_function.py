from collections import Counter
from sklearn.preprocessing import LabelEncoder
import MissingDataTree, preprocessing_Data
import function
import numpy as np
from sklearn.impute import SimpleImputer
import fileData
import pandas as pd
import preprocessing
from imblearn.over_sampling import SMOTE
import SmoteTree
from sklearn.feature_extraction.text import CountVectorizer


# 결측치 처리 함수
def MissingData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    # 내가 원하는 수 넣기(기본 설정)
    if preprocessing_Data.comboBoxIndex == 0 or preprocessing_Data.comboBoxIndex == "0":
        if preprocessing_Data.selectCell:
            try:
                processingDfs2 = fileData.dfs[fileIndex]
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    float(preprocessing_Data.cleanValue))
            except:
                processingDfs2 = fileData.dfs[fileIndex]
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    preprocessing_Data.cleanValue)

            preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
        else:

            preprocessing_Data.processingDfs = fileData.dfs[fileIndex].fillna(float(preprocessing_Data.cleanValue))

    # 평균값처리
    if preprocessing_Data.comboBoxIndex == 1:

        if preprocessing_Data.selectCell:

            if preprocessing_Data.checkFlag:
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    fileData.dfs[fileIndex].mean())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex]),
                                              columns=fileData.dfs[fileIndex].columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
            else:
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    fileData.dfs[fileIndex].mean())
                processingDfs2 = fileData.dfs[fileIndex]
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
        else:
            if preprocessing_Data.checkFlag:
                processingDfs = fileData.dfs[fileIndex].fillna(fileData.dfs[fileIndex].mean())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex]),
                                              columns=fileData.dfs[fileIndex].columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs.combine_first(processingDfs2)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
            else:
                preprocessing_Data.processingDfs = fileData.dfs[fileIndex].fillna(fileData.dfs[fileIndex].mean())

    # 중앙값처리
    if preprocessing_Data.comboBoxIndex == 2:
        if preprocessing_Data.selectCell:
            if preprocessing_Data.checkFlag:
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    fileData.dfs[fileIndex].median())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex]),
                                              columns=fileData.dfs[fileIndex].columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
            else:
                processingDfs = fileData.dfs[fileIndex][preprocessing_Data.selectCell].fillna(
                    fileData.dfs[fileIndex].median())
                processingDfs2 = fileData.dfs[fileIndex]
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
        else:
            if preprocessing_Data.checkFlag:
                processingDfs = fileData.dfs[fileIndex].fillna(fileData.dfs[fileIndex].median())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex]),
                                              columns=fileData.dfs[fileIndex].columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs.combine_first(processingDfs2)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
            else:
                preprocessing_Data.processingDfs = fileData.dfs[fileIndex].fillna(fileData.dfs[fileIndex].median())

    # 최빈값 처리
    if preprocessing_Data.comboBoxIndex == 3:
        if preprocessing_Data.selectCell:
            imputer = SimpleImputer(strategy="most_frequent")
            processingDfs = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex][preprocessing_Data.selectCell]),
                                         columns=fileData.dfs[fileIndex][preprocessing_Data.selectCell].columns)
            preprocessing_Data.processingDfs = fileData.dfs[fileIndex].combine_first(processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
        else:
            imputer = SimpleImputer(strategy="most_frequent")
            preprocessing_Data.processingDfs = pd.DataFrame(imputer.fit_transform(fileData.dfs[fileIndex]),
                                                            columns=fileData.dfs[fileIndex].columns)

    # 행처리
    if preprocessing_Data.comboBoxIndex == 4:
        preprocessing_Data.selectCell.clear()
        preprocessing_Data.processingDfs = fileData.dfs[fileIndex].dropna(thresh=int(preprocessing_Data.cleanValue))

    # 열처리
    if preprocessing_Data.comboBoxIndex == 5:
        preprocessing_Data.selectCell.clear()
        preprocessing_Data.processingDfs = fileData.dfs[fileIndex].dropna(axis=1,
                                                                          thresh=int(preprocessing_Data.cleanValue))

    if self.process not in self.name_2.text():
        if self.process not in " ":
            self.process2 = " " + self.process + " "
            self.name_2.setText(self.process2)
    preprocessing_Data.completeDfs.append(preprocessing_Data.processingDfs)
    preprocessing_Data.processCell.clear()

    col = len(preprocessing_Data.processingDfs.columns)
    title = list(preprocessing_Data.processingDfs.columns)
    for i in list(range(0, col)):
        preprocessing_Data.processCell.append(str(title[i]))
    function.fileInfo(self, fileData.dfs[fileIndex], fileIndex)
    function.processInfo(self, preprocessing_Data.processingDfs)
    function.compare(self)
    self.listWidget.setVisible(True)
    self.pushButton.setVisible(True)
    self.name_2.setVisible(True)
    preprocessing.Button.setVisible(True)
    self.listWidget_2.setVisible(True)


# 중복 행 제거
def DuplicateData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    dropCell = []
    checkCell = []
    initial = False
    if preprocessing_Data.selectCell:
        initial = True
        dfs = fileData.dfs[fileIndex].copy()
        for i in preprocessing_Data.selectCell:

            if fileData.dfs[fileIndex][i].dtypes == object:
                text = i + "_String"
                dropCell.append(text)
                checkCell.append(text)
                dfs[text] = dfs[i].astype(str)
            else:
                checkCell.append(i)
        preprocessing_Data.processingDfs = dfs.drop_duplicates(checkCell, keep=preprocessing_Data.keep)
    if initial:
        if self.process not in self.name_2.text():
            if self.process not in " ":
                self.process2 = " " + self.process + " "
                self.name_2.setText(self.process2)
        preprocessing_Data.processCell.clear()
        col = len(preprocessing_Data.processingDfs.columns)
        title = list(preprocessing_Data.processingDfs.columns)
        for i in list(range(0, col)):
            preprocessing_Data.processCell.append(str(title[i]))
        function.fileInfo(self, fileData.dfs[fileIndex], fileIndex)
        function.processInfo(self, preprocessing_Data.processingDfs)
        function.compare(self)
        self.listWidget.setVisible(True)
        self.pushButton.setVisible(True)
        self.name_2.setVisible(True)
        self.listWidget_2.setVisible(True)
        preprocessing_Data.selectCell.clear()
    else:
        pass
    preprocessing_Data.completeDfs.append(preprocessing_Data.processingDfs)


# 표준화
def SmoteData(self):
    if preprocessing_Data.completeFlag:
        fileIndex = preprocessing_Data.completeName.index(preprocessing_Data.filename)
        data = preprocessing_Data.completeDfs[fileIndex].values
        preprocessing_Data.processCell.clear()
        col = len(preprocessing_Data.completeDfs[fileIndex].columns)
        title = list(preprocessing_Data.completeDfs[fileIndex].columns)
        for i in list(range(0, col)):
            preprocessing_Data.processCell.append(str(title[i]))
        selectIndex = []
        for i in preprocessing_Data.selectCell:
            selectIndex.append(preprocessing_Data.processCell.index(i))
        if len(selectIndex) == 1:
            preprocessing_Data.SmoteDfs = preprocessing_Data.completeDfs[fileIndex]
            X, y = data[:, :selectIndex[0]], data[:, selectIndex[0]]
            y = LabelEncoder().fit_transform(y)
            smote = SMOTE(sampling_strategy=0.5, k_neighbors=int(SmoteTree.LineEdit2.text()),
                          random_state=int(SmoteTree.LineEdit3.text()))
            smote_X, smote_y = smote.fit_resample(X, y)
            function.SmoteInfo(self, preprocessing_Data.completeDfs[fileIndex])

            self.listWidget.addItem('  \n{}'.format(pd.get_dummies(y).sum()))
            self.listWidget_2.addItem('  \n{}'.format(pd.get_dummies(smote_y).sum()))
            self.listWidget.setVisible(True)
            self.pushButton.setVisible(True)
            self.name_2.setVisible(True)
            self.listWidget_2.setVisible(True)

    else:
        fileIndex = fileData.fileName.index(preprocessing_Data.filename)
        data = fileData.dfs[fileIndex].values
        preprocessing_Data.processCell.clear()
        col = len(fileData.dfs[fileIndex].columns)
        title = list(fileData.dfs[fileIndex].columns)
        for i in list(range(0, col)):
            preprocessing_Data.processCell.append(str(title[i]))

        selectIndex = []
        for i in preprocessing_Data.selectCell:
            selectIndex.append(preprocessing_Data.processCell.index(i))
        if len(selectIndex) == 1:
            preprocessing_Data.SmoteDfs = fileData.dfs[fileIndex]
            global data_X
            global data_y
            global target
            target = data[:, selectIndex[0]]
            data_X, data_y = data[:, :selectIndex[0]], data[:, selectIndex[0]]
            data_y = LabelEncoder().fit_transform(data_y)
            label = np.unique(np.array(data_y))
            if len(label) <= 2:
                smote = SMOTE(sampling_strategy=float(SmoteTree.LineEdit.text()),
                              k_neighbors=int(SmoteTree.LineEdit2.text()), random_state=int(SmoteTree.LineEdit3.text()))
            else:
                smote = SMOTE(k_neighbors=int(SmoteTree.LineEdit2.text()), random_state=int(SmoteTree.LineEdit3.text()))
            global smoteData_X
            global smoteData_y
            smoteData_X, smoteData_y = smote.fit_resample(data_X, data_y)
            smoteData_y = LabelEncoder().fit_transform(smoteData_y)
            function.SmoteInfo(self, fileData.dfs[fileIndex])
            self.listWidget.addItem('  \n{}'.format(pd.get_dummies(data_y).sum()))
            self.listWidget_2.addItem('  \n{}'.format(pd.get_dummies(smoteData_y).sum()))
            self.listWidget.setVisible(True)
            self.pushButton.setVisible(True)
            self.name_2.setVisible(True)
            self.listWidget_2.setVisible(True)
            preprocessing.Button.setVisible(True)
            self.listWidget.addItem("")
            self.listWidget_2.addItem("")
            global counter
            counter = Counter(data_y)
            for k, v in counter.items():
                per = v / len(data_y) * 100
                self.listWidget.addItem('Class=%d, n=%d (%.3f%%)' % (k, v, per))
            global counter1
            counter1 = Counter(smoteData_y)
            for k, v in counter1.items():
                per = v / len(smoteData_y) * 100
                self.listWidget_2.addItem('Class=%d, n=%d (%.3f%%)' % (k, v, per))
