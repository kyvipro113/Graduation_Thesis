from PyQt5.QtWidgets import QFileDialog, QFrame
from PyQt5 import QtWidgets
from GUI.View.Ui_MRI import Ui_MRI
from GUI.Logic.Noticfication import *
from BUS.BUS_MRI import BUS_MRI
import os
import cv2
from PyQt5.QtGui import QImage
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import shutil

class MRI(QFrame, Ui_MRI):
    def __init__(self, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.lbPatient.setText("")

        self.busMRI = BUS_MRI()

        self.PATH = "Patient/MRI/"
        self.type = ""
        self.linkMRI = ""
        self.state = ""
               
        self.IDPatient = ""
        self.totalFile = 0
        self.imgList = {}
        self.searchBT = 2

        self.hSlider.setValue(1)
        # Event Handle
        self.comboTypeMRI.currentTextChanged.connect(self.loadData)
        self.checkAllPatient.stateChanged.connect(self.loadAllData)
        self.dataTabPatient.cellClicked.connect(self.cellClickOnDataTabPatient)
        self.hSlider.valueChanged.connect(self.loadMRIImage)
        self.btUpload.clicked.connect(self.uploadMRIImage)
        self.radioBTIDPatient.toggled.connect(self.selectIDPatient)
        self.radioBTFullName.toggled.connect(self.selectedFullName)
        self.btSearch.clicked.connect(self.searchPatient)

        self.createDirectory()
        self.loadData()

    def loadData(self):
        dataMRI = self.busMRI.loadDataWithType(MRIType=self.comboTypeMRI.currentText())
        self.showData(dataMRI=dataMRI)

    def loadAllData(self):
        if(self.checkAllPatient.isChecked()):
            dataMRI = self.busMRI.loadAllData()
            self.showData(dataMRI=dataMRI)
            self.comboTypeMRI.setEnabled(False)
        else:
            self.comboTypeMRI.setEnabled(True)
            self.loadData()

    def cellClickOnDataTabPatient(self):
        self.totalFile = 0
        self.imgList.clear()
        row = self.dataTabPatient.currentRow()
        self.IDPatient = self.dataTabPatient.item(row, 0).text()
        FullName = self.dataTabPatient.item(row, 1).text()
        self.lbPatient.setText("B???nh Nh??n: " + self.IDPatient + " - " + FullName)
        itemType = self.dataTabPatient.item(row, 2).text()
        if(itemType == "S??? N??o"):
            self.type = "Brain/"
        if(itemType == "M???ch M??u N??o"):
            self.type = "Cerebrovascular/"
        if(itemType == "T??nh M???ch ?????"):
            self.type = "Venography/"
        if(itemType == "Tim"):
            self.type = "Heart/"
        if(itemType == "Tuy???n V??"):
            itemType = "Breast/"
        self.state = self.dataTabPatient.item(row, 3).text()
        if(self.state == "???? C?? K???t Qu???"):
            data = self.busMRI.getLinkMRI(IDPatient=self.IDPatient)
            self.linkMRI = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalFile += 1
                self.imgList[self.totalFile] = file
            self.hSlider.setMaximum(self.totalFile)
            #print(self.PATH + self.type + self.linkMRI + "/" +self.imgList[1])
            # First
            I = cv2.imread(self.PATH + self.type + self.linkMRI + "/" +self.imgList[1])
            img = cv2.resize(I, (384, 384))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
            pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
            self.lbMRIImg.setPixmap(QtGui.QPixmap(pixImg))
        else:
            self.lbMRIImg.clear()

    def loadMRIImage(self, value):
        if(self.totalFile > 0):
            if(value in self.imgList.keys()):
                I = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.imgList[value])
                img = cv2.resize(I, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                convertToQtFormat = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                convertToQtFormat = convertToQtFormat.convertToFormat(QImage.Format_Grayscale8)
                pixImg = convertToQtFormat.scaled(384, 384, Qt.KeepAspectRatio)
                self.lbMRIImg.setPixmap(QtGui.QPixmap(pixImg))

    def uploadMRIImage(self):
        if(self.IDPatient != ""):
            if(self.state == "???? C?? K???t Qu???"): # update
                self.lbMRIImg.clear()
                self.totalFile = 0
                self.imgList.clear()
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Ch???n Th?? M???c Ch???a ???nh MRI"))
                if(folder != "" and folder is not None):
                    linkDirectory = self.PATH + self.type + self.IDPatient
                    try:
                        for file in os.listdir(linkDirectory):
                            os.remove(linkDirectory + "/" + file)
                        for file in os.listdir(folder):
                            if not(os.path.isfile(linkDirectory + "/" + file)):
                                src = folder + "/" + file
                                shutil.copy(src=src, dst=linkDirectory)
                        self.noticfication = Notification(title="Th??ng b??o", message="Thao t??c th???c hi???n th??nh c??ng!")
                    except:
                            self.noticfication = Notification(title="C???nh b??o", message="Thao t??c th???c hi???n th???t b???i!", icon_type=1)
            else: # Upload
                dialog = QFileDialog()
                folder = str(dialog.getExistingDirectory(self, "Ch???n Th?? M???c Ch???a ???nh MRI"))
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
                        self.noticfication = Notification(title="C???nh b??o", message="Thao t??c th???c hi???n th???t b???i!", icon_type=1)
                        return
                    reuslt = self.busMRI.uploadMRI(IDPatient=self.IDPatient, MRIType=self.comboTypeMRI.currentText(), LinkMRI=self.IDPatient)
                    if(reuslt == 1):
                        self.noticfication = Notification(title="Th??ng b??o", message="Thao t??c th???c hi???n th??nh c??ng!")
                    else:
                        self.noticfication = Notification(title="C???nh b??o", message="Thao t??c th???c hi???n th???t b???i!", icon_type=1)
        else:
            self.noticfication = Notification(title="C???nh b??o", message="Ch??a ch???n b???nh nh??n!", icon_type=1)
        self.loadData()
    
    def selectIDPatient(self, selected):
        if selected:
            self.searchBT = 0

    def selectedFullName(self, selected):
        if selected:
            self.searchBT = 1

    def searchPatient(self):
        if(self.searchBT == 0 or self.searchBT == 1):
            dataMRI = self.busMRI.searchPatient(State=self.searchBT, IDPatient=self.txtSearch.text(), FullName=self.txtSearch.text())
            if(dataMRI != [] and dataMRI is not None):
                self.showData(dataMRI=dataMRI)

            else:
                self.noticfication = Notification(title="Th??ng b??o", message="Kh??ng t??m th???y b???nh nh??n!")
        else:
            self.noticfication = Notification(title="C???nh b??o", message="Ch??a ch???n ph????ng th???c t??m ki???m!", icon_type=1)

    def showData(self, dataMRI):
        self.totalFile = 0
        self.imgList.clear()
        self.lbMRIImg.clear()
        self.lbPatient.setText("")
        self.dataTabPatient.setRowCount(0)
        for row_number, row_data in enumerate(dataMRI):
            self.dataTabPatient.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
                if(col_number == 3 and data != ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("???? C?? K???t Qu???"))
                elif(col_number == 3 and data == ""):
                    self.dataTabPatient.setItem(row_number, col_number, QtWidgets.QTableWidgetItem("Ch??a C?? K???t Qu???"))
        self.dataTabPatient.resizeColumnsToContents()

    def createDirectory(self):
        if not (os.path.isdir(self.PATH + "Brain")):
            os.mkdir(self.PATH + "Brain")
        if not (os.path.isdir(self.PATH + "Cerebrovascular")):
            os.mkdir(self.PATH + "Cerebrovascular")
        if not (os.path.isdir(self.PATH + "Venography")):
            os.mkdir(self.PATH + "Venography")
        if not (os.path.isdir(self.PATH + "Heart")):
            os.mkdir(self.PATH + "Heart")
        if not (os.path.isdir(self.PATH + "Breast")):
            os.mkdir(self.PATH + "Breast")
        