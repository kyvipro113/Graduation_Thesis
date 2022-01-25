from SQL.SQLConnection import SQLConnection

class DAL_MedicalRecordPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectPatientInfo(self, IDPatient):
        data = self.queryData("Select FullName, Old, Gender, Ethnic, Job, Address From Patient Where IDPatient = '{}'".format(IDPatient))
        return data[0]

    def selectMedicalRecord(self, IDMedicalRecord):
        data = self.queryData("Select ReasonHospitalize, MedicalHistory, AdmissionStatus, Prehistoric, ClinicalExamination, Diagnose, Preclinical, GeneralConclusion, Regimen From MedicalRecord Where IDMedicalRecord = '{}'".format(IDMedicalRecord))
        return data[0]