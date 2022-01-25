from SQL.SQLConnection import SQLConnection

class DAL_UltraSonic(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllUltraSonic(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, UltraSonic.UltraSonicType, UltraSonic.LinkUltraSonic From Patient, UltraSonic Where UltraSonic.IDPatient = Patient.IDPatient And UltraSonic.UltraSonicType is not NULL")
        return data

    def selectUltraSonicWithType(self, UltraSonicType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, UltraSonic.UltraSonicType, UltraSonic.LinkUltraSonic From Patient, UltraSonic Where UltraSonic.IDPatient = Patient.IDPatient And UltraSonic.UltraSonicType = N'{}'".format(UltraSonicType))
        return data

    def selectLinkNRI(self, IDPatient):
        data = self.queryDataOnly1("Select LinkUltraSonic From UltraSonic Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateUltraSonic(self, IDPatient, UltraSonicType, LinkUltraSonic):
        self.queryNoReturn("Update UltraSonic Set LinkUltraSonic = '{}' Where IDPatient = '{}' and UltraSonicType = N'{}'".format(LinkUltraSonic, IDPatient, UltraSonicType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, UltraSonic.UltraSonicType, UltraSonic.LinkUltraSonic From Patient, UltraSonic Where UltraSonic.IDPatient = Patient.IDPatient And UltraSonic.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, UltraSonic.UltraSonicType, UltraSonic.LinkUltraSonic From Patient, UltraSonic Where UltraSonic.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And UltraSonic.UltraSonicType is not NULL".format(FullName))
        return data 