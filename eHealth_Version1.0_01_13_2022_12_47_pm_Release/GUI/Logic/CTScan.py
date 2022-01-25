from GUI.View.Ui_CTScan import Ui_CTScan
from BUS.BUS_CTScan import BUS_CTScan
from GUI.Logic.Noticfication import Notification
from PyQt5.QtWidgets import QFrame, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import os
import cv2
import shutil

class CTScan(QFrame, Ui_CTScan):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")
        self.busCTScan = BUS_CTScan()

        self.PATH = "Patient/CTScan/"
        self.type = ""
        self.linkCTScan = ""
        self.state = ""
               
        self.IDPatient = ""
        self.totalFile = 0
        self.imgList = {}
        self.searchBT = 2

        self.hSlider.setValue(1)
        # Event Handle
        self.comboTypeCTScan.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.hSlider.valueChanged.connect(self.loadCTScanImage)
        self.btUpload.clicked.connect(self.uploadCTScanImage)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def loadData(self):
        dataCTScan = self.busCTScan.loadDataWithType(CTScanType=self.comboTypeCTScan.currentText())
        print(dataCTScan)
        self.showData(dataCTScan=dataCTScan)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataCTScan = self.busCTScan.loadAllData()
            self.showData(dataCTScan=dataCTScan)
            self.comboTypeCTScan.setEnabled(False)
        else:
            self.comboTypeCTScan.setEnabled(True)
            self.loadData()

    def cellClickOnDataTabPatient(self):
        self.totalFile = 0
        self.imgList.clear()
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("Bệnh Nhân: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "Sọ Não"):
            self.type = "Brain/"
        if(itemType == "Phổi"):
            self.type = "Lung/"
        if(itemType == "Xương"):
            self.type = "Bone/"
        if(itemType == "Ổ Bụng"):
            self.type = "Abdominal/"
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "Đã Có Kết Quả"):
            data = self.busCTScan.getLinkCTScan(IDPatient=self.IDPatient)
            self.linkCTScan = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalFile += 1
                self.imgList[self.totalFile] = file
            self.hSlider.setMaximum(self.totalFile)
            #print(self.PATH + self.type + self.linkCTScan + "/" +self.imgList[1])
            # First
            I = cv2.imread(self.PATH + self.type + self.linkCTScan + "/" + self.imgList[1])
            img = cv2.resize(I, (384, 384))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
            pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
            self.lbCTScanImg.setPixmap(QtGui.QPixmap(pixImg))
        else:
            self.lbCTScanImg.clear()

    def loadCTScanImage(self, value):
        if(self.totalFile > 0):
            if(value in self.imgList.keys()):
                I = cv2.imread(self.PATH + self.type + self.linkCTScan + "/" + self.imgList[value])
                img = cv2.resize(I, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
                pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
                self.lbCTScanImg.setPixmap(QtGui.QPixmap(pixImg))

    def uploadCTScanImage(self):
        if(self.IDPatient != ""):
            if(self.state == "Đã Có Kết Quả"): # update
                self.lbCTScanImg.clear()
                self.totalFile = 0
                self.imgList.clear()
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Ảnh CTScan"))
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
            else: # Upload
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Ảnh CTScan"))
                if(folder != "" and folder is not None):
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    try:
                        if not (os.path.isdir(linkDirectory)):
                            os.mkdir(linkDirectory)
                        for file in os.listdir(folder):
                            if not(os.path.isfile(linkDirectory + "/" + file)):
                                src = folder + "/" + file
                                shutil.copy(src=src, dst=linkDirectory)
                    except:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
                        return
                    reuslt = self.busCTScan.uploadCTScan(IDPatient=self.IDPatient, CTScanType=self.comboTypeCTScan.currentText(), LinkCTScan=self.IDPatient)
                    if(reuslt == 1):
                        self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                    else:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân!", icon_type=1)
        self.loadData()
    
    def selectIDPatient(self, selected):
        if selected:
            self.searchBT = 0

    def selectedFullName(self, selected):
        if selected:
            self.searchBT = 1

    def searchPatient(self):
        if(self.searchBT == 0 or self.searchBT == 1):
            dataCTScan = self.busCTScan.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataCTScan != [] and dataCTScan is not None):
                self.showData(dataCTScan=dataCTScan)

            else:
                self.noticfication = Notification(title="Thông báo", message="Không tìm thấy bệnh nhân!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn phương thức tìm kiếm!", icon_type=1)

    def showData(self, dataCTScan):
        self.totalFile = 0
        self.imgList.clear()
        self.lbCTScanImg.clear()
        self.lbPatient.setText("")
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataCTScan):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Đã Có Kết Quả"))
                elif(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Chưa Có Kết Quả"))
        self.dataTabPatient.resizeColumnsToContents()

        # if(self.comboTypeCTScan.currentText() == "Sọ Não"):
        #     self.type = "Brain/"
        # if(self.comboTypeCTScan.currentText() == "Phổi"):
        #     self.type = "Lung/"
        # if(self.comboTypeCTScan.currentText() == "Xương"):
        #     self.type = "Bone/"
        # if(self.comboTypeCTScan.currentText() == "Ổ Bụng"):
        #     self.type = "Abdominal/"

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "Brain")):
            os.mkdir(self.PATH + "Brain")
        if not (os.path.isdir(self.PATH + "Lung")):
            os.mkdir(self.PATH + "Lung")
        if not (os.path.isdir(self.PATH + "Bone")):
            os.mkdir(self.PATH + "Bone")
        if not (os.path.isdir(self.PATH + "Abdominal")):
            os.mkdir(self.PATH + "Abdominal")
 
