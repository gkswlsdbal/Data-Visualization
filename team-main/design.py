from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


# 테이블의 열제목 색을 현재 색테마에 맞춰 설정합니다.
def setTableHeaderColor(self, bgThem):
    if bgThem == 0:
        pass
    elif bgThem == 1:
        pass
    elif bgThem == 2:
        pass
    elif bgThem == 3:
        pass



# 색 테마에따라 다른 함수를 실행합니다.
def setColorOpt(self, bgThem):
    if bgThem == 0:
        setBlackTheme(self)
    elif bgThem == 1:
        setWhiteTheme(self)
    elif bgThem == 2:
        setBlueTheme(self)
    elif bgThem == 3:
        setGreenTheme(self)


# 스타일 시트를 변경합니다.
# 메인창 배경색(1), 탭추가버튼과 파일추가버튼, tab_2콤보박스 selected 배경색(2),
# 탭화면 배경색(3), 열,셀,파일리스트와 테이블위젯, tab_2 위젯 배경색, 콤보박스 selected 글자색(4),
# 이것들의 글자색(5), 그래프 버튼 배경색(6), 메뉴글자색과 메뉴바 분리선색(7)
def setColor(self, color1, color2, color3, color4, color5, color6, color7):
    self.setStyleSheet(f"background-color: {color1.name()};")

    self.addTabBtn.setStyleSheet(f"background-color: {color2.name()};")
    self.insertButton.setStyleSheet(f"background-color: {color2.name()};"
                                    f"font: 63 10pt \"Yu Gothic UI Semibold\";"
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
                                   f"font: font: 11pt \"맑은 고딕\";"
                                   f"color: {color5.name()};")

    self.barGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.lineGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.pieChartBtn.setStyleSheet(f"background-color: {color6.name()};")
    self.scatterChartBtn.setStyleSheet(f"background-color: {color6.name()};")

    self.menuBar().setStyleSheet("""QMenuBar::item {color: %s;}
                                    QMenu::item {color: %s;}
                                    QMenuBar::item:pressed {background: rgb(90, 120, 215);}
                                    QMenu::item:selected {background: rgb(90, 120, 215);}
                                    QMenuBar {border: 1px solid;
                                              border-bottom-color: %s;
                                              border-top-color: transparent;
                                              border-left-color: transparent;
                                              border-right-color: transparent;
                                              }
                                 """ % (color5.name(), color5.name(), color7.name()))

    self.secChartCombo.setStyleSheet("""
                                     QComboBox {background-color: %s;
                                                font: 12pt "Arial";
                                                color: %s;}
                                     QComboBox::item {background: %s; color: %s}
                                     QComboBox::item:selected {background: %s; color: %s}
                                     """ % (color4.name(), color5.name(),
                                           color4.name(), color5.name(),
                                           color2.name(), color4.name()))
    self.secSortCombo.setStyleSheet("""
                                    QComboBox {background-color: %s;
                                               font: 12pt "Arial";
                                               color: %s;}
                                    QComboBox::item {background: %s; color: %s}
                                    QComboBox::item:selected {background: %s; color: %s}
                                    """ % (color4.name(), color5.name(),
                                           color4.name(), color5.name(),
                                           color2.name(), color4.name()))
    self.notshowBtn.setStyleSheet(f"background-color: {color4.name()}; font: 12pt \"Arial\";"
                                  f"color: {color5.name()}")
    self.showBtn.setStyleSheet(f"background-color: {color4.name()}; font: 12pt \"Arial\";"
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
## setColor()를 실행시킵니다.
## 각각 필요한 다른 설정도 합니다.

def setBlackTheme(self):
    color1 = QColor(90, 90, 90)  # 짙은 회색,배경 색
    color2 = QColor(150, 150, 150)  # 연한 회색, 탭추가버튼과 파일추가버튼 바탕 색
    color3 = QColor(75, 75, 75)  # 탭화면 색
    color4 = QColor(45, 45, 45)  # 많이 짙은 회색, 리스트 바탕색
    color5 = QColor(255, 255, 255)  # 흰색, 글자, 테이블 배경 색
    color6 = QColor(230, 230, 230)  # 그래프버튼 배경

    setColor(self, color1, color2, color3, color4, color5, color6, QColor(153, 153, 153))

    self.insertButton.setStyleSheet(f"background-color: {color2.name()};"
                                    f"font: 63 10pt \"Yu Gothic UI Semibold\";"
                                    f"color: {color4.name()};")
    self.tableWidget.setStyleSheet(f"background-color: {color5.name()};"
                                   f"font: font: 11pt \"맑은 고딕\";")
    self.addTabBtn.setIcon(QIcon('img/plus.png'))


def setWhiteTheme(self):
    color1 = QColor(240, 240, 240)  # 연한 회색,배경 색
    color2 = QColor(250, 250, 250)  # 탭화면 색
    color3 = QColor(255, 255, 255)  # 흰색, 그 외 전부
    color4 = QColor(0, 0, 0)  # 검은색, 글자 색

    setColor(self, color1, color3, color2, color3, color4, color3, QColor(221, 221, 221))

    self.secChartCombo.setStyleSheet("""
                                     QComboBox {background-color: %s;
                                                font: 12pt "Arial";
                                                color: %s;}
                                     QComboBox::item {background: %s; color: %s}
                                     QComboBox::item:selected {background: %s; color: %s}
                                     """ % (color1.name(), color4.name(),
                                            color1.name(), color4.name(),
                                            color4.name(), color1.name()))
    self.secSortCombo.setStyleSheet("""
                                    QComboBox {background-color: %s;
                                               font: 12pt "Arial";
                                               color: %s;}
                                    QComboBox::item {background: %s; color: %s}
                                    QComboBox::item:selected {background: %s; color: %s}
                                    """ % (color1.name(), color4.name(),
                                           color1.name(), color4.name(),
                                           color4.name(), color1.name()))
    self.secColListLeftTitle.setStyleSheet(f"background-color: {color2.name()};"
                                           f"color: {color4.name()};")
    self.secColListRightTitle.setStyleSheet(f"background-color: {color2.name()};"
                                            f"color: {color4.name()};")
    self.notshowBtn.setStyleSheet(f"background-color: {color1.name()}; font: 12pt \"Arial\";"
                                  f"color: {color4.name()}")
    self.showBtn.setStyleSheet(f"background-color: {color1.name()}; font: 12pt \"Arial\";"
                               f"color: {color4.name()}")
    self.addTabBtn.setIcon(QIcon('img/plus.png'))


def setGreenTheme(self):
    color1 = QColor(232, 242, 232)  # 연한 녹색,배경색
    color2 = QColor(255, 255, 255)  # 흰색, 모든 버튼 배경색
    color3 = QColor(220, 238, 220)  # 연한 녹색보단 진한 색, 탭화면 색
    color4 = QColor(163, 204, 163)  # 부드러운 녹색, 그 외 전부
    color5 = QColor(0, 0, 0)  # 검은색, 모든 글자 색

    setColor(self, color1, color2, color3, color4, color5, color2, QColor(180, 220, 168))

    self.addTabBtn.setIcon(QIcon('img/plus.png'))


def setBlueTheme(self):
    color1 = QColor(214, 230, 245)  # 연한 하늘색,배경 색
    color2 = QColor(50, 110, 160)  # 파란 군청색, 탭추가버튼과 파일추가버튼 색
    color3 = QColor(200, 230, 255)  # 파랑색이 조금 강한 하늘색, 탭화면 색
    color4 = QColor(255, 255, 255)  # 흰색, 리스트, 테이블위젯, 파일추가버튼 글자 색
    color5 = QColor(0, 0, 0)  # 검은색, 리스트와 테이블 글자 색

    setColor(self, color1, color2, color3, color4, color5, color4, QColor(170, 170, 238))

    self.insertButton.setStyleSheet(f"background-color: {color2.name()};"
                                    f"font: 63 10pt \"Yu Gothic UI Semibold\";"
                                    f"color: {color4.name()};")
    self.addTabBtn.setIcon(QIcon('img/white_plus.png'))

