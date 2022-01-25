from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_CreateMedicalRecordPatient import Ui_CreateMedicalRecordPatient
from GUI.Logic.Noticfication import *
from BUS.BUS_CreateMedicalRecord import BUS_CreateMedicalRecord
from DTO.DTO_MedicalRecord import DTO_MedicalRecord
from PyQt5 import QtCore

class CreateMedicalRecordPatient(QFrame, Ui_CreateMedicalRecordPatient):
    signal = QtCore.pyqtSignal(int)

    def __init__(self, IDPatient, FullName, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.setWindowTitle("Tạo Bệnh Án - " + IDPatient + " - " + FullName)
        self.IDPatient = IDPatient
        self.busCreateMedicalRecord = BUS_CreateMedicalRecord()
        self.dtoMedicalRecord = DTO_MedicalRecord()

        # Event Handle
        self.btCreate.clicked.connect(self.addMedicalRecord)
        self.btRefresh.clicked.connect(self.clearText)

        self.loadData()

    def loadData(self):
        dataPatient = self.busCreateMedicalRecord.loadPatientInfo(IDPatient=self.IDPatient)
        self.txtFullName.setText(dataPatient[0])
        self.txtOld.setText(str(dataPatient[1]))
        self.txtGender.setText(dataPatient[2])
        self.txtEthnic.setText(dataPatient[3])
        self.txtJob.setText(dataPatient[4])
        self.txtAddress.setText(dataPatient[5])

    QtCore.pyqtSlot()
    def addMedicalRecord(self):
        IDMR = 0
        with open("Config/medicalrecord.cfg", "r+") as file:
            for data in file:
                ID = int(data.strip())
                ID += 1
                IDMR = ID
                if(ID > 0 and ID < 10):
                    self.dtoMedicalRecord.IDMedicalRecord = "BA0" + str(ID)
                else:
                    self.dtoMedicalRecord.IDMedicalRecord = "BA" + str(ID)
        self.dtoMedicalRecord.IDPatient = self.IDPatient
        self.dtoMedicalRecord.ReasonHospitalize = self.txtReasonHospitalize.toPlainText()
        self.dtoMedicalRecord.MedicalHistory = self.txtMedicalHistory.toPlainText()
        self.dtoMedicalRecord.AdmissionStatus = self.txtAdmissionStatus.toPlainText()
        self.dtoMedicalRecord.Prehistoric = self.txtPrehistoric.toPlainText()
        self.dtoMedicalRecord.ClinicalExamination = self.txtPrehistoric.toPlainText()
        self.dtoMedicalRecord.Diagnose = self.txtDiagnose.toPlainText()
        self.dtoMedicalRecord.Preclinical = self.txtPreclinical.toPlainText()
        self.dtoMedicalRecord.GeneralConclusion = self.txtGeneralConclusion.toPlainText()
        self.dtoMedicalRecord.Regimen = self.txtRegimen.toPlainText()
        result = self.busCreateMedicalRecord.addMedicalRecord(dtoMedicalRecord=self.dtoMedicalRecord)
        if(result == 1):
            with open("Config/medicalrecord.cfg", "w+") as file:
                file.write(str(IDMR) + "\n")
            self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            self.signal.emit(result)
            self.btCreate.setEnabled(False)
        else:
            self.noticfication = Notification(title="Cảnh báo", message="Thao tác thực hiện thất bại!", icon_type=1)

    def clearText(self):
        self.txtReasonHospitalize.setText("")
        self.txtMedicalHistory.setText("")
        self.txtAdmissionStatus.setText("")
        self.txtPrehistoric.setText("")
        self.txtClinicalExamination.setText("")
        self.txtDiagnose.setText("")
        self.txtPreclinical.setText("")
        self.txtGeneralConclusion.setText("")
        self.txtRegimen.setText("")



       
    