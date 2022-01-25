class DTO_MedicalRecord():
    def __init__(self):
        self.IDMedicalRecord = ""
        self.IDPatient = ""
        self.ReasonHospitalize = ""
        self.MedicalHistory = ""
        self.AdmissionStatus = ""
        self.Prehistoric = ""
        self.ClinicalExamination = ""
        self.Diagnose = ""
        self.Preclinical = ""
        self.GeneralConclusion = ""
        self.Regimen = ""

    def TestPrint(self):
        print(self.IDMedicalRecord)
        print(self.IDPatient)
        print(self.ReasonHospitalize)
        print(self.MedicalHistory)
        print(self.AdmissionStatus)
        print(self.Prehistoric)
        print(self.ClinicalExamination)
        print(self.Diagnose)
        print(self.Preclinical)
        print(self.GeneralConclusion)
        print(self.Regimen)