from SQL.SQLConnection import SQLConnection

class DAL_Test(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllTest(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, Test.TestType, Test.LinkTest From Patient, Test Where Test.IDPatient = Patient.IDPatient And Test.TestType is not NULL")
        return data
    
    def selectTestWithType(self, TestType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, Test.TestType, Test.LinkTest From Patient, Test Where Test.IDPatient = Patient.IDPatient And Test.TestType = N'{}'".format(TestType))
        return data

    def selectLinkTest(self, IDPatient):
        data = self.queryDataOnly1("Select LinkTest From Test Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateTest(self, IDPatient, TestType, LinkTest):
        self.queryNoReturn("Update Test Set LinkTest = '{}' Where IDPatient = '{}' and TestType = N'{}'".format(LinkTest, IDPatient, TestType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, Test.TestType, Test.LinkTest From Patient, Test Where Test.IDPatient = Patient.IDPatient And Test.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, Test.TestType, Test.LinkTest From Patient, Test Where Test.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And Test.TestType is not NULL".format(FullName))
        return data 