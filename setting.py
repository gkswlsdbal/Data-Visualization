from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtCore import *
import sys
import design as ds

par = 0 #메인 창이 들어갑니다.
bgTheme = 0 # 처음 창이 생성됐을 때 배경콤보박스의 currentIndex입니다.

class SettingDialog(QDialog):

    def __init__(self, parent):
        global par
        global bgTheme
        par = parent

        super(SettingDialog, self).__init__(parent)
        setUI = 'Setting.ui'
        loadUi(setUI, self)
        bgTheme = self.bgcCombo.currentIndex()

        self.buttonBox.accepted.connect(self.acceptChg)
        #self.buttonBox.rejected.connect(self.rejectChg)
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.applyChg)
        self.setWindowFlags(Qt.Tool)
        self.show()

    ### 창을 나갔을 때 이벤트들입니다.
    ### 메인 화면의 Setting메뉴를 반드시 활성화합니다.

    # 확인 버튼을 눌렀을 경우입니다.
    # 변경된 부분을 적용하고 창을 종료합니다.
    def acceptChg(self):
        self.applyChg()
        self.close()

    # 취소 버튼을 눌렀을 경우입니다.
    def rejectChg(self):
        if self.bgc.currentIndex() != bgTheme:
            pass
        self.close()

    # 적용 버튼을 눌렀을 경우입니다.
    def applyChg(self):
        # global parent
        global bgTheme
        if self.bgcCombo.currentIndex() != bgTheme:
            bgTheme = self.bgcCombo.currentIndex()
            ds.setColorOpt(par, self.bgcCombo.currentIndex())


    #setting창을 종료할 때 메인 화면의 메뉴 중 Setting을 활성화 합니다.
    def closeEvent(self, event):
        par.actionSetting.setEnabled(True)
