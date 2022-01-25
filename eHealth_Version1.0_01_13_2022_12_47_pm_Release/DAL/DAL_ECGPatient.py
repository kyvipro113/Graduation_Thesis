from SQL.SQLConnection import SQLConnection

class DAL_ECGPatient(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectLinkECGViaIDPatient(self, IDPatient):
        data = self.queryDataOnly1("Select ECGType, LinkECG From ECG Where IDPatient = '{}'".format(IDPatient))
        return data

    def selectLinkECG(self, IDPatient, ECGType):
        data = self.queryDataOnly1("Select LinkECG From ECG where IDPatient = '{}' and ECGType = N'{}'".format(IDPatient, ECGType))
        return data