
from GUI.View.Ui_UltraSonic import Ui_UltraSonic
from GUI.Logic.Noticfication import Notification
from BUS.BUS_UltraSonic import BUS_UltraSonic
from PyQt5.QtWidgets import QFrame, QFileDialog
from PyQt5.QtGui import QImage
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
import os
import cv2
import shutil

class UltraSonic(QFrame, Ui_UltraSonic):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")
        self.busUltraSonic = BUS_UltraSonic()

        self.PATH = "Patient/UltraSonic/"
        self.type = ""
        self.linkUltraSonic = ""
        self.state = ""
               
        self.IDPatient = ""
        self.totalFile = 0
        self.imgList = {}
        self.searchBT = 2

        self.hSlider.setValue(1)
        # Event Handle
        self.comboTypeUltraSonic.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.hSlider.valueChanged.connect(self.loadUltraSonicImage)
        self.btUpload.clicked.connect(self.uploadUltraSonicImage)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def loadData(self):
        dataUltraSonic = self.busUltraSonic.loadDataWithType(UltraSonicType=self.comboTypeUltraSonic.currentText())
        self.showData(dataUltraSonic=dataUltraSonic)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataUltraSonic = self.busUltraSonic.loadAllData()
            self.showData(dataUltraSonic=dataUltraSonic)
            self.comboTypeUltraSonic.setEnabled(False)
        else:
            self.comboTypeUltraSonic.setEnabled(True)
            self.loadData()

    def cellClickOnDataTabPatient(self):
        self.totalFile = 0
        self.imgList.clear()
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("Bệnh Nhân: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "Tim"):
            self.type = "Heart/"
        if(itemType == "Thai Nhi"):
            self.type = "Fetus/"
        if(itemType == "Gan Mật"):
            self.type = "Liver_Gallbladder/"
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "Đã Có Kết Quả"):
            data = self.busUltraSonic.getLinkUltraSonic(IDPatient=self.IDPatient)
            self.linkUltraSonic = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalFile += 1
                self.imgList[self.totalFile] = file
            self.hSlider.setMaximum(self.totalFile)
            #print(self.PATH + self.type + self.linkUltraSonic + "/" +self.imgList[1])
            # First
            I = cv2.imread(self.PATH + self.type + self.linkUltraSonic + "/" +self.imgList[1])
            img = cv2.resize(I, (384, 384))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
            pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
            self.lbUltraSonicImg.setPixmap(QtGui.QPixmap(pixImg))
        else:
            self.lbUltraSonicImg.clear()

    def loadUltraSonicImage(self, value):
        if(self.totalFile > 0):
            if(value in self.imgList.keys()):
                I = cv2.imread(self.PATH + self.type + self.linkUltraSonic + "/" + self.imgList[value])
                img = cv2.resize(I, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
                pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
                self.lbUltraSonicImg.setPixmap(QtGui.QPixmap(pixImg))

    def uploadUltraSonicImage(self):
        if(self.IDPatient != ""):
            if(self.state == "Đã Có Kết Quả"): # update
                self.lbUltraSonicImg.clear()
                self.totalFile = 0
                self.imgList.clear()
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Ảnh UltraSonic"))
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
                folder = str(dialog.getExistingDirectory(self, "Chọn Thư Mục Chứa Ảnh UltraSonic"))
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
                    reuslt = self.busUltraSonic.uploadUltraSonic(IDPatient=self.IDPatient, UltraSonicType=self.comboTypeUltraSonic.currentText(), LinkUltraSonic=self.IDPatient)
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
            dataUltraSonic = self.busUltraSonic.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataUltraSonic != [] and dataUltraSonic is not None):
                self.showData(dataUltraSonic=dataUltraSonic)

            else:
                self.noticfication = Notification(title="Thông báo", message="Không tìm thấy bệnh nhân!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn phương thức tìm kiếm!", icon_type=1)

    def showData(self, dataUltraSonic):
        self.totalFile = 0
        self.imgList.clear()
        self.lbPatient.setText("")
        self.lbUltraSonicImg.clear()
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataUltraSonic):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Đã Có Kết Quả"))
                elif(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Chưa Có Kết Quả"))
        self.dataTabPatient.resizeColumnsToContents()

        # if(self.comboTypeUltraSonic.currentText() == "Tim"):
        #     self.type = "Heart/"
        # if(self.comboTypeUltraSonic.currentText() == "Thai Nhi"):
        #     self.type = "Fetus/"
        # if(self.comboTypeUltraSonic.currentText() == "Gan Mật"):
        #     self.type = "Liver_Gallbladder/"

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "Heart")):
            os.mkdir(self.PATH + "Heart")
        if not (os.path.isdir(self.PATH + "Fetus")):
            os.mkdir(self.PATH + "Fetus")
        if not (os.path.isdir(self.PATH + "Liver_Gallbladder")):
            os.mkdir(self.PATH + "Liver_Gallbladder")