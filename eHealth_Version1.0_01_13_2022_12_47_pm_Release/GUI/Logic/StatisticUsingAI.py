from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_StatisticUsingAI import Ui_StatisticUsingAI
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import matplotlib.pyplot as plt 

class StatisticUsingAI(QFrame, Ui_StatisticUsingAI):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.figure = None
        self.canvas = None
        self.toolbar = None

        # Event Handle
        self.comboStatisticType.currentTextChanged.connect(self.plotData)

        self.plotData()

    def plotData(self):
        self.cleanWidget()
        self.figure = plt.figure() 
        self.canvas = FigureCanvas(self.figure) 
        self.toolbar = NavigationToolbar(self.canvas, self) 

        if(self.comboStatisticType.currentText() == "Tất Cả"):
            Y = ["MRI", "X-Quang"]
            data_dr = []
            with open("Config/MRIStatisticAI.cfg", "r+") as file:
                for data in file:
                    data_dr.append(int(data.strip()))
            with open("Config/XRayStatisticAI.cfg", "r+") as file:
                for data in file:
                    data_dr.append(int(data.strip()))
            ax = self.figure.add_subplot(111) 
            ax.axes.bar(Y, data_dr, width=0.8)
            #self.canvas.draw()
            self.mainLayout.addWidget(self.toolbar)
            self.mainLayout.addWidget(self.canvas)
            self.mainFrame.show()
        if(self.comboStatisticType.currentText() == "Chẩn Đoán Khối U Não"):
            Y = ["MRI"]
            data_dr = []
            with open("Config/MRIStatisticAI.cfg", "r+") as file:
                for data in file:
                    data_dr.append(int(data.strip()))
            ax = self.figure.add_subplot(111) 
            ax.axes.bar(Y, data_dr, width=0.8)
            #self.canvas.draw()
            self.mainLayout.addWidget(self.toolbar)
            self.mainLayout.addWidget(self.canvas)
            self.mainFrame.show()
        if(self.comboStatisticType.currentText() == "Chẩn Đoán Bất Thường Tim - Phổi"):
            Y = ["X-Quang"]
            data_dr = []
            with open("Config/XRayStatisticAI.cfg", "r+") as file:
                for data in file:
                    data_dr.append(int(data.strip()))
            ax = self.figure.add_subplot(111) 
            ax.axes.bar(Y, data_dr, width=0.8)
            #self.canvas.draw()
            self.mainLayout.addWidget(self.toolbar)
            self.mainLayout.addWidget(self.canvas)
            self.mainFrame.show()
        
    def cleanWidget(self):
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()  