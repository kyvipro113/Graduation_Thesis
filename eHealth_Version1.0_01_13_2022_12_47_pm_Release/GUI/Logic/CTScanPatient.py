from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_CTScanPatient import Ui_CTScanPatient
from GUI.Logic.Noticfication import Notification
from BUS.BUS_CTScanPatient import BUS_CTScanPatient
from PyQt5 import QtGui
import os
import cv2

class CTScanPatient(QFrame, Ui_CTScanPatient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busCTScanPatient = BUS_CTScanPatient()

        self.PATH = "Patient/CTScan/"
        self.type = ""
        self.linkCTScan = ""

        self.CTScanImgList = {}
        self.totalImg = 0
        
        # Event Handle
        self.comboCTScanType.currentTextChanged.connect(self.changeCTScanType)
        self.hSlider.valueChanged.connect(self.loadCTScanImg)

        self.firtLoadData()
        

    def changeCTScanType(self):
        if(self.comboCTScanType.currentText() == "Sọ Não"):
            self.type = "Brain/"
        if(self.comboCTScanType.currentText() == "Phổi"):
            self.type = "Lung/"
        if(self.comboCTScanType.currentText() == "Xương"):
            self.type = "Bone/"
        if(self.comboCTScanType.currentText() == "Ổ Bụng"):
            self.type = "Abdominal/"
        
        self.linkCTScan = ""
        self.CTScanImgList.clear()
        self.lbCTScanImg.clear()
        self.totalImg = 0
        data = self.busCTScanPatient.loadLinkCTScan(IDPatient=self.IDPatient, CTScanType=self.comboCTScanType.currentText())
        print(data)
        if(data is not None and data[0] != ""):
            self.linkCTScan = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalImg += 1
                self.CTScanImgList[self.totalImg] = file
            self.hSlider.setMaximum(self.totalImg)
            # Firt
            img = cv2.imread(self.PATH + self.type + self.linkCTScan + "/" + self.CTScanImgList[1])
            img = cv2.resize(img, (384, 384))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.lbCTScanImg.setPixmap(QtGui.QPixmap.fromImage(img))

        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    
    def firtLoadData(self):
        data = self.busCTScanPatient.firstLoadLinkCTScan(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboCTScanType.setCurrentText(data[0])
            if(self.comboCTScanType.currentText() == "Sọ Não"):
                self.type = "Brain/"
            if(self.comboCTScanType.currentText() == "Phổi"):
                self.type = "Lung/"
            if(self.comboCTScanType.currentText() == "Xương"):
                self.type = "Bone/"
            if(self.comboCTScanType.currentText() == "Ổ Bụng"):
                self.type = "Abdominal/"
            print(data)
            if(data[1] != "" and data[1] is not None):
                self.linkCTScan = data[1]
                print(self.type)
                for file in os.listdir(self.PATH + self.type + data[1]):
                    self.totalImg += 1
                    self.CTScanImgList[self.totalImg] = file
                self.hSlider.setMaximum(self.totalImg)
                # Firt
                img = cv2.imread(self.PATH + self.type + self.linkCTScan + "/" + self.CTScanImgList[1])
                img = cv2.resize(img, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbCTScanImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def loadCTScanImg(self, value):
        if(self.totalImg > 0):
            if(value in self.CTScanImgList.keys()):
                img = cv2.imread(self.PATH + self.type + self.linkCTScan + "/" + self.CTScanImgList[value])
                img = cv2.resize(img, (384, 384))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbCTScanImg.setPixmap(QtGui.QPixmap.fromImage(img))


   