from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_MRIPatient import Ui_MRIPaitient
from GUI.Logic.Noticfication import Notification
from BUS.BUS_MRIPatient import BUS_MRIPatient
from PyQt5 import QtGui
import os
import cv2
import numpy as np
import gc


class MRIPatient(QFrame, Ui_MRIPaitient):
    def __init__(self, IDPatient, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.busMRIPatient = BUS_MRIPatient()

        self.PATH = "Patient/MRI/"
        self.type = ""
        self.linkMRI = ""

        self.MRIImgList = {}
        self.totalImg = 0
        self.MRIMaskList = {}
        self.stateAI = False
        self.model = None

        # Event Handle
        self.comboMRIType.currentTextChanged.connect(self.changeMRIType)
        self.btDiagnoseAI.clicked.connect(self.changeStateAIDiagnose)
        self.hSlider.valueChanged.connect(self.loadMRIImg)

        self.firtLoadData()
        

    def changeMRIType(self):
        if(self.comboMRIType.currentText() == "Sọ Não"):
            self.type = "Brain/"
        if(self.comboMRIType.currentText() == "Mạch Máu Não"):
            self.type = "Cerebrovascular/"
        if(self.comboMRIType.currentText() == "Tĩnh Mạch Đồ"):
            self.type = "Venography/"
        if(self.comboMRIType.currentText() == "Tim"):
            self.type = "Heart/"
        if(self.comboMRIType.currentText() == "Tuyến Vú"):
            self.type = "Breast/"
        
        self.linkMRI = ""
        self.MRIMaskList.clear()
        self.MRIImgList.clear()
        self.lbMRIImg.clear()
        self.lbMaskPredict.clear()
        self.totalImg = 0
        self.btDiagnoseAI.setText("Bật Hỗ Trợ Chẩn Đoán")
        self.stateAI = False
        data = self.busMRIPatient.loadLinkMRI(IDPatient=self.IDPatient, MRIType=self.comboMRIType.currentText())
        print(data)
        if(data is not None and data[0] != ""):
            self.linkMRI = data[0]
            for file in os.listdir(self.PATH + self.type + data[0]):
                self.totalImg += 1
                self.MRIImgList[self.totalImg] = file
            self.hSlider.setMaximum(self.totalImg)
            # Firt
            img = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.MRIImgList[1])
            img = cv2.resize(img, (256, 256))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
            self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))

        else:
            self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    
    def firtLoadData(self):
        data = self.busMRIPatient.firstLoadLinkMRI(IDPatient=self.IDPatient)
        if(data != None and data != ""):
            self.comboMRIType.setCurrentText(data[0])
            if(self.comboMRIType.currentText() == "Sọ Não"):
                self.type = "Brain/"
            if(self.comboMRIType.currentText() == "Mạch Máu Não"):
                self.type = "Cerebrovascular/"
            if(self.comboMRIType.currentText() == "Tĩnh Mạch Đồ"):
                self.type = "Venography/"
            if(self.comboMRIType.currentText() == "Tim"):
                self.type = "Heart/"
            if(self.comboMRIType.currentText() == "Tuyến Vú"):
                self.type = "Breast/"
            print(data)
            if(data[1] != "" and data[1] is not None):
                self.linkMRI = data[1]
                print(self.type)
                for file in os.listdir(self.PATH + self.type + data[1]):
                    self.totalImg += 1
                    self.MRIImgList[self.totalImg] = file
                self.hSlider.setMaximum(self.totalImg)
                # Firt
                img = cv2.imread(self.PATH + self.type + self.linkMRI + "/" +self.MRIImgList[1])
                img = cv2.resize(img, (256, 256))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Không Có Dữ Liệu", icon_type=1)

    def loadMRIImg(self, value):
        if not self.stateAI: # Without AI
            if(self.totalImg > 0):
                if(value in self.MRIImgList.keys()):
                    img = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.MRIImgList[value])
                    img = cv2.resize(img, (256, 256))
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                    self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))
                    #print(self.hSlider.value()) # Test
        if self.stateAI:
            if(self.totalImg > 0):
                if(value in self.MRIImgList.keys()):
                    I = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.MRIImgList[value])
                    img = cv2.resize(I, (256, 256))
                    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                    result = self.MRIMaskList[value]
                    mask = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
                    mask = QtGui.QImage(bytes(mask.data), mask.shape[1], mask.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                    self.lbMaskPredict.setPixmap(QtGui.QPixmap.fromImage(mask))
                    img[result == 255] = (0, 255, 0)
                    img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                    self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))

    def changeStateAIDiagnose(self):
        if(self.btDiagnoseAI.text() == "Bật Hỗ Trợ Chẩn Đoán"):
            if(self.comboMRIType.currentText() == "Sọ Não"):
                self.btDiagnoseAI.setText("Tắt Hỗ Trợ Chẩn Đoán")
                self.stateAI = True
                print(self.stateAI)
                self.noticfication = Notification(title="Thông báo", message="Xin chờ hệ thống xử lý!")
                self.model = self.loadModel()
                for id, file in enumerate(os.listdir(self.PATH + self.type + self.linkMRI)):
                    result = self.predict(img_path=self.PATH + self.type + self.linkMRI + "/" + file, model=self.model)
                    self.MRIMaskList[id + 1] = result
                del self.model
                gc.collect()
                self.model = None
                # # Free memory gpu
                # if(tf.test.is_gpu_available()):
                #     device = cuda.get_current_device()
                #     device.reset()
                #     cuda.close()
                time = 0
                with open("Config/MRIStatisticAI.cfg", "r+") as file:
                    for data in file:
                        time = int(data.strip())
                        time += 1
                with open("Config/MRIStatisticAI.cfg", "w+") as file:
                    file.write(str(time) + "\n")
                self.noticfication = Notification(title="Thông báo", message="Hệ thống đã xử lý xong!")

                I = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.MRIImgList[self.hSlider.value()])
                img = cv2.resize(I, (256, 256))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
                result = self.MRIMaskList[self.hSlider.value()]
                mask = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)
                mask = QtGui.QImage(bytes(mask.data), mask.shape[1], mask.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbMaskPredict.setPixmap(QtGui.QPixmap.fromImage(mask))
                img[result == 255] = (0, 255, 0)
                img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
                self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))
            else:
                self.noticfication = Notification(title="Cảnh báo", message="Hệ thống chưa hỗ trợ chẩn đoán loại MRI này!", icon_type=1)
        else:
            self.btDiagnoseAI.setText("Bật Hỗ Trợ Chẩn Đoán")
            self.stateAI = False
            self.lbMaskPredict.clear()
            print(self.stateAI)
            img = cv2.imread(self.PATH + self.type + self.linkMRI + "/" + self.MRIImgList[self.hSlider.value()])
            img = cv2.resize(img, (256, 256))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = QtGui.QImage(bytes(img.data), img.shape[1], img.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()                
            self.lbMRIImg.setPixmap(QtGui.QPixmap.fromImage(img))

    def loadModel(self, json_file="ModelAI/Brain_Tumor_Segmentation/weights/imgSeg_brainMRI_unet.json", weights_file="ModelAI/Brain_Tumor_Segmentation/weights/brain_seg_unet.hdf5"):
        os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
        from tensorflow.keras.models import load_model, model_from_json
        # Load model
        json_model = open(json_file, "r")
        load_model_json = json_model.read()
        json_model.close()
        model = model_from_json(load_model_json)
        model.summary()
        # Load weights
        model.load_weights(weights_file)
        return model

    def predict(self, img_path, model):
        img = cv2.imread(img_path)
        img = cv2.resize(img, (256, 256))
        img = img / 255
        img = np.expand_dims(img, axis=0)
        result = model.predict(img, verbose=0)
        #print((result[0]*255).shape)
        result = cv2.normalize(src=result[0], dst=None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        return result
