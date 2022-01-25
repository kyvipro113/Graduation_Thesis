from DAL.DAL_UpdateMedicalRecord import DAL_UpdateMedicalRecord

class BUS_UpdateMedicalRecord():
    def __init__(self):
        self.dalUpdateMedicalRecord = DAL_UpdateMedicalRecord()

    def loadPatientInfo(self, IDPatient):
        return self.dalUpdateMedicalRecord.selectPatientInfo(IDPatient=IDPatient)

    def loadMedicalRecordPatient(self, IDMedicalRecord):
        return self.dalUpdateMedicalRecord.selectMedicalRecordPatient(IDMedicalRecord=IDMedicalRecord)

    def updateMedicalRecordPatient(self, dtoMedicalRecord):
        try:
            self.dalUpdateMedicalRecord.updateMedicalRecordPatient(dtoMedicalRecord=dtoMedicalRecord)
            return 1
        except:
            return 0