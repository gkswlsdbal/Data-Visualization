from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import checkIniFile as ini

par = 0  # 메인 창이 들어갑니다.
toolStyle = 0  # 툴바 메뉴버튼 스타일 입니다.
toolPosition = 0  # 툴바 위치입니다.
tableGrid = 0  # 테이블 선 여부입니다.
coloredRow = 0  # 색이 입혀지는 행입니다.
headColor = 0  # 테이블 헤더 색입니다.
rowColor = 0  # 테이블 열 색입니다.

class SettingDialog(QDialog):

    def __init__(self, parent):

        global par
        par = parent

        super(SettingDialog, self).__init__(parent)
        setUI = 'Setting.ui'
        loadUi(setUI, self)

        import configparser
        config = configparser.ConfigParser()
        config.read('setting.ini')

        # style화면
        self.bgcLabel = QLabel('Color Theme:')
        self.bgcCombo = QComboBox()
        self.bgcCombo.addItem('White')
        self.bgcCombo.addItem('Blue')
        self.bgcCombo.addItem('Green')
        self.bgcCombo.setCurrentText(config['STYLE']['theme'])

        self.sizeLabel = QLabel('Size:')
        self.sizeCombo = QComboBox()
        for i in range(1, 51):
            self.sizeCombo.addItem(str(i))
        self.sizeCombo.setCurrentText(config['STYLE']['font_size'])
        self.sizeCombo.setStyleSheet("combobox-popup: 0;")
        self.sizeCombo.setMaxVisibleItems(5)

        self.fontLabel = QLabel('Font')
        self.fontCombo = QFontComboBox()
        self.fontCombo.setCurrentFont(QFont(config['STYLE']['font_family']))

        colorLay = QBoxLayout(QBoxLayout.LeftToRight)
        colorLay.addWidget(self.bgcLabel)
        colorLay.addWidget(self.bgcCombo)

        fontLay = QBoxLayout(QBoxLayout.LeftToRight)
        fontLay.addWidget(self.fontLabel)
        fontLay.addWidget(self.fontCombo)
        fontLay.addWidget(self.sizeLabel)
        fontLay.addWidget(self.sizeCombo)

        styleLay = QBoxLayout(QBoxLayout.TopToBottom)
        styleLay.addLayout(colorLay)
        styleLay.addLayout(fontLay)
        self.styleWid = QWidget()
        self.styleWid.setLayout(styleLay)

        # table 화면
        self.gridChkBox = QCheckBox('Grid')
        self.gridChkBox.clicked.connect(self.gridChg)

        if config['STYLE']['table_grid'] == 'true':
            self.gridChkBox.setChecked(True)
        global tableGrid
        tableGrid = config['STYLE']['table_grid']

        self.evenRow = QRadioButton('Even row color')
        self.evenRow.clicked.connect(self.slctRowChg)
        self.oddRow = QRadioButton('Odd row color')
        self.oddRow.clicked.connect(self.slctRowChg)
        self.allRow = QRadioButton('All row color')
        self.allRow.clicked.connect(self.slctRowChg)

        if config['STYLE']['table_colored_row'] == 'all':
            self.allRow.setChecked(True)
        elif config['STYLE']['table_colored_row'] == 'odd':
            self.oddRow.setChecked(True)
        elif config['STYLE']['table_colored_row'] == 'even':
            self.evenRow.setChecked(True)
        global coloredRow
        coloredRow = config['STYLE']['table_colored_row']

        self.hClrLabel = QLabel('Header color')
        self.rClrLabel = QLabel('Row color')
        self.hColorBtn = QPushButton('color')
        self.hColorBtn.clicked.connect(lambda: self.getColor(self.hColorBtn, 'h'))
        self.rColorBtn = QPushButton('color')
        self.rColorBtn.clicked.connect(lambda: self.getColor(self.rColorBtn, 'r'))

        self.hColorBtn.setStyleSheet('background-color:'
                                     f'{QColor(config["STYLE"]["table_header_color"]).name()};')
        self.rColorBtn.setStyleSheet('background-color:'
                                     f'{QColor(config["STYLE"]["table_row_color"]).name()};')
        global headColor
        global rowColor
        headColor = config["STYLE"]["table_header_color"]
        rowColor = config["STYLE"]["table_row_color"]

        gridLay = QBoxLayout(QBoxLayout.LeftToRight)
        gridLay.addWidget(self.gridChkBox)

        hClrLay = QBoxLayout(QBoxLayout.LeftToRight)
        hClrLay.addWidget(self.hClrLabel)
        hClrLay.addWidget(self.hColorBtn)

        rClrLay = QBoxLayout(QBoxLayout.LeftToRight)
        rClrLay.addWidget(self.rClrLabel)
        rClrLay.addWidget(self.rColorBtn)

        slctRowLay = QBoxLayout(QBoxLayout.LeftToRight)
        slctRowLay.addWidget(self.evenRow)
        slctRowLay.addWidget(self.oddRow)
        slctRowLay.addWidget(self.allRow)

        tableLay = QBoxLayout(QBoxLayout.TopToBottom)
        tableLay.addLayout(gridLay)
        tableLay.addLayout(hClrLay)
        tableLay.addLayout(rClrLay)
        tableLay.addLayout(slctRowLay)
        self.tableWid = QWidget()
        self.tableWid.setLayout(tableLay)

        # toolbar 화면
        self.toolPosGroup = QGroupBox('Toolbar Position')
        self.toolPosUp = QRadioButton('Up')
        self.toolPosUp.clicked.connect(self.toolPosChg)
        self.toolPosLeft = QRadioButton('Left')
        self.toolPosLeft.clicked.connect(self.toolPosChg)
        self.toolPosRight = QRadioButton('Right')
        self.toolPosRight.clicked.connect(self.toolPosChg)
        self.toolPosBottom = QRadioButton('Down')
        self.toolPosBottom.clicked.connect(self.toolPosChg)

        if config['STYLE']['tool_pos'] == '1':
            self.toolPosLeft.setChecked(True)
        elif config['STYLE']['tool_pos'] == '2':
            self.toolPosRight.setChecked(True)
        elif config['STYLE']['tool_pos'] == '4':
            self.toolPosUp.setChecked(True)
        elif config['STYLE']['tool_pos'] == '8':
            self.toolPosBottom.setChecked(True)
        global toolPosition
        toolPosition = config['STYLE']['tool_pos']

        self.toolStyGroup = QGroupBox('Toolbar Style')
        self.toolIcon = QRadioButton('Icon')
        self.toolIcon.clicked.connect(self.toolStyleChg)
        self.toolText = QRadioButton('Text')
        self.toolText.clicked.connect(self.toolStyleChg)
        self.toolTextBesideIcon = QRadioButton('Text beside Icon')
        self.toolTextBesideIcon.clicked.connect(self.toolStyleChg)
        self.toolTextUnderIcon = QRadioButton('Text under Icon')
        self.toolTextUnderIcon.clicked.connect(self.toolStyleChg)

        if config['STYLE']['tool_style'] == 'icon':
            self.toolIcon.setChecked(True)
        elif config['STYLE']['tool_style'] == 'text':
            self.toolText.setChecked(True)
        elif config['STYLE']['tool_style'] == 'textBesideIcon':
            self.toolTextBesideIcon.setChecked(True)
        elif config['STYLE']['tool_style'] == 'textUnderIcon':
            self.toolTextUnderIcon.setChecked(True)
        global toolStyle
        toolStyle = config['STYLE']['tool_style']

        toolStyLay = QBoxLayout(QBoxLayout.LeftToRight)
        self.toolPosGroup.setLayout(toolStyLay)
        toolStyLay.addWidget(self.toolIcon)
        toolStyLay.addWidget(self.toolText)
        toolStyLay.addWidget(self.toolTextBesideIcon)
        toolStyLay.addWidget(self.toolTextUnderIcon)

        toolPosLay = QBoxLayout(QBoxLayout.LeftToRight)
        self.toolStyGroup.setLayout(toolPosLay)
        toolPosLay.addWidget(self.toolPosUp)
        toolPosLay.addWidget(self.toolPosRight)
        toolPosLay.addWidget(self.toolPosLeft)
        toolPosLay.addWidget(self.toolPosBottom)

        toolLay = QBoxLayout(QBoxLayout.TopToBottom)
        toolLay.addWidget(self.toolPosGroup)
        toolLay.addWidget(self.toolStyGroup)
        self.toolWid = QWidget()
        self.toolWid.setLayout(toolLay)

        # stackedWidget에 추가
        self.stackWidget.insertWidget(0, self.styleWid)
        self.stackWidget.insertWidget(1, self.tableWid)
        self.stackWidget.insertWidget(2, self.toolWid)
        self.stackWidget.setCurrentIndex(0)

        self.optionListWid.setCurrentItem(self.optionListWid.setCurrentRow(0))
        self.optionListWid.setStyleSheet("border: 0px;")
        self.optionListWid.clicked.connect(self.display)
        ini.chckIniSett(self)
        ##

        self.buttonBox.accepted.connect(self.acceptChg)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.applyChg)
        self.setWindowFlags(Qt.Tool)
        self.show()

    ### 창을 나갈땐 메인 화면의 Setting메뉴를 반드시 활성화합니다.
    # 확인 버튼을 눌렀을 경우입니다.
    # 변경된 부분을 적용하고 창을 종료합니다.
    def acceptChg(self):
        self.applyChg()
        self.close()

    # 적용 버튼을 눌렀을 경우입니다.
    def applyChg(self):
        ini.writeIni(self, par, self.bgcCombo.currentText(),
                     self.sizeCombo.currentText(), self.fontCombo.currentFont(),
                     toolPosition, toolStyle, tableGrid, headColor, rowColor, coloredRow)

    # setting창을 종료할 때 메인 화면의 메뉴 중 Setting을 활성화 합니다.
    def closeEvent(self, event):
        par.settAction.setEnabled(True)

    def display(self, item):
        self.stackWidget.setCurrentIndex(item.row())

    def toolStyleChg(self):
        global toolStyle
        if self.toolIcon.isChecked():
            toolStyle = 'icon'
        elif self.toolText.isChecked():
            toolStyle = 'text'
        elif self.toolTextBesideIcon.isChecked():
            toolStyle = 'textBesideIcon'
        elif self.toolTextUnderIcon.isChecked():
            toolStyle = 'textUnderIcon'


    def toolPosChg(self):
        global toolPosition
        if self.toolPosLeft.isChecked():
            toolPosition = '1'
        elif self.toolPosRight.isChecked():
            toolPosition = '2'
        elif self.toolPosUp.isChecked():
            toolPosition = '4'
        elif self.toolPosBottom.isChecked():
            toolPosition = '8'


    def gridChg(self):
        global tableGrid
        if self.gridChkBox.isChecked():
            tableGrid = 'true'
        else:
            tableGrid = 'false'

    def slctRowChg(self):
        global coloredRow
        if self.evenRow.isChecked():
            coloredRow = 'even'
        elif self.oddRow.isChecked():
            coloredRow = 'odd'
        elif self.allRow.isChecked():
            coloredRow = 'all'

    def getColor(self, btn, hr):
        color = QColorDialog.getColor()
        btn.setStyleSheet(f'background-color: {color.name()}')
        if hr == 'h':
            global headColor
            headColor = color.name()
        else:
            global rowColor
            rowColor = color.name()
