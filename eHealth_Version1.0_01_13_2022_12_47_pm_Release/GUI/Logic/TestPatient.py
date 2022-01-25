from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_TestPatient import Ui_TestPaitient
from GUI.Logic.Noticfication import Notification
from BUS.BUS_TestPatient import BUS_TestPatient
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
import os
import cv2

class TestPatient(QFrame, Ui_TestPaitient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busTestPatient = BUS_TestPatient()
        self.PATH = "Patient/Test/"
        self.type = ""
        self.linkTest = ""
        self.img = ""
        self.sizeIMG = ()

        # Event Handle
        self.comboTestType.currentTextChanged.connect(self.changeTestType)

        self.firtLoad()

    def firtLoad(self):
        data = self.busTestPatient.firstLoadLinkTest(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboTestType.setCurrentText(data[0])
            if(self.comboTestType.currentText() == "Máu"):
                self.type = "Blood/"
                self.sizeIMG  = (564, 469)
            if(self.comboTestType.currentText() == "Nước Tiểu"):
                self.type = "Urine/"
                self.sizeIMG  = (564, 469)
            if(self.comboTestType.currentText() == "SARS - COV - 2"):
                self.type = "Covid19/"
                self.sizeIMG  = (803, 264)
            if(self.comboTestType.currentText() == "Sinh Thiết"):
                self.type = "Biopsy/"
                self.sizeIMG  = (564, 469)
            if(self.comboTestType.currentText() == "CRP"):
                self.type = "CRP/"
                self.sizeIMG  = (564, 469)

            if(data[1] != "" and data[1] is not None):
                self.linkTest = data[1]
                print(self.type)
                for file in os.listdir(self.PATH + self.type + data[1]):
                    self.img = file
                # First
                img = cv2.imread(self.PATH + self.type + self.linkTest + "/" + self.img)
                img = cv2.resize(img, self.sizeIMG)
                h, w, ch = img.shape
                bytesPerLine = ch * w
                img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                self.lbTestImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def changeTestType(self):
        if(self.comboTestType.currentText() == "Máu"):
            self.type = "Blood/"
            self.sizeIMG  = (564, 469)
        if(self.comboTestType.currentText() == "Nước Tiểu"):
            self.type = "Urine/"
            self.sizeIMG  = (564, 469)
        if(self.comboTestType.currentText() == "SARS - COV - 2"):
            self.type = "Covid19/"
            self.sizeIMG  = (803, 264)
        if(self.comboTestType.currentText() == "Sinh Thiết"):
            self.type = "Biopsy/"
            self.sizeIMG  = (564, 469)
        if(self.comboTestType.currentText() == "CRP"):
            self.type = "CRP/"
            self.sizeIMG  = (564, 469)

        self.linkTest = ""
        self.lbTestImg.clear()
        self.img = ""
        data = self.busTestPatient.loadLinkTest(IDPatient=self.IDPatient, TestType=self.comboTestType.currentText())
        print(data)
        if(data is not None and data[0] != ""):
            self.linkTest = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.img = file

            # First
            img = cv2.imread(self.PATH + self.type + self.linkTest + "/" + self.img)
            img = cv2.resize(img, self.sizeIMG)
            h, w, ch = img.shape
            bytesPerLine = ch * w
            img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.lbTestImg.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

