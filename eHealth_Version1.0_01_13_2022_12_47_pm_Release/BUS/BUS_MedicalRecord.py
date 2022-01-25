from DAL.DAL_MedicalRecord import DAL_MedicalRecord

class BUS_MedicalRecord():
    def __init__(self):
        self.dalMedicalRecord = DAL_MedicalRecord()

    def loadPatientData(self):
        return self.dalMedicalRecord.selectAllPatient()

    def loadMedicalRecordData(self):
        return self.dalMedicalRecord.selectAllMedicalRecord()

    def deleteMedicalRecord(self, IDMedicalRecord):
        try:
            self.dalMedicalRecord.deleteMedicalRecord(IDMedicalRecord=IDMedicalRecord)
            return 1
        except:
            return 0