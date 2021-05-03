from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Color:
    def setBlack(self):
        self.color1 = QColor(90, 90, 90)  # 짙은 회색,배경 색
        self.color2 = QColor(75, 75, 75)  # 탭화면 색
        self.color3 = QColor(130, 130, 130)  # 툴바 밑줄
        self.color4 = QColor(45, 45, 45)  # 많이 짙은 회색

    def setWhite(self):
        self.color1 = QColor(240, 240, 240)  # 연한 회색,배경 색
        self.color2 = QColor(250, 250, 250)  # 탭화면 색
        self.color3 = QColor(200, 200, 200)  # 툴바 밑줄
        self.color4 = QColor(100, 100, 100)

    def setBlue(self):
        self.color1 = QColor(214, 230, 245)  # 연한 하늘색,배경 색
        self.color2 = QColor(200, 230, 255)  # 파랑색이 조금 강한 하늘색, 탭화면 색
        self.color3 = QColor(170, 170, 238)  # 툴바 밑줄
        self.color4 = QColor(50, 110, 160)  # 파란 군청색, 탭추가버튼과 파일추가버튼 색

    def setGreen(self):
        self.color1 = QColor(232, 242, 232)  # 연한 녹색,배경색
        self.color2 = QColor(220, 238, 220)  # 연한 녹색보단 진한 색, 탭화면 색
        self.color3 = QColor(180, 220, 168)  # 툴바 밑줄
        self.color4 = QColor(85, 155, 85)


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
    self.topWidget.setStyleSheet(f"background-color: {color1.name()};"
                                 f"font: {font_size}pt {font_family};")
    self.FileList.setStyleSheet(f"background-color: white;")
    self.abList.setStyleSheet(f"background-color: {color2.name()};")
    self.abList2.setStyleSheet(f"background-color: {color2.name()};")
    self.bottomWidget.setStyleSheet(f"background-color: {color1.name()};")
    self.splitter.setStyleSheet(f'''border: 1px solid;
                                   border-bottom-color: {color4.name()};
                                   border-top-color: transparent;
                                   border-left-color: transparent;
                                   border-right-color:transparent;''')
    self.JoinList.setStyleSheet('background-color: white')
    self.JoinList2.setStyleSheet('background-color: white')


def setFAbsorBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()
    setFAbsorStyle(self, c.color1, QColor(0, 0, 0), c.color3, QColor(255, 255, 255), font_family, font_size)


def setFAbsorWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()
    setFAbsorStyle(self, c.color3, QColor(255, 255, 255), c.color2, QColor(0, 0, 0), font_family, font_size)


def setFAbsorBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()
    setFAbsorStyle(self, c.color1, QColor(255, 255, 255), c.color1, c.color4, font_family, font_size)


def setFAbsorGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()
    setFAbsorStyle(self, c.color3, c.color1, QColor(0, 0, 0), c.color4, font_family, font_size)


def selectCAbsorColor(self, bg, font_family, font_size):
    if bg == 'Black':
        setCAbsorBlack(self, font_family, font_size)
    elif bg == 'White':
        setCAbsorWhite(self, font_family, font_size)
    elif bg == 'Blue':
        setCAbsorBlue(self, font_family, font_size)
    elif bg == 'Green':
        setCAbsorGreen(self, font_family, font_size)


def setCAbsorStyle(self, color1, color2, font_family, font_size):
    self.setStyleSheet(f"background-color: {color1.name()};"
                       f"font: {font_size}pt '{font_family}';")
    self.comboBox.setStyleSheet("""QComboBox
                                   {background-color: white; color: black;}
                                   QComboBox::item:selected
                                   {background-color: %s; color: white;}"""
                                % (color2.name()))
    self.listWidget.setStyleSheet("background-color: white;"
                                  "color: black;")
    self.slctListWidget.setStyleSheet("background-color: white;"
                                      "color: black;")
    self.colLabel.setAlignment(Qt.AlignCenter)
    self.colLabel.setStyleSheet("border: 1px solid black;"
                                "color: white"
                                f"background-color: {color2.name()}")
    self.slctColLabel.setAlignment(Qt.AlignCenter)
    self.slctColLabel.setStyleSheet("border: 1px solid black;"
                                    "color: white"
                                    f"background-color: {color2.name()}")
    self.topWidget.setStyleSheet(f"border: 1px solid {color2.name}")
    # self.buttonBox.setStyleSheet(f"background-color: {color2.name()};"
    #                              f"color: {color3.name()};")


def setCAbsorBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()
    setCAbsorStyle(self, c.color2, c.color4, font_family, font_size)
    # self.colLabel.setStyleSheet("border: 1px solid rgb(0, 0, 0);")
    # self.slctColLabel.setStyleSheet("border: 1px solid rgb(0, 0, 0);")


def setCAbsorWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()
    setCAbsorStyle(self, c.color1, c.color4, font_family, font_size)


def setCAbsorBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()
    setCAbsorStyle(self, c.color1, c.color2, font_family, font_size)


def setCAbsorGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()
    setCAbsorStyle(self, c.color1, c.color3, font_family, font_size)


###setting UI###
# def setSett(tool_pos, too_style, table_grid,
#             table_header_color, table_row_color, table_colored_row):
#     if tool_pos == 'up'

def selectSettStyle(self, bg, font_family, font_size):
    c = Color()
    if bg == 'Black':
        c.setBlack()
        # setSettBlack(self, font_family, font_size)
        setSettStyle(self, c.color1, QColor(255, 255, 255),
                     c.color3, c.color4, font_family, font_size)
    elif bg == 'White':
        c.setWhite()
        # setSettWhite(self, font_family, font_size)
        setSettStyle(self, c.color1, QColor(0, 0, 0),
                     c.color3, c.color2, font_family, font_size)
    elif bg == 'Blue':
        c.setBlue()
        # setSettBlue(self, font_family, font_size)
        setSettStyle(self, c.color1, QColor(0, 0, 0),
                     c.color3, QColor(255, 255, 255), font_family, font_size)
    elif bg == 'Green':
        c.setGreen()
        # setSettGreen(self, font_family, font_size)
        setSettStyle(self, c.color1, QColor(0, 0, 0),
                     c.color3, QColor(255, 255, 255), font_family, font_size)
    self.fontCombo.setCurrentFont(QFont(font_family))
    self.sizeCombo.setCurrentText(font_size)


# 1: 배경, 2: 폰트색, 3: 확인취소버튼 분리줄 색
def setSettStyle(self, color1, color2, color3, color4, font_family, font_size):
    import configparser
    config = configparser.ConfigParser()
    config.read('setting.ini')

    self.setStyleSheet(f"font: {font_size}pt {font_family};"
                       f"color: {color2.name()}")

    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: white;
                                            border: 0px;
                                            color: black;
                                            }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: %s; }
                                     """ % (color1.name(), color2.name()))
    self.topWidget.setStyleSheet(f"background-color: {color1.name()};"
                                 f"border: 2px solid {color3.name()};"
                                 "border-top-color: transparent;"
                                 "border-left-color: transparent;"
                                 "border-right-color: transparent;")
    self.bgcCombo.setStyleSheet("""QComboBox {
                                        background-color: %s;
                                        color: %s;}
                                   QComboBox::item:selected {
                                        background: %s;
                                        color: %s;"""
                                % (color4.name(), color2.name(),
                                   color2.name(), color4.name()))
    self.fontCombo.setStyleSheet("""QComboBox {
                                        background-color: %s;
                                        color: %s;}
                                   QComboBox::item:selected {
                                        background: %s;
                                        color: %s;"""
                                 % (color4.name(), color2.name(),
                                    color2.name(), color4.name()))
    self.sizeCombo.setStyleSheet("""QComboBox {
                                        background-color: %s;
                                        color: %s;
                                        combobox-popup: 0;}
                                   QComboBox::item:selected {
                                        background: %s;
                                        color: %s;"""
                                 % (color4.name(), color2.name(),
                                    color2.name(), color4.name()))
    self.toolPosGroup.setStyleSheet(f"border: 2px solid {color4.name()};")
    self.toolStyGroup.setStyleSheet(f"border: 2px solid {color4.name()};")
    self.bottomWidget.setStyleSheet(f"background-color: {color1.name()};")
    self.bgcLabel.setStyleSheet("border: transparent;")
    self.sizeLabel.setStyleSheet("border: transparent;")
    self.fontLabel.setStyleSheet("border: transparent;")
    self.gridChkBox.setStyleSheet("border: transparent;")
    self.hClrLabel.setStyleSheet("border: transparent;")
    self.rClrLabel.setStyleSheet("border: transparent;")
    self.evenRow.setStyleSheet("border: transparent;")
    self.oddRow.setStyleSheet("border: transparent;")
    self.allRow.setStyleSheet("border: transparent;")
    self.toolPosUp.setStyleSheet("border: transparent;")
    self.toolPosLeft.setStyleSheet("border: transparent;")
    self.toolPosRight.setStyleSheet("border: transparent;")
    self.toolPosBottom.setStyleSheet("border: transparent;")
    self.toolIcon.setStyleSheet("border: transparent;")
    self.toolText.setStyleSheet("border: transparent;")
    self.toolTextBesideIcon.setStyleSheet("border: transparent;")
    self.toolTextUnderIcon.setStyleSheet("border: transparent;")
    self.stackWidget.setStyleSheet("border: transparent;")

    self.hColorBtn.setStyleSheet('background-color:'
                                 f'{QColor(config["STYLE"]["table_header_color"]).name()};'
                                 'color: black;')
    self.rColorBtn.setStyleSheet('background-color:'
                                 f'{QColor(config["STYLE"]["table_row_color"]).name()};'
                                 'color: black;')


def setToolBarStyle(self, pos, style, color):
    if pos == 'top':
        self.addToolBar(Qt.TopToolBarArea, self.toolbar)
        self.toolbar.setStyleSheet("QToolBar {"
                                   "background-color: white;"
                                   "border:2px solid %s;"
                                   "border-top-color:transparent;"
                                   "border-left-color:transparent;"
                                   "border-right-color:transparent;}" % (color.name()))
    elif pos == 'left':
        self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
        self.toolbar.setStyleSheet("QToolBar {"
                                   "background-color: white;"
                                   "border:2px solid %s;"
                                   "border-top-color:transparent;"
                                   "border-left-color:transparent;"
                                   "border-bottom-color:transparent;}" % (color.name()))
    elif pos == 'right':
        self.addToolBar(Qt.RightToolBarArea, self.toolbar)
        self.toolbar.setStyleSheet("QToolBar {"
                                   "background-color: white;"
                                   "border:2px solid %s;"
                                   "border-top-color:transparent;"
                                   "border-right-color:transparent;"
                                   "border-bottom-color:transparent;}" % (color.name()))
    elif pos == 'bottom':
        self.addToolBar(Qt.BottomToolBarArea, self.toolbar)
        self.toolbar.setStyleSheet("QToolBar {"
                                   "background-color: white;"
                                   "border:2px solid %s;"
                                   "border-bottom-color:transparent;"
                                   "border-left-color:transparent;"
                                   "border-right-color:transparent;}" % (color.name()))

    if style == 'icon':
        self.toolbar.setToolButtonStyle(Qt.ToolButtonIconOnly)
    elif style == 'text':
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextOnly)
    elif style == 'textBesideIcon':
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
    elif style == 'textUnderIcon':
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)


def setTableStyle(self, table_grid, table_header_color, table_row_color, table_colored_row):
    table_header_color = QColor(table_header_color)
    table_row_color = QColor(table_row_color)

    if table_grid == 'true':
        self.tableWidget.setShowGrid(True)
    else:
        self.tableWidget.setShowGrid(False)

    if table_colored_row == 'all':
        for col in range(self.tableWidget.columnCount()):
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.item(row, col).setBackground(table_row_color)
    elif table_colored_row == 'odd':
        for col in range(self.tableWidget.columnCount()):
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.item(row, col).setBackground(QColor(255, 255, 255))

        for col in range(self.tableWidget.columnCount()):
            for row in range(0, self.tableWidget.rowCount(), 2):
                self.tableWidget.item(row, col).setBackground(table_row_color)
        self.tableWidget.setStyleSheet("background-color: white")
    elif table_colored_row == 'even':
        for col in range(self.tableWidget.columnCount()):
            for row in range(self.tableWidget.rowCount()):
                self.tableWidget.item(row, col).setBackground(QColor(255, 255, 255))

        for col in range(self.tableWidget.columnCount()):
            for row in range(1, self.tableWidget.rowCount(), 2):
                self.tableWidget.item(row, col).setBackground(table_row_color)

    self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section"
                                                      "{background-color:%s;}"
                                                      % (table_header_color.name()))


###Main UI###
def selectMainStyle(self, bg, font_family, font_size, tool_pos, tool_style,
                    table_grid, table_header_color, table_row_color, table_colored_row):
    c = Color()
    if bg == 'Black':
        c.setBlack()
        setMainStyle(self, c.color1, c.color2, c.color4,
                     font_family, font_size)
        setToolBarStyle(self, tool_pos, tool_style, c.color3)
        setTableStyle(self, table_grid, table_header_color,
                      table_row_color, table_colored_row)
        self.viewLabel.setStyleSheet("font: 10pt; color: white;")
    elif bg == 'White':
        c.setWhite()
        setMainStyle(self, c.color1, c.color2, c.color4,
                     font_family, font_size)
        setToolBarStyle(self, tool_pos, tool_style, c.color3)
        setTableStyle(self, table_grid, table_header_color,
                      table_row_color, table_colored_row)
    elif bg == 'Blue':
        c.setBlue()
        setMainStyle(self, c.color1, c.color2, c.color4,
                     font_family, font_size)
        setToolBarStyle(self, tool_pos, tool_style, c.color3)
        setTableStyle(self, table_grid, table_header_color,
                      table_row_color, table_colored_row)
    elif bg == 'Green':
        c.setGreen()
        setMainStyle(self, c.color1, c.color2, c.color4,
                     font_family, font_size)
        setToolBarStyle(self, tool_pos, tool_style, c.color3)
        setTableStyle(self, table_grid, table_header_color,
                      table_row_color, table_colored_row)

    # 스타일 시트를 변경합니다.


def setMainStyle(self, color1, color2, color4, font_family, font_size):
    self.widget.setStyleSheet(f"background-color: {color1.name()};"
                              f"font: " + font_size + "pt '" + font_family + "';")
    self.viewLabel.setStyleSheet("font: 10pt; color: black;")

    self.insertButton.setStyleSheet(f"background-color: {color4.name()};"
                                    f"color: white;")

    self.tabWidget.setStyleSheet("color: black")
    self.tab_1.setStyleSheet(f"""background-color: {color2.name()};
                                     border-color: {color2.name()}""")
    self.tab_2.setStyleSheet(f"""background-color: {color2.name()};
                                     border-color: {color2.name()}""")

    self.colInfoListWidget.setStyleSheet(f"background-color: white;"
                                         f"color: black;")
    self.cellList.setStyleSheet(f"background-color: white;"
                                f"color: black;")
    self.FileList.setStyleSheet(f"background-color: white;"
                                f"color: black;")
    self.tableWidget.setStyleSheet(f"background-color: white;"
                                   f"color: black;")

    # self.barGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    # self.lineGraphBtn.setStyleSheet(f"background-color: {color6.name()};")
    # self.pieChartBtn.setStyleSheet(f"background-color: {color6.name()};")
    # self.scatterChartBtn.setStyleSheet(f"background-color: {color6.name()};")

    # self.menuBar().setStyleSheet("""
    #                                 QMenuBar::item:pressed {background: rgb(90, 120, 215);}
    #                                 QMenu::item:selected {background: rgb(90, 120, 215);}
    #                                 QMenuBar {border: 1px solid;
    #                                             border-bottom-color: %s;
    #                                             border-top-color: transparent;
    #                                             border-left-color: transparent;
    #                                             border-right-color: transparent;
    #                                           }
    #                             """ % (color7.name()))

    self.secChartCombo.setStyleSheet("""
                                        QComboBox {background-color: white;"""
                                     """color: black;}
                              QComboBox::item {background: white; color: black}
                              QComboBox::item:selected {background: %s; color: white}
                              """ % (color4.name()))
    self.secSortCombo.setStyleSheet("""
                                    QComboBox {background-color: white;"""
                                    """ color: black;}
                                QComboBox::item {background: white; color: black}
                                QComboBox::item:selected {background: %s; color: white}
                                """ % (color4.name()))
    self.notshowBtn.setStyleSheet("background-color: white;")
    self.showBtn.setStyleSheet("background-color: white;")
    self.secColListLeftTitle.setStyleSheet(f"background-color: {color4.name()};"
                                           f"color: white;")
    self.secColListRightTitle.setStyleSheet(f"background-color: {color4.name()};"
                                            f"color: white;")
    self.showingColList.setStyleSheet("QListWidget {background-color: white; color: black;}")
    self.unshowingColList.setStyleSheet("QListWidget {background-color: white; color: black;}")


## 이 아래부턴 스타일시트변경에 들어갈 색을 만들고
## setMainColor()()를 실행시킵니다.
## 각각 필요한 다른 설정도 합니다.

def setMainBlack(self, font_family, font_size):
    c = Color()
    c.setBlack()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 QColor(255, 255, 255), font_family, font_size)

    # self.insertButton.setStyleSheet(f"background-color: {c.color3.name()};"
    #                                 f"color: {c.color5.name()};")
    # self.tableWidget.setStyleSheet(f"background-color: {c.color1.name()};")
    # self.tabWidget.setStyleSheet(f"color: {c.color1.name()};")


def setMainWhite(self, font_family, font_size):
    c = Color()
    c.setWhite()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 QColor(255, 255, 255), font_family, font_size)
    #
    # self.secChartCombo.setStyleSheet("""
    #                                  QComboBox {background-color: %s;"""
    #                                  """color: %s;}
    #                                  QComboBox::item {background: %s; color: %s}
    #                                  QComboBox::item:selected {background: %s; color: %s}
    #                                  """ % (c.color3.name(), c.color2.name(),
    #                                         c.color3.name(), c.color2.name(),
    #                                         c.color2.name(), c.color3.name()))
    # self.secSortCombo.setStyleSheet("""
    #                                 QComboBox {background-color: %s;"""
    #                                 """color: %s;}
    #                                 QComboBox::item {background: %s; color: %s}
    #                                 QComboBox::item:selected {background: %s; color: %s}
    #                                 """ % (c.color3.name(), c.color2.name(),
    #                                        c.color3.name(), c.color2.name(),
    #                                        c.color2.name(), c.color3.name()))
    # self.secColListLeftTitle.setStyleSheet(f"background-color: {c.color4.name()};"
    #                                        f"color: {c.color2.name()};")
    # self.secColListRightTitle.setStyleSheet(f"background-color: {c.color4.name()};"
    #                                         f"color: {c.color2.name()};")
    # self.notshowBtn.setStyleSheet(f"background-color: {c.color3.name()};"
    #                               f"color: {c.color2.name()}")
    # self.showBtn.setStyleSheet(f"background-color: {c.color3.name()};"
    #                            f"color: {c.color2.name()}")


def setMainBlue(self, font_family, font_size):
    c = Color()
    c.setBlue()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 QColor(255, 255, 255), font_family, font_size)
    # self.insertButton.setStyleSheet(f"background-color: {c.color4.name()};"
    #                                 f"color: {c.color1.name()};")


def setMainGreen(self, font_family, font_size):
    c = Color()
    c.setGreen()

    setMainStyle(self, c.color1, c.color2, c.color3, c.color4,
                 Qt.White, font_family, font_size)


def setProcess(self):
    self.treeWidget.setStyleSheet(
        "background-color: rgb(255, 255, 255);"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(240, 240, 240);")
    self.listView.setStyleSheet(
        "background-color: rgb(240, 240, 240);"
        "border-style: solid;"
        "border-color: rgb(240, 240, 240);")
    self.treeWidget_2.setStyleSheet(
        "background-color: rgb(255, 255, 255);"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(240, 240, 240);")

    self.label.setStyleSheet(
        "background-color: rgb(255, 255, 255);"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(240, 240, 240);")
