from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_ECGPatient import Ui_ECGPatient
from GUI.Logic.Noticfication import Notification
from BUS.BUS_ECGPatient import BUS_ECGPatient
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import wfdb
import matplotlib.pyplot as plt 
import os

class ECGPatient(QFrame, Ui_ECGPatient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busECGPatient = BUS_ECGPatient()

        self.PATH = "Patient/ECG/"
        self.type = ""
        self.linkECG = ""
        self.firstFile = ""

        self.figure = None
        self.canvas = None
        self.toolbar = None

        # Event Handle
        self.comboECGType.currentTextChanged.connect(self.changeECGType)

        self.firstLoad()


    def firstLoad(self):
        data = self.busECGPatient.firstLoadLinkECG(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboECGType.setCurrentText(data[0])
            if(self.comboECGType.currentText() == "Điện Tâm Đồ"):
                self.type = "ECG/"
            if(self.comboECGType.currentText() == "Điện Não Đồ"):
                self.type = "EEG/"
            if(data[1] != "" and data[1] is not None):
                self.linkECG = data[1]
                for file in os.listdir(self.PATH + self.type + data[1]):
                    if(self.comboECGType.currentText() == "Điện Tâm Đồ"):
                        self.cleanWidget()
                        if(file.split(".")[1] == "qrs"):
                            self.firstFile = file.split(".")[0]
                    else:
                        self.cleanWidget()
                        if(file.split(".")[1] == "trigger"):
                            self.firstFile = file.split(".")[0]
                print(self.PATH + self.type + self.linkECG + "/" + self.firstFile)
                try:
                    record = wfdb.rdrecord(record_name=self.PATH + self.type + self.linkECG + "/" + self.firstFile, sampfrom=0, sampto=6000)
                    title_name = "Bệnh Nhân: " + self.IDPatient
                    self.figure = wfdb.plot_wfdb(record=record, title=title_name, return_fig=True) 
                    self.canvas = FigureCanvas(self.figure) 
                    self.toolbar = NavigationToolbar(self.canvas, self) 
                    plt.axis([0, 480, -0.9, 1.8])

                    #FFF
                    if(self.type == "ECG/"):
                        self.mainFrame.setMaximumSize(9999, 250)
                    else:
                        self.mainFrame.setMaximumSize(9999, 9999)

                    self.mainLayout.addWidget(self.toolbar)
                    self.mainLayout.addWidget(self.canvas)
                    self.mainFrame.show()
                except:
                    self.noticfication = Notification(title="Cảnh báo", message="Có Lỗi!, Kiểm Tra Lại File!", icon_type=1)


            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu")

    def changeECGType(self):
        self.cleanWidget()
        if(self.comboECGType.currentText() == "Điện Tâm Đồ"):
            self.type = "ECG/"
        if(self.comboECGType.currentText() == "Điện Não Đồ"):
            self.type = "EEG/"
        
        self.linkECG = ""
        self.firstFile = ""

        data = self.busECGPatient.loadLinkECG(IDPatient=self.IDPatient, ECGType=self.comboECGType.currentText())
        if(data is not None and data[0] != ""):
            self.linkECG = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                if(self.comboECGType.currentText() == "Điện Tâm Đồ"):
                    if(file.split(".")[1] == "qrs"):
                        self.firstFile = file.split(".")[0]
                else:
                    if(file.split(".")[1] == "trigger"):
                        self.firstFile = file.split(".")[0]
            print(self.PATH + self.type + self.linkECG + "/" + self.firstFile)
            try:
                record = wfdb.rdrecord(record_name=self.PATH + self.type + self.linkECG + "/" + self.firstFile, sampfrom=0, sampto=6000)
                title_name = "Bệnh Nhân: " + self.IDPatient
                self.figure = wfdb.plot_wfdb(record=record, title=title_name, return_fig=True) 
                self.canvas = FigureCanvas(self.figure) 
                self.toolbar = NavigationToolbar(self.canvas, self) 
                plt.axis([0, 480, -0.9, 1.8])

                #FFF
                if(self.type == "ECG/"):
                    self.mainFrame.setMaximumSize(9999, 250)
                else:
                    self.mainFrame.setMaximumSize(9999, 9999)

                self.mainLayout.addWidget(self.toolbar)
                self.mainLayout.addWidget(self.canvas)
                self.mainFrame.show()
            except:
                self.noticfication = Notification(title="Cảnh báo", message="Có Lỗi!, Kiểm Tra Lại File!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def cleanWidget(self):
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()
