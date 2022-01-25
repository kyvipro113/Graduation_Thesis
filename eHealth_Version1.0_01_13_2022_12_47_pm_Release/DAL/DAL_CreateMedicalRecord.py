from SQL.SQLConnection import SQLConnection

class DAL_CreateMedicalRecord(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectPatientInfo(self, IDPatient):
        data = self.queryData("Select FullName, Old, Gender, Ethnic, Job, Address From Patient Where IDPatient = '{}'".format(IDPatient))
        return data[0]

    def addMedicalRecord(self, dtoMedicalRecord):
        self.queryNoReturn("Insert Into MedicalRecord Values('{}', '{}', N'{}', N'{}', N'{}', N'{}', N'{}', N'{}', N'{}', N'{}', N'{}')".format(dtoMedicalRecord.IDMedicalRecord, dtoMedicalRecord.IDPatient, dtoMedicalRecord.ReasonHospitalize, dtoMedicalRecord.MedicalHistory, dtoMedicalRecord.AdmissionStatus, dtoMedicalRecord.Prehistoric, dtoMedicalRecord.ClinicalExamination, dtoMedicalRecord.Diagnose, dtoMedicalRecord.Preclinical, dtoMedicalRecord.GeneralConclusion, dtoMedicalRecord.Regimen))

