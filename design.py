from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys

class Color:
    def setBlack(self):
        self.color1 = QColor(90, 90, 90)  # 짙은 회색,배경 색
        self.color2 = QColor(150, 150, 150)  # 연한 회색, 탭추가버튼과 파일추가버튼 바탕 색
        self.color3 = QColor(75, 75, 75)  # 탭화면 색
        self.color4 = QColor(45, 45, 45)  # 많이 짙은 회색, 리스트 바탕색
        self.color5 = QColor(255, 255, 255)  # 흰색, 글자, 테이블 배경 색
        self.color6 = QColor(230, 230, 230)  # 그래프버튼 배경
        self.color7 = QColor(153, 153, 153)  # 메뉴바와 툴바 밑줄

    def setWhite(self):
        self.color1 = QColor(240, 240, 240)  # 연한 회색,배경 색
        self.color2 = QColor(250, 250, 250)  # 탭화면 색
        self.color3 = QColor(255, 255, 255)  # 흰색, 그 외 전부
        self.color4 = QColor(0, 0, 0)  # 검은색, 글자 색
        self.color5 = QColor(221, 221, 221)  # 메뉴바와 툴바 밑줄

    def setBlue(self):
        self.color1 = QColor(214, 230, 245)  # 연한 하늘색,배경 색
        self.color2 = QColor(50, 110, 160)  # 파란 군청색, 탭추가버튼과 파일추가버튼 색
        self.color3 = QColor(200, 230, 255)  # 파랑색이 조금 강한 하늘색, 탭화면 색
        self.color4 = QColor(255, 255, 255)  # 흰색, 리스트, 테이블위젯, 파일추가버튼 글자 색
        self.color5 = QColor(0, 0, 0)  # 검은색, 리스트와 테이블 글자 색
        self.color6 = QColor(170, 170, 238)  # 메뉴바와 툴바 밑줄

    def setGreen(self):
        self.color1 = QColor(232, 242, 232)  # 연한 녹색,배경색
        self.color2 = QColor(255, 255, 255)  # 흰색, 모든 버튼 배경색
        self.color3 = QColor(220, 238, 220)  # 연한 녹색보단 진한 색, 탭화면 색
        self.color4 = QColor(163, 204, 163)  # 부드러운 녹색, 그 외 전부
        self.color5 = QColor(0, 0, 0)  # 검은색, 모든 글자 색
        self.color6 = QColor(180, 220, 168)  # 메뉴바와 툴바 밑줄


def selectJoinColor(self, bg, font_family, font_size):
    c = Color()
    if bg == 'Black':
        c.setBlack()
        self.widget.setStyleSheet(f"background-color: {c.color7.name()};"
                           f"font: {font_size}pt '{font_family}';")
    elif bg == 'White':
        c.setWhite()
        self.widget.setStyleSheet(f"background-color: {c.color1.name()};"
                           f"font: {font_size}pt '{font_family}';")
    elif bg == 'Blue':
        c.setBlue()
        self.widget.setStyleSheet(f"background-color: {c.color1.name()};"
                                  f"font: {font_size}pt '{font_family}';")
    elif bg == 'Green':
        c.setGreen()
        self.widget.setStyleSheet(f"background-color: {c.color3.name()};"
                           f"font: {font_size}pt '{font_family}';")
    self.JoinList.setStyleSheet(f"background-color: rgb(255, 255, 255)")
    self.JoinList2.setStyleSheet(f"background-color: rgb(255, 255, 255)")
    self.cellName.setStyleSheet(f"background-color: rgb(255, 255, 255)")
    self.cellName2.setStyleSheet(f"background-color: rgb(255, 255, 255)")


def selectFAbsorColor(self, bg, font_family, font_size):
    if bg == 'Black':
        setFAbsorBlack(self, font_family, font_size)
    elif bg == 'White':
        setFAbsorWhite(self, font_family, font_size)
    elif bg == 'Blue':
        setFAbsorBlue(self, font_family, font_size)
    elif bg == 'Green':
        setFAbsorGreen(self, font_family, font_size)


def setFAbsorStyle(self, color1, color2, color3, color4, font_family, font_size):
    self.widget.setStyleSheet(f"background-color: {color1.name()};"
                              f"font: {font_size}pt '{font_family}';")
    self.FileList.setStyleSheet(f"border: 1px solid {color4.name()};"
                                f"background-color: {color2.name()};")
    self.abList.setStyleSheet(f"background-color: {color2.name()};")
    self.abList_2.setStyleSheet(f"background-color: {color2.name()};")
    self.bottomWidget.setStyleSheet(f"background-color: {color1.name()};"
                                    f"color: {color2.name()};")
    self.splitter.setStyleSheet(f'''border: 1px solid;
                                   border-bottom-color: {color4.name()};
                                   border-top-color: transparent;
                                   border-left-color: transparent;
                                   border-right-color:transparent;''')

def setFAbsorBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()
    setFAbsorStyle(self, c.color1, c.color5, c.color3, c.color4, font_family, font_size)

def setFAbsorWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()
    setFAbsorStyle(self, c.color1, c.color2, c.color4, c.color5, font_family, font_size)

def setFAbsorBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()
    setFAbsorStyle(self, c.color3, c.color4, c.color4, c.color6, font_family, font_size)

def setFAbsorGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()
    setFAbsorStyle(self, c.color3, c.color2, c.color4, c.color6, font_family, font_size)


def selectCAbsorColor(self, bg, font_family, font_size):
    if bg == 'Black':
        setCAbsorBlack(self, font_family, font_size)
    elif bg == 'White':
        setCAbsorWhite(self, font_family, font_size)
    elif bg == 'Blue':
        setCAbsorBlue(self, font_family, font_size)
    elif bg == 'Green':
        setCAbsorGreen(self, font_family, font_size)


def setCAbsorStyle(self, color1, color2, color3, color4, font_family, font_size):
    self.setStyleSheet(f"background-color: {color1.name()};"
                       f"font: {font_size}pt '{font_family}';")
    self.comboBox.setStyleSheet(f"background-color: {color3.name()};"
                                f"color: {color4.name()};")
    self.colLabel.setAlignment(Qt.AlignCenter)
    self.colLabel.setStyleSheet("border: 1px solid rgb(220, 220, 220);")
    self.slctColLabel.setAlignment(Qt.AlignCenter)
    self.slctColLabel.setStyleSheet("border: 1px solid rgb(220, 220, 220);")
    self.midLWidget.setStyleSheet(f"background-color: {color3.name()};"
                                  f"color: {color4.name()};")
    self.midRWidget.setStyleSheet(f"background-color: {color3.name()};"
                                  f"color: {color4.name()};")
    self.buttonBox.setStyleSheet(f"background-color: {color2.name()};"
                                 f"color: {color3.name()};")


def setCAbsorBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()
    setCAbsorStyle(self, c.color1, c.color5, c.color4, c.color5, font_family, font_size)
    self.colLabel.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
    self.slctColLabel.setStyleSheet("border: 1px solid rgb(0, 0, 0);")


def setCAbsorWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()
    setCAbsorStyle(self, c.color1, c.color1, c.color3, c.color4, font_family, font_size)


def setCAbsorBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()
    setCAbsorStyle(self, c.color1, c.color2, c.color4, c.color5, font_family, font_size)


def setCAbsorGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()
    setCAbsorStyle(self, c.color3, c.color2, c.color2, c.color5, font_family, font_size)


###setting UI###
def selectSettColor(self, bg, font_family, font_size):
    if bg == 'Black':
        setSettBlack(self, font_size)
    elif bg == 'White':
        setSettWhite(self, font_size)
    elif bg == 'Blue':
        setSettBlue(self, font_size)
    elif bg == 'Green':
        setSettGreen(self, font_size)
    self.fontCombo.setCurrentFont(QFont(font_family))
    self.sizeCombo.setCurrentText(font_size)


def setSettStyle(self, color1, color2, color3, color4, color5, font_size):
    self.setStyleSheet(f"background-color: {color3.name()};"
                       f"font: {font_size}pt;"
                       f"color: {color4.name()}")

    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: %s;
                                            color: %s;
                                            font: %spt; }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s; }
                                     """ % (color1.name(), color3.name(), font_size,
                                            color3.name(), color1.name()))
    self.setWidget.setStyleSheet(f"background-color: {color3.name()};"
                                 f"color: {color1.name()};")
    self.line.setStyleSheet(f"background-color: {color5.name()};")

def setSettBlack(self, font_size):
    c = Color()
    c.setBlack()
    setSettStyle(self, c.color5, c.color4, c.color1, c.color6, c.color7, font_size)
    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: %s;
                                            color: %s;
                                            font: %spt; }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s; }
                                     """ % (c.color4.name(), c.color5.name(), font_size,
                                            c.color5.name(), c.color4.name()))

def setSettWhite(self, font_size):
    c = Color()
    c.setWhite()
    setSettStyle(self, c.color4, c.color3, c.color1, c.color4, c.color5, font_size)
    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: %s;
                                            color: %s;
                                            font: %spt; }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s; }
                                     """ % (c.color3.name(), c.color4.name(), font_size,
                                            c.color1.name(), c.color4.name()))

def setSettBlue(self, font_size):
    c = Color()
    c.setBlue()
    setSettStyle(self, c.color5, c.color2, c.color3, c.color5, c.color6, font_size)

    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: %s;
                                            color: %s;
                                            font: %spt;}
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s;}
                                     """ % (c.color4.name(), c.color5.name(), font_size,
                                            c.color3.name(), c.color5.name()))

def setSettGreen(self, font_size):
    c = Color()
    c.setGreen()
    setSettStyle(self, c.color5, c.color3, c.color3, c.color5, c.color4, font_size)
    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: %s;
                                            color: %s;
                                            font: %spt; }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s; }
                                     """ % (c.color2.name(), c.color3.name(), font_size,
                                            c.color3.name(), c.color5.name()))

###Main UI###
def selectMainColor(self, bg, font_family, font_size):
    if bg == 'Black':
        setMainBlack(self, font_family, font_size)
    elif bg == 'White':
        setMainWhite(self, font_family, font_size)
    elif bg == 'Blue':
        setMainBlue(self, font_family, font_size)
    elif bg == 'Green':
        setMainGreen(self, font_family, font_size)

    # 스타일 시트를 변경합니다.
    # 메인창 배경색(1), 탭추가버튼과 파일추가버튼, tab_2콤보박스 selected 배경색(2),
    # 탭화면 배경색(3), 열,셀,파일리스트와 테이블위젯, tab_2 위젯 배경색, 콤보박스 selected 글자색(4),
    # 이것들의 글자색(5), 그래프 버튼 배경색(6), 메뉴글자색과 메뉴바 분리선색(7)


def setMainStyle(self, color1, color2, color3, color4, color5, color6, color7, font_family, font_size):
    self.widget.setStyleSheet(f"background-color: {color1.name()};"
                              f"font: " + font_size + "pt '" + font_family + "';")
    self.statusBar().setStyleSheet(f"background-color: {color1.name()};")

    self.insertButton.setStyleSheet(f"background-color: {color2.name()};"
                                    f"color: {color5.name()};")

    self.tab_1.setStyleSheet(f"""background-color: {color3.name()};
                                     border-color: {color3.name()}""")
    self.tab_2.setStyleSheet(f"""background-color: {color3.name()};
                                     border-color: {color3.name()}""")

    self.colInfoListWidget.setStyleSheet(f"background-color: {color4.name()};"
                                         f"color: {color5.name()};")
    self.cellList.setStyleSheet(f"background-color: {color4.name()};"
                                f"color: {color5.name()};")
    self.FileList.setStyleSheet(f"background-color: {color4.name()};"
                                f"color: {color5.name()};")
    self.tableWidget.setStyleSheet(f"background-color: {color4.name()};"
                                   f"color: {color5.name()};")

    self.barGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.lineGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.pieChartBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.scatterChartBtn.setStyleSheet(f"background-color: {color6.name()};")

    self.menuBar().setStyleSheet("""
                                    QMenuBar::item:pressed {background: rgb(90, 120, 215);}
                                    QMenu::item:selected {background: rgb(90, 120, 215);}
                                    QMenuBar {border: 1px solid;
                                                border-bottom-color: %s;
                                                border-top-color: transparent;
                                                border-left-color: transparent;
                                                border-right-color: transparent;
                                              }
                                """ % (color7.name()))

    self.secChartCombo.setStyleSheet("""
                                        QComboBox {background-color: %s;"""
                                     """color: %s;}
                              QComboBox::item {background: %s; color: %s}
                              QComboBox::item:selected {background: %s; color: %s}
                              """ % (color4.name(), color5.name(),
                                     color4.name(), color5.name(),
                                     color2.name(), color4.name()))
    self.secSortCombo.setStyleSheet("""
                                    QComboBox {background-color: %s;"""
                                    """ color: %s;}
                                QComboBox::item {background: %s; color: %s}
                                QComboBox::item:selected {background: %s; color: %s}
                                """ % (color4.name(), color5.name(),
                                       color4.name(), color5.name(),
                                       color2.name(), color4.name()))
    self.notshowBtn.setStyleSheet(f"background-color: {color4.name()};"
                                  f"color: {color5.name()}")
    self.showBtn.setStyleSheet(f"background-color: {color4.name()};"
                               f"color: {color5.name()}")
    self.secColListLeftTitle.setStyleSheet(f"background-color: {color4.name()};"
                                           f"color: {color5.name()};")
    self.secColListRightTitle.setStyleSheet(f"background-color: {color4.name()};"
                                            f"color: {color5.name()};")
    self.showingColList.setStyleSheet("""QListWidget {background-color: %s; color: %s;}
                                      """ % (color4.name(), color5.name()))
    self.unshowingColList.setStyleSheet("""QListWidget {background-color: %s; color: %s;}
                                        """ % (color4.name(), color5.name()))


## 이 아래부턴 스타일시트변경에 들어갈 색을 만들고
## setMainColor()()를 실행시킵니다.
## 각각 필요한 다른 설정도 합니다.

def setMainBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 c.color5, c.color6, c.color7, font_family, font_size)

    self.insertButton.setStyleSheet(f"background-color: {c.color2.name()};"
                                    f"color: {c.color4.name()};")
    self.tableWidget.setStyleSheet(f"background-color: {c.color5.name()};")
    self.tabWidget.setStyleSheet(f"color: {c.color5.name()};")

def setMainWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()

    setMainStyle(self, c.color1, c.color3, c.color2, c.color3,
                 c.color4, c.color3, c.color5, font_family, font_size)

    self.secChartCombo.setStyleSheet("""
                                     QComboBox {background-color: %s;"""
                                     """color: %s;}
                                     QComboBox::item {background: %s; color: %s}
                                     QComboBox::item:selected {background: %s; color: %s}
                                     """ % (c.color1.name(), c.color4.name(),
                                            c.color1.name(), c.color4.name(),
                                            c.color4.name(), c.color1.name()))
    self.secSortCombo.setStyleSheet("""
                                    QComboBox {background-color: %s;"""
                                    """color: %s;}
                                    QComboBox::item {background: %s; color: %s}
                                    QComboBox::item:selected {background: %s; color: %s}
                                    """ % (c.color1.name(), c.color4.name(),
                                           c.color1.name(), c.color4.name(),
                                           c.color4.name(), c.color1.name()))
    self.secColListLeftTitle.setStyleSheet(f"background-color: {c.color2.name()};"
                                           f"color: {c.color4.name()};")
    self.secColListRightTitle.setStyleSheet(f"background-color: {c.color2.name()};"
                                            f"color: {c.color4.name()};")
    self.notshowBtn.setStyleSheet(f"background-color: {c.color1.name()};"
                                  f"color: {c.color4.name()}")
    self.showBtn.setStyleSheet(f"background-color: {c.color1.name()};"
                               f"color: {c.color4.name()}")

def setMainBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 c.color5, c.color4, c.color6, font_family, font_size)
    self.insertButton.setStyleSheet(f"background-color: {c.color2.name()};"
                                    f"color: {c.color4.name()};")

def setMainGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 c.color5, c.color2, c.color6, font_family, font_size)
