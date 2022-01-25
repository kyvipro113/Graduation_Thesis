from datetime import time
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import QDate
from GUI.View.Ui_StatisticVisit import Ui_StatisticVisit
from GUI.Logic.Noticfication import Notification
from BUS.BUS_StatisticVisit import BUS_StatisticVisit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 
import datetime

class StatisticVisit(QFrame, Ui_StatisticVisit):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.time = QDate(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
        self.deStatistic.setDate(self.time)

        self.figure = None
        self.canvas = None
        self.toolbar = None

        self.busStatisticVisit = BUS_StatisticVisit()

        # Event handle
        self.deStatistic.dateChanged.connect(self.onChangeDate)
        self.comboTypeStatistic.currentTextChanged.connect(self.statisticVisit)

        self.load()

    def onChangeDate(self, QDate):
        self.time = QDate
        self.load()

    def statisticVisit(self):
        self.load()
        

    def load(self):
        timeStat = 0
        data = None
        dtype = ""
        if(self.comboTypeStatistic.currentText() == "Ngày"):
            timeStat = str(self.time.day())
            data = self.busStatisticVisit.loadVisitTimeViaDay(day=timeStat)
            dtype = self.comboTypeStatistic.currentText()
        if(self.comboTypeStatistic.currentText() == "Tháng"):
            timeStat = str(self.time.month())
            data = self.busStatisticVisit.loadVisitTimeViaMonth(month=timeStat)
            dtype = self.comboTypeStatistic.currentText()
        if(self.comboTypeStatistic.currentText() == "Năm"):
            timeStat = str(self.time.year())
            data = self.busStatisticVisit.loadVisitTimeViaYear(year=timeStat)
            dtype = self.comboTypeStatistic.currentText()
        if(data is not None):
            dtplot = [data[0]]
            self.plotData(data=dtplot, type=[dtype])
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu!", icon_type=1)


    def plotData(self, data=[], type=[""]):
        self.cleanWidget()
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 
        ax = self.figure.add_subplot(111) 
        ax.axes.bar(type, data, width=0.8)
        #self.canvas.draw()
        self.mainLayout.addWidget(self.toolbar)
        self.mainLayout.addWidget(self.canvas)
        self.mainFrame.show()

    def cleanWidget(self):
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()  