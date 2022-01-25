class DTO_Prescription():
    def __init__(self):
        self.IDPrescription = ""
        self.IDPatient = ""
        self.ContentPS = ""
        self.IDEmployee = ""
        self.Time = ""

    def TestPrint(self):
        print(self.IDPrescription)
        print(self.IDPatient)
        print(self.ContentPS)
        print(self.IDEmployee)
        print(self.Time)