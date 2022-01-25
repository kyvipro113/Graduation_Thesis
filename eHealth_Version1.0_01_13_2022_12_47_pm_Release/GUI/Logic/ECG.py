import shutil
from PyQt5.QtWidgets import QFrame, QFileDialog
from PyQt5 import QtWidgets
from GUI.View.Ui_ECG import Ui_ECG
from GUI.Logic.Noticfication import Notification
from BUS.BUS_ECG import BUS_ECG
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas 
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar 
import wfdb
import matplotlib.pyplot as plt 
import os

class ECG(QFrame, Ui_ECG):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")
        self.busECG = BUS_ECG()

        self.PATH = "Patient/ECG/"
        self.type = ""
        self.linkECG = ""
        self.firstFile = ""
        self.state = ""

        self.figure = None
        self.canvas = None
        self.toolbar = None

        self.IDPatient = ""
        self.searchBT = 2

        # Event Handle
        self.comboTypeECG.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.btUpload.clicked.connect(self.uploadECG)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def loadData(self):
        dataECG = self.busECG.loadDataWithType(ECGType=self.comboTypeECG.currentText())
        print(dataECG)
        self.showData(dataECG=dataECG)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataECG = self.busECG.loadAllData()
            self.showData(dataECG=dataECG)
            self.comboTypeECG.setEnabled(False)
        else:
            self.comboTypeECG.setEnabled(True)
            self.loadData()

    def showData(self, dataECG):
        self.cleanWidget()
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataECG):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Đã Có Kết Quả"))
                elif(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Chưa Có Kết Quả"))
        self.dataTabPatient.resizeColumnsToContents()

        # if(self.comboTypeECG.currentText() == "Điện Tâm Đồ"):
        #     self.type = "ECG/"
        # if(self.comboTypeECG.currentText() == "Điện Não Đồ"):
        #     self.type = "EEG/"

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "ECG")):
            os.mkdir(self.PATH + "ECG")
        if not (os.path.isdir(self.PATH + "EEG")):
            os.mkdir(self.PATH + "EEG")

    def cellClickOnDataTabPatient(self):
        self.cleanWidget()
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("Bệnh Nhân: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "Điện Tâm Đồ"):
            self.type = "ECG/"
        if(itemType == "Điện Não Đồ"):
            self.type = "EEG/"
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "Đã Có Kết Quả"):
            data = self.busECG.getLinkECG(IDPatient=self.IDPatient)
            self.linkECG = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                if(itemType == "Điện Tâm Đồ"):
                    if(file.split(".")[1] == "qrs"):
                        self.firstFile = file.split(".")[0]
                else:
                    if(file.split(".")[1] == "trigger"):
                        self.firstFile = file.split(".")[0]
            print(self.PATH + self.type + self.linkECG + "/" + self.firstFile)
            try:
                record = wfdb.rdrecord(record_name=self.PATH + self.type + self.linkECG + "/" + self.firstFile, sampfrom=0, sampto=6000)
                title_name = self.lbPatient.text().split(":")[1]
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
            self.cleanWidget()
        
    def uploadECG(self):
        if(self.IDPatient != ""):
            if(self.state == "Đã Có Kết Quả"): # update
                self.cleanWidget()
                self.firstFile = ""
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Ảnh ECG"))
                if(folder != "" and folder is not None):
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    try:
                        for file in os.listdir(linkDirectory):
                            os.remove(linkDirectory + "/" + file)
                        for file in os.listdir(folder):
                            if not(os.path.isfile(linkDirectory + "/" + file)):
                                src = folder + "/" + file
                                shutil.copy(src=src, dst=linkDirectory)
                        self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                    except:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)

            else: # upload
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Dữ Liệu EG"))
                if(folder != "" and folder is not None):
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    try:
                        if not (os.path.isdir(linkDirectory)):
                            os.mkdir(linkDirectory)
                        for file in os.listdir(folder):
                            if not (os.path.isfile(linkDirectory + "/" + file)):
                                src = folder + "/" + file
                                shutil.copy(src=src, dst=linkDirectory)
                    except:
                        self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Bệnh Nhân!", icon_type=1)
                        return
                    result = self.busECG.uploadECG(IDPatient=self.IDPatient, ECGType=self.comboTypeECG.currentText(), LinkECG=self.IDPatient)
                    if(result == 1):
                        self.noticfication = Notification(title="Thông báo", message="Thao Tác Thực Hiện Thành Công!")
                    else:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao Tác Thực Hiện Thất Bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa Chọn Bệnh Nhân!", icon_type=1)
        self.loadData()

    def cleanWidget(self):
        while self.mainLayout.count():
            childFrame = self.mainLayout.takeAt(0)
            if childFrame.widget():
                childFrame.widget().deleteLater()

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataECG = self.busECG.loadAllData()
            self.showData(dataECG=dataECG)
            self.comboTypeECG.setEnabled(False)
        else:
            self.comboTypeECG.setEnabled(True)
            self.loadData()

    def searchPatient(self):
        if(self.searchBT == 0 or self.searchBT == 1):
            dataECG = self.busECG.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataECG != [] and dataECG is not None):
                self.showData(dataECG=dataECG)

            else:
                self.noticfication = Notification(title="Thông báo", message="Không tìm thấy bệnh nhân!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn phương thức tìm kiếm!", icon_type=1)

    def selectIDPatient(self, selected):
        if selected:
            self.searchBT = 0

    def selectedFullName(self, selected):
        if selected:
            self.searchBT = 1