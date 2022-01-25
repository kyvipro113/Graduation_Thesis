from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_UltraSonicPatient import Ui_UltraSonicPatient
from GUI.Logic.Noticfication import Notification
from BUS.BUS_UltraSonicPatient import BUS_UltraSonicPatient
from PyQt5 import QtGui
import os
import cv2

class UltraSonicPatient(QFrame, Ui_UltraSonicPatient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busUltraSonicPatient = BUS_UltraSonicPatient()

        self.PATH = "Patient/UltraSonic/"
        self.type = ""
        self.linkUltraSonic = ""

        self.UltraSonicImgList = {}
        self.totalImg = 0
        
        # Event Handle
        self.comboUltraSonicType.currentTextChanged.connect(self.changeUltraSonicType)
        self.hSlider.valueChanged.connect(self.loadUltraSonicImg)

        self.firtLoadData()

    def changeUltraSonicType(self):
        if(self.comboUltraSonicType.currentText() == "Tim"):
            self.type = "Heart/"
        if(self.comboUltraSonicType.currentText() == "Thai Nhi"):
            self.type = "Fetus/"
        if(self.comboUltraSonicType.currentText() == "Gan Mật"):
            self.type = "Liver_Gallbladder/"
        
        self.linkUltraSonic = ""
        self.UltraSonicImgList.clear()
        self.lbUltraSonicImg.clear()
        self.totalImg = 0
        data = self.busUltraSonicPatient.loadLinkUltraSonic(IDPatient=self.IDPatient, UltraSonicType=self.comboUltraSonicType.currentText())
        print(data)
        if(data is not None and data[0] != ""):
            self.linkUltraSonic = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalImg += 1
                self.UltraSonicImgList[self.totalImg] = file
            self.hSlider.setMaximum(self.totalImg)
            # Firt
            img = cv2.imread(self.PATH + self.type + self.linkUltraSonic + "/" + self.UltraSonicImgList[1])
            img = cv2.resize(img, (384, 384))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.lbUltraSonicImg.setPixmap(QtGui.QPixmap.fromImage(img))

        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    
    def firtLoadData(self):
        data = self.busUltraSonicPatient.firstLoadLinkUltraSonic(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboUltraSonicType.setCurrentText(data[0])
            if(self.comboUltraSonicType.currentText() == "Tim"):
                self.type = "Heart/"
            if(self.comboUltraSonicType.currentText() == "Thai Nhi"):
                self.type = "Fetus/"
            if(self.comboUltraSonicType.currentText() == "Gan Mật"):
                self.type = "Liver_Gallbladder/"
            print(data)
            if(data[1] != "" and data[1] is not None):
                self.linkUltraSonic = data[1]
                print(self.type)
                for file in os.listdir(self.PATH + self.type + data[1]):
                    self.totalImg += 1
                    self.UltraSonicImgList[self.totalImg] = file
                self.hSlider.setMaximum(self.totalImg)
                # Firt
                img = cv2.imread(self.PATH + self.type + self.linkUltraSonic + "/" + self.UltraSonicImgList[1])
                img = cv2.resize(img, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbUltraSonicImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def loadUltraSonicImg(self, value):
        if(self.totalImg > 0):
            if(value in self.UltraSonicImgList.keys()):
                img = cv2.imread(self.PATH + self.type + self.linkUltraSonic + "/" + self.UltraSonicImgList[value])
                img = cv2.resize(img, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbUltraSonicImg.setPixmap(QtGui.QPixmap.fromImage(img))