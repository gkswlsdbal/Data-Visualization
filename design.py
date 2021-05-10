from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Color:
    def setWhite(self):
        self.bg_color = QColor(240, 240, 240)
        self.label_color = QColor(250, 250, 250)
        self.separate_color = QColor(200, 200, 200)

    def setBlue(self):
        self.bg_color = QColor(214, 230, 245)
        self.label_color = QColor(200, 230, 255)
        self.separate_color = QColor(170, 170, 238)

    def setGreen(self):
        # self.bg_color = QColor(232, 242, 232)
        self.bg_color = QColor(181, 214, 146)
        # self.bg_color = QColor(163, 204, 163)
        self.label_color = QColor(163, 204, 163)
        # self.label_color = QColor(178, 215, 178)
        # self.separate_color = QColor(180, 220, 168)
        self.separate_color = QColor(142, 174, 109)


def selectJoinColor(self, bg, font_family, font_size):
    c = Color()
    if bg == 'White':
        c.setWhite()
    elif bg == 'Blue':
        c.setBlue()
    elif bg == 'Green':
        c.setGreen()

    self.widget.setStyleSheet(f"background-color: {c.bg_color.name()};"
                              f"font: {font_size}pt '{font_family}';")
    self.JoinList.setStyleSheet(f"background-color: rgb(255, 255, 255);")
    self.JoinList2.setStyleSheet(f"background-color: rgb(255, 255, 255);")
    self.cellName.setStyleSheet(f"background-color: rgb(255, 255, 255);")
    self.cellName2.setStyleSheet(f"background-color: rgb(255, 255, 255);")


def setFAbsorColor(self, bg, font_family, font_size):
    c = Color()
    if bg == 'White':
        c.setWhite()
    elif bg == 'Blue':
        c.setBlue()
    elif bg == 'Green':
        c.setGreen()

    self.widget.setStyleSheet(f"background-color: {c.bg_color.name()};"
                              f"font: {font_size}pt '{font_family}';")
    self.FileList.setStyleSheet(f"background-color: white;")
    self.abList.setStyleSheet(f"background-color: white;")
    self.abList2.setStyleSheet(f"background-color: white;")
    self.bottomWidget.setStyleSheet(f"background-color: {c.bg_color.name()};"
                                    f"color: white;")
    self.buttonBox.setStyleSheet("background-color: white;")


def selectCAbsorColor(self, bg, font_family, font_size):
    c = Color()
    if bg == 'White':
        c.setWhite()
    elif bg == 'Blue':
        c.setBlue()
    elif bg == 'Green':
        c.setGreen()

    setCAbsorStyle(self, c.bg_color, c.label_color, font_family, font_size)


def setCAbsorStyle(self, bg_color, label_color, font_family, font_size):
    self.setStyleSheet(f"background-color: {bg_color.name()};"
                       f"font: {font_size}pt '{font_family}';")
    self.comboBox.setStyleSheet("""QComboBox {background-color: white;}
                                   QComboBox::item {background-color: white;}
                                   QComboBox::item:selected
                                   {background-color: %s; color: black;}"""
                                % (bg_color.name()))
    self.listWidget.setStyleSheet("background-color: white;"
                                  "color: black;")
    self.slctListWidget.setStyleSheet("background-color: white;"
                                      "color: black;")
    self.colLabel.setAlignment(Qt.AlignCenter)
    self.colLabel.setStyleSheet("border: 1px solid lightgray;"
                                f"background-color: {label_color.name()};")
    self.slctColLabel.setAlignment(Qt.AlignCenter)
    self.slctColLabel.setStyleSheet("border: 1px solid lightgray;"
                                    f"background-color: {label_color.name()};")
    self.topWidget.setStyleSheet(f"border: 1px solid {label_color.name};")
    self.buttonBox.setStyleSheet("background-color: white;")


###setting UI###
def selectSettStyle(self, bg, font_family, font_size):
    c = Color()
    if bg == 'White':
        c.setWhite()
    elif bg == 'Blue':
        c.setBlue()
    elif bg == 'Green':
        c.setGreen()

    setSettStyle(self, c.bg_color, c.separate_color, font_size)
    self.fontCombo.setCurrentFont(QFont(font_family))
    self.sizeCombo.setCurrentText(font_size)


# 1: 배경, 2: 폰트색, 3: 확인취소버튼 분리줄 색
def setSettStyle(self, bg_color, separate_color, font_size):
    import configparser
    config = configparser.ConfigParser()
    config.read('setting.ini')

    self.setStyleSheet(f"font: {font_size}pt;"
                       f"color: black;")

    self.optionTreeWid.setStyleSheet("""QTreeWidget {
                                            background-color: white;
                                            border: 0px;
                                            color: black;
                                            }
                                        QTreeWidget::item:selected {
                                            background-color: %s;
                                            color: black; }
                                     """ % (bg_color.name()))
    self.topWidget.setStyleSheet(f"background-color: {bg_color.name()};"
                                 f"border: 2px solid {separate_color.name()};"
                                 "border-top-color: transparent;"
                                 "border-left-color: transparent;"
                                 "border-right-color: transparent;")
    self.bgcCombo.setStyleSheet("""QComboBox {
                                        background-color: white;
                                        color: black;}
                                """)
    self.fontCombo.setStyleSheet("""QComboBox {
                                        background-color: white;
                                        color: black;}
                                 """)
    self.sizeCombo.setStyleSheet("""QComboBox {
                                        combobox-popup: 0;
                                        background-color: white;
                                        color: black;}
                                 """)
    self.toolPosGroup.setStyleSheet(f"border: 2px solid white;")
    self.toolStyGroup.setStyleSheet(f"border: 2px solid white;")
    self.bottomWidget.setStyleSheet(f"background-color: {bg_color.name()};")
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
    self.buttonBox.setStyleSheet("background-color: white;")


###Main UI###
def selectMainStyle(self, bg, font_family, font_size, tool_pos, tool_style,
                    table_grid, table_header_color, table_row_color, table_colored_row):
    c = Color()
    if bg == 'White':
        c.setWhite()
    elif bg == 'Blue':
        c.setBlue()
    elif bg == 'Green':
        c.setGreen()

    setMainStyle(self, c.bg_color, c.label_color,
                 font_family, font_size)
    setToolBarStyle(self, tool_pos, tool_style, c.separate_color)
    setTableStyle(self, table_grid, table_header_color,
                  table_row_color, table_colored_row)

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


def setMainStyle(self, bg_color, label_color, font_family, font_size):
    self.widget.setStyleSheet(f"background-color: {bg_color.name()};"
                              f"color: black;"
                              f"font: {font_size}pt {font_family};")
    self.viewLabel.setStyleSheet("font: 10pt; color: black;")

    self.insertButton.setStyleSheet(f"background-color: {label_color.name()};")

    self.tab_1.setStyleSheet(f"""background-color: {bg_color.name()};
                                     border-color: {bg_color.name()}""")
    self.tab_2.setStyleSheet(f"""background-color: {bg_color.name()};
                                     border-color: {bg_color.name()}""")

    self.colInfoListWidget.setStyleSheet(f"background-color: white;")
    self.cellList.setStyleSheet(f"background-color: white;")
    self.FileList.setStyleSheet(f"background-color: white;")
    self.tableWidget.setStyleSheet(f"background-color: white;")

    self.secChartCombo.setStyleSheet("""
                                        QComboBox {background-color: white;}
                                        QComboBox::item {background: white;}
                                      QComboBox::item:selected {background: %s;}
                                     """ % (bg_color.name()))
    self.notshowBtn.setStyleSheet("background-color: white;")
    self.showBtn.setStyleSheet("background-color: white;")
    self.secColListLeftTitle.setStyleSheet(f"background-color: {label_color.name()};")
    self.secColListLeftTitle.setAlignment(Qt.AlignCenter)
    self.secColListRightTitle.setAlignment(Qt.AlignCenter)
    self.secColListRightTitle.setStyleSheet(f"background-color: {label_color.name()};")
    self.showingColList.setStyleSheet("QListWidget {background-color: white;}")
    self.unshowingColList.setStyleSheet("QListWidget {background-color: white;}")


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
        "border-color: rgb(240, 240, 240);"
        "selection-background-color:rgb(255, 255, 255);")

    self.label.setStyleSheet(
        "background-color: rgb(255, 255, 255);"
        "border-style: solid;"
        "border-width: 2px;"
        "border-color: rgb(240, 240, 240);")
