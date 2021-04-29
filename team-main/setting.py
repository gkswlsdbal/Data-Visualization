from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import checkIniFile as ini


par = 0 #메인 창이 들어갑니다.

class SettingDialog(QDialog):

    def __init__(self, parent):
        global par
        par = parent

        super(SettingDialog, self).__init__(parent)
        setUI = 'Setting.ui'
        loadUi(setUI, self)

        ##변경
        import configparser
        config = configparser.ConfigParser()
        config.read('setting.ini')

        for i in range(1, 51):
            self.sizeCombo.addItem(str(i))
        self.sizeCombo.setStyleSheet("combobox-popup: 0; color: #000000; background-color: #ffffff;")
        self.sizeCombo.setMaxVisibleItems(5)
        self.sizeCombo.setCurrentText(config['STYLE']['font_size'])
        self.fontCombo.setCurrentFont(QFont(config['STYLE']['font_family']))
        self.bgcCombo.setCurrentText(config['STYLE']['theme'])
        self.optionTreeWid.setCurrentItem(self.optionTreeWid.topLevelItem(0))
        ini.chckIniDialog(self)
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
                     self.sizeCombo.currentText(), self.fontCombo.currentFont())

    #setting창을 종료할 때 메인 화면의 메뉴 중 Setting을 활성화 합니다.
    def closeEvent(self, event):
        par.actionSetting.setEnabled(True)
