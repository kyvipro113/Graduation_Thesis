from DAL.DAL_CreateMedicalRecord import DAL_CreateMedicalRecord

class BUS_CreateMedicalRecord():
    def __init__(self):
        self.dalCreateMedicalRecord = DAL_CreateMedicalRecord()

    def loadPatientInfo(self, IDPatient):
        return self.dalCreateMedicalRecord.selectPatientInfo(IDPatient=IDPatient)

    def addMedicalRecord(self, dtoMedicalRecord):
        try:
            self.dalCreateMedicalRecord.addMedicalRecord(dtoMedicalRecord=dtoMedicalRecord)
            return 1
        except:
            return 0

