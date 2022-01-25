from SQL.SQLConnection import SQLConnection

class DAL_TestPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkTestViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select TestType, LinkTest From Test Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkTest(self, IDPatient, TestType):
        data = self.queryDataOnly1("Select LinkTest From Test where IDPatient = '{}' and TestType = N'{}'".format(IDPatient, TestType))
        return data