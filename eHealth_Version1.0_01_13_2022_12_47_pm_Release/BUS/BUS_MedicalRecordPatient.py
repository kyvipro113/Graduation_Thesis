
from DAL.DAL_MedicalRecordPatient import DAL_MedicalRecordPatient

class BUS_MedicalRecordPatient():
    def __init__(self):
        self.dalMedicalRecordPatient = DAL_MedicalRecordPatient()

    def loadPatientInfo(self, IDPatient):
        return self.dalMedicalRecordPatient.selectPatientInfo(IDPatient=IDPatient)

    def loadMedicalRecord(self, IDMedicalRecord):
        return self.dalMedicalRecordPatient.selectMedicalRecord(IDMedicalRecord=IDMedicalRecord)