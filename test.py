import sys
import pandas as pd
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtWidgets, QtGui



df = pd.read_excel('C:/Users/admin/Desktop/pythonProject/data/sdw_dataset_list.xlsx')
print(df)

class TableWidget(QtWidgets.QWidget):
    """표를 보여주는 위젯"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('테이블 테스트')

        """
        표 위젯 초기화
        """
        table = QtWidgets.QTableWidget(self)
        table.resize(1000, 700)
        # 표의 크기를 지정
        col = len(df.columns)
        row = len(df)
        table.setColumnCount(col)
        table.setRowCount(row)
        # 열 제목 지정
        title = list(df.columns)
        for i in list(range(0, col)):
            header = QtWidgets.QTableWidgetItem(title[i])
            header.setBackground(Qt.yellow)
            table.setHorizontalHeaderItem(i, header)


        # 셀 내용 채우기
        for i in list(range(0, col)):
            a = list(df[title[i]])
            for j in list(range(0, row)):
                s = str(a[j])
                if s == 'nan':
                    s = ''
                table.setItem(j, i, QtWidgets.QTableWidgetItem(s))


if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    APP.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    WINDOW = TableWidget()
    WINDOW.show()
    APP.exec()