from PyQt5.sip import delete
from DAL.DAL_MedicalRegister import DAL_MedicalRegister

class BUS_MedicalRegister():
    def __init__(self):
        self.dalMedicalRegister = DAL_MedicalRegister()

    def loadData(self):
        return self.dalMedicalRegister.selectAllPatient()

    def addPatientRegister(self, dtoPatient):
        try:
            self.dalMedicalRegister.addPatientRegister(dtoPatient=dtoPatient)
            return 1
        except:
            return 0

    def updatePatientRegister(self, dtoPatient):
        try:
            self.dalMedicalRegister.updatePatientRegister(dtoPatient=dtoPatient)
            return 1
        except:
            return 0

    def deleteMedicalRegister(self, IDPatient):
        try:
            self.dalMedicalRegister.deleteMedicalRegister(IDPatient=IDPatient)
            return 1
        except:
            return 0

    def getFaculty(self):
        return self.dalMedicalRegister.getFaculty()

    def getIDFaculty(self, FacultyName):
        return self.dalMedicalRegister.getIDFaculty(FacultyName=FacultyName)

    def getNameFaculty(self, IDFaculty):
        return self.dalMedicalRegister.getNameFaculty(IDFaculty=IDFaculty)


    def getEmployeeInFaculty(self, IDFaculty):
        return self.dalMedicalRegister.getEmployeeInFaculty(IDFaculty=IDFaculty)

    def getNameEmployee(self, IDEmployee):
        return self.dalMedicalRegister.getNameEmployee(IDEmployee=IDEmployee)

    def getIDEmployee(self, FullName):
        return self.dalMedicalRegister.getIDEmployee(FullName=FullName)