from SQL.SQLConnection import SQLConnection

class DAL_ECG(SQLConnection):
    def __init__(self):
        SQLConnection.__init__(self)

    def selectAllECG(self):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, ECG.ECGType, ECG.LinkECG From Patient, ECG Where ECG.IDPatient = Patient.IDPatient And ECG.ECGType is not NULL")
        return data

    def selectECGWithType(self, ECGType):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, ECG.ECGType, ECG.LinkECG From Patient, ECG Where ECG.IDPatient = Patient.IDPatient And ECG.ECGType = N'{}'".format(ECGType))
        return data

    def selectLinkNRI(self, IDPatient):
        data = self.queryDataOnly1("Select LinkECG From ECG Where IDPatient = '{}'".format(IDPatient))
        return data

    def updateECG(self, IDPatient, ECGType, LinkECG):
        self.queryNoReturn("Update ECG Set LinkECG = '{}' Where IDPatient = '{}' and ECGType = N'{}'".format(LinkECG, IDPatient, ECGType))

    def searchPatientWithIDPatient(self, IDPatient):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, ECG.ECGType, ECG.LinkECG From Patient, ECG Where ECG.IDPatient = Patient.IDPatient And ECG.IDPatient = '{}'".format(IDPatient))
        return data

    def searchPatientWithFullName(self, FullName):
        data = self.queryData("Select Patient.IDPatient, Patient.FullName, ECG.ECGType, ECG.LinkECG From Patient, ECG Where ECG.IDPatient = Patient.IDPatient And Patient.FullName Like N'%{}%' And ECG.ECGType is not NULL".format(FullName))
        return data 