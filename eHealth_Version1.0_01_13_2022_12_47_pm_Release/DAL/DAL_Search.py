from SQL.SQLConnection import SQLConnection

class DAL_Search(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectEmployeeViaID(self, IDEmployee):
        data = self.queryData("Select IDEmployee, FullName, DateOfBirth, Gender, CitizenID, NumberPhone, Address From Employee Where IDEmployee = '{}'".format(IDEmployee))
        return data

    def selectEmployeeViaFullName(self, FullName):
        data = self.queryData("Select IDEmployee, FullName, DateOfBirth, Gender, CitizenID, NumberPhone, Address From Employee Where FullName Like N'%{}%'".format(FullName))
        return data
    
    def selectPatientViaID(self, IDPatient):
        data = self.queryData("Select IDPatient, FullName, Old, Gender, Ethnic, Job, Address, NumberPhone, CitizenID, IDHealthInsurance From Patient Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectPatientViaFullName(self, FullName):
        data = self.queryData("Select IDPatient, FullName, Old, Gender, Ethnic, Job, Address, NumberPhone, CitizenID, IDHealthInsurance From Patient Where FullName like N'%{}%'".format(FullName))
        return data