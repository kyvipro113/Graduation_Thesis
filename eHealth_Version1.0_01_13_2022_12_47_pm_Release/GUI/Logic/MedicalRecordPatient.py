from PyQt5.QtWidgets import QFrame
from GUI.View.Ui_MedicalRecordPatient import Ui_MedicalRecordPatient
from BUS.BUS_MedicalRecordPatient import BUS_MedicalRecordPatient

class MedicalRecordPatient(QFrame, Ui_MedicalRecordPatient):
    def __init__(self, IDPatient, IDMedicalRecord, parent=None):
        QFrame.__init__(self, parent=parent)
        self.setupUi(self)

        self.busMedicalRecordPatient = BUS_MedicalRecordPatient()
        dataPatientInfo = self.busMedicalRecordPatient.loadPatientInfo(IDPatient=IDPatient)
        dataMedicalRecord = self.busMedicalRecordPatient.loadMedicalRecord(IDMedicalRecord=IDMedicalRecord)
        
        self.setWindowTitle("Bệnh Án - " + IDPatient + " - " + dataPatientInfo[0])

        self.txtFullName.setText(dataPatientInfo[0])
        self.txtOld.setText(str(dataPatientInfo[1]))
        self.txtGender.setText(dataPatientInfo[2])
        self.txtEthnic.setText(dataPatientInfo[3])
        self.txtJob.setText(dataPatientInfo[4])
        self.txtAddress.setText(dataPatientInfo[5])

        self.txtReasonHospitalize.setText(dataMedicalRecord[0])
        self.txtMedicalHistory.setText(dataMedicalRecord[1])
        self.txtAdmissionStatus.setText(dataMedicalRecord[2])
        self.txtPrehistoric.setText(dataMedicalRecord[3])
        self.txtClinicalExamination.setText(dataMedicalRecord[4])
        self.txtDiagnose.setText(dataMedicalRecord[5])
        self.txtPreclinical.setText(dataMedicalRecord[6])
        self.txtGeneralConclusion.setText(dataMedicalRecord[7])
        self.txtRegimen.setText(dataMedicalRecord[8])
