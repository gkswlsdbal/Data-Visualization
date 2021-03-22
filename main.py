import sys
from builtins import list

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd
from pytz import unicode
import urllib

form_class = uic.loadUiType('ProjectUI.ui')[0]
#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :

    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.xlsxBtn.clicked.connect(self.btnClick)
        self.tableWidget.installEventFilter(self)
        self.tableWidget.setAcceptDrops(True)
        self.tableWidget.setDragEnabled(True)


    @QtCore.pyqtSlot(str)
    def eventFilter(self, object,event):
        if(object is self.tableWidget):
            if(event.type()==QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()
                    print("accept")
                    url=event.mimeData().urls()[0]
                    print(type(url))

                else:
                    event.ignore()
                    print("ignore")

        return False

    def btnClick(self):

        filename = QFileDialog.getOpenFileNames(self)
        file="".join(filename[0])
        print(file)
        df = pd.read_excel(file)
        table = self.tableWidget
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






if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()
    #프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()