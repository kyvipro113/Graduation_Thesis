from GUI.View.Ui_XRayPatient import Ui_XRayPaitient
from GUI.Logic.Noticfication import Notification
from PyQt5.QtWidgets import QFrame
from BUS.BUS_XRayPatient import BUS_XRayPatient
from PyQt5 import QtGui
from PyQt5.QtGui import QImage
import os
import cv2
import gc

class XRayPatient(QFrame, Ui_XRayPaitient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busXRayPatient = BUS_XRayPatient()
        self.PATH = "Patient/XRay/"
        self.type = ""
        self.linkXRay = ""
        self.img = ""
        self.stateAI = False
        self.model = None

        # Event Handle
        self.comboXRayType.currentTextChanged.connect(self.changeXRayType)
        self.btDiagnoseAI.clicked.connect(self.predictWithAI)

        self.firtLoad()

    def firtLoad(self):
        data = self.busXRayPatient.firstLoadLinkXRay(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboXRayType.setCurrentText(data[0])
            if(self.comboXRayType.currentText() == "Phổi"):
                self.type = "Chest/"
            if(self.comboXRayType.currentText() == "Cột Sống"):
                self.type = "Spine/"
            if(self.comboXRayType.currentText() == "Xương"):
                self.type = "Bone/"
            if(self.comboXRayType.currentText() == "Tuyến Vú"):
                self.type = "Breast/"

            if(data[1] != "" and data[1] is not None):
                self.linkXRay = data[1]
                print(self.type)
                for file in os.listdir(self.PATH + self.type + data[1]):
                    self.img = file
                # First
                img = cv2.imread(self.PATH + self.type + self.linkXRay + "/" + self.img)
                img = cv2.resize(img, (622, 800))
                h, w, ch = img.shape
                bytesPerLine = ch * w
                img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                self.lbXRayImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def changeXRayType(self):
        if(self.comboXRayType.currentText() == "Phổi"):
            self.type = "Chest/"
        if(self.comboXRayType.currentText() == "Cột Sống"):
            self.type = "Spine/"
        if(self.comboXRayType.currentText() == "Xương"):
            self.type = "Bone/"
        if(self.comboXRayType.currentText() == "Tuyến Vú"):
            self.type = "Breast/"

        self.linkXRay = ""
        self.lbXRayImg.clear()
        self.img = ""
        self.btDiagnoseAI.setText("Bật Hỗ Trợ Chẩn Đoán")
        self.stateAI = False
        data = self.busXRayPatient.loadLinkXRay(IDPatient=self.IDPatient, XRayType=self.comboXRayType.currentText())
        print(data)
        if(data is not None and data[0] != ""):
            self.linkXRay = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.img = file

            # First
            img = cv2.imread(self.PATH + self.type + self.linkXRay + "/" + self.img)
            img = cv2.resize(img, (622, 800))
            h, w, ch = img.shape
            bytesPerLine = ch * w
            img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.lbXRayImg.setPixmap(QtGui.QPixmap.fromImage(img))
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def predictWithAI(self):
        if(self.btDiagnoseAI.text() == "Bật Hỗ Trợ Chẩn Đoán"):
            if(self.comboXRayType.currentText() == "Phổi"):
                self.btDiagnoseAI.setText("Tắt Hỗ Trợ Chẩn Đoán")
                self.stateAI = True
                self.noticfication = Notification(title="Thông báo", message="Xin chờ hệ thống xử lý!")
                src = self.PATH + self.type + self.linkXRay + "/" + self.img
                img = self.predict(src=src)
                time = 0
                with open("Config/XRayStatisticAI.cfg", "r+") as file:
                    for data in file:
                        time = int(data.strip())
                        time += 1
                with open("Config/XRayStatisticAI.cfg", "w+") as file:
                    file.write(str(time) + "\n")
                self.noticfication = Notification(title="Thông báo", message="Hệ Thống Đã Xử Lý Xong!")
                img = cv2.resize(img, (622, 800))
                h, w, ch = img.shape
                bytesPerLine = ch * w
                img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
                self.lbXRayImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Hệ Thống Chưa Hỗ Trợ Chẩn Đoán Loại X-Quang Này!", icon_type=1)
        else:
            self.btDiagnoseAI.setText("Bật Hỗ Trợ Chẩn Đoán")
            self.stateAI = False
            src = self.PATH + self.type + self.linkXRay + "/" + self.img
            img = cv2.imread(src)
            img = cv2.resize(img, (622, 800))
            h, w, ch = img.shape
            bytesPerLine = ch * w
            img = QImage(img.data, w, h, bytesPerLine, QImage.Format_RGB888)
            self.lbXRayImg.setPixmap(QtGui.QPixmap.fromImage(img))



    def predict(self, src):
        #import torch
        import yolov5
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        img = cv2.imread(src)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        model = yolov5.load("ModelAI/Chest_XRay_YOLOv5/weights/best_xray.pt")
        result = model(img)
        result.save("ModelAI/temp")
        del model
        gc.collect()
        try:
            res = cv2.imread("ModelAI/temp/image0.jpg")
            return res
        except:
            return



        