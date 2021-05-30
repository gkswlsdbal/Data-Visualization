
import data
import numpy as np

# 셀리스트의 셀제목을 클릭했을때 실행
def cellClick(self):
    resetGraphType(self)
    self.fig.clear()
    table = self.tableWidget
    row = table.rowCount()
    self.y = []
    self.x = []
    mod = False
    try:
        if data.graphType == 2:
            raise
        for i in range(0, row):
            aa = table.item(i, self.cellList.currentRow()).text()
            if aa == '':
                aa = 0
            try:
                self.y.append(int(aa))
            except:
                self.y.append(float(aa))
            self.x = np.arange(1, row + 1, 1)
    except:
        mod = True
        self.ele = []
        for i in range(0, row):
            aa = str(table.item(i, self.cellList.currentRow()).text())
            if aa in self.ele:
                self.y[self.ele.index(aa)] += 1
            else:
                self.ele.append(aa)
                self.y.append(1)
        self.x = np.arange(1, len(self.y) + 1, 1)
    self.ax = self.fig.add_subplot(111)
    if data.graphType == 0:
        self.barGraphBtn.toggle()
        self.bars = self.ax.bar(self.x, self.y)
        if mod:
            self.ax.set_xticks(self.x)
            self.ax.set_xticklabels(self.ele)
    elif data.graphType == 1:
        self.lineGraphBtn.toggle()
        self.line, = self.ax.plot(self.x, self.y)
        if mod:
            self.ax.set_xticks(self.x)
            self.ax.set_xticklabels(self.ele)
    elif data.graphType == 2:
        self.pieChartBtn.toggle()
        if mod:
            self.pies = self.ax.pie(self.y, labels=self.ele, autopct='%0.1f%%')
        else:
            self.pies = self.ax.pie(self.y, labels=self.y, autopct='%0.1f%%')
    elif data.graphType == 3:
        self.scatterChartBtn.toggle()
        self.ax.boxplot(self.y)
        # self.scat = self.ax.scatter(self.x, self.y)
        # if mod:
        #     self.ax.set_xticks(self.x)
        #     self.ax.set_xticklabels(self.ele)

    try:
        self.ax.set_title(self.cellList.currentItem().text())
        self.annot = self.ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                                      bbox=dict(boxstyle="round", fc="w"),
                                      arrowprops=dict(arrowstyle="->"))
        self.annot.set_visible(False)
        self.canvas.draw()
        data.graphOn = True
    except:
        pass

# 그래프 버튼 초기화
def resetGraphType(self):
    if self.barGraphBtn.isChecked():
        self.barGraphBtn.toggle()
    if self.lineGraphBtn.isChecked():
        self.lineGraphBtn.toggle()
    if self.pieChartBtn.isChecked():
        self.pieChartBtn.toggle()
    if self.scatterChartBtn.isChecked():
        self.scatterChartBtn.toggle()

# 그래프 위에서 마우스가 움직일때
def move_cursor(self, event):
    if not data.graphOn:
        return
    vis = self.annot.get_visible()
    if event.inaxes == self.ax:
        if data.graphType == 0:
            bar_move_cursor(self, event)
        elif data.graphType == 1:
            line_move_cursor(self, event)
        elif data.graphType == 2:
            #pie_move_cursor(self, event)
            pass
        elif data.graphType == 3:
            #scat_move_cursor(self, event)
            pass
        return
    if vis:
        self.annot.set_visible(False)
        self.canvas.draw()

# 막대그래프 주석 설정
def bar_move_cursor(self, event):
    for bar in self.bars:
        cont, ind = bar.contains(event)
        if cont:
            bar_update_annot(bar, self)
            self.annot.set_visible(True)
            self.canvas.draw()

# 막대그래프 주석 업데이트
def bar_update_annot(bar, self):
    x = bar.get_x() + bar.get_width() / 2.
    y = bar.get_y() + bar.get_height()
    self.annot.xy = (x, y)
    posy = self.y[int(x)-1]
    text = str(posy)
    self.annot.set_text(text)
    self.annot.get_bbox_patch().set_alpha(0.4)

# 꺽은선그래프 주석 설정
def line_move_cursor(self, event):
    cont, ind = self.line.contains(event)
    if cont and len(ind['ind']) == 1:
        line_update_annot(ind['ind'][0], self)
        self.annot.set_visible(True)
        self.canvas.draw()

# 꺽은선그래프의 주석 업데이트
def line_update_annot(ind, self):
    posx = ind
    posy = self.y[posx]
    self.annot.xy = (posx + 1, posy)
    text = str(posy)
    self.annot.set_text(text)
    self.annot.get_bbox_patch().set_alpha(0.4)

# 원그래프 주석 설정
def pie_move_cursor(self, event):
    for pie in self.pies[0]:
        cont, ind = pie.contains(event)
        if cont:
            pie_update_annot(pie, self)
            self.annot.set_visible(True)
            self.canvas.draw()

# 원그래프 주석 업데이트
def pie_update_annot(pie, self):
    ang1, ang2 = pie.theta1, pie.theta2
    r = pie.r
    x = ((r + 0.5) / 2) * np.cos(np.pi / 180 * ((ang1 + ang2) / 2))
    y = ((r + 0.5) / 2) * np.sin(np.pi / 180 * ((ang1 + ang2) / 2))
    self.annot.xy = (x, y)
    posy = self.y[int(x) - 1]
    text = str(posy)
    self.annot.set_text(text)
    self.annot.get_bbox_patch().set_alpha(0.4)

# 스카터그래프 주석 설정
def scat_move_cursor(self, event):
    cont, ind = self.scat.contains(event)
    if cont:
        line_update_annot(ind['ind'][0], self)
        self.annot.set_visible(True)
        self.canvas.draw()


# 막대 그래프 버튼
def barGraphBtnClick(self):
    resetGraphType(self)
    self.barGraphBtn.toggle()
    data.graphType = 0
    if data.graphOn:
        cellClick(self)

# 꺽은선 그래프 버튼
def lineGraphBtnClick(self):
    resetGraphType(self)
    self.lineGraphBtn.toggle()
    data.graphType = 1
    if data.graphOn:
        cellClick(self)


# 원 그래프 버튼
def pieChartBtnClick(self):
    resetGraphType(self)
    self.pieChartBtn.toggle()
    data.graphType = 2
    if data.graphOn:
        cellClick(self)


# 스케터 그래프 버튼
def scatterChartBtnClick(self):
    resetGraphType(self)
    self.scatterChartBtn.toggle()
    data.graphType = 3
    if data.graphOn:
        cellClick(self)
