from PyQt5.QtWidgets import QFrame, QFileDialog
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from GUI.View.Ui_Test import Ui_Test
from GUI.Logic.Noticfication import Notification
from BUS.BUS_Test import BUS_Test
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
import os
import cv2
import shutil
from pathlib import Path

class Test(QFrame, Ui_Test):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")
        
        self.busTest = BUS_Test()

        self.PATH = "Patient/Test/"
        self.type = ""
        self.linkTest = ""
        self.state = ""
               
        self.IDPatient = ""
        self.img = ""
        self.searchBT = 2

        self.sizeIMG = ()
        
        # Event Handle
        self.comboTypeTest.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.btUpload.clicked.connect(self.uploadTestImage)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def showData(self, dataTest):
        self.lbTestImg.clear()
        self.lbPatient.setText("")
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataTest):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Đã Có Kết Quả"))
                if(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Chưa Có Kết Quả"))
        self.dataTabPatient.resizeColumnsToContents()

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "Blood")):
            os.mkdir(self.PATH + "Blood")
        if not (os.path.isdir(self.PATH + "Urine")):
            os.mkdir(self.PATH + "Urine")
        if not (os.path.isdir(self.PATH + "Covid19")):
            os.mkdir(self.PATH + "Covid19")
        if not (os.path.isdir(self.PATH + "Biopsy")):
            os.mkdir(self.PATH + "Biopsy")
        if not (os.path.isdir(self.PATH + "CRP")):
            os.mkdir(self.PATH + "CRP")

    def loadData(self):
        self.lbPatient.setText("")
        self.lbTestImg.clear()
        dataTest = self.busTest.loadDataWithType(TestType=self.comboTypeTest.currentText())
        self.showData(dataTest=dataTest)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataTest = self.busTest.loadAllData()
            self.showData(dataTest=dataTest)
            self.comboTypeTest.setEnabled(False)
        else:
            self.comboTypeTest.setEnabled(True)
            self.loadData()

    def cellClickOnDataTabPatient(self):
        self.img = ""
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("Bệnh Nhân: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "Máu"):
            self.type = "Blood/"
            self.sizeIMG  = (564, 469)
        if(itemType == "Nước Tiểu"):
            self.type = "Urine/"
            self.sizeIMG  = (564, 469)
        if(itemType == "SARS - COV - 2"):
            self.type = "Covid19/"
            self.sizeIMG  = (803, 264)
        if(itemType == "Sinh Thiết"):
            self.type = "Biopsy/"
            self.sizeIMG  = (564, 469)
        if(itemType == "CRP"):
            self.type = "CRP/"
            self.sizeIMG  = (564, 469)
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "Đã Có Kết Quả"):
            data = self.busTest.getLinkTest(IDPatient=self.IDPatient)
            self.linkTest = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.img = file

            img = cv2.imread(self.PATH + self.type + self.linkTest + "/" + self.img)
            img = cv2.resize(img, self.sizeIMG)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.lbTestImg.setPixmap(QtGui.QPixmap.fromImage(img))

        else:
            self.lbTestImg.clear()

    def uploadTestImage(self):
        if(self.IDPatient != ""):
            if(self.state == "Đã Có Kết Quả"): #Update
                dialog = QFileDialog()
                image, _ = dialog.getOpenFileName(None, "Chọn Kết Quả Xét Nghiệm Của Bệnh Nhân", "","Image Files (*.jpg *.jpeg *png *gif);;All Files (*)")
                if(image != ""):
                    # img = cv2.imread(image)
                    # img = cv2.resize(img, (622, 800))
                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # h, w, ch = img.shape
                    # bytesPerLine = ch * w
                    # img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    # self.lbTestImg.setPixmap(QtGui.QPixmap.fromImage(img))
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
                image, _ = dialog.getOpenFileName(None, "Chọn Kết Quả Xét Nghiệm Của Bệnh Nhân", "","Image Files (*.jpg *.jpeg *png *gif);;All Files (*)")
                if(image != ""):
                    # print(image)
                    # img = cv2.imread(image)
                    # img = cv2.resize(img, (622, 800))
                    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # h, w, ch = img.shape
                    # bytesPerLine = ch * w
                    # img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                    # self.lbTestImg.setPixmap(QtGui.QPixmap.fromImage(img))
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
                    result = self.busTest.uploadTest(IDPatient=self.IDPatient, TestType=self.comboTypeTest.currentText(), LinkTest=self.IDPatient)
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
            dataTest = self.busTest.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataTest != [] and dataTest is not None):
                self.showData(dataTest=dataTest)
            else:
                self.noticfication = Notification(title="Thông báo", message="Không tìm thấy bệnh nhân!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Chưa chọn phương thức tìm kiếm!", icon_type=1)
