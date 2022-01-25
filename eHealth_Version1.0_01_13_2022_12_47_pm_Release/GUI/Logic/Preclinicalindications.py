from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_PreclinicalIndications import Ui_PreclinicalIndications
from GUI.Logic.Noticfication import *
from BUS.BUS_PreclinicalIndications import BUS_PreclinicalIndications

class PreclinicalIndications(QFrame, Ui_PreclinicalIndications):
    def __init__(self, IDPatient, FullName, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.FullName = FullName
        self.busPreclinicalIndications = BUS_PreclinicalIndications()

        self.setWindowTitle("Chỉ Định Cận Lâm Sàng - " + IDPatient + " - " + FullName)
        self.lbPatient.setText("Bệnh Nhân: " + IDPatient + " - " + FullName)

        # Event Handle
        self.checkXRays.stateChanged.connect(self.stateXRays)   
        self.checkCTScan.stateChanged.connect(self.stateCTScan)
        self.checkMRI.stateChanged.connect(self.stateMRI)
        self.checkUltrasonic.stateChanged.connect(self.stateUltrasonic)
        self.checkTest.stateChanged.connect(self.stateTest)
        self.checkECG.stateChanged.connect(self.stateECG) 
        self.btUpdate.clicked.connect(self.updatePreclinicalIndications)

        self.loadData()

    def stateXRays(self):
        if(self.checkXRays.isChecked()):
            self.comboTypeXRays.setEnabled(True)
        else:
            self.comboTypeXRays.setEnabled(False)

    def stateCTScan(self):
        if(self.checkCTScan.isChecked()):
            self.comboTypeCTScan.setEnabled(True)
        else:
            self.comboTypeCTScan.setEnabled(False)

    def stateMRI(self):
        if(self.checkMRI.isChecked()):
            self.comboTypeMRI.setEnabled(True)
        else:
            self.comboTypeMRI.setEnabled(False)

    def stateUltrasonic(self):
        if(self.checkUltrasonic.isChecked()):
            self.comboTypeUltrasonic.setEnabled(True)
        else:
            self.comboTypeUltrasonic.setEnabled(False)

    def stateTest(self):
        if(self.checkTest.isChecked()):
            self.comboTypeTest.setEnabled(True)
        else:
            self.comboTypeTest.setEnabled(False)

    def stateECG(self):
        if(self.checkECG.isChecked()):
            self.comboTypeECG.setEnabled(True)
        else:
            self.comboTypeECG.setEnabled(False)

    def loadData(self):
        data = self.busPreclinicalIndications.loadPreclinicalXray(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkXRays.setChecked(True)
            self.comboTypeXRays.setCurrentText(data[0])
        else:
            self.checkXRays.setChecked(False)
        data = self.busPreclinicalIndications.loadPreclinicalCTScan(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkCTScan.setChecked(True)
            self.comboTypeCTScan.setCurrentText(data[0])
        else:
            self.checkCTScan.setChecked(False)
        data = self.busPreclinicalIndications.loadPreclinicalMRI(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkMRI.setChecked(True)
            self.comboTypeMRI.setCurrentText(data[0])
        else:
            self.checkMRI.setChecked(False)
        data = self.busPreclinicalIndications.loadPreclinicalUltrasonic(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkUltrasonic.setChecked(True)
            self.comboTypeUltrasonic.setCurrentText(data[0])
        else:
            self.checkUltrasonic.setChecked(False)
        data = self.busPreclinicalIndications.loadPreclinicalTest(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkTest.setChecked(True)
            self.comboTypeTest.setCurrentText(data[0])
        else:
            self.checkTest.setChecked(False)
        data = self.busPreclinicalIndications.loadPreclinicalECG(IDPatient=self.IDPatient)
        if(data[0] is not None):
            self.checkECG.setChecked(True)
            self.comboTypeECG.setCurrentText(data[0])
        else:
            self.checkECG.setChecked(False)

    # def deleteAllPreclinicalIndications(self):
    #     result = self.busPreclinicalIndications.deletePreclinicalIndications(IDPatient=self.IDPatient)
    #     if(result == 1):
    #         self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công")

    def updatePreclinicalIndications(self):
        result = 1
        if(result == 1):
            if(self.checkXRays.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalXray(IDPatient=self.IDPatient, XrayType=self.comboTypeXRays.currentText(), LinkXray="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalXray(IDPatient=self.IDPatient)
        if(result == 1):
            if(self.checkCTScan.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalCTScan(IDPatient=self.IDPatient, CTScanType=self.comboTypeCTScan.currentText(), LinkCTScan="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalCTScan(IDPatient=self.IDPatient)
        if(result == 1):
            if(self.checkMRI.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalMRI(IDPatient=self.IDPatient, MRIType=self.comboTypeMRI.currentText(), LinkMRI="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalMRI(IDPatient=self.IDPatient)
        if(result == 1):
            if(self.checkUltrasonic.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalUltrasonic(IDPatient=self.IDPatient, UltrasonicType=self.comboTypeUltrasonic.currentText(), LinkUltrasonic="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalUltrasonic(IDPatient=self.IDPatient)
        if(result == 1):
            if(self.checkTest.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalTest(IDPatient=self.IDPatient, TestType=self.comboTypeTest.currentText(), LinkTest="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalTest(IDPatient=self.IDPatient)
        if(result == 1):
            if(self.checkECG.isChecked()):
                result = self.busPreclinicalIndications.updatePreclinicalECG(IDPatient=self.IDPatient, ECGType=self.comboTypeECG.currentText(), LinkECG="")
            else:
                result = self.busPreclinicalIndications.deletePreclinicalECG(IDPatient=self.IDPatient)

        if(result == 1):
            self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)
        self.loadData()