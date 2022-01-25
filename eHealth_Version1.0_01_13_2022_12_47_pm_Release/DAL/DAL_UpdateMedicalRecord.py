from SQL.SQLConnection import SQLConnection

class DAL_UpdateMedicalRecord(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectPatientInfo(self, IDPatient):
        data = self.queryData("Select FullName, Old, Gender, Ethnic, Job, Address From Patient Where IDPatient = '{}'".format(IDPatient))
        return data[0]
    
    def selectMedicalRecordPatient(self, IDMedicalRecord):
        data = self.queryData("Select ReasonHospitalize, MedicalHistory, AdmissionStatus, Prehistoric, ClinicalExamination, Diagnose, Preclinical, GeneralConclusion, Regimen From MedicalRecord Where IDMedicalRecord = '{}'".format(IDMedicalRecord))
        return data[0]

    def updateMedicalRecordPatient(self, dtoMedicalRecord):
        self.queryNoReturn("Update MedicalRecord Set ReasonHospitalize = N'{}', MedicalHistory = N'{}', AdmissionStatus = N'{}', Prehistoric = N'{}', ClinicalExamination = N'{}', Diagnose = N'{}', Preclinical = N'{}', GeneralConclusion = N'{}', Regimen = N'{}' Where IDMedicalRecord = '{}'".format(dtoMedicalRecord.ReasonHospitalize, dtoMedicalRecord.MedicalHistory, dtoMedicalRecord.AdmissionStatus, dtoMedicalRecord.Prehistoric, dtoMedicalRecord.ClinicalExamination, dtoMedicalRecord.Diagnose, dtoMedicalRecord.Preclinical, dtoMedicalRecord.GeneralConclusion, dtoMedicalRecord.Regimen, dtoMedicalRecord.IDMedicalRecord))
