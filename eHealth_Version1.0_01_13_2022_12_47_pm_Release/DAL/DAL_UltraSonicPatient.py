from SQL.SQLConnection import SQLConnection

class DAL_UltraSonicPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkUltraSonicViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select UltraSonicType, LinkUltraSonic From UltraSonic Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkUltraSonic(self, IDPatient, UltraSonicType):
        data = self.queryDataOnly1("Select LinkUltraSonic From UltraSonic where IDPatient = '{}' and UltraSonicType = N'{}'".format(IDPatient, UltraSonicType))
        return data