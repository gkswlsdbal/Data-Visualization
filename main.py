import sys

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic
import pandas as pd

form_class = uic.loadUiType('ProjectUI.ui')[0]

# 파일 경로 리스트
links = []

# 화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class):

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.insertButton.clicked.connect(self.btnClick)
        self.installEventFilter(self)
        self.setAcceptDrops(True)
        self.FileList.itemDoubleClicked.connect(self.fileClick)

    # 표 그리는 함수
    def draw(self, fl):

        df = pd.read_csv(fl)
        # 리스트로 변환후 파일이름 가져오기
        table = self.tableWidget
        table.setSortingEnabled(True)

        # 표의 크기를 지정
        col = len(df.columns)
        row = len(df)
        table.setColumnCount(col)
        table.setRowCount(row)

        # 열 제목 지정
        title = list(df.columns)
        self.cellList.clear()
        for i in list(range(0, col)):
            header = QtWidgets.QTableWidgetItem(title[i])
            header.setBackground(Qt.yellow)
            table.setHorizontalHeaderItem(i, header)
            self.cellList.addItem(str(title[i]))

        # 셀 내용 채우기
        for i in list(range(0, col)):
            a = list(df[title[i]])
            for j in list(range(0, row)):
                s = str(a[j])
                if s == 'nan':
                    s = ''
                table.setItem(j, i, QtWidgets.QTableWidgetItem(s))

    # 파일 드레그앤 드랍
    @QtCore.pyqtSlot(str)
    def eventFilter(self, object, event):

        if (object is self):
            if (event.type() == QtCore.QEvent.DragEnter):
                if event.mimeData().hasUrls():
                    event.accept()

                else:
                    event.ignore()

            if (event.type() == QtCore.QEvent.Drop):
                if event.mimeData().hasUrls():
                    url = event.mimeData().urls()[0]
                    link = []
                    for url in event.mimeData().urls():
                        link.append(str(url.toLocalFile()))

                file = "".join(link)
                self.fileCheck(file)

                return False

        return False

    # insert버튼 클릭할때 실행
    def btnClick(self):

        filename = QFileDialog.getOpenFileNames(self)
        file = "".join(filename[0])
        self.fileCheck(file)

    # 파일 리스트안에 있는 파일 더블클릭할 때 실행
    def fileClick(self):

        i = self.FileList.currentRow()
        self.fileCheck("".join(links[i]))

    # 파일리스트에 이미 파일 있는지 검사
    def fileCheck(self, file):

        if file in links:
            self.draw(file)
        else:
            links.append(file)
            site = file.split("/")
            self.FileList.addItem(site[-1])
            self.draw(file)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()
    app.exec_()





