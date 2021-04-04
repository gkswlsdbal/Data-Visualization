import math
import numpy as np
import pandas as pd
import data


# 셀 정보를 출력하는 함수
def cellInfo(self):
    self.colInfoListWidget.clear()

    coltitle = self.cellList.currentItem().text()  # 열 제목
    roundnum = 4  # 평균을 구할 때 소수점 아래로 남길 숫자 개수

    collist = list(data.tableDf[coltitle])  # 열을 리스트 타입으로 바꿉니다.
    collist = deleteSpaceVal(collist)

    coltable = pd.DataFrame(collist)  # 정리된 리스트를 다시 dataframe으로 바꿉니다.
    coltable.columns = [coltitle]

    # 열 이름, 행 개수
    self.colInfoListWidget.addItem(str("Title: " + coltitle))
    self.colInfoListWidget.addItem(str("Row: " + str(self.tableWidget.rowCount())))

    # 열의 타입이 숫자일 경우 열의 평균값, 중간값, 최대값, 열의 최소값, 타입을 출력합니다.
    if isNumber(coltable, coltitle):

        try:
            collist = list(map(int, collist))
        except:
            collist = list(map(float, collist))

        collist = [x for x in collist if math.isnan(x) == False]  # nan 제거

        self.colInfoListWidget.addItem(str("Average: ") + str(round(sum(collist) / len(collist), roundnum)))
        self.colInfoListWidget.addItem(str("Median: ") + str(np.median(collist)))
        self.colInfoListWidget.addItem(str("Max: ") + str(max(collist)))
        self.colInfoListWidget.addItem(str("Min:  ") + str(min(collist)))
        self.colInfoListWidget.addItem("Type: Number")
    else:  # 숫자가 아니면 타입만 출력합니다.
        self.colInfoListWidget.addItem("Type: String")

    # 빈 값 개수입니다.
    self.colInfoListWidget.addItem(str("Missing: ") + str(countEmptyRow(data.tableDf[coltitle])))


# 데이터프레임변수 열의 타입이 실수인지 확인합니다.
def isNumber(coltable, title):
    try:
        coltable = coltable.astype({title: 'int'})
        return True
    except ValueError:
        try:
            coltable = coltable.astype({title: 'float'})
            return True
        except ValueError:
            return False


# 리스트에 스페이스 값이 들어있으면 지웁니다.
def deleteSpaceVal(collist):
    a = 0
    while a < len(collist) - 1:
        if str(collist[a]).isspace():
            del collist[a]
        else:
            a += 1
    return collist


# nan과 빈칸 개수를 셉니다.
def countEmptyRow(df):
    empty = df.isnull().sum().sum()
    for i in list(df):
        if str(i).isspace():
            empty += 1
    return empty