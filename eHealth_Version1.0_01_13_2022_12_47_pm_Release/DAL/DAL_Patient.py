from SQL.SQLConnection import SQLConnection

class DAL_Patient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllPatient(self):
        data = self.queryData("Select IDPatient, FullName, Diagnose From Patient")
        return data

    def selectPatientOfEmployee(self, IDEmployee):
        data = self.queryData("Select IDPatient, FullName, RequestDiagnose, Diagnose From Patient Where IDEmployee = '{}'".format(IDEmployee))
        return data

    def updateDiagnose(self, dtoPatient):
        self.queryNoReturn("Update Patient Set Diagnose = N'{}' Where IDPatient = '{}'".format(dtoPatient.Diagnose, dtoPatient.IDPatient))
