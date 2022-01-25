from SQL.SQLConnection import SQLConnection

class DAL_MedicalRecord(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllPatient(self):
        data = self.queryData("Select IDPatient, FullName From Patient")
        return data

    def selectAllMedicalRecord(self):
        data = self.queryData("Select MedicalRecord.IDMedicalRecord, MedicalRecord.IDPatient, Patient.FullName From MedicalRecord, Patient Where MedicalRecord.IDPatient = Patient.IDPatient")
        return data

    def deleteMedicalRecord(self, IDMedicalRecord):
        self.queryNoReturn("Delete From MedicalRecord Where IDMedicalRecord = '{}'".format(IDMedicalRecord))