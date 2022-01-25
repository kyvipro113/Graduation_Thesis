from GUI.View.Ui_UpdateMedicalRecordPatient import Ui_CreateMedicalRecordPatient
from PyQt5.QtWidgets import QFrame
from PyQt5 import QtCore
from GUI.Logic.Noticfication import *
from BUS.BUS_UpdateMedicalRecord import BUS_UpdateMedicalRecord
from DTO.DTO_MedicalRecord import DTO_MedicalRecord

class UpdateMedicalRecord(QFrame, Ui_CreateMedicalRecordPatient):
    signal = QtCore.pyqtSignal(int)

    def __init__(self, IDPatient, IDMedicalRecord, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.IDPatient = IDPatient
        self.IDMedicalRecord = IDMedicalRecord
        self.dtoMedicalRecord = DTO_MedicalRecord()
        self.busMedicalRecord = BUS_UpdateMedicalRecord()
       
       # Event Handle
        self.btUpdate.clicked.connect(self.updateMedicalRecord)
        self.btRefresh.clicked.connect(self.clearText)

        self.loadData()
    
    def loadData(self):
        dataPatientInfo = self.busMedicalRecord.loadPatientInfo(IDPatient=self.IDPatient)
        self.setWindowTitle("Cập Nhật Bệnh Án - " + self.IDPatient + " - " + dataPatientInfo[0])
        self.txtFullName.setText(dataPatientInfo[0])
        self.txtOld.setText(str(dataPatientInfo[1]))
        self.txtGender.setText(dataPatientInfo[2])
        self.txtEthnic.setText(dataPatientInfo[3])
        self.txtJob.setText(dataPatientInfo[4])
        self.txtAddress.setText(dataPatientInfo[5])

        dataMedicalRecord = self.busMedicalRecord.loadMedicalRecordPatient(IDMedicalRecord=self.IDMedicalRecord)
        self.txtReasonHospitalize.setText(dataMedicalRecord[0])
        self.txtMedicalHistory.setText(dataMedicalRecord[1])
        self.txtAdmissionStatus.setText(dataMedicalRecord[2])
        self.txtPrehistoric.setText(dataMedicalRecord[3])
        self.txtClinicalExamination.setText(dataMedicalRecord[4])
        self.txtDiagnose.setText(dataMedicalRecord[5])
        self.txtPreclinical.setText(dataMedicalRecord[6])
        self.txtGeneralConclusion.setText(dataMedicalRecord[7])
        self.txtRegimen.setText(dataMedicalRecord[8])

    QtCore.pyqtSlot()
    def updateMedicalRecord(self):
        self.dtoMedicalRecord.IDMedicalRecord = self.IDMedicalRecord
        self.dtoMedicalRecord.IDPatient = self.IDPatient
        self.dtoMedicalRecord.ReasonHospitalize = self.txtReasonHospitalize.toPlainText()
        self.dtoMedicalRecord.MedicalHistory = self.txtMedicalHistory.toPlainText()
        self.dtoMedicalRecord.AdmissionStatus = self.txtAdmissionStatus.toPlainText()
        self.dtoMedicalRecord.Prehistoric = self.txtPrehistoric.toPlainText()
        self.dtoMedicalRecord.ClinicalExamination = self.txtClinicalExamination.toPlainText()
        self.dtoMedicalRecord.Diagnose = self.txtDiagnose.toPlainText()
        self.dtoMedicalRecord.Preclinical = self.txtPreclinical.toPlainText()
        self.dtoMedicalRecord.GeneralConclusion = self.txtGeneralConclusion.toPlainText()
        self.dtoMedicalRecord.Regimen = self.txtRegimen.toPlainText()
        #self.dtoMedicalRecord.TestPrint()
        result = self.busMedicalRecord.updateMedicalRecordPatient(dtoMedicalRecord=self.dtoMedicalRecord)
        if(result == 1):
            self.noticfication = Notification(title="Thông báo", message="Thao tác thực hiện thành công!")
            self.signal.emit(result)
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
