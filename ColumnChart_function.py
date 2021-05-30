
import data
import numpy as np
import math

def secChartComboChanged(self):
    data.secCombo = self.secChartCombo.currentIndex()
    if data.secCombo == 0:
        self.secSortCombo.setEnabled(False)
    if data.secCombo == 1:
        self.secSortCombo.setEnabled(True)
    if data.secCombo == 2:
        self.secSortCombo.setEnabled(False)
    secGraphRefresh(self)

def secShowBtn(self):
    i = 0
    self.showingColList.clear()
    while 1:
        try:
            self.showingColList.addItem(self.cellList.item(i).text())
            i += 1
        except:
            self.unshowingColList.clear()
            break

    secGraphRefresh(self)

def secNotShowBtn(self):
    i = 0
    self.unshowingColList.clear()
    while 1:
        try:
            self.unshowingColList.addItem(self.cellList.item(i).text())
            i += 1
        except:
            self.showingColList.clear()
            break

    secGraphRefresh(self)

def secShowCellClick(self):
    tar = self.showingColList.currentRow()
    self.unshowingColList.addItem(self.showingColList.item(tar).text())
    self.showingColList.takeItem(tar)

    secGraphRefresh(self)

def secNotShowCellClick(self):
    tar = self.unshowingColList.currentRow()
    self.showingColList.addItem(self.unshowingColList.item(tar).text())
    self.unshowingColList.takeItem(tar)

    secGraphRefresh(self)

def secGraphRefresh(self):
    if data.secCombo == 0:
        secGraphColOnly(self)
    if data.secCombo == 1:
        secGraphColNMissingValue(self)
    if data.secCombo == 2:
        secGraphMissingValue(self)

def secGraphColOnly(self):
    self.fig_sec.clear()
    table = self.tableWidget
    row = table.rowCount()
    sec_count = 0
    while 1:
        check = self.showingColList.item(sec_count)
        sec_count += 1
        if check == None:
            sec_count -= 1
            break

    for j in range(0, sec_count):
        p = 0
        while 1:
            tartext = self.showingColList.item(j).text()
            if self.cellList.item(p).text() == tartext:
                break
            else:
                p += 1
        self.y_sec = []
        self.x_sec = []
        mod = False
        try:
            for i in range(0, row):
                aa_sec = table.item(i, p).text()
                if aa_sec == '':
                    aa_sec = 0
                try:
                    self.y_sec.append(int(aa_sec))
                except:
                    self.y_sec.append(float(aa_sec))
                self.x_sec = np.arange(1, row + 1, 1)
        except:
            self.y_sec = []
            self.x_sec = []
            mod = True
            self.ele_sec = []
            for i in range(0, row):
                aa_sec = str(table.item(i, p).text())
                if aa_sec in self.ele_sec:
                    self.y_sec[self.ele_sec.index(aa_sec)] += 1
                else:
                    self.ele_sec.append(aa_sec)
                    self.y_sec.append(1)
            self.x_sec = np.arange(1, len(self.y_sec) + 1, 1)
        yyy = math.ceil(sec_count / 2)
        xxx = 2
        if sec_count == 1:
            xxx = 1
        
        ##추가
        if yyy > 2:
            fig_sec_height = 8 + (yyy - 2) * 4
            self.fig_sec.set_size_inches(7.8, fig_sec_height)
            self.canvas_sec = FigureCanvas(self.fig_sec)
            self.scroll.setWidget(self.canvas_sec)
        else:
            self.fig_sec.set_size_inches(7.8, 8)
            self.canvas_sec = FigureCanvas(self.fig_sec)
            self.scroll.setWidget(self.canvas_sec)
        ##
        
        self.ax_sec = self.fig_sec.add_subplot(yyy, xxx, j+1)
        self.bars_sec = self.ax_sec.bar(self.x_sec, self.y_sec)
        if mod:
            self.ax_sec.set_xticks(self.x_sec)
            self.ax_sec.set_xticklabels(self.ele_sec, rotation=13)
        self.ax_sec.set_title(tartext)

    self.canvas_sec.draw()

def secGraphColNMissingValue(self):
    self.fig_sec.clear()
    table = self.tableWidget
    row = table.rowCount()
    sec_count = 0
    xxx = 2
    jjj = 0
    while 1:
        check = self.showingColList.item(sec_count)
        sec_count += 1
        if check == None:
            sec_count -= 1
            break
    yyy = math.ceil((sec_count + 1) / 2)
    for j in range(0, sec_count):
        p = 0
        while 1:
            tartext = self.showingColList.item(j).text()
            if self.cellList.item(p).text() == tartext:
                break
            else:
                p += 1
        self.y_sec = []
        self.x_sec = []
        mod = False
        try:
            for i in range(0, row):
                aa_sec = table.item(i, p).text()
                if aa_sec == '':
                    aa_sec = 0
                try:
                    self.y_sec.append(int(aa_sec))
                except:
                    self.y_sec.append(float(aa_sec))
                self.x_sec = np.arange(1, row + 1, 1)
        except:
            self.y_sec = []
            self.x_sec = []
            mod = True
            self.ele_sec = []
            for i in range(0, row):
                aa_sec = str(table.item(i, p).text())
                if aa_sec in self.ele_sec:
                    self.y_sec[self.ele_sec.index(aa_sec)] += 1
                else:
                    self.ele_sec.append(aa_sec)
                    self.y_sec.append(1)
            self.x_sec = np.arange(1, len(self.y_sec) + 1, 1)

        self.ax_sec = self.fig_sec.add_subplot(yyy, xxx, j + 1)
        self.bars_sec = self.ax_sec.bar(self.x_sec, self.y_sec)
        if mod:
            self.ax_sec.set_xticks(self.x_sec)
            self.ax_sec.set_xticklabels(self.ele_sec, rotation=13)
        self.ax_sec.set_title(tartext)
        jjj = j + 1

    while 1:
        check = self.showingColList.item(sec_count)
        sec_count += 1
        if check == None:
            sec_count -= 1
            break
    self.y_sec = []
    self.x_sec = []
    self.ele_sec = []
    for j in range(0, sec_count):
        p = 0
        tartext = ''
        while 1:
            tartext = self.showingColList.item(j).text()
            if self.cellList.item(p).text() == tartext:
                break
            else:
                p += 1
        self.ele_sec.append(tartext)  # 속성 새로 생성
        self.y_sec.append(0)  # y에 값 추가
        for i in range(0, row):
            #값 불러오기
            aa_sec = str(table.item(i, p).text())
            if aa_sec == '': #조건에 맞을 경우
                # y에 1추가
                self.y_sec[self.ele_sec.index(tartext)] += 1

    self.x_sec = np.arange(1, len(self.y_sec) + 1, 1)
    self.ax_sec = self.fig_sec.add_subplot(yyy, xxx, sec_count + 1)
    self.bars_sec = self.ax_sec.bar(self.x_sec, self.y_sec)
    self.ax_sec.set_xticks(self.x_sec)
    self.ax_sec.set_xticklabels(self.ele_sec, rotation=13)
    self.ax_sec.set_title('Missing Value')
    self.canvas_sec.draw()

def secGraphMissingValue(self):
    self.fig_sec.clear()
    table = self.tableWidget
    row = table.rowCount()
    sec_count = 0
    while 1:
        check = self.showingColList.item(sec_count)
        sec_count += 1
        if check == None:
            sec_count -= 1
            break
    self.y_sec = []
    self.x_sec = []
    self.ele_sec = []
    for j in range(0, sec_count):
        p = 0
        tartext = ''
        while 1:
            tartext = self.showingColList.item(j).text()
            if self.cellList.item(p).text() == tartext:
                break
            else:
                p += 1
        self.ele_sec.append(tartext)  # 속성 새로 생성
        self.y_sec.append(0)  # y에 값 추가
        for i in range(0, row):
            #값 불러오기
            aa_sec = str(table.item(i, p).text())
            if aa_sec == '': #조건에 맞을 경우
                # y에 1추가
                self.y_sec[self.ele_sec.index(tartext)] += 1

    self.x_sec = np.arange(1, len(self.y_sec) + 1, 1)
    self.ax_sec = self.fig_sec.add_subplot(111)
    self.bars_sec = self.ax_sec.bar(self.x_sec, self.y_sec)
    self.ax_sec.set_xticks(self.x_sec)
    self.ax_sec.set_xticklabels(self.ele_sec, rotation=13)
    self.ax_sec.set_title('Missing Value')

    self.canvas_sec.draw()
