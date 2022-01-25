from SQL.SQLConnection import SQLConnection

class DAL_MedicalRegister(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllPatient(self):
        data = self.queryData("Select IDPatient, FullName, Old, Gender, Ethnic, Job, Address, NumberPhone, CitizenID, IDHealthInsurance, RequestDiagnose, IDFaculty, IDEmployee, Time From Patient")
        return data

    def addPatientRegister(self, dtoPatient):
        self.queryNoReturn("Insert Into Patient Values('{}', N'{}', {}, N'{}', N'{}', N'{}', N'{}', '{}', '{}', '{}', N'{}', '{}', '{}', '{}', '')".format(dtoPatient.IDPatient, dtoPatient.FullName, dtoPatient.Old, dtoPatient.Gender, dtoPatient.Ethnic, dtoPatient.Job, dtoPatient.Address, dtoPatient.NumberPhone, dtoPatient.CitizenID, dtoPatient.IDHealthInsurance, dtoPatient.RequestDiagnose, dtoPatient.IDFaculty, dtoPatient.IDEmployee, dtoPatient.Time))
        self.queryNoReturn("Insert Into Xray Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))
        self.queryNoReturn("Insert Into MRI Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))
        self.queryNoReturn("Insert Into CTScan Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))
        self.queryNoReturn("Insert Into ECG Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))
        self.queryNoReturn("Insert Into Ultrasonic Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))
        self.queryNoReturn("Insert Into Test Values('{}', NULL,  NULL)".format(dtoPatient.IDPatient))

    def updatePatientRegister(self, dtoPatient):
        self.queryNoReturn("Update Patient Set FullName = N'{}', Old = {}, Gender = N'{}', Ethnic = N'{}', Job = N'{}', Address = N'{}', NumberPhone = '{}', CitizenID = '{}', IDHealthInsurance = '{}', RequestDiagnose = N'{}', IDFaculty = '{}', IDEmployee = '{}', Time = '{}' Where IDPatient = '{}'".format(dtoPatient.FullName, dtoPatient.Old, dtoPatient.Gender, dtoPatient.Ethnic, dtoPatient.Job, dtoPatient.Address, dtoPatient.NumberPhone, dtoPatient.CitizenID, dtoPatient.IDHealthInsurance, dtoPatient.RequestDiagnose, dtoPatient.IDFaculty, dtoPatient.IDEmployee, dtoPatient.Time, dtoPatient.IDPatient))

    def deleteMedicalRegister(self, IDPatient):
        self.queryNoReturn("Delete From Xray Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From MRI Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From CTScan Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From ECG Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From Ultrasonic Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From Test Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From Prescription Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From MedicalRecord Where IDPatient = '{}'".format(IDPatient))
        self.queryNoReturn("Delete From Patient Where IDPatient = '{}'".format(IDPatient))
    
    def getFaculty(self):
        data = self.queryData("Select FacultyName From Faculty")
        return data

    def getNameFaculty(self, IDFaculty):
        data = self.queryDataOnly1("Select FacultyName From Faculty Where IDFaculty = '{}'".format(IDFaculty))
        return data[0]

    def getIDFaculty(self, FacultyName):
        data = self.queryDataOnly1("Select IDFaculty From Faculty Where FacultyName = N'{}'".format(FacultyName))
        return data

    def getEmployeeInFaculty(self, IDFaculty):
        data = self.queryData("Select FullName From Employee Where IDFaculty = '{}'".format(IDFaculty))
        return data

    def getNameEmployee(self, IDEmployee):
        data = self.queryDataOnly1("Select FullName From Employee Where IDEmployee = '{}'".format(IDEmployee))
        return data[0]

    def getIDEmployee(self, FullName):
        data = self.queryDataOnly1("Select IDEmployee From Employee Where FullName = N'{}'".format(FullName))
        return data
