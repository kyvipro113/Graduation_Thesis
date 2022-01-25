from GUI.View.Ui_XRay import Ui_XRay
from PyQt5.QtWidgets import QFrame
from GUI.Logic.Noticfication import *
from BUS.BUS_XRay import BUS_XRay
import os
import cv2
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import shutil
from pathlib import Path

class XRay(QFrame, Ui_XRay):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")
        
        self.busXRay = BUS_XRay()

        self.PATH = "Patient/XRay/"
        self.type = ""
        self.linkXRay = ""
        self.state = ""
               
        self.IDPatient = ""
        self.img = ""
        self.searchBT = 2

        # Event Handle
        self.comboTypeXray.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.btUpload.clicked.connect(self.uploadXRayImage)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def showData(self, dataXRay):
        self.lbXrayImg.clear()
        self.lbPatient.setText("")
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataXRay):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Đã Có Kết Quả"))
                if(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Chưa Có Kết Quả"))
        self.dataTabPatient.resizeColumnsToContents()
        
        # if(self.comboTypeXray.currentText() == "Phổi"):
        #     self.type = "Chest/"
        # if(self.comboTypeXray.currentText() == "Cột Sống"):
        #     self.type = "Spine/"
        # if(self.comboTypeXray.currentText() == "Xương"):
        #     self.type = "Bone/"
        # if(self.comboTypeXray.currentText() == "Tuyến Vú"):
        #     self.type = "Breast/"

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "Chest")):
            os.mkdir(self.PATH + "Chest")
        if not (os.path.isdir(self.PATH + "Spine")):
            os.mkdir(self.PATH + "Spine")
        if not (os.path.isdir(self.PATH + "Bone")):
            os.mkdir(self.PATH + "Bone")
        if not (os.path.isdir(self.PATH + "Breast")):
            os.mkdir(self.PATH + "Breast")


    def loadData(self):
        self.lbPatient.setText("")
        self.lbXrayImg.clear()
        dataXRay = self.busXRay.loadDataWithType(XRayType=self.comboTypeXray.currentText())
        self.showData(dataXRay=dataXRay)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataXRay = self.busXRay.loadAllData()
            self.showData(dataXRay=dataXRay)
            self.comboTypeXray.setEnabled(False)
        else:
            self.comboTypeXray.setEnabled(True)
            self.loadData()

    def cellClickOnDataTabPatient(self):
        self.img = ""
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("Bệnh Nhân: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "Phổi"):
            self.type = "Chest/"
        if(itemType == "Cột Sống"):
            self.type = "Spine/"
        if(itemType == "Xương"):
            self.type = "Bone/"
        if(itemType == "Tuyến Vú"):
            self.type = "Breast/"
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "Đã Có Kết Quả"):
            data = self.busXRay.getLinkXRay(IDPatient=self.IDPatient)
            self.linkXRay = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.img = file

            img = cv2.imread(self.PATH + self.type + self.linkXRay + "/" + self.img)
            img = cv2.resize(img, (622, 800))
            h, w, ch = img.shape
            bytesPerLine = ch * w
            img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.lbXrayImg.setPixmap(QtGui.QPixmap.fromImage(img))

        else:
            self.lbXrayImg.clear()

    def uploadXRayImage(self):
        if(self.IDPatient != ""):
            if(self.state == "Đã Có Kết Quả"): #Update
                dialog = QFileDialog()
                image, _ = dialog.getOpenFileName(None, "Chọn Ảnh X-Quang Của Bệnh Nhân", "","Image Files (*.jpg *.jpeg *png *gif);;All Files (*)")
                if(image != ""):
                    # img = cv2.imread(image)
                    # img = cv2.resize(img, (622, 800))
                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # h, w, ch = img.shape
                    # bytesPerLine = ch * w
                    # img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    # self.lbXrayImg.setPixmap(QtGui.QPixmap.fromImage(img))
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    fileName = Path(image).resolve().stem   #Get file name
                    fileTail =os.path.splitext(image)[1] #Get extension file tail
                    self.img = fileName + fileTail
                    try:
                        for file in os.listdir(linkDirectory):
                            os.remove(linkDirectory + "/" + file)
                        if not (os.path.isfile(linkDirectory + "/" + self.img)):
                            shutil.copy(src=image, dst=linkDirectory)
                    except:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
            else: #Upload
                dialog = QFileDialog()
                image, _ = dialog.getOpenFileName(None, "Chọn Ảnh X-Quang Của Bệnh Nhân", "","Image Files (*.jpg *.jpeg *png *gif);;All Files (*)")
                if(image != ""):
                    # print(image)
                    # img = cv2.imread(image)
                    # img = cv2.resize(img, (622, 800))
                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # h, w, ch = img.shape
                    # bytesPerLine = ch * w
                    # img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    # self.lbXrayImg.setPixmap(QtGui.QPixmap.fromImage(img))
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    fileName = Path(image).resolve().stem   #Get file name
                    fileTail =os.path.splitext(image)[1] #Get extension file tail
                    self.img = fileName + fileTail
                    try:
                        if not (os.path.isdir(linkDirectory)):
                            os.mkdir(linkDirectory)
                        if not (os.path.isfile(linkDirectory + "/" + self.img)):
                            shutil.copy(src=image, dst=linkDirectory)
                    except:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
                        return
                    result = self.busXRay.uploadXRay(IDPatient=self.IDPatient, XRayType=self.comboTypeXray.currentText(), LinkXRay=self.IDPatient)
                    if(result == 1):
                        self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
                    else:
                        self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn bệnh nhân", icon_type=1)
        self.loadData()

    def selectIDPatient(self, selected):
        if selected:
            self.searchBT = 0

    def selectedFullName(self, selected):
        if selected:
            self.searchBT = 1

    def searchPatient(self):
        if(self.searchBT == 0 or self.searchBT == 1):
            dataXray = self.busXRay.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataXray != [] and dataXray is not None):
                self.showData(dataXRay=dataXray)
            else:
                self.noticfication = Notification(title="Thông báo", message="Không tìm thấy bệnh nhân!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn phương thức tìm kiếm!", icon_type=1)
