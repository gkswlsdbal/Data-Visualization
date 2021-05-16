from collections import Counter
from sklearn.preprocessing import LabelEncoder

import ClipTree
import MissingDataTree, preprocessing_Data
import function
import numpy as np
from sklearn.impute import SimpleImputer
import fileData
import pandas as pd
import preprocessing
from imblearn.over_sampling import SMOTE
import SmoteTree
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler


# 결측치 처리 함수
def MissingData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    # 내가 원하는 수 넣기(기본 설정)
    if preprocessing_Data.comboBoxIndex == 0 or preprocessing_Data.comboBoxIndex == "0":
        if preprocessing_Data.selectCell:
            try:
                processingDfs2 = preprocessing_Data.completeDfs
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    float(preprocessing_Data.cleanValue))
            except:
                processingDfs2 = preprocessing_Data.completeDfs
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    preprocessing_Data.cleanValue)

            preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
        else:

            preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.fillna(float(preprocessing_Data.cleanValue))

    # 평균값처리
    if preprocessing_Data.comboBoxIndex == 1:

        if preprocessing_Data.selectCell:
            if preprocessing_Data.checkFlag:
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    round(preprocessing_Data.completeDfs.mean(),1))
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs),
                                              columns=preprocessing_Data.completeDfs.columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
            else:
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    round(preprocessing_Data.completeDfs.mean(),1))
                processingDfs2 = preprocessing_Data.completeDfs
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
        else:
            if preprocessing_Data.checkFlag:
                processingDfs = preprocessing_Data.completeDfs.fillna(round(preprocessing_Data.completeDfs.mean(),1))
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs),
                                              columns=preprocessing_Data.completeDfs.columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs.combine_first(processingDfs2)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
            else:
                preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.fillna(round(preprocessing_Data.completeDfs.mean(),1))

    # 중앙값처리
    if preprocessing_Data.comboBoxIndex == 2:
        if preprocessing_Data.selectCell:
            if preprocessing_Data.checkFlag:
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    preprocessing_Data.completeDfs.median())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs),
                                              columns=preprocessing_Data.completeDfs.columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
            else:
                processingDfs = preprocessing_Data.completeDfs[preprocessing_Data.selectCell].fillna(
                    preprocessing_Data.completeDfs.median())
                processingDfs2 = preprocessing_Data.completeDfs
                preprocessing_Data.processingDfs = processingDfs2.combine_first(processingDfs)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
        else:
            if preprocessing_Data.checkFlag:
                processingDfs = preprocessing_Data.completeDfs.fillna(preprocessing_Data.completeDfs.median())
                imputer = SimpleImputer(strategy="most_frequent")
                processingDfs2 = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs),
                                              columns=preprocessing_Data.completeDfs.columns)
                # 덮어 쓰기
                preprocessing_Data.processingDfs = processingDfs.combine_first(processingDfs2)
                preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
            else:
                preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.fillna(preprocessing_Data.completeDfs.median())

    # 최빈값 처리
    if preprocessing_Data.comboBoxIndex == 3:
        if preprocessing_Data.selectCell:
            imputer = SimpleImputer(strategy="most_frequent")
            processingDfs = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs[preprocessing_Data.selectCell]),
                                         columns=preprocessing_Data.completeDfs[preprocessing_Data.selectCell].columns)
            preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.combine_first(processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]
        else:
            imputer = SimpleImputer(strategy="most_frequent")
            preprocessing_Data.processingDfs = pd.DataFrame(imputer.fit_transform(preprocessing_Data.completeDfs),
                                                            columns=preprocessing_Data.completeDfs.columns)

    # 행처리
    if preprocessing_Data.comboBoxIndex == 4:
        preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.dropna(thresh=int(preprocessing_Data.cleanValue))

    # 열처리
    if preprocessing_Data.comboBoxIndex == 5:
        preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.dropna(axis=1,
                                                                          thresh=int(preprocessing_Data.cleanValue))

    if self.process not in self.name_2.text():
        if self.process not in " ":
            self.process2 = " " + self.process + " "
            self.name_2.setText(self.process2)
    preprocessing_Data.completeDfs = preprocessing_Data.processingDfs.copy()
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
    if "Missing" not in preprocessing_Data.label:
        preprocessing_Data.label += " Missing "
        self.label_2.setText(preprocessing_Data.label)


# 중복 행 제거
def DuplicateData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    dropCell = []
    checkCell = []
    initial = False
    if preprocessing_Data.selectCell:
        initial = True
        dfs = preprocessing_Data.completeDfs.copy()
        for i in preprocessing_Data.selectCell:

            if preprocessing_Data.completeDfs[i].dtypes == object:
                text = i + "_String"
                dropCell.append(text)
                checkCell.append(text)
                dfs[text] = dfs[i].astype(str)
            else:
                checkCell.append(i)
        preprocessing_Data.processingDfs = dfs.drop_duplicates(checkCell, keep=preprocessing_Data.keep)
        preprocessing_Data.processingDfs = preprocessing_Data.processingDfs.drop(dropCell, axis=1)
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
        preprocessing_Data.completeDfs = preprocessing_Data.processingDfs.copy()
        preprocessing_Data.processCell.clear()
        preprocessing_Data.completeFlag = True
        if "Duplicate" not in preprocessing_Data.label:
            preprocessing_Data.label += " Duplicate "
            self.label_2.setText(preprocessing_Data.label)

    else:
        pass

# 이상치 제거
def ClipData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    global NumberDfs
    preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.copy()
    dfs = preprocessing_Data.processingDfs.copy()
    preprocessing_Data.processCell.clear()
    col = len(fileData.dfs[fileIndex].columns)
    title = list(fileData.dfs[fileIndex].columns)
    outliers_indices = []
    cell = []
    if preprocessing_Data.selectCell:
        for i in list(range(0, col)):
            if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                    preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                    preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                preprocessing_Data.processCell.append(str(title[i]))
            cell.append(str(title[i]))

        if preprocessing_Data.threshold == 0:
            if preprocessing_Data.clipIndex == 0:

                for col in preprocessing_Data.selectCell:

                    outlier_list_col = dfs[(dfs[col] > float(ClipTree.LineEdit.text()))].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

            elif preprocessing_Data.clipIndex == 1:
                for col in preprocessing_Data.selectCell:

                    outlier_list_col = dfs[(dfs[col] < float(ClipTree.LineEdit.text()))].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

        if preprocessing_Data.threshold == 1:

            if preprocessing_Data.clipIndex == 0:

                for col in preprocessing_Data.selectCell:

                    Q1 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))
                    IQR = Q3 - Q1
                    outlier_step = 1.5 * IQR
                    upper_bound = Q3 + outlier_step

                    outlier_list_col = dfs[(dfs[col] > upper_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

            elif preprocessing_Data.clipIndex == 1:
                for col in preprocessing_Data.selectCell:
                    Q1 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    IQR = Q3 - Q1

                    outlier_step = 1.5 * IQR

                    lower_bound = Q1 - outlier_step

                    outlier_list_col = dfs[(dfs[col] < lower_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

            else:
                for col in preprocessing_Data.selectCell:
                    Q1 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))

                    IQR = Q3 - Q1

                    outlier_step = 1.5 * IQR

                    lower_bound = Q1 - outlier_step
                    upper_bound = Q3 + outlier_step

                    outlier_list_col = dfs[(dfs[col] < lower_bound) | (dfs[col] > upper_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue, multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

    else:
        for i in list(range(0, col)):
            if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                    preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                    preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                preprocessing_Data.processCell.append(str(title[i]))
                preprocessing_Data.selectCell.append(str(title[i]))

        if preprocessing_Data.threshold == 0:
            if preprocessing_Data.clipIndex == 0:

                for col in preprocessing_Data.selectCell:
                    outlier_list_col = dfs[(dfs[col] > float(ClipTree.LineEdit.text()))].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

            elif preprocessing_Data.clipIndex == 1:
                for col in preprocessing_Data.selectCell:
                    outlier_list_col = dfs[(dfs[col] < float(ClipTree.LineEdit.text()))].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.selectCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.selectCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

        if preprocessing_Data.threshold == 1:
            if preprocessing_Data.clipIndex == 0:
                for col in preprocessing_Data.processCell:
                    Q1 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))
                    IQR = Q3 - Q1

                    outlier_step = 1.5 * IQR
                    upper_bound = Q3 + outlier_step

                    outlier_list_col = dfs[(dfs[col] > upper_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.processCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.processCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

            elif preprocessing_Data.clipIndex == 1:
                for col in preprocessing_Data.processCell:
                    Q1 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    IQR = Q3 - Q1

                    outlier_step = 1.5 * IQR

                    lower_bound = Q1 - outlier_step

                    outlier_list_col = dfs[(dfs[col] < lower_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.processCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.processCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()
            else:
                for col in preprocessing_Data.processCell:
                    Q1 = np.percentile(dfs[col], 100 - float(ClipTree.LineEdit.text()))
                    Q3 = np.percentile(dfs[col], float(ClipTree.LineEdit.text()))
                    IQR = Q3 - Q1

                    outlier_step = 1.5 * IQR

                    lower_bound = Q1 - outlier_step
                    upper_bound = Q3 + outlier_step

                    outlier_list_col = dfs[(dfs[col] < lower_bound) | (dfs[col] > upper_bound)].index

                    outliers_indices.extend(outlier_list_col)
                outliers_indices = Counter(outliers_indices)
                multiple_outliers = list(k for k, v in outliers_indices.items() if v > 0)
                if preprocessing_Data.clipValue == 2:
                    dfs = dfs.drop(multiple_outliers, axis=0).reset_index(drop=True)
                else:
                    target = clipValue(dfs[preprocessing_Data.processCell].copy(), dfs, preprocessing_Data.clipValue,
                                       multiple_outliers)
                    processingDfs2 = pd.DataFrame(target, columns=preprocessing_Data.processCell)
                    dfs = processingDfs2.combine_first(dfs)
                    dfs = dfs[list(fileData.dfs[fileIndex])]
                preprocessing_Data.processingDfs = dfs.copy()

    if self.process not in self.name_2.text():
        if self.process not in " ":
            self.process2 = " " + self.process + " "
            self.name_2.setText(self.process2)

    preprocessing_Data.completeDfs = preprocessing_Data.processingDfs.copy()
    preprocessing_Data.processCell.clear()
    preprocessing_Data.completeFlag = True
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
    if "Normalize" not in preprocessing_Data.label:
        preprocessing_Data.label += " Normalize "
        self.label_2.setText(preprocessing_Data.label)


# 불균형한 결과값 처리
def SmoteData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    dfs = preprocessing_Data.completeDfs.copy()
    preprocessing_Data.processingDfs = preprocessing_Data.completeDfs.copy()
    data = preprocessing_Data.completeDfs.values
    preprocessing_Data.processCell.clear()
    col = len(preprocessing_Data.completeDfs.columns)
    title = list(preprocessing_Data.completeDfs.columns)
    for i in list(range(0, col)):
        preprocessing_Data.processCell.append(str(title[i]))

    selectIndex = []
    for i in preprocessing_Data.selectCell:
        selectIndex.append(preprocessing_Data.processCell.index(i))
    if len(selectIndex) == 1:

        global data_X
        global data_y
        global target
        target = data[:, selectIndex[0]]
        le = LabelEncoder()
        for i in range(0, len(preprocessing_Data.processCell)):
            if data[:, i].dtype == "int32" or data[:, i].dtype == "float64":
                pass
            elif i == selectIndex[0]:
                pass
            else:
                try:
                    data[:, i] = le.fit_transform(data[:, i])
                except:
                    data[:, i] = le.fit_transform(data[:, i].astype(str))
        data_X, data_y = data[:, :selectIndex[0]], data[:, selectIndex[0]]
        if selectIndex[0] <= 1:
            data_X, data_y = data[:, selectIndex[0]:-1], data[:, selectIndex[0]]
        le2 = LabelEncoder()
        le2.fit(data_y)
        data_y = le2.transform(data_y)
        label = np.unique(np.array(data_y))

        if len(label) <= 2:
            global counter
            counter3 = Counter(data_y)
            global classLable1
            global classLable2
            classLable1 = 0
            classLable2 = 0
            count = 0
            for k, v in counter3.items():
                if count == 0:
                    classLable1 = v
                elif count == 1:
                    classLable2 = v
                count += 1
            global strategy
            strategy = 0.0
            if classLable1 > classLable2:
                strategy = str(round(classLable2 / classLable1, 2) + 0.01)

            if classLable2 > classLable1:
                strategy = str(round(classLable1 / classLable2, 2) + 0.01)

            if float(strategy) > float(SmoteTree.LineEdit.text()):
                SmoteTree.LineEdit.setText(str(strategy))
            else:
                strategy = SmoteTree.LineEdit.text()
            smote = SMOTE(sampling_strategy=float(strategy),
                          k_neighbors=int(SmoteTree.LineEdit2.text()), random_state=int(SmoteTree.LineEdit3.text()))
        else:
            smote = SMOTE(k_neighbors=int(SmoteTree.LineEdit2.text()), random_state=int(SmoteTree.LineEdit3.text()))
        global smoteData_X
        global smoteData_y
        smoteData_X, smoteData_y = smote.fit_resample(data_X, data_y)
        y = le2.inverse_transform(smoteData_y)
        df = pd.DataFrame(data=y, columns=preprocessing_Data.selectCell)
        preprocessing_Data.processingDfs = preprocessing_Data.processingDfs.combine_first(df)
        preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(fileData.dfs[fileIndex])]
        preprocessing_Data.SmoteDfs = preprocessing_Data.processingDfs.copy()
        preprocessing_Data.completeDfs = preprocessing_Data.processingDfs.copy()
        preprocessing_Data.processCell.clear()
        preprocessing_Data.completeFlag = True
        if self.process not in self.name_2.text():
            if self.process not in " ":
                self.process2 = " " + self.process + " "
                self.name_2.setText(self.process2)
        function.SmoteInfo(self, dfs, preprocessing_Data.completeDfs)
        self.listWidget.addItem('  \n{}'.format(pd.get_dummies(data_y).sum()))
        self.listWidget_2.addItem('  \n{}'.format(pd.get_dummies(smoteData_y).sum()))
        self.listWidget.setVisible(True)
        self.pushButton.setVisible(True)
        self.name_2.setVisible(True)
        self.listWidget_2.setVisible(True)
        preprocessing.Button.setVisible(True)
        self.listWidget.addItem("")
        self.listWidget_2.addItem("")
        if "SMOTE" not in preprocessing_Data.label:
            preprocessing_Data.label += " SMOTE "
            self.label_2.setText(preprocessing_Data.label)

        counter = Counter(data_y)
        for k, v in counter.items():
            per = v / len(data_y) * 100
            self.listWidget.addItem('Class=%d, n=%d (%.3f%%)' % (k, v, per))

        global counter1
        counter1 = Counter(smoteData_y)
        for k, v in counter1.items():
            per = v / len(smoteData_y) * 100
            self.listWidget_2.addItem('Class=%d, n=%d (%.3f%%)' % (k, v, per))


# 특성 표준화
def NormalizeData(self):
    fileIndex = fileData.fileName.index(preprocessing_Data.filename)
    global NumberDfs
    preprocessing_Data.processingDfs = preprocessing_Data.completeDfs
    preprocessing_Data.processCell.clear()
    col = len(preprocessing_Data.completeDfs.columns)
    title = list(preprocessing_Data.completeDfs.columns)

    # ZScore (StandardScaler)
    if preprocessing_Data.comboBoxIndex == 0 or preprocessing_Data.comboBoxIndex == "0":
        if preprocessing_Data.selectCell:
            scaler = StandardScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.selectCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = StandardScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.processCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    # MinMax
    if preprocessing_Data.comboBoxIndex == 1:
        if preprocessing_Data.selectCell:
            scaler = MinMaxScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.selectCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = MinMaxScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.processCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    # RobustScaler
    if preprocessing_Data.comboBoxIndex == 2:
        if preprocessing_Data.selectCell:
            scaler = RobustScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.selectCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = RobustScaler()
            scaler = scaler.fit_transform(preprocessing_Data.processingDfs[preprocessing_Data.processCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    # Logistic
    if preprocessing_Data.comboBoxIndex == 3:
        if preprocessing_Data.selectCell:
            scaler = 1/(1/+np.exp(-preprocessing_Data.processingDfs[preprocessing_Data.selectCell]))
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = 1/(1/+np.exp(-preprocessing_Data.processingDfs[preprocessing_Data.processCell]))
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    # LogNormal
    if preprocessing_Data.comboBoxIndex == 4:
        if preprocessing_Data.selectCell:
            preprocessing_Data.processingDfs[preprocessing_Data.selectCell] = preprocessing_Data.processingDfs[preprocessing_Data.selectCell].astype(float)
            scaler = np.log1p(preprocessing_Data.processingDfs[preprocessing_Data.selectCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = np.log1p(preprocessing_Data.processingDfs[preprocessing_Data.processCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    # Tanh
    if preprocessing_Data.comboBoxIndex == 5:
        if preprocessing_Data.selectCell:
            scaler = np.tanh(preprocessing_Data.processingDfs[preprocessing_Data.selectCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.selectCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

        else:
            for i in list(range(0, col)):
                if preprocessing_Data.processingDfs[str(title[i])].dtype == "int32" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "float64" or \
                        preprocessing_Data.processingDfs[str(title[i])].dtype == "int64":
                    preprocessing_Data.processCell.append(str(title[i]))
            scaler = np.tanh(preprocessing_Data.processingDfs[preprocessing_Data.processCell])
            NumberDfs = pd.DataFrame(data=scaler, columns=preprocessing_Data.processCell)
            preprocessing_Data.processingDfs = NumberDfs.combine_first(preprocessing_Data.processingDfs)
            preprocessing_Data.processingDfs = preprocessing_Data.processingDfs[list(preprocessing_Data.completeDfs)]

    if self.process not in self.name_2.text():
        if self.process not in " ":
            self.process2 = " " + self.process + " "
            self.name_2.setText(self.process2)

    preprocessing_Data.completeDfs = preprocessing_Data.processingDfs.copy()
    preprocessing_Data.processCell.clear()
    preprocessing_Data.completeFlag = True
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
    if "Normalize" not in preprocessing_Data.label:
        preprocessing_Data.label += " Normalize "
        self.label_2.setText(preprocessing_Data.label)


def clipValue(target, dfs, index, mt):

    if index == 0:
        for i in mt:
            target.iloc[i] = round(dfs[preprocessing_Data.selectCell].mean(), 1)

    elif index == 1:
        for i in mt:
            target.iloc[i] = round(dfs[preprocessing_Data.selectCell].median(), 1)

    return target




